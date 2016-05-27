class CORSMiddleware:

    def __init__(self, cxt):
        self._cxt = cxt

    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
