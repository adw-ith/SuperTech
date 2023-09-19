from django.contrib import admin
from .models import Category,Items,Tags,DisplayImages


admin.site.register(Category)
admin.site.register(Items)
admin.site.register(Tags)
admin.site.register(DisplayImages)