from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


class listedPropSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    moduleName = serializers.CharField(max_length=200)
    propName = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    numberStaff = serializers.IntegerField()
    totalInvNum = serializers.IntegerField()


class BookingDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    moduleName = serializers.CharField(max_length=200)
    propName = serializers.CharField(max_length=200)
    type = serializers.CharField(max_length=200)
    checkin = serializers.DateField()
    checkout = serializers.DateField()
    customer = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField()
    address = serializers.CharField(max_length=200)
    booking_id = serializers.IntegerField()


# Aashish: API created at March 29, 2020

class CancellationPolicySerializer(serializers.Serializer):
    cancelIdentity = serializers.IntegerField()
    hotel = serializers.IntegerField()
    inventory = serializers.IntegerField()
    type = serializers.CharField(max_length=50)
    hourBefore = serializers.CharField(max_length=50)
    deductedPrice = serializers.CharField(max_length=50)
    deductedNoShowPrice = serializers.CharField(max_length=50)
    applicableFrom = serializers.DateField()
    applicableTo = serializers.DateField()
    applicableDays = serializers.CharField(max_length=50)
    cvvRequired = serializers.BooleanField()
    cardDetailRequired = serializers.BooleanField()
    chargeToModify = serializers.DecimalField(max_digits=5, decimal_places=2)
    chargeToCancel = serializers.DecimalField(max_digits=5, decimal_places=2)


# include crib, child supplement and extra bed policy
# they all have same db model so single serializer is created
class OtherPolicySerializer(serializers.Serializer):
    policyIdentity = serializers.IntegerField()
    hotel = serializers.IntegerField()
    inventory = serializers.IntegerField()
    ageCategory = serializers.CharField(max_length=200)
    ageStart = serializers.IntegerField()
    ageEnd = serializers.IntegerField()
    costType = serializers.CharField(max_length=200)
    percentage = serializers.DecimalField(max_digits=5, decimal_places=2)
    unitOfCost = serializers.CharField(max_length=200)
    applicableFrom = serializers.DateField()
    applicableTo = serializers.DateField()
    applicableDays = serializers.CharField(max_length=50)
