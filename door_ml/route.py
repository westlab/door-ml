import falcon

from door_ml.api import Trend
from door_ml.middleware import CORSMiddleware
from door_ml.context import cxt

api = falcon.API(middleware=[CORSMiddleware(cxt)])

trend = Trend(cxt)

api.add_route('/v1/trend', trend)
