from django.shortcuts import render, HttpResponseRedirect,HttpResponse, redirect
from .forms import invoice_data_form,line_items_form,contacts_form,L2_form,item_cal_form
from .models import invoice_data,line_items,files,contacts,L2,item_cal
from fpdf import FPDF
from django.views.generic import View
from .utils import render_to_pdf 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
# def user_reg(request):
#  if request.method == 'POST':
#   fm = user_form(request.POST)
#   if fm.is_valid():
#             a = fm.cleaned_data['username']
#             d = fm.cleaned_data['password']
#             deg = user_data(username=a,password=d) # the reg is the foreign key of invoice table
#             deg.save()
#             return HttpResponse("registration successful!")
#  else:
#   fm = user_form()
#  return render(request, 'enroll/userregs.html', {'form':fm})




# def user_login(request):
#     if request.method=="POST":
#         # Get the post parameters
#         loginusername=request.POST['username']
#         loginpassword=request.POST['password']

#         user=authenticate(username= loginusername, password= loginpassword)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("home")
#         else:
#             messages.error(request, "Invalid credentials! Please try again")
#             return redirect("/")

#     # return HttpResponse("404- Not found")
   
#     else:
#         fm = user_form()
#     return render(request, 'enroll/userregs.html', {'form':fm})
#     # return HttpResponse("login")

# def user_login1(request):
#     if request.method=="POST":
#         fm = user_form(request.POST)
#         if fm.is_valid():
#         # Get the post parameters
#             user=fm.cleaned_data['username']
#             pwd=fm.cleaned_data['password']
#             use=authenticate(username= user, password= pwd)
#             if use is not None:
#                 login(request, use)
#                 messages.success(request, "Successfully Logged In")
#                 return HttpResponse("login success!")
#             else:
#                 messages.error(request, "Invalid credentials! Please try again")
#                 return HttpResponse("invalid login!")

#     else:
#         fm = user_form()
#     return render(request, 'enroll/userregs.html', {'form':fm})

# def user_logout(request):
#     logout(request)
#     messages.success(request, "Successfully logged out")
#     return HttpResponse("logged out!")

