from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando una base de datos de usuarios
users = [
    { 'id': 1, 'name': 'Daniela Cáceres' },
    { 'id': 2, 'name': 'Juan Pérez' }
]

# Obtener lista de usuarios
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Obtener un usuario por ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user)

# Crear un nuevo usuario con el mensaje
@app.route('/users', methods=['POST'])
def create_user():
    new_user = {
        'id': len(users) + 1,
        'name': 'Hy guys, my name is Daniela Cáceres'
    }
    users.append(new_user)
    return jsonify({
        'message': new_user['name'], 
        'user': new_user
    }), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
