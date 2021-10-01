from django.contrib.auth import get_user
from rest_framework import serializers

from account.models import User
from hotel.amenities.models import HotelAmenities
from hotel.gallery.models import HotelGallery
from hotel.hotel_facilities.models import HotelFacilities
from hotel.models import Hotels, HotelFacilitiesMiddle
from hotel.address.models import HotelAddress
from hotel.city.models import City
from hotel.landmark.models import Landmark
from hotel.owner.models import HotelOwner
from hotel.inventory.models import HotelInventory
from hotel.inventorygallery.models import InventoryGallery
from hotel.Country.models import Country

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)
from django.db.models import Q
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from hotel.roomfeature.models import HotelRoomFeature
from hotel.roomtype.models import HotelRoomType


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotels
        fields = ('name', 'owner_id_id', 'created_at', 'description')

# This Api is in use
class HotelCitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'image', 'name', 'state', 'country')
# This Api is in use


class HotelLandmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Landmark
        fields = ('id', 'name', 'image')


class HotelNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotels
        fields = ('name',)


class HotelCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name',)


class CityListSerializaer(ModelSerializer):
    class Meta:
        model = City
        fields = [
            'name',
            'image',
        ]


# class HotelQuerySerializer(ModelSerializer):
#     city = CharField(required = True)
#     name = CharField(allow_blank=True, read_only = True)
#     description = CharField(allow_blank=True, read_only = True)
#     # hotel_id = CharField()
#     # email = EmailField(label  = 'Email Address', required = False, allow_blank = True)
#     class Meta:
#         model = Hotels
#         fields = [
#             'city',
#             'name',
#             'description'
#         ]
#
#     def validate(self, data):
#         hotel_obj = None
#         city = data.get('city')
#         # print(city)
#         hoteladdress = HotelAddress.objects.values_list('hotel_id_id', flat=True).filter(city=city)
#         abc = hoteladdress.count()
#         # print(abc)
#         if hoteladdress:
#             for a in hoteladdress:
#                 # print(a)
#                 hotel = Hotels.objects.get(pk=a)
#                 print("hello123")
#                 print(hotel)
#                 data['name']=hotel.name
#                 data['description']=hotel.description
#         return data

# our serializer
class HotelOwnerListSerializaer(ModelSerializer):
    class Meta:
        model = HotelOwner
        fields = [
            'name',
            'contact'
        ]


class HotelListSerializaer(ModelSerializer):
    # hoteladdress = HotelAddressListSerializer()
    # hotelinventory = HotelInventoryListSerializer()
    # owner_id = HotelOwnerListSerializaer()
    class Meta:
        model = Hotels
        fields = [
            'id',
            'name',
            'description',
            # 'owner_id'

        ]


class CityListSerializaer(ModelSerializer):
    class Meta:
        model = City
        fields = [
            'name',
            'image',
        ]


class HotelAddressListSerializer(ModelSerializer):
    city = CityListSerializaer()

    class Meta:
        model = HotelAddress
        fields = [
            # 'hotel',
            'city',
            'state',
            'country',
            'address',
            'contact1',
            'contact2',
            'latitude',
            'longitude'
            # 'landmarks'
        ]


class HotelInventoryListSerializer(ModelSerializer):
    hotel = HotelListSerializaer()
    hoteladdress = HotelAddressListSerializer()

    class Meta:
        model = HotelInventory
        fields = [
            'hotel',
            'hoteladdress',
            'id',
            'room_name',
            'price',
            'description',
            'child_max',
            'adult_max',
            'no_of_rooms',
        ]


# def to_representation(self, instance):
#     # instance is the model object. create the custom json format by accessing instance attributes normaly and return it
#     hotel = dict()
#     hotel['id'] = instance.hotel.id
#     hotel['name'] = instance.hotel.name
#     hotel['description'] = instance.hotel.description
#
#     hoteladdress = dict()
#     hoteladdress['city'] = instance.hoteladdress.city
#     hoteladdress['state'] = instance.hoteladdress.state
#     hoteladdress['country'] = instance.hoteladdress.country
#     hoteladdress['address'] = instance.hoteladdress.address
#     hoteladdress['contact1'] = instance.hoteladdress.contact1
#     hoteladdress['contact2'] = instance.hoteladdress.contact2
#     hoteladdress['latitude'] = instance.hoteladdress.latitude
#     hoteladdress['longitude'] = instance.hoteladdress.longitude
#     hoteladdress['landmarks'] = instance.hoteladdress.landmarks
#
#     hotelinventory = dict()
#     hotelinventory['id'] = instance.id
#     hotelinventory['room_name'] = instance.room_name
#     hotelinventory['price'] = instance.price
#     hotelinventory['description'] = instance.description
#     hotelinventory['child_max'] = instance.child_max
#     hotelinventory['adult_max'] = instance.adult_max
#     hotelinventory['no_of_rooms'] = instance.no_of_rooms
#
#     representation = {
#         'hotel': hotel,
#         'hoteladdress': hoteladdress,
#         'hotelinventory': hotelinventory,
#
#     }
#
#     return representation


