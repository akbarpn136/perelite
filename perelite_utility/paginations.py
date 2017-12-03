import json

from django.conf import settings
from django.http import HttpResponse
from rest_framework import status


class Pagination:
    def __init__(self, req_get, query, params='page'):
        """
        Pagination init
        :param req_get: something like self.request.GET
        :param query: Queryset like models.q.objects
        :param params: URL parameters for page number like 'page'
        """

        self.req_get = req_get
        self.query = query
        self.params = params

    def paginate(self):
        """
        Do paginate from queryset
        :return:  Mongo list object
        """

        if self.params in self.req_get:
            page_nb = int(self.req_get.get(self.params))

        else:
            page_nb = 1

        offset = (page_nb - 1) * settings.ITEMS_PER_PAGE
        count = self.query.count()

        if offset > count:
            offset = settings.ITEMS_PER_PAGE

        try:
            q = self.query.skip(offset).limit(settings.ITEMS_PER_PAGE)

            return q.to_json()

        except ValueError:
            return HttpResponse(json.dumps({
                'detail': 'Must be greater than 0'
            }), status=status.HTTP_400_BAD_REQUEST)
