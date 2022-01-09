from io import BytesIO
import weasyprint
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from celery import task
from orders.models import Order

@task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)

    html = render_to_string('orders/order/pdf.html', {'order': order})
    
    subject = f'Seu pedido Nº {order.id}'
    message = f'Por favor, verifique seus anexos para detalhes de seu pedido.'
    email = EmailMessage(subject,
                        message,
                        'admin@myshop.com',
                        [order.email])
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    email.attach(f'order_{order.id}.pdf',
                out.getvalue(),
                'application/pdf')
    email.send()