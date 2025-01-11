from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from sqlalchemy import text
from models import db, Expense

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123121@db_expense:5432/stroski'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'my_jwt_secret_key'

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)

# Routes
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Expenses page"}), 201

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


# @app.route('/expenses', methods=['GET'])
# @jwt_required
# def get_expenses():

#     current_user = get_jwt_identity()
#     expenses = Expense.query.filter_by(payer_id=current_user['id']).all()

#     expenses_list = [{"id":expense.id, "description": expense.description, "amount": expense.amount} for expense in expenses]

#     return jsonify(expenses_list), 200

@app.route('/health', methods=['GET'])
def health_check():
    try:
        db.session.execute(text('SELECT 1'))
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
