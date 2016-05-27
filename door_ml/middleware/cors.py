class CORSMiddleware:
    def process_request(self, req, resp):
        resp.set_header('Acess-Control-Allow-Origin', '*')
