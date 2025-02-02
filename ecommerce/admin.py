from django.contrib import admin
from django.apps import apps 
from django.contrib.admin.sites import AlreadyRegistered
from .models import Produk, Review

# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model) 
#     except AlreadyRegistered:
#         pass

class ProdukAdmin(admin.ModelAdmin):
    list_display = ['nama_produk']
    search_fields = ['nama_produk']
    list_per_page = 10


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['reviewers']
    search_fields = ['reviewers', 'produk__nama_produk']
    list_per_page = 10

admin.site.register(Produk, ProdukAdmin)
admin.site.register(Review, ReviewAdmin)