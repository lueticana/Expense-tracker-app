from flask import Flask, request, jsonify, Response
from sqlalchemy import text
from models import db, Group, GroupMember
from prometheus_client import generate_latest, Counter, Histogram
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123121@db_skupine:5432/skupine'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# metrics
REQUEST_COUNT = Counter('request_count', 'Total number of requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['endpoint'])

# db
db.init_app(app)

# ENDPOINT

# before & after for metrics
@app.before_request
def before_request():
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
    request.start_time = time.time()

@app.after_request
def after_request(response):
    elapsed_time = time.time() - request.start_time
    REQUEST_LATENCY.labels(endpoint=request.path).observe(elapsed_time)
    return response

# home
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Groups page"}), 201

# get groups
@app.route('/groups', methods=['GET'])
def get_skupine():
    try:
        skupine = Group.query.all()
        if not skupine:
            return jsonify({"message": "No groups found"}), 404
        return jsonify([skupina.to_dict() for skupina in skupine])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # data = request.json
    # group_name = data.get('group_name')

    # if Group.query.filter_by(group_name=group_name).first():
    #     return jsonify({"error": "Group already exists"}), 400

    # new_group = Group(group_name=group_name)
    # db.session.add(new_group)
    # db.session.commit()
    # return jsonify({"message": "Group created successfully"}), 201
    # return jsonify({"message": "Add group page", "group": group}), 201

# health: can it execute in db
@app.route('/health', methods=['GET'])
def health_check():
    try:
        db.session.execute(text('SELECT 1'))
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500
    
# readiness: db connection
def is_database_connected():
    return True

@app.route('/readiness', methods=['GET'])
def readiness_check():
    if is_database_connected():
        return jsonify({"status": "ready"}), 200
    else:
        return jsonify({"status": "not ready"}), 500
 
# metrics
@app.route('/metrics', methods=['GET'])
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
