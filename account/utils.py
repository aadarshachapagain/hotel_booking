import tempfile
from email.mime.image import MIMEImage

from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags
from weasyprint import HTML, CSS, pdf
from django.core.mail import EmailMessage, message, EmailMultiAlternatives

from hotel.models import Hotels
from django.contrib.staticfiles.templatetags.staticfiles import static

from travel.devsettings import url


def generate_pdf(request, template_src, context_dict={}):
    html_string = render_to_string(template_src, context_dict)
    
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf()

    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = 'abc.pdf'
    return response
