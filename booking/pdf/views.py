from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from booking.booking_table.models import BookingTable
from booking.customer.models import Customer
from booking.module_booking.models import ModuleBooking
from hotel.cancellation_policy.models import Cancellation_Policy
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels
from django.http import HttpResponse
from django.views.generic import View

from booking.pdf.utils import render_to_pdf  # created in step 4


@permission_classes((IsAuthenticated,))
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs['id']
        booking_instance = BookingTable.objects.get(id=id)
        customer_instance = Customer.objects.get(user=booking_instance.customer)
        module_instance = ModuleBooking.objects.filter(booking=id)
        hotel_instance = Hotels.objects.get(id=module_instance[0].company_id)
        cancellation_instance = Cancellation_Policy.objects.filter(hotel=module_instance[0].company_id)
        print(cancellation_instance)
        for m in module_instance:
            invetory_instance = HotelInventory.objects.get(id=m.inventory_id, hotel=m.company_id)
            m.room_name = invetory_instance.room_name
        data = {
            'customer': customer_instance,
            'cancellation': cancellation_instance,
            'booking': booking_instance,
            'module': module_instance,
            'hotel': hotel_instance,
        }
        pdf = render_to_pdf(request, 'pdf/summary.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
