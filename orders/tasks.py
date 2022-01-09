from celery import task
from orders.models import Order
from django.core.mail import send_mail


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f' Seu pedido{order.id} '
    message = f'Sr(a). {order.first_name}, \n\n' \
             f'Seu pedido de nº {order.id}, foi realizado com sucesso!\n' \
             f'agradecemos pela compra!'
    
    mail_send = send_mail(
                        subject, 
                        message, 
                        'admin@dshouse@gmail.com',
                        [order.email])
    return mail_send