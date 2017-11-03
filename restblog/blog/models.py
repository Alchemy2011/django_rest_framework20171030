# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    """
    类别
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 一般一篇文章有一个类别，但可以有多个标签
# 掌握修改代码的技巧，与类别极其相似，直接复制
@python_2_unicode_compatible
class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible  # 向前兼容
class Post(models.Model):
    """
    博文
    """
    title = models.CharField(max_length=70)  # 长度参考今日头条
    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)  # 这两条直接复制
    updated = models.DateTimeField(auto_now=True)  # 项目几乎都要有

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