class HotelListSerializaer(ModelSerializer):
    # hoteladdress = HotelAddressListSerializer()
    # hotelinventory = HotelInventoryListSerializer()
    # owner_id = HotelOwnerListSerializaer()

    class Meta:
        model = Hotels
        fields = [
            'id',
            'name',
            'description',
            'owner_id',
            'star_rating',


        ]


class HotelGalleryListSerializaer(ModelSerializer):
    hotel_inventory_id = HotelInventoryListSerializer()

    class Meta:
        model = InventoryGallery
        fields = [
            'image',
            'hotel_inventory_id'
        ]

    def to_representation(self, instance):
        # instance is the model object. create the custom json format by accessing instance attributes normaly and return it
        hotel = dict()
        hotel['id'] = instance.hotel_inventory_id.hotel.id
        hotel['name'] = instance.hotel_inventory_id.hotel.name
        hotel['description'] = instance.hotel_inventory_id.hotel.description

        hoteladdress = dict()
        hoteladdress['city'] = instance.hotel_inventory_id.hoteladdress.city.name
        hoteladdress['state'] = instance.hotel_inventory_id.hoteladdress.state
        hoteladdress['country'] = instance.hotel_inventory_id.hoteladdress.country
        hoteladdress['address'] = instance.hotel_inventory_id.hoteladdress.address
        hoteladdress['contact1'] = instance.hotel_inventory_id.hoteladdress.contact1
        hoteladdress['contact2'] = instance.hotel_inventory_id.hoteladdress.contact2
        hoteladdress['latitude'] = instance.hotel_inventory_id.hoteladdress.latitude
        hoteladdress['longitude'] = instance.hotel_inventory_id.hoteladdress.longitude
        # hoteladdress['landmarks']=instance.hotel_inventory_id.hoteladdress.landmarks
        #
        hotelinventory = dict()
        hotelinventory['id'] = instance.hotel_inventory_id.id
        hotelinventory['room_name'] = instance.hotel_inventory_id.room_name
        hotelinventory['price'] = instance.hotel_inventory_id.price
        hotelinventory['description'] = instance.hotel_inventory_id.description
        hotelinventory['child_max'] = instance.hotel_inventory_id.child_max
        hotelinventory['adult_max'] = instance.hotel_inventory_id.adult_max
        hotelinventory['no_of_rooms'] = instance.hotel_inventory_id.no_of_rooms
        hotelinventory['image'] = "http://127.0.0.1:8000" + instance.image.url
        #
        #

        representation = {
            'hotel': hotel,
            'hoteladdress': hoteladdress,
            'hotelinventory': hotelinventory,

        }

        return representation


class CommentSerializer(serializers.Serializer):
    # tmpimage = HotelOwner.objects.all()
    # image = HotelOwnerListSerializaer(tmpimage)
    # print(image)

    email = serializers.EmailField(required=False)
    content = serializers.CharField(max_length=200, required=False)
    image = serializers.CharField(max_length=200, required=False)
    user = serializers.CharField(max_length=200, required=False)


# user = serializers.SerializerMethodField()
# newobj=None

# def get_user(self, obj):
#     print(self)
#     return User.objects.values_list('username').get(email=self.email)
#
# def create(self, validated_data):
#     validated_data._mutable = True
#     email = validated_data['email']
#     content = validated_data['content']
#     user=get_user(validated_data['email'])
#     validated_data['user'] = user
#     validated_data['email'] = email
#     validated_data['content'] = content
#     return validated_data


class MyNewSerializer(ModelSerializer):
    owner_id = HotelOwnerListSerializaer()

    class Meta:
        model = Hotels
        fields = [
            'name',
            'description',
            'owner_id'
        ]


class HotelGallerySerializer(ModelSerializer):
    class Meta:
        model = HotelGallery
        fields = [
            'image',
            'title',
        ]