@login_required
def add_show(request):
 user = request.user
 if request.method == 'POST':
  fm = invoice_data_form(request.POST)
  if fm.is_valid():
            inv_1 = fm.cleaned_data['invoice_number']
            inv_2 = fm.cleaned_data['terms']
            inv_3 = fm.cleaned_data['sales_man']
            inv_4 = fm.cleaned_data['customer_ref']
            inv_5 = fm.cleaned_data['customer_id']
            inv_6 = fm.cleaned_data['customer_name']
            inv_7 = fm.cleaned_data['customer_address']
            inv_8 = fm.cleaned_data['customer_city']
            inv_9 = fm.cleaned_data['customer_contact_name']
            inv_10 = fm.cleaned_data['customer_contact_tel']
            inv_11 = fm.cleaned_data['customer_postal_code']
            inv_12 = fm.cleaned_data['customer_vat_number']
            inv_13 = fm.cleaned_data['seller_id']
            inv_14 = fm.cleaned_data['seller_name']
            inv_15 = fm.cleaned_data['seller_address']
            inv_16 = fm.cleaned_data['seller_city']
            inv_17 = fm.cleaned_data['seller_contact_name']
            inv_18 = fm.cleaned_data['seller_contact_tel']
            inv_19 = fm.cleaned_data['seller_postal_code']
            inv_20 = fm.cleaned_data['seller_vat_number']
            inv_21 = fm.cleaned_data['seller_IBAN']
            inv_22 = fm.cleaned_data['vehicle_make']
            inv_23 = fm.cleaned_data['vehicle_model']
            inv_24 = fm.cleaned_data['vehicle_model_year']
            inv_25 = fm.cleaned_data['vehicle_plate_info']
            inv_26 = fm.cleaned_data['vehicle_vin']
            inv_27 = fm.cleaned_data['claim_number']
            inv_28 = fm.cleaned_data['insurance_name']
            inv_29 = fm.cleaned_data['assessor_name']
            reg = invoice_data(invoice_number=inv_1,terms=inv_2,sales_man=inv_3,customer_ref=inv_4,customer_id=inv_5,customer_name=inv_6,customer_address=inv_7,customer_city=inv_8,customer_contact_name=inv_9,customer_contact_tel=inv_10,customer_postal_code=inv_11,customer_vat_number=inv_12,seller_id=inv_13,seller_name=inv_14,seller_address=inv_15,seller_city=inv_16,seller_contact_name=inv_17,seller_contact_tel=inv_18,seller_postal_code=inv_19,seller_vat_number=inv_20,seller_IBAN=inv_21,vehicle_make=inv_22,vehicle_model=inv_23,vehicle_model_year=inv_24,vehicle_plate_info=inv_25,vehicle_vin=inv_26,claim_number=inv_27,insurance_name=inv_28,assessor_name=inv_29,user_id=user)
            reg.save()
            ag = invoice_data.objects.get(pk=reg.invoice_id)
            # qr_data = f"Invoice_issue_date : {reg.date_time} \n invoice_number : {reg.invoice_number} \n insurance_info_name : {reg.insurance_info_name} \n insurance_info_claim_no : {reg.insurance_info_claim_no} \n insurance_info_assessor : {reg.insurance_info_assessor} \n make : {reg.make} \n model : {reg.model} \n vin : {reg.vin} \n plate_info : {reg.plate_info} \n bill_to_name : {reg.bill_to_name} \n bill_to_building_no : {reg.bill_to_building_no} \n bill_to_street_name : {reg.bill_to_street_name} \n bill_to_district : {reg.bill_to_disctrict} \n bill_to_city : {reg.bill_to_city} \n bill_to_country : {reg.bill_to_country} \n bill_to_postal_code : {reg.bill_to_postal_code} \n bill_to_additional_no : {reg.bill_to_additional_no} \n bill_to_vat_number : {reg.bill_to_vat_number} \n bill_to_other_seller_id : {reg.bill_to_other_seller_id} \n workshop_name : {reg.workshop_name} \n workshop_building_no : {reg.workshop_building_no} \n workshop_street_name : {reg.workshop_street_name} \n workshop_disctrict : {reg.workshop_disctrict} \n workshop_city : {reg.workshop_city} \n workshop_country : {reg.workshop_country} \n workshop_postal_code : {reg.workshop_postal_code} \n workshop_additional_no : {reg.workshop_additional_no} \n workshop_vat_number : {reg.workshop_vat_number} \n workshop_other_seller_id : {reg.workshop_other_seller_id}"  
            # a = files.objects.create(url=qr_data,invoice=reg)
            # print(a.qr_id)
            # imgg = files.objects.get(pk=a.qr_id)
            # return HttpResponseRedirect(f'/inv/{reg.invoice_id}',{'invoice_data':ag,'img':imgg})
            return render(request, 'enroll/cong.html', {'invoice_data':ag})
 else:
  fm = invoice_data_form()
 return render(request, 'enroll/addandshow.html', {'form':fm})



@login_required
def calculate(request,id):
 user = request.user
 if request.method == 'POST':
  item = invoice_data.objects.get(pk=id)
  fm = line_items_form(request.POST)
  if fm.is_valid():
            line_1 = fm.cleaned_data['item_code']
            line_2= fm.cleaned_data['item_name']
            line_3 = fm.cleaned_data['pack']
            line_4 = fm.cleaned_data['quantity']
            line_5 = fm.cleaned_data['unit_price']
            line_6 = fm.cleaned_data['taxable_amount']
            line_7 = fm.cleaned_data['discount']
            line_8 = fm.cleaned_data['tax_rate']
            line_9 = fm.cleaned_data['tax_amount']
            line_10 = fm.cleaned_data['item_sub_total_including_vat']
            deg = line_items(item_code=line_1,item_name=line_2,pack=line_3,quantity=line_4,unit_price=line_5,taxable_amount=line_6,discount=line_7,tax_rate=line_8,tax_amount=line_9,item_sub_total_including_vat=line_10,invoice=item,user_id=user) # the reg is the foreign key of invoice table
            deg.save()
            ag = invoice_data.objects.get(pk=item.invoice_id)
            bg = line_items.objects.filter(invoice=item.invoice_id)
            ego = line_items.objects.filter(invoice=item.invoice_id)
            fego = line_items.objects.get(pk=deg.item_id)
            fm = line_items_form()
            ag = invoice_data.objects.get(pk=id)
            return render(request, 'enroll/second.html', {'line_items_data':ego,'worm':fm,'invoice_data':ag,'line_items_data2':fego})
 else:
  fm = line_items_form()
  ag = invoice_data.objects.get(pk=id)
 stud = line_items.objects.all()
 return render(request, 'enroll/second.html', {'worm':fm, 'stu':stud,'invoice_data':ag})

