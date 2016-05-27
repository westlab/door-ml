import json

import falcon


class Trend:
    def __init__(self, cxt):
        self._cxt = cxt

    def on_get(self, req, resp):
        resp.body = json.dumps(dict(foo="bar"))
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200
