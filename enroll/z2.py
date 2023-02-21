# qrcode and pdf code for invoice data
'''
qr = qrcode.QRCode(
              version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
              box_size=5,
              border=5
            )
            qr_data = f"invoice_number : {a} \n insurance_info_name : {d} \n insurance_info_claim_no : {e} \n insurance_info_assessor : {f} \n make : {g} \n model : {h} \n vin : {i} \n plate_info : {j} \n bill_to_name : {k} \n bill_to_building_no : {l} \n bill_to_street_name : {m} \n bill_to_disctrict : {n} \n bill_to_city : {o} \n bill_to_country : {p} \n bill_to_postal_code : {q} \n bill_to_additional_no : {r} \n bill_to_vat_number : {s} \n bill_to_other_seller_id : {t} \n workshop_name : {u} \n workshop_building_no : {v} \n workshop_street_name : {w} \n workshop_disctrict : {x} \n workshop_city : {y} \n workshop_country : {z} \n workshop_postal_code : {aa} \n workshop_additional_no : {bb} \n workshop_vat_number : {cc} \n workshop_other_seller_id : {dd}"
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image(fill_color='blue', back_color='white')
            img.save(f'{a}.png')
            data = (
                ("invoice_number",a),
                ("insurance_info_name",d),
                ("insurance_info_claim_no",e),
                ("insurance_info_assessor",f),
                ("make",g),
                ("model",h),
                ("vin",i),
                ("plate_info",j),
                ("bill_to_name",k),
                ("bill_to_building_no",l),
                ("bill_to_street_name",m),
                ("bill_to_disctrict",n),
                ("bill_to_city",o),
                ("bill_to_country",p),
                ("bill_to_postal_code",q),
                ("bill_to_additional_no",r),
                ("bill_to_vat_number",s),
                ("bill_to_other_seller_id",t),
                ("workshop_name",u),
                ("workshop_building_no",v),
                ("workshop_street_name",w),
                ("workshop_disctrict",x),
                ("workshop_city",y),
                ("workshop_country",z),
                ("workshop_postal_code",aa),
                ("workshop_additional_no",bb),
                ("workshop_vat_number",cc),
                ("workshop_other_seller_id",dd),
            )
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Times", size=10)
            line_height = pdf.font_size * 2.5
            col_width = pdf.epw / 4 
            for row in data:
                for datum in row:
                    pdf.multi_cell(col_width, line_height, datum, border=1,
                            new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
                pdf.ln(line_height)
            pdf.output('table_with_cells.pdf')
'''




# qr code and pdf code for line items
'''
qr = qrcode.QRCode(
              version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
              box_size=5,
              border=5
            )
            qr_data = f"nature : {a} \n unit_price : {d} \n quantity : {e} \n taxable_amount : {f} \n discount : {g} \n tax_rate : {h} \n tax_amount : {i} \n item_sub_total_including_vat : {j} \n total_excluding_vat : {k} \n total_discount : {l} \n total_taxable_amount_excluding_vat : {m} \n total_vat : {n} \n total_amount_due : {o}"
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image(fill_color='blue', back_color='white')
            img.save(f'{a}.png')
            data = (
                ("nature",a),
                ("unit_price",d),
                ("quantity",e),
                ("taxable_amount",f),
                ("discount",g),
                ("tax_rate",h),
                ("tax_amount",i),
                ("item_sub_total_including_vat",j),
                ("total_excluding_vat",k),
                ("total_discount",l),
                ("total_taxable_amount_excluding_vat",m),
                ("total_vat",n),
                ("total_amount_due",o),
            )
            global pdf
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Times", size=10)
            line_height = pdf.font_size * 2.5
            col_width = pdf.epw / 4 
            for row in data:
                for datum in row:
                    pdf.multi_cell(col_width, line_height, datum, border=1,
                            new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
                pdf.ln(line_height)
'''