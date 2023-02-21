# import pdfkit

# #Define path to wkhtmltopdf.exe
# path_to_wkhtmltopdf = r"wkhtmltopdf\\bin\\wkhtmltopdf.exe"

# #Define path to HTML file
# path_to_file = 'enroll/invoice.html'

# #Point pdfkit configuration to wkhtmltopdf.exe
# config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# #Convert HTML file to PDF
# pdfkit.from_file(path_to_file, output_path='sample.pdf', configuration=config)






# qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=5,border=5)
# qr_data = f"invoice_number : {reg.invoice_number} \n insurance_info_name : {d} \n insurance_info_claim_no : {e} \n insurance_info_assessor : {f} \n make : {g} \n model : {h} \n vin : {i} \n plate_info : {j} \n bill_to_name : {k} \n bill_to_building_no : {l} \n bill_to_street_name : {m} \n bill_to_disctrict : {n} \n bill_to_city : {o} \n bill_to_country : {p} \n bill_to_postal_code : {q} \n bill_to_additional_no : {r} \n bill_to_vat_number : {s} \n bill_to_other_seller_id : {t} \n workshop_name : {u} \n workshop_building_no : {v} \n workshop_street_name : {w} \n workshop_disctrict : {x} \n workshop_city : {y} \n workshop_country : {z} \n workshop_postal_code : {aa} \n workshop_additional_no : {bb} \n workshop_vat_number : {cc} \n workshop_other_seller_id : {dd}"
# qr.add_data(qr_data)
# qr.make(fit=True)
# img = qr.make_image(fill_color='blue', back_color='white')
# # '/media/users/%Y/%m/%d/'
# # img.save()
# file = img.save(f'/media/users/%Y/%m/%d/{reg.invoice_id}_{reg.invoice_number}.jpg')