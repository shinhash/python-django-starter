from django.shortcuts import render
from django.template.loader import render_to_string

from blog.utils import *


# Create your views here.
def posts(request):
    query_params = {
        'query_id': 'selectPostList',
        'board_id': 'BD001',
        'post_id': '',
    }
    sql = render_to_string('blog/back/sql/post.sql', query_params)
    list = dict_sel_posts(sql)
    print("list : ", list)
    context = {
        'post_list': list
    }
    return render(request, 'blog/front/posts.html', context)
