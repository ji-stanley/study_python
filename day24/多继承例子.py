# __author__: Stanley
# date: 2018/5/28

class BaseRequest():
    def __init__(self):
        print("BaseRequest.init")

class RequestHandler(BaseRequest):
    def __init__(self):
        print("RequestHandler.init ")
        super(RequestHandler, self).__init__()

    def server_forever(self):
        print("RequestHandler.server_forever")
        self.process_request()

    def process_request(self):
        print("RequestHandler.process_request")

class Minx:
    def process_request(self):
        print("minx.process_request")

class Son(Minx, RequestHandler):
    pass
obj = Son()
obj.server_forever()


import  socketserver
obj = socketserver.ThreadingTCPServer(1,2)
obj.serve_forever()