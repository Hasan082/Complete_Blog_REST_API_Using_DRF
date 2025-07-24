from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math

class BlogPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        page_size = int(self.get_page_size(self.request))
        count = self.page.paginator.count
        total_pages = math.ceil(count / page_size) if page_size else 1
        current_page = self.page.number

        return Response({
            'count': count,
            'page_size': page_size,
            'current_page': current_page,
            'total_pages': total_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
