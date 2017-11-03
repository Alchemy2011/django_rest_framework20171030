from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag


# 来自django官方文档
class PostAdmin(admin.ModelAdmin):
    # 这里需要注意，自己竟然不知道该使用什么变量，结果弄了一个model=Post
    # 增加模型管理的目的是，在后台显示模型中希望显示的字段。
    list_display = ['title', 'content', 'category', ]


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Tag, TagAdmin)
