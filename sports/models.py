from django.db import models
from django.contrib.auth.models import User

from django.db import models
# models sports_news
# Create your models here.
class Articles(models.Model):
    tittle = models.CharField('Название', max_length=150)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    data = models.DateTimeField('Дата')
    user = models.ForeignKey('auth.User',null=True, on_delete=models.CASCADE)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Articles, self).form_valid(form)

    def __str__(self):
        return self.tittle
    def get_absolute_url(self):
        return f'/sports/{self.id}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"