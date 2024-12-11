from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Simulating a users database
users = [
    { 'id': 1, 'name': 'Daniela Cáceres' },
    { 'id': 2, 'name': 'Juan Pérez' }
]

# Swagger URL (API documentation)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

# Configuring Swagger UI
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Base URL to access Swagger
    API_URL,      # URL for the swagger.json file
    config={'app_name': "My REST API with Swagger"}
)

# Register Swagger UI blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Define API routes
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user)

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

# Serve the swagger.json file
@app.route('/static/swagger.json')
def swagger_json():
    return jsonify({
        "swagger": "2.0",
        "info": {
            "title": "My REST API",
            "description": "REST API Documentation",
            "version": "1.0.0"
        },
        "host": "127.0.0.1:5000",
        "basePath": "/",
        "paths": {
            "/users": {
                "get": {
                    "summary": "Get all users",
                    "responses": {
                        "200": {
                            "description": "List of users",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/User"
                                }
                            }
                        }
                    }
                },
                "post": {
                    "summary": "Create a new user",
                    "responses": {
                        "201": {
                            "description": "User created",
                            "schema": {
                                "$ref": "#/definitions/User"
                            }
                        }
                    }
                }
            },
            "/users/{id}": {
                "get": {
                    "summary": "Get a user by ID",
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "required": True,
                            "type": "integer"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "User found",
                            "schema": {
                                "$ref": "#/definitions/User"
                            }
                        },
                        "404": {
                            "description": "User not found"
                        }
                    }
                }
            }
        },
        "definitions": {
            "User": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    }
                }
            }
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
