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


def render_to_pdf(request, template_src, context_dict={}):
    html_string = render_to_string(template_src, context_dict)
    module = context_dict.get('module')
    customer = context_dict.get('customer')
    hotel_instance = Hotels.objects.get(id=module[0].company_id)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf()

    data = {
        'customer': customer,
        'hotel': hotel_instance,
        'module': module[0],

    }
    image_url = url + static('image/email_wallpaper.png')
    # Creating http response
    customer.name_underscore = customer.name.replace(" ", "_")
    filename = 'confirmation_' + customer.name + '.pdf'
    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename=confirmation{}'.format(customer.name_underscore) + '.pdf'

    mail_subject = 'Confirmation Letter for your booking at' + " " + hotel_instance.name
    message = render_to_string('booking/booking_confirmed_email.html', data)
    text_content = strip_tags(message)  # Strip the html tag. So people can see the pure text at least.
    to_email = customer.user.email
    email = EmailMultiAlternatives(
        mail_subject, body=text_content, from_email='flytrip@codeforcore.com', to=[to_email]
    )
    email.content_subtype = 'html'
    email.mixed_subtype = 'related'
    email.attach("confirmation_{}".format(customer.name_underscore) + '.pdf', result, "application/pdf")
    email.attach_alternative(message, "text/html")

    # email.send()
    return response
