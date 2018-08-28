from django.contrib import admin

# Register your models here.
from app1.models import *

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     def xxx(self, obj):
#         return 'xxx'
#
#     list_display = ['nid','title', 'publish', 'xxx']
#     list_display_links = ['title']


from django.utils.translation import ugettext_lazy as _

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    empty_value_display = "列数据为空时，默认显示"

    list_display = ('title', 'publishDate', 'up')

    def up(self, obj):
        try:
            return obj.publish.name
        except Exception:
            return None

    up.empty_value_display = "指定列数据为空时，默认显示"

admin.site.register(Author)
admin.site.register(AuthorDetail)

admin.site.site_url = 'hahah'

