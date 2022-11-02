from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import Mail
from core.serializers import Mail_Serializer
from django.conf import settings
from django.core.mail import send_mail


# ==============Create Product====================
class Product_Create_ViewSet(ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = Mail_Serializer
    http_method_names = ['post', ]

    def create(self, request, *args, **kwargs):
        # Send Mail

        subject = request.data.get("subject")
        message = request.data.get("body")
        email_from = settings.EMAIL_HOST_USER
        email_to = [request.data.get("mail_to"),]
        data = {
            "subject": subject,
            "body": message,
            "mail_from": settings.EMAIL_HOST_USER,
            "mail_to": request.data.get("mail_to")
        }
        _serializer = self.serializer_class(data=data)
        if _serializer.is_valid():
            _serializer.save()
            send_mail(subject, message, email_from, email_to)
            return Response("Mail sent success")

        else:
            return Response(data=_serializer.errors)


