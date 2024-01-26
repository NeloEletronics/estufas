from flask import Flask
from flask_restful import Resource, Api
from SensorSHT30 import TemperatureSensor

app = Flask(__name__)
api = Api(app)

sensor = TemperatureSensor()


class Estufa2(Resource):
    def get(self):
        data = sensor.read()

        return data


api.add_resource(Estufa2, '/estufa/2')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