def calculations(request,id):
 user = request.user
 if request.method == 'POST':
  item = invoice_data.objects.get(pk=id)
  fm = item_cal_form(request.POST)
  if fm.is_valid():
            line_1 = fm.cleaned_data['total_excluding_vat']
            line_2= fm.cleaned_data['total_discount']
            line_3 = fm.cleaned_data['total_taxable_amount_excluding_vat']
            line_4 = fm.cleaned_data['net_excluding_VAT']
            line_5 = fm.cleaned_data['total_vat_15perc']
            line_6 = fm.cleaned_data['net_amount']
            line_7 = fm.cleaned_data['excess_amount_plus_VAT']
            line_8 = fm.cleaned_data['deprecation_amount_plus_VAT']
            line_9 = fm.cleaned_data['total_amount_due']
            line_10 = fm.cleaned_data['remarks']
            deg = item_cal(total_excluding_vat=line_1,total_discount=line_2,total_taxable_amount_excluding_vat=line_3,net_excluding_VAT=line_4,total_vat_15perc=line_5,net_amount=line_6,excess_amount_plus_VAT=line_7,deprecation_amount_plus_VAT=line_8,total_amount_due=line_9,remarks=line_10,invoice=item,user_id=user) # the reg is the foreign key of invoice table
            deg.save()
            ag = invoice_data.objects.get(pk=item.invoice_id)
            bg = line_items.objects.filter(invoice=item.invoice_id)
            ego = line_items.objects.filter(invoice=item.invoice_id)
            # fego = line_items.objects.get(pk=deg.item_id)
            fm = line_items_form()
            ag = invoice_data.objects.get(pk=id)
            return render(request, 'enroll/qr3.html', {'worm':fm,'invoice_data':ag})
            # return render(request, 'enroll/second.html', {'line_items_data':ego,'worm':fm,'invoice_data':ag,'line_items_data2':fego})
 else:
  fm = item_cal_form()
  ag = invoice_data.objects.get(pk=id)
 stud = line_items.objects.all()
 return render(request, 'enroll/third.html', {'worm':fm, 'stu':stud,'invoice_data':ag})


@login_required
# This Function will Update/Edit
def update_data(request, id):
 if request.method == 'POST':
  pi = line_items.objects.get(pk=id)
  fm = line_items_form(request.POST, instance=pi)
  if fm.is_valid():
   fm.save()
   fm = line_items_form()
 else:
  pi = line_items.objects.get(pk=id)
  fm = line_items_form(instance=pi)
 return render(request, 'enroll/second.html', {'worm':fm,'invoice_data':pi})

@login_required
# This Function will Delete
def delete_data(request, id):
 if request.method == 'POST':
  pi = line_items.objects.get(pk=id)
  gr = model_to_dict(pi)
  cr = gr["invoice"]
  ag = invoice_data.objects.get(pk=cr)
  pi.delete()
  fm = line_items_form()
  stud = line_items.objects.all()
  return HttpResponseRedirect(f'/cal/{ag.invoice_id}', {'invoice_data':pi,'worm':fm,'line_items_data':stud})
 else:
  pi = line_items.objects.get(pk=id)
  fm = line_items_form(instance=pi)
  stud = line_items.objects.all()
 return render(request, 'enroll/second.html', {'invoice_data':pi,'worm':fm,'line_items_data':stud})

@login_required
def show_invoice(request,id):
    i1 = invoice_data.objects.get(pk=id)
    print(i1.invoice_id)
    l1 = line_items.objects.filter(invoice=i1.invoice_id)
    # l1 = line_items.objects.get(invoice=i1.invoice_id)
    qr = files.objects.get(invoice=i1.invoice_id)
    pr = item_cal.objects.get(invoice=i1.invoice_id)
    return render(request, 'enroll/invoice_data2.html', {'invoice_data':i1,'line_items':l1,'img':qr,'pro':pr})

