from django.contrib import admin
from air.models import City, Region, Comment, Counter

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('chinese_name', 'click',)
    search_fields = ('chinese_name',)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
	
class CounterAdmin(admin.ModelAdmin):
    list_display = ('city', 'night4', 'morning5', 'afternoon5', 'night5', 'morning6', 'afternoon6', 'night6',)
    search_fields = ('city',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'date_time', 'content')
    ordering = ('date_time',)
    

admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Counter,CounterAdmin)
