from django.db import models


# Create your models here.
class USERS(models.Model):
    USER_ID = models.CharField(primary_key=True, max_length=50)
    USER_PW = models.CharField(max_length=30)
    USER_NM = models.CharField(max_length=50)
    REG_DT = models.CharField(max_length=20)
    REG_USER_ID = models.CharField(max_length=50)
    REG_IP = models.CharField(max_length=20)
    MOD_DT = models.CharField(max_length=50)
    MOD_USER_ID = models.CharField(max_length=50)
    MOD_IP = models.CharField(max_length=20)
    USE_YN = models.CharField(max_length=2)
    SNS_SIGN_ID = models.CharField(max_length=200)

    def __str__(self):
        return self.USER_ID
