from django.contrib import admin
from .models import invoice_data, line_items,files,contacts,files2,L2,item_cal
# Register your models here.

@admin.register(invoice_data)
class invoice_admin(admin.ModelAdmin):
    list_display = ('invoice_id','invoice_number','line_item','user_id')

@admin.register(line_items)
class line_admin(admin.ModelAdmin):
    list_display = ('item_id','item_name','invoice','user_id')

@admin.register(item_cal)
class itemcal_admin(admin.ModelAdmin):
    list_display = ('cal_id','invoice','user_id')

@admin.register(files)
class files_admin(admin.ModelAdmin):
    list_display = ('qr_id','url','image','invoice','user_id')

@admin.register(files2)
class files2_admin(admin.ModelAdmin):
    list_display = ('pdf_id','pdf_file','invoice','user_id')

@admin.register(contacts)
class contacts_admin(admin.ModelAdmin):
    list_display = ('c_id','c_name','c_phone','c_mail','timestamp')

@admin.register(L2)
class L2admin(admin.ModelAdmin):
    list_display = ('license_id','license_key')