@login_required
def generate_qr(request,id):
    user = request.user
    i1 = invoice_data.objects.get(pk=id)
    item_names = {"User":user.username,"Invoice":i1.invoice_number}
    l1 = line_items.objects.filter(invoice=i1.invoice_id)
    for c in l1:
        # Total Excluding VAT : {c.total_excluding_vat} Total Discount : {c.total_discount} Total Taxable Amount Excluding VAT : {c.total_taxable_amount_excluding_vat} Net Excluding VAT : {c.net_excluding_VAT} Total VAT 15% : {c.total_vat_15perc} Net Amount : {c.net_amount} Excess Amount + VAT : {c.excess_amount_plus_VAT} Deprecation Amount + VAT : {c.deprecation_amount_plus_VAT} Total Amount Due : {c.total_amount_due} Remarks : {c.remarks}
        item_names[f"Line Items {c.item_id}"]= {f"Item ID : {c.item_id} Item Code : {c.item_code} Item Name : {c.item_name} Pack : {c.pack} Quantity : {c.quantity} Unit Price : {c.unit_price} Taxable Amount : {c.taxable_amount} Discount : {c.discount} Tax Rate : {c.tax_rate} Tax Amount : {c.tax_amount} Item Subtotal Including VAT : {c.item_sub_total_including_vat}"}
    # l1 = line_items.objects.get(invoice=i1.invoice_id)
    qr_data= f"Invoice Information \n Invoice ID : {i1.invoice_id} \n Invoice Number : {i1.invoice_number} \n Date & Time : {i1.date_time} \n Issue Date : {i1.issue_date} \n Supply Date : {i1.supply_date} \n Terms : {i1.terms} \n Sales Man : {i1.sales_man} \n Customer Reference : {i1.customer_ref} \n Customer Information \n Customer ID : {i1.customer_id} \n Customer Name : {i1.customer_name} \n Customer Address : {i1.customer_address} \n Customer City : {i1.customer_city} \n Customer Contact Name : {i1.customer_contact_name} \n Customer Contact Telephone : {i1.customer_contact_tel} \n Customer Postal Code : {i1.customer_postal_code} \n Customer VAT Number : {i1.customer_vat_number} \n Seller Information \n Seller ID : {i1.seller_id} \n Seller Name : {i1.seller_name} \n Seller Address : {i1.seller_address} \n Seller City : {i1.seller_city} \n Seller Contact Name : {i1.seller_contact_name} \n Seller Contact Telephone : {i1.seller_contact_tel} \n Seller Postal Code : {i1.seller_postal_code} \n Seller VAT Number : {i1.seller_vat_number} \n Seller IBAN Number : {i1.seller_IBAN} \n Vehicle Information \n Vehicle Make : {i1.vehicle_make} \n Vehicle Model : {i1.vehicle_model} \n Vehicle Model Year : {i1.vehicle_model_year} \n Vehicle Plate Information : {i1.vehicle_plate_info} \n Vehicle VIN Number : {i1.vehicle_vin} \n Insurance Information \n Claim Number : {i1.claim_number} \n Insurance Name : {i1.insurance_name} \n Assessor Name : {i1.assessor_name} \n Line Items : {i1.line_item} \n User : {i1.user_id} \n\n\n Item Information : {item_names}"
    # qr_data= f"invoice_number : {i1.invoice_number} nature : {item_names}"
    # qr_data = f"Invoice_issue_date : {reg.date_time} \n invoice_number : {reg.invoice_number} \n insurance_info_name : {reg.insurance_info_name} \n insurance_info_claim_no : {reg.insurance_info_claim_no} \n insurance_info_assessor : {reg.insurance_info_assessor} \n make : {reg.make} \n model : {reg.model} \n vin : {reg.vin} \n plate_info : {reg.plate_info} \n bill_to_name : {reg.bill_to_name} \n bill_to_building_no : {reg.bill_to_building_no} \n bill_to_street_name : {reg.bill_to_street_name} \n bill_to_district : {reg.bill_to_disctrict} \n bill_to_city : {reg.bill_to_city} \n bill_to_country : {reg.bill_to_country} \n bill_to_postal_code : {reg.bill_to_postal_code} \n bill_to_additional_no : {reg.bill_to_additional_no} \n bill_to_vat_number : {reg.bill_to_vat_number} \n bill_to_other_seller_id : {reg.bill_to_other_seller_id} \n workshop_name : {reg.workshop_name} \n workshop_building_no : {reg.workshop_building_no} \n workshop_street_name : {reg.workshop_street_name} \n workshop_disctrict : {reg.workshop_disctrict} \n workshop_city : {reg.workshop_city} \n workshop_country : {reg.workshop_country} \n workshop_postal_code : {reg.workshop_postal_code} \n workshop_additional_no : {reg.workshop_additional_no} \n workshop_vat_number : {reg.workshop_vat_number} \n workshop_other_seller_id : {reg.workshop_other_seller_id}"  
    if files.objects.filter(invoice=i1.invoice_id) != i1:
        a = files.objects.create(url=qr_data,invoice=i1,user_id=user)
    qr = files.objects.get(invoice=i1.invoice_id)
    return render(request, 'enroll/qr2.html', {'invoice_data':i1,'line_items':l1,'img':qr})

