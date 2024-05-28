from django.db import connection
from django.shortcuts import render
from mariaDBProject.models import USERS
from django.template.loader import render_to_string
from django.db import connections
from mariaDBProject.utils import dict_fetchall


# Create your views here.
def user_list(request):

    # userList = USERS.objects.all()
    # print("userList : ", userList)
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(user_select_query('TT'))
    #     rows = cursor.fetchall()
    #     print("rows : ", rows)

    query_param = {
        'use_yn': 'Y',
        'queryType': 'selectAll',
    }
    sql = render_to_string('mariaDBProject/sql/user/user_list.sql', query_param)
    list = dict_fetchall(sql)
    print("list : ", list)

    context = {
        # 'userList' : rows,
    }
    return render(request, 'mariaDBProject/front/userList.html', context)


def user_select_query(params):
    query_select = " SELECT "
    query_colum_front = " USER_ID, USER_PW, USER_NM, "
    query_colum_back = " REG_DT, REG_USER_ID, REG_IP, MOD_DT, MOD_USER_ID, MOD_IP, USE_YN, SNS_SIGN_ID "
    query_from = " FROM HASH_SERVER.USERS "
    query_where = " WHERE USE_YN = 'Y' "
    query_text = query_select + query_colum_front + query_colum_back + query_from + query_where


    query_select = """
                        SELECT USER_ID, USER_PW, USER_NM,
                                REG_DT, REG_USER_ID, REG_IP, MOD_DT, 
                                MOD_USER_ID, MOD_IP, USE_YN, SNS_SIGN_ID 
                        FROM HASH_SERVER.USERS
                    """

    query_where = """
                    WHERE USE_YN = 'Y'
                  """

    query_text = query_select + query_where

    return query_text

