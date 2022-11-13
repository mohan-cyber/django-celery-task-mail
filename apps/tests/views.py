from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework.permissions import AllowAny, IsAuthenticated

# import tasks
from apps.tests.tasks import send_email




# Mail testing methods
class MailTest(APIView):
    permission_classes = (AllowAny, )
    def get(self, request ):

        mail_to = "mohanselvan@gmail.com"
        data = { 
            'email' : "mohanselvan@gmail.com",
        }
        send_email.delay(mail_to, data=data)
        return Response({"message": "email has been sent successfully"}, status=status.HTTP_200_OK)

