from flask import Flask, request, jsonify, Response
from sqlalchemy import text
from models import db, Expense
from prometheus_client import generate_latest, Counter, Histogram
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123121@db_stroski:5432/stroski'
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
    return jsonify({"message": "Expenses page"}), 201

# add expense
@app.route('/expenses', methods=['POST'])
def add_expense():
    # data = request.json
    # description = data.get('description')
    # amount = data.get('amount_in_eur')
    # group_id = data.get('group_id')
    # payer_id = data.get('payer_id')

    # if not description or not amount:
    #     return jsonify({"error": "Description and amount are required"}), 400

    # if amount <= 0:
    #     return jsonify({"error": "Amount must be greater than zero"}), 400

    # new_expense = Expense(description=description, amount=amount, group_id=group_id, payer_id=payer_id)
    # db.session.add(new_expense)
    # db.session.commit()
    # return jsonify({"message": "Expense added successfully", "expense_id": new_expense.id}), 201
    return jsonify({"message": "Add expense page"}), 201

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
    app.run(debug=True, host='0.0.0.0', port=5002)
