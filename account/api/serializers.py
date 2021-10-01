from django.contrib.auth.tokens import default_token_generator
from django.contrib.contenttypes.models import ContentType
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from account.models import User
from django.db.models import Q, ImageField, IntegerField

from account.passwordReset.models import PasswordReset
from booking.customer.models import Customer

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from rest_framework.response import Response

from booking.customer.models import Customer
from travel.devsettings import url

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import math, random


class UserCreateSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        # fields required to return back 
        fields = [
            'id',
            # 'username',
            'password',
            'email',
            'token'
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already been registered.")

        return data

    def create(self, validated_data):
        # username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            # username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.is_active = True
        user_obj.save()

        user_profile = Customer(
            user=user_obj
        )
        user_profile.save()
        token = Token.objects.get(user_id=user_obj.id)
        # print(validated_data)
        # print(token.key)
        validated_data['token'] = token.key
        validated_data['id'] = user_obj.id
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    name = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)
    image = CharField(required=False, allow_blank=True)
    id = CharField(required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'password',
            'token',
            'name',
            'image'
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        # username = data.get('username', None)
        password = data["password"]
        # if not email and not username:
        if not email:
            raise ValidationError("A username or email is required to login.")
        user = User.objects.filter(
            Q(email=email)
            # |
            # Q(username=username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username / email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect Credentials please try again.")

        token = Token.objects.get(user_id=user_obj.id)
        data['id'] = user_obj.id
        data['token'] = token.key
        data['name'] = Customer.objects.get(user__email=email).name
        data['image'] = Customer.objects.get(user__email=email).image.url
        return data

    # # This code is triggered whenever a new user has been created and saved to the database


# function to generate OTP
def generateOTP(n):
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

    # length of password can be chaged
    # by changing value in range
    for i in range(n):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


class UserPasswordResetSerializer(ModelSerializer):
    msg = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'email',
            'msg',
        ]

    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        # if not email and not username:
        if not email:
            raise ValidationError("An email is required to reset password.")
        user = User.objects.filter(
            Q(email=email)
            # |
            # Q(username=username)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
            token = generateOTP(6)
            mail_subject = 'Reset your Password.'
            msg = render_to_string('account/reset.html', {
                'user': user,
                'token': token,
            })

            # to_email = email
            # email = EmailMultiAlternatives(
            #     mail_subject, message, 'KTM VOYAGE <info@ktmvoyage.com>', to=[to_email]
            # )
            # email.content_subtype = 'html'
            # email.send()

            # send mail via sendgrid
            message = Mail(
                from_email='info@ktmvoyage.com',
                to_emails=email,
                subject='Reset your Password.',
                html_content=msg)
            try:
                sg = SendGridAPIClient('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')
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.msg)

            if PasswordReset.objects.filter(user=user_obj.id).exists():
                PasswordReset.objects.filter(user=user_obj.id).delete()

            passwordInstance = PasswordReset()
            passwordInstance.code = token
            passwordInstance.user = User.objects.get(id=user_obj.id)
            passwordInstance.status = 0
            passwordInstance.save()
        else:
            raise ValidationError("This email is not valid.")
        data['msg'] = "We have send 6 digit code in your email. Please check your email."
        return data


class UserPasswordChangeSerializer(ModelSerializer):
    msg = CharField(allow_blank=True, read_only=True)
    password = CharField(required=True, write_only=True)
    code = IntegerField(max_length=6)
    email = EmailField(label='Email Address', required=True, allow_blank=True)

    class Meta:
        model = PasswordReset
        fields = [
            'email',
            'msg',
            'code',
            'password'
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        user_obj = None
        password = data.get('password')
        email = data.get('email')
        code = data.get('code')
        # if not email and not username:
        if not code and password:
            raise ValidationError("A code is required to change password.")
        user = PasswordReset.objects.filter(
            Q(user__email=email)
            |
            Q(code=code)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()

            if user_obj.code == code:
                user_instance = User.objects.get(id=user_obj.user.id)
                user_instance.set_password(password)
                user_instance.save()
                PasswordReset.objects.filter(user=user_obj.user.id).delete()

            else:
                raise ValidationError("Code did not match.")

        else:
            raise ValidationError("Code did not match.")
        # del data['code']
        # del data['email']
        # my= "Your password was successfully changed."
        # print(data)
        # return my
        data['msg'] = "Password Changed Successfully."
        return data
