from django.shortcuts import render,HttpResponse
from django.views.generic import View


class Homepage(View):
    def get(self, request):
        return HttpResponse("<h2>Hi</h2>")

