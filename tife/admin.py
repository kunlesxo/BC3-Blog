from django.contrib import admin
from .models import comment
from .models import like

from .models import Tife


class TifeAdmin(admin.ModelAdmin):
    list_display = (  'id', 'image', 'title', 'created_at')
    list_filter =["created_at"]
    search_fields = ['title', "content"]
admin.site.register(Tife, TifeAdmin)



class commentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'content',  'created_at')
    list_filter = ['created_at']
    search_fields = ['comment']
    
admin.site.register(comment, commentAdmin)


class likeAdmin(admin.ModelAdmin):
    list_display = ('id', 'like','tife', 'created_at')
    list_filter = ['created_at']
admin.site.register(like, likeAdmin)