@login_required
def generate_inv(request,id):
    user = request.user
    i1 = invoice_data.objects.get(pk=id)
    # item_names = {"User":user.username,"Invoice":i1.invoice_number}
    l1 = line_items.objects.filter(invoice=i1.invoice_id)
    # for c in l1:
    #     item_names[f"Line Items {c.item_id}"]= {f"Item ID : {c.item_id} Item Code : {c.item_code} Item Name : {c.item_name} Pack : {c.pack} Quantity : {c.quantity} Unit Price : {c.unit_price} Taxable Amount : {c.taxable_amount} Discount : {c.discount} Tax Rate : {c.tax_rate} Tax Amount : {c.tax_amount} Item Subtotal Including VAT : {c.item_sub_total_including_vat} Total Excluding VAT : {c.total_excluding_vat} Total Discount : {c.total_discount} Total Taxable Amount Excluding VAT : {c.total_taxable_amount_excluding_vat} Net Excluding VAT : {c.net_excluding_VAT} Total VAT 15% : {c.total_vat_15perc} Net Amount : {c.net_amount} Excess Amount + VAT : {c.excess_amount_plus_VAT} Deprecation Amount + VAT : {c.deprecation_amount_plus_VAT} Total Amount Due : {c.total_amount_due} Remarks : {c.remarks}"}
    # # l1 = line_items.objects.get(invoice=i1.invoice_id)
    # qr_data= f"Invoice Information \n Invoice ID : {i1.invoice_id} \n Invoice Number : {i1.invoice_number} \n Date & Time : {i1.date_time} \n Issue Date : {i1.issue_date} \n Supply Date : {i1.supply_date} \n Terms : {i1.terms} \n Sales Man : {i1.sales_man} \n Customer Reference : {i1.customer_ref} \n Customer Information \n Customer ID : {i1.customer_id} \n Customer Name : {i1.customer_name} \n Customer Address : {i1.customer_address} \n Customer City : {i1.customer_city} \n Customer Contact Name : {i1.customer_contact_name} \n Customer Contact Telephone : {i1.customer_contact_tel} \n Customer Postal Code : {i1.customer_postal_code} \n Customer VAT Number : {i1.customer_vat_number} \n Seller Information \n Seller ID : {i1.seller_id} \n Seller Name : {i1.seller_name} \n Seller Address : {i1.seller_address} \n Seller City : {i1.seller_city} \n Seller Contact Name : {i1.seller_contact_name} \n Seller Contact Telephone : {i1.seller_contact_tel} \n Seller Postal Code : {i1.seller_postal_code} \n Seller VAT Number : {i1.seller_vat_number} \n Seller IBAN Number : {i1.seller_IBAN} \n Vehicle Information \n Vehicle Make : {i1.vehicle_make} \n Vehicle Model : {i1.vehicle_model} \n Vehicle Model Year : {i1.vehicle_model_year} \n Vehicle Plate Information : {i1.vehicle_plate_info} \n Vehicle VIN Number : {i1.vehicle_vin} \n Insurance Information \n Claim Number : {i1.claim_number} \n Insurance Name : {i1.insurance_name} \n Assessor Name : {i1.assessor_name} \n Line Items : {i1.line_item} \n User : {i1.user_id} \n\n\n Item Information : {item_names}"
    # # qr_data= f"invoice_number : {i1.invoice_number} nature : {item_names}"
    # # qr_data = f"Invoice_issue_date : {reg.date_time} \n invoice_number : {reg.invoice_number} \n insurance_info_name : {reg.insurance_info_name} \n insurance_info_claim_no : {reg.insurance_info_claim_no} \n insurance_info_assessor : {reg.insurance_info_assessor} \n make : {reg.make} \n model : {reg.model} \n vin : {reg.vin} \n plate_info : {reg.plate_info} \n bill_to_name : {reg.bill_to_name} \n bill_to_building_no : {reg.bill_to_building_no} \n bill_to_street_name : {reg.bill_to_street_name} \n bill_to_district : {reg.bill_to_disctrict} \n bill_to_city : {reg.bill_to_city} \n bill_to_country : {reg.bill_to_country} \n bill_to_postal_code : {reg.bill_to_postal_code} \n bill_to_additional_no : {reg.bill_to_additional_no} \n bill_to_vat_number : {reg.bill_to_vat_number} \n bill_to_other_seller_id : {reg.bill_to_other_seller_id} \n workshop_name : {reg.workshop_name} \n workshop_building_no : {reg.workshop_building_no} \n workshop_street_name : {reg.workshop_street_name} \n workshop_disctrict : {reg.workshop_disctrict} \n workshop_city : {reg.workshop_city} \n workshop_country : {reg.workshop_country} \n workshop_postal_code : {reg.workshop_postal_code} \n workshop_additional_no : {reg.workshop_additional_no} \n workshop_vat_number : {reg.workshop_vat_number} \n workshop_other_seller_id : {reg.workshop_other_seller_id}"  
    # if files.objects.filter(invoice=i1.invoice_id) != i1:
    #     a = files.objects.create(url=qr_data,invoice=i1,user_id=user)
    qr = files.objects.get(invoice=i1.invoice_id)
    pr = item_cal.objects.get(invoice=i1.invoice_id)
    return render(request, 'enroll/invoice_data2.html', {'invoice_data':i1,'line_items':l1,'img':qr,'pr':pr})

