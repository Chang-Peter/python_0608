from django.contrib import admin
from mysite.models import Post, Country, City 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'pub_date')  #建立欄位

admin.site.register(Post, PostAdmin)
admin.site.register(Country)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name','population','country')
    
admin.site.register(City, CityAdmin)
