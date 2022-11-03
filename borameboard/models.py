from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200, verbose_name='글 제목', help_text='*제목은 최대 100자 이내')
    author = models.CharField(max_length=100, verbose_name='글쓴이')
    content = models.TextField(verbose_name='글 내용')
    published_date = models.DateTimeField(auto_now=True, verbose_name='등록(수정)일')
    
    def __str__(self) :    #객체가 생성되면 객체를 문자열로 반환해주는 함수,여기선 제목 반환
        return self.title
    
