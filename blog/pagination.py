from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BlogPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = "page_size"
    max_page_size = 96

    # Create a list of page numbers (1, 2, 3, ..., total_pages)
    def get_paginated_response(self, data):
        total_pages = self.page.paginator.num_pages
        current_page = self.page.number

        page_range = list(range(1, total_pages + 1))

        # Optional: If you want to show a range of pages around the current page
        # page_range = self.get_page_range(current_page, total_pages)
        
        return Response(
            {
                "pagination": {
                    "count": self.page.paginator.count,
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                    "current_page": current_page,
                    "total_pages": total_pages,
                    "page_range": page_range,
                },
                "results": data,
            }
        )

    # # Optional: If you want to show a range of pages around the current page
    # # This method can be customized to show a specific range of pages
    # # For example, showing 2 pages before and after the current page
    # # Uncomment if you want to use this feature
    # def get_page_range(self, current_page, total_pages, surrounding=2):
    #     # Ensure the page range is within bounds
    #     start = max(1, current_page - surrounding)  # Minimum of 1
    #     end = min(total_pages, current_page + surrounding)  # Maximum of total_pages

    #     # Generate the page numbers to show
    #     return list(range(start, end + 1))
