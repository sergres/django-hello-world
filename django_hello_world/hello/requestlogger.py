from django_hello_world.hello.models import RequestsStorage

class RequestLogger():
    def process_request(self, request):
        new_request = RequestsStorage(body = request.path, method = request.method)
        new_request.save(force_insert=True)
        #new_request.time will be set to now by default
        return None
