from django.db import connections


def dict_sel_posts(sql, using='default'):
    with connections[using].cursor() as cursor:
        print(sql)
        cursor.execute(sql)
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]