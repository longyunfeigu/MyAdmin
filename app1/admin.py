from django.contrib import admin

# Register your models here.
from app1.models import *

admin.site.register(Book)
admin.site.register(Publish)
admin.site.register(Author)
admin.site.register(AuthorDetail)

