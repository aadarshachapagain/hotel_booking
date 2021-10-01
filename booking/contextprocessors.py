from account.models import User
from booking.referee_and_referred.models import RefereeAndReferred
from hotel.models import Hotels
# from rental.rental_company.models import RentalCompany
# from restaurant.restaurant_company.models import RestaurantCompany
# from travel_tour.tour_company.models import TravelCompany


def membershipUpgradesCount(request):
    # exists = RefereeAndReferred.objects.filter(status='pending', membership__isnull=False).exists()
    exists = RefereeAndReferred.objects.filter(status='pending').exists()
    count = 0
    if exists:
        # count = RefereeAndReferred.objects.filter(status='pending', membership__isnull=False).count()
        count = RefereeAndReferred.objects.filter(status='pending').count()
        data = {
            'membershipupdatescount': count,
            'membership': RefereeAndReferred.objects.filter(status='pending'),
        }
    else:
        data = {
            'membershipupdatescount': count,
        }

    return data


def PartnershipUpgradesCount(request):
    exists = RefereeAndReferred.objects.filter(status='pending', partnership__isnull=False).exists()
    count = 0
    if exists:
        count = RefereeAndReferred.objects.filter(status='pending', partnership__isnull=False).count()
        data = {
            'partnershipupdatescount': count,
        }

    else:
        data = {
            'partnershipupdatescount': count,
        }

    return data


def moduleCount(request):
    hotel_count=0
    tour_count=0
    rental_count=0
    restaurant_count=0
    user_count=0
    user_count = User.objects.all().count()
    hotel_count = Hotels.objects.all().count()
    # tour_count = TravelCompany.objects.all().count()
    # rental_count = RentalCompany.objects.all().count()
    # restaurant_count = RestaurantCompany.objects.all().count()
    data = {
        'user_count': user_count,
        'hotel_count': hotel_count,
        'tour_count': tour_count,
        'rental_count': rental_count,
        'restaurant_count': restaurant_count,
    }
    return data
