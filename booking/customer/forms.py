from django import forms

from booking.customer.models import Customer


# name = models.CharField(max_length=60, null=True)
#     email = models.EmailField(unique=True)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
#                                  message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     contact = models.CharField(validators=[phone_regex], max_length=17, blank=True,
#                                null=True)  # validators should be a list
#     status = models.IntegerField(null=True, default=0)
#     address = models.CharField(max_length=80, blank=True, null=True)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
#     state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
#     gender = models.CharField(max_length=10, null=True)
#     dob = models.DateField(validators=[no_future], blank=True)
#     #validator for future date
#     image = models.ImageField(blank=True, default='default.png')
#     reward = models.IntegerField(null=True, default=0)
#     created_at = models.DateTimeField(default=datetime.now, blank=True)
#


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "name",
            "contact",
            "status",
            "address",
            "country",
            # "state",
            # "city",
            "gender",
            "dob",
            "image",
            "reward",
            "created_at",
            "user",
            "memplan",
            "uniqtoken",
        ]
