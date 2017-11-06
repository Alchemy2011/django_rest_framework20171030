from django.db import models

# Create your models here.


class Post(models.Model):
    """
    贴子
    """
    pid = models.BigIntegerField(primary_key=True, default=0)
    title = models.CharField(max_length=256)
    preview = models.CharField(max_length=512, blank=True)  # 预览图
    video = models.CharField(max_length=512, blank=True)
    video_format = models.CharField(max_length=512, blank=True)
    category = models.CharField(max_length=512)
    created_at = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    play_counts = models.IntegerField()
    like_counts = models.IntegerField()
    thumbnail = models.CharField(max_length=512, blank=True)  # 缩略图

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title

    def increase_views(self):
        self.play_counts += 1
        self.save(update_fields=['play_counts'])


class Composer(models.Model):
    """
    作者
    """
    cid = models.BigIntegerField(primary_key=True, default=0)
    banner = models.CharField(max_length=256)  # 横幅广告
    avatar = models.CharField(max_length=512)  # 头像
    verified = models.BooleanField(default=0)  # 已验证
    name = models.CharField(max_length=128)
    intro = models.TextField(blank=True)
    like_counts = models.IntegerField(blank=True)
    play_counts = models.IntegerField()
    fans_counts = models.IntegerField()
    follow_counts = models.IntegerField()

    class Meta:
        db_table = 'composers'

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    评论
    """
    comment_id = models.IntegerField(primary_key=True)
    pid = models.BigIntegerField()
    cid = models.BigIntegerField()
    avatar = models.CharField(max_length=512, blank=True)  # 头像
    username = models.CharField(max_length=512, blank=True)  # 用户名称
    created_at = models.CharField(max_length=128)
    content = models.TextField(blank=True)
    like_counts = models.IntegerField(blank=True)
    reply = models.IntegerField()  # 回复

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.content


class Copyright(models.Model):
    """
    版权，关联表
    """
    pcid = models.CharField(primary_key=True, max_length=32)
    pid = models.BigIntegerField()
    cid = models.BigIntegerField()
    roles = models.CharField(max_length=32)

    class Meta:
        db_table = 'copyrights'

    def __str__(self):
        return self.pcid
