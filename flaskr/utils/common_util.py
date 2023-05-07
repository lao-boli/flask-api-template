
from flask_sqlalchemy.pagination import QueryPagination


def get_page_info(pagination: QueryPagination = None):
    return {
        'total': pagination.total,
        'page': pagination.page,
        'per_page': pagination.per_page,
        'items': [user.to_dict() for user in pagination.items]}
