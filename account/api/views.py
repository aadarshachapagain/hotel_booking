from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes

from account.api.serializers import UserCreateSerializer, UserPasswordResetSerializer, UserPasswordChangeSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from account.faq.models import FAQ
from account.models import User
from account.api.serializers import UserLoginSerializer
from account.api import serializers

# from hotel.api.serializers import HotelQuerySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.utils import json

from account.owner_profile.models import OwnerProfile
from booking.customer.models import Customer
from django.forms import model_to_dict


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    # since we are using base api view we need to define every method we use

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            # print(new_data)
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserPasswordResetAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserPasswordResetSerializer

    # since we are using base api view we need to define every method we use

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserPasswordResetSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            # print(new_data)
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserPasswordChangeAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserPasswordChangeSerializer

    # since we are using base api view we need to define every method we use

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserPasswordChangeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            # print(new_data)
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


from rest_framework.authtoken.models import Token


@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def fireBaseRegister(request):
    if request.method == "POST":
        email = request.POST.get('email')
        token = request.POST.get('token')
        provider = request.POST.get('provider')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        obj = User()

        if User.objects.filter(email=email).exists():
            user_instance = User.objects.get(email=email)
            Token.objects.filter(user=user_instance).update(key=token)
            return JsonResponse('User already exists, Token Updated', safe=False)
        else:
            obj.email = email
            obj.set_password(password)
            obj.provider = provider
            obj.contact = phone
            obj.is_active = True
            obj.save()
            user_profile = Customer(
                user=obj
            )
            user_profile.save()
            Token.objects.filter(user=obj.id).update(key=token)
            return JsonResponse('User Succesfully Created', safe=False)

    # return HttpResponse('User Succesfully Created')


@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def fireBaseLogin(request):
    data = {}
    if request.method == "POST":
        token = request.POST.get('token')
        try:
            userObjToken = Token.objects.get(key=token)
            data['email'] = User.objects.get(id=userObjToken.user_id).email
            data['provider'] = User.objects.get(id=userObjToken.user_id).provider
            data['phone'] = User.objects.get(id=userObjToken.user_id).contact
            data['token'] = token
        except:
            return JsonResponse('Sorry User doesnot exist', safe=False)
    return JsonResponse(data, safe=False)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def faqAPI(request):
    data = {}
    list_faq = []
    if request.method == "GET":
        try:
            instance = FAQ.objects.filter(device='Mobile Application')
            for item in instance:
                dict_faq = model_to_dict(item)
                del dict_faq['device']
                list_faq.append(dict_faq)
            data.update({'faq': list_faq})
        except:
            data.update({'faq': list_faq})
            return JsonResponse(data, safe=False)
    return JsonResponse(data, safe=False)


from account.models import User


@csrf_exempt
@api_view(['POST'])
def ownerProfile(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        if User.objects.filter(id=user_id).exists():
            if OwnerProfile.objects.filter(user_id=user_id).exists():
                dict_owner = model_to_dict(OwnerProfile.objects.get(user_id=user_id))
                dict_owner.update({'image': dict_owner['image'].url})
                return JsonResponse(dict_owner, safe=False)
            else:
                return JsonResponse('Sorry Owner Profile doesnot exist', safe=False)
        else:
            return JsonResponse('Sorry User Profile doesnot exist', safe=False)
