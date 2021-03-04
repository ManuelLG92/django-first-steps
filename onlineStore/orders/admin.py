from django.contrib import admin
from orders.models import Client, Article, Order

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display=('name','email','tlf') #Son los campos del modelo que se mostraran en el admin site
    search_fields=('name','email') #crea barra para buscar por nombre o email desde el admin site

class ArticleAdmin(admin.ModelAdmin):
    list_filter=("section",) #Crea una section lateral para filtrar por seccion o lo que queramos

class OrderAdmin(admin.ModelAdmin):
    list_display=('number','date','delivered')
    list_filter=('date','delivered',)
    date_hierarchy = 'date' #Detecta todos los meses para mostrarlos

admin.site.register(Client, ClientAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Order, OrderAdmin)

