from django.conf import settings


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
        q = self.query.skip(offset).limit(settings.ITEMS_PER_PAGE)

        return q.to_json()
