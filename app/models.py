#coding:utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)  # 标题
    category = models.CharField(max_length=50, blank=True)  # 标签
    date_time = models.DateTimeField(auto_now_add=True)  # 日期
    content = models.TextField(blank=True, null=True)  # 正文


def __unicod__(self):
    return self.title


class Meta:  # 按时间下降顺序
    ordering = ['-date_time']
