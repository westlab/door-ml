import falcon

from door_ml.api import Trend
from door_ml.middleware import CORSMiddleware

api = falcon.API(middleware=[CORSMiddleware()])

trend = Trend()

api.add_route('/v1/trend', trend)
