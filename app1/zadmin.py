#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app1.models import *
from Zadmin.service import zadmin
from django.utils.safestring import mark_safe

class BookAdmin(zadmin.ZModelAdmin):
    def edit(self, obj=None, is_header=False):
        if is_header:
            return '编辑'
        url = '<a href="%s/change">编辑</a>'%obj.nid
        return mark_safe(url)

    list_display = ('title', 'publishDate',edit)

zadmin.site.register(Book, BookAdmin)
