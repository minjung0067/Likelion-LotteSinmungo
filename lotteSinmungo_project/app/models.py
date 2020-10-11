from django.db import models

class Problem (models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True) 

class myUser(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    objects = models.Manager()
    username = models.CharField(max_length=64,verbose_name = '사용자명')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')
    
    def __str__(self): # 이 함수 추가
        return self.username  # User object 대신 나타낼 문자 

    class Meta:
        db_table = 'test_user'
