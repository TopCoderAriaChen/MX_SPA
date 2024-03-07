from werkzeug.exceptions import NotFound
def paginate(query_set, page_num, per_page_limit=10):
    try:
        paginated_objects = query_set.paginate(page=page_num, per_page=per_page_limit)
        return {
            "total": paginated_objects.total,
            "page": page_num,
            "pages": paginated_objects.pages,
            "limit": per_page_limit,
            "items": list(paginated_objects.items),
        }
    except NotFound:
        raise NotFound("Page not found")
