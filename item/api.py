from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Items(Resource):
    def get(self):
        return {
            'items': [
                'bag',
                'laptop',
                'cellphone',
                'wallet'
            ]
        }


# Routes
api.add_resource(Items, '/')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
