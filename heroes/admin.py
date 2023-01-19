
from django.contrib import admin
from .models import Hero, Element, Country


admin.site.register(Hero)

class HeroAdmin(admin.ModelAdmin):
    fields = ['name', 'element', 'photo']

    # def get_image(self.obj):
    #     return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    #  get_image.short_description='Изображение'