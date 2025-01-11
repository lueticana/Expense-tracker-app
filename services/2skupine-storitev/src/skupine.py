from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, Group, GroupMember

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123121@localhost:5432/skupine'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'my_jwt_secret_key'

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)

# Routes
@app.route('/', methods=['GET'])
def groups():
    current_user = get_jwt_identity()
    

    groups = GroupMember.query.filter_by(user_id=current_user)

    return jsonify(groups), 200


@app.route('/groups', methods=['POST'])
def create_group():
    data = request.json
    group_name = data.get('group_name')

    if Group.query.filter_by(group_name=group_name).first():
        return jsonify({"error": "Group already exists"}), 400

    new_group = Group(group_name=group_name)
    db.session.add(new_group)
    db.session.commit()
    return jsonify({"message": "Group created successfully"}), 201


@app.route('/groups/<int:group_id>/add-member', methods=['POST'])
@jwt_required()
def add_member(group_id):
    data = request.json
    user_id = data.get('user_id')

    group = Group.query.get(group_id=group_id)
    if not group:
        return jsonify({"error": "Invalid group id"}), 401
    
    if GroupMember.query.filter_by(group_id=group_id, user_id=user_id).first():
        return jsonify({"error": "User is already a member"}), 400
    
    new_member = GroupMember(group_id=group_id, user_id=user_id)
    db.session.add(new_member)
    db.session.commit()
    return jsonify({"message": "Member added to group"}), 200

@app.route('/group/<int:group_id>', methods=['GET'])
@jwt_required()
def get_group(group_id):
    group = Group.query.get(group_id=group_id)

    if not group:
        return jsonify({"error": "Invalid group id"}), 404
    
    members = GroupMember.query.filter_by(group_id=group_id).all()
    members_list = [{"username": member.username, "email": member.email, "user_id": member.id} for member in members]
    return jsonify({
        "group_id": group_id,
        "group_name": group.group_name,
        "members": members_list 
    }), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
