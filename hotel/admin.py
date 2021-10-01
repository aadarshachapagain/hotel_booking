from django.contrib import admin

from hotel.inventoryUpdate.models import InventoryUpdate
from .models import Hotels
from .amenities.models import HotelAmenities
from .inventory.models import HotelInventory
from .booking.models import HotelBooking
from .reviews.models import HotelReview
from .gallery.models import HotelGallery
from .address.models import HotelAddress
from .hotellog.models import HotelLog
from .owner.models import HotelOwner
from .roomfeature.models import HotelRoomFeature
from .roomtype.models import HotelRoomType
from hotel.Country.models import Country
from hotel.state.models import State
from hotel.cancellation_policy.models import Cancellation_Policy
from hotel.bedType.models import BedType
from hotel.inventory_bed_type.models import Inventory_Bed_Type
from hotel.offers.models import Offers
from hotel.inventoryOffers.models import InventoryOffers
from hotel.bankDetail.models import BankDetail
from hotel.addonservices.models import AddOnServices
from hotel.b2b.models import B2B
from hotel.child_supplement_policy.models import ChildSupplementPolicy
from hotel.extraBed.models import ExtraBedPolicy
from hotel.cribsPolicy.models import cribsPolicy
from hotel.specialRequest.models import specialRequest
from hotel.bulkEdit.models import PriceAlterLog
from hotel.charges.models import Charges
from hotel.mealPlan.models import MealPlan
from hotel.similarSystems.models import SimilarSystems
from hotel.groupRate.models import GroupRate
from hotel.propertyDetail.models import PropertyDetail
from hotel.propertyDetail.models import Accomodation
from hotel.room_facilities.models import RoomFacilities
from hotel.CreditCard.models import CreditCard
from hotel.PaymentPolicies.models import PaymentPolicies
from hotel.CommissionPaymentPolicies.models import CommissionPaymentPolicies


# Register your models here.

admin.site.register(Hotels)
admin.site.register(HotelAddress)
admin.site.register(Cancellation_Policy)
admin.site.register(HotelAmenities)
admin.site.register(HotelInventory)
admin.site.register(HotelBooking)
admin.site.register(HotelReview)
admin.site.register(HotelGallery)
admin.site.register(HotelLog)
admin.site.register(HotelOwner)
admin.site.register(HotelRoomFeature)
admin.site.register(HotelRoomType)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(BedType)
admin.site.register(Inventory_Bed_Type)
admin.site.register(Offers)
admin.site.register(InventoryOffers)
admin.site.register(InventoryUpdate)
admin.site.register(BankDetail)
admin.site.register(AddOnServices)
admin.site.register(B2B)
admin.site.register(ChildSupplementPolicy)
admin.site.register(ExtraBedPolicy)
admin.site.register(cribsPolicy)
admin.site.register(specialRequest)
admin.site.register(PriceAlterLog)
admin.site.register(Charges)
admin.site.register(MealPlan)
admin.site.register(SimilarSystems)
admin.site.register(GroupRate)
admin.site.register(PropertyDetail)
admin.site.register(Accomodation)
admin.site.register(RoomFacilities)
admin.site.register(CreditCard)
admin.site.register(PaymentPolicies)
admin.site.register(CommissionPaymentPolicies)