@login_required
def generate_qr_nli(request,id):
    user = request.user
    i1 = invoice_data.objects.get(pk=id)
    qr_data= f"Invoice Information \n Invoice ID : {i1.invoice_id} \n Invoice Number : {i1.invoice_number} \n Date & Time : {i1.date_time} \n Issue Date : {i1.issue_date} \n Supply Date : {i1.supply_date} \n Terms : {i1.terms} \n Sales Man : {i1.sales_man} \n Customer Reference : {i1.customer_ref} \n Customer Information \n Customer ID : {i1.customer_id} \n Customer Name : {i1.customer_name} \n Customer Address : {i1.customer_address} \n Customer City : {i1.customer_city} \n Customer Contact Name : {i1.customer_contact_name} \n Customer Contact Telephone : {i1.customer_contact_tel} \n Customer Postal Code : {i1.customer_postal_code} \n Customer VAT Number : {i1.customer_vat_number} \n Seller Information \n Seller ID : {i1.seller_id} \n Seller Name : {i1.seller_name} \n Seller Address : {i1.seller_address} \n Seller City : {i1.seller_city} \n Seller Contact Name : {i1.seller_contact_name} \n Seller Contact Telephone : {i1.seller_contact_tel} \n Seller Postal Code : {i1.seller_postal_code} \n Seller VAT Number : {i1.seller_vat_number} \n Seller IBAN Number : {i1.seller_IBAN} \n Vehicle Information \n Vehicle Make : {i1.vehicle_make} \n Vehicle Model : {i1.vehicle_model} \n Vehicle Model Year : {i1.vehicle_model_year} \n Vehicle Plate Information : {i1.vehicle_plate_info} \n Vehicle VIN Number : {i1.vehicle_vin} \n Insurance Information \n Claim Number : {i1.claim_number} \n Insurance Name : {i1.insurance_name} \n Assessor Name : {i1.assessor_name} \n Line Items : {i1.line_item} \n User : {i1.user_id}"
    print(qr_data)  
    if files.objects.filter(invoice=i1.invoice_id) != i1:
        a = files.objects.create(url=qr_data,invoice=i1,user_id=user)
    qr = files.objects.get(invoice=i1.invoice_id)
    return render(request, 'enroll/qr1.html', {'invoice_data':i1,'img':qr})

