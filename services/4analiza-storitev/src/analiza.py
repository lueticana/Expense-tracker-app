from flask import Flask, request, jsonify, Response
from sqlalchemy import text
from models import db
from prometheus_client import generate_latest, Counter, Histogram
import time
from flask_cors import CORS
#from confluent_kafka import Consumer
import json

app = Flask(__name__)
CORS(app)

# config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123121@db_analiza:5432/analiza'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# metrics
REQUEST_COUNT = Counter('request_count', 'Total number of requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['endpoint'])

# #kafka
# consumer = Consumer({
#     'bootstrap.servers': 'localhost:9092',
#     'group.id': 'analysis-group',
#     'auto.offset.reset': 'earliest'
# })

# consumer.subscribe(['expenses-to-analysis'])

# def process_expenses():
#     try:
#         while True:
#             msg = consumer.poll(1.0)
#             if msg is None:
#                 continue
#             if msg.error():
#                 print(f"Consumer error: {msg.error()}")
#                 continue

#             # Process the message
#             expense_data = json.loads(msg.value().decode('utf-8'))
#             print(f"Received data: {expense_data}")
#     except KeyboardInterrupt:
#         pass
#     finally:
#         consumer.close()

# # Example usage
# #process_expenses()

# db
db.init_app(app)

# ENDPOINTs

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
    return jsonify({"message": "Analysis page"}), 201

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
    app.run(debug=True, host='0.0.0.0', port=5003)
