from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.html import escape
from xhtml2pdf import pisa


def renderPdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    send_data = html.encode("UTF-8")
    pdf=pisa.pisaDocument(BytesIO(send_data), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))