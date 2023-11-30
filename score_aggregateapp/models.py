from django.db import models

# Create your models here.
from accounts.models import CustomUser
class Category(models.Model):
    title = models.CharField(
        verbose_name='科目',
        max_length=20)
    def __str__(self):
        return self.title
class ScoreAggregateappPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
        )
    category = models.ForeignKey(
        Category,
        verbose_name='科目',
        on_delete=models.PROTECT
        )
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    comment = models.TextField(
        verbose_name='コメント',
        )
    # image1 = models.ImageField(
    #     verbose_name='イメージ１',
    #     upload_to = 'score_aggregateapps'
    #     )
    # image2 = models.ImageField(
    #     verbose_name='イメージ２',
    #     upload_to = 'score_aggregateapps'
    #     )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
        )
    def __str__(self):
        return self.title
        