import sys
from door_ml.context import cxt
from door_ml.conf import parse_conf, conf

# Provide params from gunicorn command line
# conf_file = ''
# cxt['conf'] = parse_conf(conf_file)

from door_ml.route import api
application = api