class LandmarkNameSerializaer(ModelSerializer):
    class Meta:
        model = Landmark
        fields = [
            'name',
            'image',
        ]


class CityNameSerializaer(ModelSerializer):
    landmark = LandmarkNameSerializaer(many=True)

    class Meta:
        model = City
        fields = [
            'name',
            # 'image',
            'landmark'
        ]


class HotelAddressSerializer(ModelSerializer):
    city = CityNameSerializaer()

    class Meta:
        model = HotelAddress
        fields = [
            'city',
            'state',
            'country',
            'address',
            'contact1',
            'contact2',
            'latitude',
            'longitude',
        ]


class HotelAmenitiesSerializer(ModelSerializer):
    # hotel=HotelSearchSerializer()
    class Meta:
        model = HotelFacilities
        fields = [
            'name',
            'image',

        ]


# class HotelMiddleSerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField(source='hotelsfacilities.id')
#     name = serializers.ReadOnlyField(source='hotelsfacilities.name')
#     class Meta:
#         model = HotelFacilitiesMiddle
#         fields = [
#             'id',
#             'name',
#
#         ]

class InventoryFeatureSerializer(ModelSerializer):
    # hotel=HotelSearchSerializer()
    class Meta:
        model = HotelRoomFeature
        fields = [
            'name',

        ]


class InventoryRoomTypeSerializer(ModelSerializer):
    # hotel=HotelSearchSerializer()
    class Meta:
        model = HotelRoomType
        fields = [
            'name',

        ]


class InventoryAmenitiesSerializer(ModelSerializer):
    # hotel=HotelSearchSerializer()
    class Meta:
        model = HotelAmenities
        fields = [
            'name',
            'image',

        ]


class InventorySearchSerializer(ModelSerializer):
    roomfeatures = InventoryFeatureSerializer(many=True, read_only=True)
    roomtype = InventoryRoomTypeSerializer(many=True, read_only=True)
    amenities = InventoryAmenitiesSerializer(many=True, read_only=True)

    class Meta:
        model = HotelInventory
        fields = [
            'id',
            'room_name',
            'price',
            'description',
            'no_of_rooms',
            'child_max',
            'adult_max',
            'roomfeatures',
            'roomtype',
            'amenities'

        ]


class HotelSearchSerializer(ModelSerializer):
    galleries = HotelGallerySerializer(many=True, read_only=True)
    facilities = HotelAmenitiesSerializer(many=True, read_only=True)
    # hotel=HotelMiddleSerializer(many=True,read_only=True)
    address = HotelAddressSerializer(read_only=True)
    inventory = InventorySearchSerializer(read_only=True, many=True)

    # facilities = HotelMiddleSerializer(source='HotelFacilitiesMiddle', many=True)
    # facilities = HotelMiddleSerializer(many=True)

    class Meta:
        model = Hotels
        fields = [
            'id',
            'name',
            'wordsbyowner',
            'description',
            'galleries',
            'address',
            'facilities',
            'inventory',

        ]


class InventoryDetailSerializer(ModelSerializer):
    # roomfeatures = InventoryFeatureSerializer(many=True, read_only=True)
    # roomtype = InventoryRoomTypeSerializer(many=True, read_only=True)
    # amenities = InventoryAmenitiesSerializer(many=True, read_only=True)
    id = CharField(required=False, allow_blank=True)

    class Meta:
        model = HotelInventory
        fields = [
            'id',
            'room_name',
            'price',
            # 'description',
            # 'no_of_rooms',
            # 'child_max',
            # 'adult_max',
            # 'roomfeatures',
            # 'roomtype',
            # 'amenities'
        ]

    def validate(self, data):
        user_obj = None
        hotel_id = data.get('hotel_id', None)
        # inventory_id = data.get('inventory_id', None)
        # if not email and not username:
        # 	raise ValidationError("A username or email is required to login.")
        # user = User.objects.filter(
        # 	Q(email=email) |
        # 	Q(username=username)
        # ).distinct()
        # if user.exists() and user.count() == 1:
        # 	user_obj = user.first()
        # else:
        # 	raise ValidationError("This username / email is not valid.")
        #
        # if user_obj:
        # 	if not user_obj.check_password(password):
        # 		raise ValidationError("Incorrect Credentials please try again.")
        #
        # token = Token.objects.get(user_id=user_obj.id)
        # data['token'] = token.key
        return data
