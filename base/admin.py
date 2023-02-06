from django.contrib import admin

# Register your models here.

from .models import Post, Comment, Baqueros, Caballos, FloraFauna

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Baqueros)
admin.site.register(Caballos)
admin.site.register(FloraFauna)
