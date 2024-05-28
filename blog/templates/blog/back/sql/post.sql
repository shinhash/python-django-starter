{% if query_id == 'selectPostList' %}
    SELECT   BOARD_ID
           , POST_ID
           , POST_TITLE
           , POST_CONT
           , REG_DT
           , REG_USER_ID
           , REG_IP
           , MOD_DT
           , MOD_USER_ID
           , MOD_IP
           , USE_YN
      FROM HASH_SERVER.POST
     WHERE 1 = 1
    {% if board_id %}
        AND BOARD_ID = '{{ board_id }}'
    {% endif %}
    {% if post_id %}
        AND POST_ID = '{{ post_id }}'
    {% endif %}
{% endif %}