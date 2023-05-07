from flask_sqlalchemy.pagination import QueryPagination


class PageInfo:
    def __init__(self, pagination: QueryPagination = None):
        self.page = pagination.page
        self.per_page = pagination.per_page
        self.total = pagination.total
        self.items = [item.to_dict() for item in pagination.items]

    @classmethod
    def get(cls, pagination: QueryPagination = None):
        info = PageInfo(pagination)
        return {
        'total': info.total,
        'page': info.page,
        'per_page': info.per_page,
        'list': [user.to_dict() for user in info.list]}