from django.db import connections


def dict_fetchall(sql, using='mariadb'):
    with connections[using].cursor() as cursor:
        cursor.execute(sql)
        desc = cursor.description
        dict_arr = []
        for row in cursor.fetchall():
            zip_result = zip([col[0] for col in desc], row)
            dict_arr.append(dict(zip_result))

        return dict_arr
