from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        return HttpResponse(exception)

