from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User
from sqlalchemy import text

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123121@db_user:5432/uporabniki'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'my_jwt_secret_key'

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Users page"}), 201


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

@app.route('/profile_mock')
def get_profile2():
    return jsonify({"message": "your profile"}), 200


# @app.route('/profile', methods=['GET'])
# @jwt_required()
# def get_profile():
#     current_user = get_jwt_identity()
#     return jsonify(current_user), 200


@app.route('/health', methods=['GET'])
def health_check():
    try:
        db.session.execute(text('SELECT 1'))
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
