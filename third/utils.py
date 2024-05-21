import os
from datetime import datetime
from uuid import uuid4


def image_path_rename(filename):
    ext = filename.split('.')[-1]

    now = datetime.now()
    this_time = now.strftime('%Y%m%d%H%M%S')
    time_uuid = this_time + '_' + uuid4().hex
    file_trance_name = '{}.{}'.format(time_uuid, ext)

    return file_trance_name
