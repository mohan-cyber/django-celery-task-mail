from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


class Utils:
    @staticmethod
    def send_welcome_mail(mail_to, data):

        if not settings.SEND_MAIL_ENABLED:
            return None


        email = data['email']
        subject = 'Welcome to Forgery Detection'
        template_data = {
            
            "welcome_email" : "Hi you have successfully received an email to your id "+ email
            
        }
        html_message = render_to_string('welcome.html', template_data)
        plain_message = strip_tags(html_message)
        from_email = 'mohanpop0310@gmail.com'
        return send_mail(subject, plain_message, from_email, [mail_to], html_message=html_message)