@login_required
def generate_inv_nli(request,id):
    user = request.user
    i1 = invoice_data.objects.get(pk=id)
    # qr_data= f"Invoice Information \n Invoice ID : {i1.invoice_id} \n Invoice Number : {i1.invoice_number} \n Date & Time : {i1.date_time} \n Issue Date : {i1.issue_date} \n Supply Date : {i1.supply_date} \n Terms : {i1.terms} \n Sales Man : {i1.sales_man} \n Customer Reference : {i1.customer_ref} \n Customer Information \n Customer ID : {i1.customer_id} \n Customer Name : {i1.customer_name} \n Customer Address : {i1.customer_address} \n Customer City : {i1.customer_city} \n Customer Contact Name : {i1.customer_contact_name} \n Customer Contact Telephone : {i1.customer_contact_tel} \n Customer Postal Code : {i1.customer_postal_code} \n Customer VAT Number : {i1.customer_vat_number} \n Seller Information \n Seller ID : {i1.seller_id} \n Seller Name : {i1.seller_name} \n Seller Address : {i1.seller_address} \n Seller City : {i1.seller_city} \n Seller Contact Name : {i1.seller_contact_name} \n Seller Contact Telephone : {i1.seller_contact_tel} \n Seller Postal Code : {i1.seller_postal_code} \n Seller VAT Number : {i1.seller_vat_number} \n Seller IBAN Number : {i1.seller_IBAN} \n Vehicle Information \n Vehicle Make : {i1.vehicle_make} \n Vehicle Model : {i1.vehicle_model} \n Vehicle Model Year : {i1.vehicle_model_year} \n Vehicle Plate Information : {i1.vehicle_plate_info} \n Vehicle VIN Number : {i1.vehicle_vin} \n Insurance Information \n Claim Number : {i1.claim_number} \n Insurance Name : {i1.insurance_name} \n Assessor Name : {i1.assessor_name} \n Line Items : {i1.line_item} \n User : {i1.user_id}"
    # print(qr_data)  
    # if files.objects.filter(invoice=i1.invoice_id) != i1:
    #     a = files.objects.create(url=qr_data,invoice=i1,user_id=user)
    qr = files.objects.get(invoice=i1.invoice_id)
    return render(request, 'enroll/invoice_data.html', {'invoice_data':i1,'img':qr})

@login_required
def download_invoice(request):
      
    return render(request, 'enroll/invoice.html')

from django.forms.models import model_to_dict

class GeneratePdf(View):
    def get(self, request,id, *args, **kwargs):

        data = invoice_data.objects.get(pk=id)
        fine = {"d":data.date_time}
        print(fine)
        da = model_to_dict(data)
        da["date"] = data.date_time
        print(da)
        pdf = render_to_pdf('enroll/pdf.html',da)
        if pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            filename = "Report_for_%s.pdf" %(da['invoice_id'])
            content = "inline; filename= %s" %(filename)
            response['Content-Disposition']=content
            return response
        else:
            pi = invoice_data.objects.get(pk=id)
            stud = invoice_data.objects.all()
        return render(request, 'enroll/invoice_data.html', {'stu':stud,'pi':pi})
        # return HttpResponse("Page Not Found")

 # qr code sirf invoice data k liye hi generate ho raha hai , others ko include karna baaqi hai
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=contacts(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "enroll/contact.html")

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        # if len(username)<10:
        #     messages.error(request, " Your user name must be under 10 characters")
        #     return redirect('home')

        # if not username.isalnum():
        #     messages.error(request, " User name should only contain letters and numbers")
        #     return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, " Your invoice account has been successfully created")
        return redirect('home')

    else:
        return render(request, "enroll/base1.html")

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
    #   'refresh': str(refresh),
      'access': str(refresh.access_token),
   }

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            token = get_tokens_for_user(user)
            ret = token["access"]
            a = L2(license_key=ret)
            a.save()
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("base2")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")


def license_valid(request):
    if request.method == 'POST':
        fm = L2_form(request.POST)
        if fm.is_valid():
            a = fm.cleaned_data['license_key']
    # if request.method=="POST":
    #     # Get the post parameters
    #     license=request.POST['LicenseKey']

        user=authenticate(license_key= a)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully authenticated")
            return redirect("base2")
        else:
            messages.error(request, "Invalid authentications! Please try again")
            return redirect("home")

    else:
        fm = line_items_form()
    return render(request, 'enroll/second.html', {'worm':fm})
   

    return HttpResponse("login")

    
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def about(request): 
    return render(request, "home/about.html")

def landing(request):
    return render(request,'enroll/landing.html')

def home(request):
    return render(request,'enroll/base1.html')

def base2(request):
    return render(request,'enroll/base2.html')

def shownewinvoice(request):
    return render(request,'enroll/invoice_data2.html')

def calqr(request):
    return render(request,'enroll/qr3.html')