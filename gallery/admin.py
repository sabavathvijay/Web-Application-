from django.contrib import admin
from .models import gallery,buy_art 
@admin.register(gallery)
class galleryAdmin(admin.ModelAdmin):
    list_display=['id','title','owner','price']
@admin.register(buy_art)
class artAdmin(admin.ModelAdmin):
    list_display=['id','user','art']