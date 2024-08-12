from django.db import models
from django.conf import settings
from apps.users.models import User

class Post(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    picture = models.ImageField(verbose_name='Картина', 
                                upload_to='images/', 
                                null=True,
                                blank=True)
    publication_time = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    content = models.TextField(verbose_name=' Контент')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural= 'Посты'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name='Комментарий')
    publication_time = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)

    def __str__(self) -> str:
        return f'Комментарий от {self.author} к посту {self.post}'