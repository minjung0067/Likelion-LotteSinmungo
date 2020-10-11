from django.db import models


class myUser(models.Model): 
    objects = models.Manager()
    username = models.CharField(max_length=64,verbose_name = '사용자명')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')
    
    def __str__(self):
        return self.username  

    class Meta:
        db_table = 'test_user'
class Problem (models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    userid = models.IntegerField()
