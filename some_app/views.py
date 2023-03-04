from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request, params=None):
        return render(request, 'some_app/index.html')
