from django import forms
from django.forms import widgets
from .models import invoice_data,line_items,contacts,L2,item_cal

class invoice_data_form(forms.ModelForm):
    class Meta:
        model = invoice_data
        fields = ["invoice_number","terms","sales_man","customer_ref","customer_id","customer_name","customer_address","customer_city","customer_contact_name","customer_contact_tel","customer_postal_code","customer_vat_number","seller_id","seller_name","seller_address","seller_city","seller_contact_name","seller_contact_tel","seller_postal_code","seller_vat_number","seller_IBAN","vehicle_make","vehicle_model","vehicle_model_year","vehicle_plate_info","vehicle_vin","claim_number","insurance_name","assessor_name"]
        widgets = {
                    "invoice_number" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "terms" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "sales_man" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "customer_ref" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "customer_id" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "customer_name" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "customer_address" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "customer_city" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "customer_contact_name" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "customer_contact_tel" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "customer_postal_code" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "customer_vat_number" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "seller_id" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "seller_name" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "seller_address" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "seller_city" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "seller_contact_name" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "seller_contact_tel" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "seller_postal_code" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "seller_vat_number" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "seller_IBAN" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "vehicle_make" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "vehicle_model" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "vehicle_model_year" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "vehicle_plate_info" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "vehicle_vin" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "claim_number" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "insurance_name" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "assessor_name" : forms.TextInput(attrs={'class' : 'form-control'}),
                  }

class line_items_form(forms.ModelForm):
    class Meta:
        model = line_items
        fields = ["item_code","item_name","pack","quantity","unit_price","taxable_amount","discount","tax_rate","tax_amount","item_sub_total_including_vat"]
        widgets = {
                    "item_code" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "item_name" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "pack" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "quantity" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "unit_price" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "taxable_amount" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "discount" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "tax_rate" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "tax_amount" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "item_sub_total_including_vat" : forms.TextInput(attrs={'class' : 'form-control'}),
                    }

class item_cal_form(forms.ModelForm):
    class Meta:
        model = item_cal
        fields = ["cal_id","total_excluding_vat","total_discount","total_taxable_amount_excluding_vat","net_excluding_VAT","total_vat_15perc","net_amount","excess_amount_plus_VAT","deprecation_amount_plus_VAT","total_amount_due","remarks"]
        widgets = {
                    "total_excluding_vat" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "total_discount" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "total_taxable_amount_excluding_vat" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "net_excluding_VAT" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "total_vat_15perc" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "net_amount" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "excess_amount_plus_VAT" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "deprecation_amount_plus_VAT" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "total_amount_due" : forms.TextInput(attrs={'class' : 'form-control'}),
                    "remarks" : forms.TextInput(attrs={'class' : 'form-control'}),
                    }

class contacts_form(forms.ModelForm):
    class Meta:
        model = contacts
        fields = ['c_name','c_phone','c_mail','c_category','c_description']
        widgets = {
            'c_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'c_phone' : forms.TextInput(attrs={'class' : 'form-control'}),
            'c_mail' : forms.TextInput(attrs={'class' : 'form-control'}),
            'c_category' : forms.TextInput(attrs={'class' : 'form-control'}),
            'c_description' : forms.Textarea(attrs={'class' : 'form-control'}),
        }


class L2_form(forms.ModelForm):
    class Meta:
        model = L2
        fields = ["license_id","license_key"]
        widgets = {
            'license_key' : forms.TextInput(attrs={'class' : 'form-control'})    
        }
