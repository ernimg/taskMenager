from django.contrib import admin
from .models import Tasks, Vote 
from django.utils.html import format_html
# admin.site.register(Tasks)
# admin.site.register(Vote)

class VoteInline(admin.TabularInline):
    model = Vote
@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id','title','priority','show_youtube_link']
    list_filter = ['priority']
    inlines = [VoteInline]
    def show_youtube_link(self,obj):
        if len(obj.URL)>0:
            return format_html(f'<a href="{obj.URL}">{obj.URL}</a>')
        else:
            return 'brak linku'

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
   list_display = ['id','tasks','usersVote']
   list_filter = ['tasks']
# Register your models here.
