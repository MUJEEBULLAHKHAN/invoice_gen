from django.db import models
from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
from django.shortcuts import reverse
import random
from django.conf import settings
from django.contrib.auth.models import User

class contacts(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField('Name   اسم',max_length=255)
    c_phone = models.CharField('Phone Number   رقم التليفون',max_length=13)
    c_mail = models.CharField('Mail Address   عنوان البريد',max_length=100)
    c_category = models.CharField('Category   فئة',max_length=100)
    c_description = models.TextField('Description   وصف')
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.c_name + self.c_mail

class invoice_data(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number =models.CharField('Invoice Number   رقم الفاتورة',unique=True, max_length=200)
    date_time =models.DateTimeField(auto_now=True)
    issue_date = models.DateTimeField(auto_now=True)
    supply_date = models.DateTimeField(auto_now=True)
    terms = models.CharField('Terms   مصطلحات',max_length=200)
    sales_man = models.CharField('Sales Man   مندوب مبيعات',max_length=200)
    customer_ref = models.CharField('Customer Reference   إشارة العملاء',max_length=200)
    customer_id = models.CharField('Customer ID   هوية الزبون',max_length=100)
    customer_name = models.CharField('Customer Name   اسم الزبون',max_length=100)
    customer_address = models.CharField('Customer Address   عنوان العميل',max_length=100)
    # bill_to_building_no = models.CharField('bill_to_building_no   فاتورة لرقم المبنى',max_length=100)
    # bill_to_street_name = models.CharField('bill_to_street_name   فاتورة لاسم الشارع',max_length=100)
    # bill_to_disctrict = models.CharField('bill_to_disctrict   مشروع قانون للتخلص',max_length=100)
    customer_city =models.CharField('Customer City    مدينة العميل',max_length=100)
    customer_contact_name = models.CharField('Customer Contact Name   اسم جهة اتصال العميل',max_length=100)
    customer_contact_tel = models.CharField('Customer Contact Telephone   هاتف جهة اتصال العملاء',max_length=100)
    # bill_to_country =models.CharField('bill_to_country   فاتورة للبلد',max_length=100)
    customer_postal_code = models.CharField('Customer Postal Code   الرمز البريدي للعميل',max_length=100)
    # bill_to_additional_no = models.CharField('bill_to_additional_no   فاتورة لرقم إضافي',max_length=100)
    customer_vat_number = models.CharField('Customer VAT Number   رقم ضريبة القيمة المضافة للعميل',max_length=100)
    # bill_to_other_seller_id = models.CharField('bill_to_other_seller_id   فاتورة لمعرف البائع الآخر',max_length=100)
    seller_id = models.CharField('Seller ID    معرف البائع',max_length=100)
    seller_name = models.CharField('Seller Name    البائع اسم',max_length=100)
    # workshop_building_no = models.CharField('workshop_building_no   رقم مبنى الورشة',max_length=100)
    # workshop_street_name = models.CharField('workshop_street_name   اسم شارع ورشة العمل',max_length=100)
    # workshop_disctrict = models.CharField('workshop_district   ورشة عمل ديسبكتريكت',max_length=100)
    seller_address = models.CharField('Seller Address    عنوان البائع',max_length=100)
    seller_city =models.CharField('Seller City    مدينة البائع',max_length=100)
    seller_contact_name = models.CharField('Seller Contact Name    اسم جهة اتصال البائع',max_length=100)
    # workshop_country =models.CharField('workshop_country   بلد ورشة العمل',max_length=100)
    seller_contact_tel = models.CharField('Seller Contact Telephone    هاتف الاتصال بالبائع',max_length=100)
    seller_postal_code = models.CharField('Seller Postal Code   رمز البائع البريدي',max_length=100)
    seller_vat_number = models.CharField('Seller VAT Number   رقم ضريبة القيمة المضافة للبائع',max_length=100)
    # workshop_additional_no = models.CharField('workshop_additional_no   رقم ورشة العمل الإضافي',max_length=100)
    # workshop_vat_number = models.CharField('workshop_vat_number   رقم ضريبة القيمة المضافة لورشة العمل',max_length=100)
    # workshop_other_seller_id = models.CharField('workshop_other_seller_id   ورشة عمل معرف البائع الآخر',max_length=100)
    seller_IBAN = models.CharField('Seller IBAN Number   رقم IBAN للبائع',max_length=100)
    vehicle_make = models.CharField('Vehicle Make   صناعة المركبات',max_length=100)
    vehicle_model = models.CharField('Vehicle Model   طراز السيارة',max_length=100)
    vehicle_model_year = models.CharField('Vehicle Model Year   سنة صنع السيارة',max_length=100)
    vehicle_plate_info = models.CharField('Vehicle Plate Information   معلومات لوحة المركبة',max_length=100)
    vehicle_vin = models.CharField('Vehicle VIN Number   رقم VIN للمركبة',max_length=100)
    claim_number = models.CharField('Claim Number   رقم المطالبة',max_length=100)
    insurance_name = models.CharField('Insurance Name   اسم التأمين',max_length=100)
    assessor_name = models.CharField('Assessor Name   اسم المقيم',max_length=100)
    line_item = models.BooleanField(default=False)
    user_id = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.invoice_id)

class line_items(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_code = models.CharField('Item Code   رمز الصنف',max_length=100 ,blank =True)
    # nature = models.CharField('nature   طبيعة سجية',max_length=100 ,blank =True)
    item_name = models.CharField('Item Name   اسم العنصر',max_length=100 ,blank =True)
    pack = models.CharField('Pack   رزمة',max_length=100 ,blank =True)
    quantity = models.CharField('Quantity   كمية',max_length=100 ,blank =True)
    unit_price = models.CharField('Unit Price   سعر الوحدة',max_length=100 ,blank =True)
    taxable_amount = models.CharField('Taxable Amount   المبلغ الخاضع للضريبة',max_length=100,blank=True)
    discount = models.CharField('Discount   تخفيض',max_length=100, blank = True)
    tax_rate = models.CharField('Tax Rate   معدل الضريبة',max_length=100 ,blank =True)
    tax_amount = models.CharField('Tax Amount   قيمة الضريبة',max_length=100 ,blank =True)
    item_sub_total_including_vat = models.CharField('Item Subtotal Including VAT   إجمالي البند بما في ذلك ضريبة القيمة المضافة',max_length=100 ,blank =True)
    invoice = models.ForeignKey(invoice_data, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.item_id

class item_cal(models.Model):
    cal_id = models.AutoField(primary_key=True)
    total_excluding_vat = models.CharField('Total Excluding VAT   الإجمالي باستثناء ضريبة القيمة المضافة',max_length=100 ,blank =True)
    total_discount = models.CharField('Total Discount   إجمالي الخصم',max_length=100, blank=True)
    total_taxable_amount_excluding_vat = models.CharField('Total Taxable Amount Excluding VAT   إجمالي المبلغ الخاضع للضريبة  باستثناء الضريبة على القيمة المضافة',max_length=100 ,blank =True)
    net_excluding_VAT = models.CharField('Net Excluding VAT   صافي باستثناء ضريبة القيمة المضافة',max_length=100 ,blank =True)
    total_vat_15perc = models.CharField('Total VAT 15%   إجمالي ضريبة القيمة المضافة 15٪',max_length=100 ,blank =True)
    net_amount = models.CharField('Net Amount   كمية الشبكة',max_length=100 ,blank =True)
    excess_amount_plus_VAT = models.CharField('Excess Amount + VAT   المبلغ الزائد + ضريبة القيمة المضافة',max_length=100 ,blank =True)
    deprecation_amount_plus_VAT = models.CharField('Deprecation Amount + VAT   مبلغ الإيقاف + ضريبة القيمة المضافة',max_length=100 ,blank =True)
    total_amount_due = models.CharField('Total Amount Due   إجمالي المبلغ المستحق',max_length=100 ,blank =True)
    remarks = models.CharField('Remarks   ملاحظات', max_length=100 ,blank =True)
    invoice = models.ForeignKey(invoice_data, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.cal_id

class files(models.Model):
    qr_id = models.AutoField(primary_key=True)
    url=models.URLField()
    image=models.ImageField(upload_to='qr_codes/',blank=True)
    invoice = models.ForeignKey(invoice_data, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.url)
        canvas=Image.new("RGB", (2000,2000),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)

class files2(models.Model):
    pdf_id = models.AutoField(primary_key=True)
    pdf_file = models.FileField(upload_to='pdf_files/', blank=True)
    invoice = models.ForeignKey(invoice_data, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    

class L2(models.Model):
    license_id =models.AutoField(primary_key=True,unique=True)
    license_key = models.CharField(max_length=5000)
    user_id = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.license_id

