"""
View to the GraphQL endpoint.

Import the View class and use it in Django's urlpatterns.
"""
from django.views import View
from django.http import HttpResponse
from graphql import graphql


class View(View):
    def _process(self, query):
        result = graphql(schema, query)
        return HttpResponse(result)

    def get(self, request):
        query = request.GET.get('q')
        return self._process(query)
