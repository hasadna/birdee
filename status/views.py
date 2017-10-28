from django.http.response import HttpResponse
from django.views.generic.base import View


class StatusView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('OK')
