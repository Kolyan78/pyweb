from datetime import datetime
from random import random

from django.views import View
from django.http import HttpRequest, HttpResponse


class DatetimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()

        return HttpResponse(now)

class RandomView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        rand = f"Случайное число: <b>{round(random() * 10, 2)}</b>"

        return HttpResponse(rand)