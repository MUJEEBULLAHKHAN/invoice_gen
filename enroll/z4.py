# from unittest import result
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from io import BytesIO

# def html2pdf(template_source,context_dict={}):
#     template = get_template(template_source)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")),result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(),content_type = "application/pdf")
#     return None


# template code for get image from the database and show on template
'''
<div class="col-sm-8">
        <h4 class="text-center alert alert-info">Your Line Items   البنود الخاصة بك</h4>
         {% if imgg %}
             {% for st in imgg %}
             <tr>
               <td><img src="/{{ BASIC_DIR }}/{{st.qr_code}}" width="120"/></td>
             </tr>
             {% endfor %}
         </table>  
         
         {% endif %}
       </div>
'''

# import pdfkit
# pdfkit.from_url('http://google.com', 'tom.pdf')

