from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter

from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

# Create your models here.
# 语法分析程序，高亮显示，官方教程里提供的，看不懂没关系
# STEP <这里代码倒着看>
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    # 只知道需要建立外键，但具体怎么用，忘了，查一下官方文档或之前写过的代码
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    # STEP <这个地方容易忘记，元组>
    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        # FIXME <这个地方如果有时间，就查一下文档，没有就算了>
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
