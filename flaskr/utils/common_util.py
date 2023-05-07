
from flask_sqlalchemy.pagination import QueryPagination


def get_page_info(pagination: QueryPagination = None):
    return {
        'total': pagination.total,
        'pageNum': pagination.page,
        'pageSize': pagination.per_page,
        'items': [item.to_dict() for item in pagination.items]}
