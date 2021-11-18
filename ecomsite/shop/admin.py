from django.contrib import admin
from .models import Products,Order
    
# Register your models here.
admin.site.site_header = "Online Shoping"
admin.site.site_title = "Online ecom shop"
admin.site.index_title = "Manage Online Shop "

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category = "default")

    def change_category_to_number(self,request,questyset):
        questyset.update(price="50")
    
    
    #price
    change_category_to_number.short_description = "Update Price"

    #instade of writing function you can simply do default by only  line
    change_category_to_default.short_description = 'Default Category' 
    list_display = ('title','price','discount_price','category','description',)
    search_fields = ('title',)
    actions = ('change_category_to_default',)
    actions = ('change_category_to_number',)
    fields = ('title','price',   )
    list_editable = ('price','category',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
