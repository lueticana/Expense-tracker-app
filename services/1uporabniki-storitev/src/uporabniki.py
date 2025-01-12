from flask import Flask, request, jsonify, Response
from models import db, User
from sqlalchemy import text
from prometheus_client import generate_latest, Counter, Histogram
import time

app = Flask(__name__)

# config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123121@db_user:5432/uporabniki'
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
    return jsonify({"message": "Users page"}), 201

# register
@app.route('/register', methods=['POST'])
def register_user():
    # data = request.json
    # username = data.get('username')
    # email = data.get('email')
    # password = data.get('password')

    # if User.query.filter_by(email=email).first():
    #     return jsonify({"error": "Email already exists"}), 400

    # new_user = User(username=username, email=email)
    # new_user.set_password(password)
    # db.session.add(new_user)
    # db.session.commit()
    # return jsonify({"message": "User registered successfully"}), 201
    return jsonify({"message": "Register page"}), 201

# login
@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return jsonify({"message": "Login valid"}), 200
    #     access_token = create_access_token(identity={"id": user.id, "email": user.email})
    #     return jsonify({"access_token": access_token}), 200

    # return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"message": "Login invalid"}), 401

# profile
@app.route('/profile')
def get_profile():
    return jsonify({"message": "your profile"}), 200

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
    app.run(debug=True, host='0.0.0.0', port=5000)
