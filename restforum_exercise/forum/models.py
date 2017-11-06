from django.db import models

# Create your models here.
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible  # 向前兼容
class Topic(models.Model):
    """
    话题
    """
    content = models.CharField(max_length=200)  # django官方文档最大长度
    # 级联删除
    user = models.ForeignKey('auth.User', related_name='topics_of', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)  # 这两条直接复制
    updated = models.DateTimeField(auto_now=True)  # 几乎每个应用都会有

    def __str__(self):
        return self.content


@python_2_unicode_compatible  # 向前兼容
class Comment(models.Model):
    """
    评论
    """
    content = models.CharField(max_length=200)  # django官方文档最大长度

    created = models.DateTimeField(auto_now_add=True)  # 这两条直接复制
    updated = models.DateTimeField(auto_now=True)  # 几乎每个应用都会有

    # 评论还有什么字段？不知道，评论是哪个话题的，评论的人是谁
    # 模型模块的外键类，实例化谁，那么就是谁的外键
    topic = models.ForeignKey(Topic, related_name='topic_comments_of', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='user_comments_of',
                             on_delete=models.CASCADE, blank=True, null=True)
