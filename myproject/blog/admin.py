from django.contrib import admin

from blog.models import Blog


@admin.register ( Blog )
class BlogAdmin ( admin.ModelAdmin ):
    list_display = ('id', 'title')
    list_filter = ('counter_views',)
    search_field = ('title', 'flag_publication')

