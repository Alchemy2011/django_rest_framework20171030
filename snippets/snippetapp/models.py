# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# 语法分析程序，高亮显示，官方教程里提供的，看不懂没关系
# STEP <这里代码倒着看>
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# STEP <读代码顺序，先看类>
class Snippet(models.Model):
    # 惯例，新加的模型都要加一个created字段
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    # 是否启动行号
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        # 加负号就是倒序-created
        ordering = ('created',)
