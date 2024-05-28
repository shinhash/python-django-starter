{% if queryType == 'selectAll' %}
    SELECT   USER_ID
           , USER_PW
           , USER_NM
           , REG_DT
           , REG_USER_ID
           , REG_IP
           , MOD_DT
           , MOD_USER_ID
           , MOD_IP
           , USE_YN
           , SNS_SIGN_ID
      FROM HASH_SERVER.USERS
     WHERE 1 = 1
        {% if use_yn %}
          AND USE_YN = '{{ use_yn }}'
        {% endif %}
 {% endif %}

{% if queryType == 'selectOne' %}
    SELECT   USER_ID
           , USER_PW
           , USER_NM
           , REG_DT
           , REG_USER_ID
           , REG_IP
           , MOD_DT
           , MOD_USER_ID
           , MOD_IP
           , USE_YN
           , SNS_SIGN_ID
      FROM HASH_SERVER.USERS
     WHERE USER_ID = 'test@gmail.com'
 {% endif %}
;