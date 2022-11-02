from .models import Mail
from rest_framework import serializers
import re

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class Mail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = "__all__"

    def validate(self, data):
        if not re.match(EMAIL_REGEX, data['mail_to']):
            raise serializers.ValidationError('Enter Valid Email Address')

        return data
