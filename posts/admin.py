from django.contrib import admin 
from .models import Post,Student,Comment,Tag

# Register your models here. 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','post_tittle','post_date']
    list_display_links=['id','post_tittle'] 
    list_filter=['post_date'] 
    search_fields=['post_tittle']
# admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
@admin.register(Student)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','name','stu_class']
    list_display_links=['id','name']
# admin.site.register(Student)

