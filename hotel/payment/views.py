import json

import requests
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from hotel.decorators import is_superuser
from hotel.models import Hotels
from hotel.propertyDetail.models import PropertyDetail
from travel.devsettings import FINANCE_MEDIA_BASE_SHIVAJI


def get_incoming_payments_from_api(startDate=None, endDate=None):
    """

    :param startDate:
    :param endDate:
    :return:
      all incomimgs payaments recievec from api
    """
    baseurl = 'http://128.199.22.231:8006/'
    endpoint = 'get_incoming_payment_info'
    requestApi = baseurl + endpoint
    post_data = {}
    if startDate and endDate:
        post_data = {'startDate': str(startDate),
                     'endDate': str(endDate)
                     }
    r = ''

    try:
        r = requests.post(requestApi, json=post_data)
    except:
        pass
    return r


@is_superuser
def incomingPayment(request):
    """
    :return: 
    all incomimgs payaments recievec from api to tabular index
    """""

    'http://128.199.22.231:8006/get_incoming_payment_info'
    return render(request, 'payment/incoming/index.html', context=None, )


@is_superuser
def incomingPayment_json(request):
    """
    :return: 
    all incomimgs payaments recievec from api to tabular index
    """""

    'http://128.199.22.231:8006/get_incoming_payment_info'
    content = ''
    starDate = None
    endDate = None
    if request.is_ajax():
        if request.method == 'POST':
            print('in incomingPayment_json')
            raw_data = (request.POST)
            starDate = raw_data['startDate']
            endDate = raw_data['endDate']
        content = get_incoming_payments_from_api(starDate, endDate).json()

    return HttpResponse(json.dumps(content), content_type="application/json")


@is_superuser
def single_incoming_payments(request, bookingConfirmation):
    """

    :param request:
    :param bookingConfirmation:
    :return:
    record mactching the bookingConfirmation
    """
    content = get_incoming_payments_from_api().json()
    # bookingConfirmation = 'B5f146eb8482c0a08b9bfa113'

    for c in content['data']:
        if c['bookingConfirmation'] == bookingConfirmation:
            data = c

    return render(request, 'payment/incoming/show.html', context=data)


@is_superuser
def get_outgoing_payments(request):
    Hotel_list = Hotels.objects.all()
    properties = ''
    content = Hotel_list
    context = {

        'hotels': Hotel_list
    }

    # for hotel in Hotel_list:
    #     hotel_dict = {}
    #     hotel_dict['id'] = hotel.id
    #     print('prop_name:"%s"' % hotel.prop_id)
    #     prop_name = PropertyDetail.objects.get(id=hotel.prop_id).legal_name
    #     hotel_dict['name'] = prop_name
    #     if hotel not in content:
    #         content.append(hotel)

    # outgoing_payments
    return render(request, 'payment/outgoing/index.html', context=context, )


def get_outgoing_payments_from_api(startDate=None, endDate=None, hotelId=None):
    """
    :param startDate:
    :param endDate:
    :return:
      all outgoing payaments recievec from api
    """
    # TODO:add hotel add dynamically
    # FINANCE_MEDIA_BASE_SHIVAJI

    # baseurl = 'http://128.199.22.231:8006/'
    baseurl = FINANCE_MEDIA_BASE_SHIVAJI
    endpoint = 'get_outgoing_payment_info'
    requestApi = baseurl + endpoint
    post_data = {}
    if startDate and endDate:
        post_data = {'startDate': str(startDate),
                     'endDate': str(endDate),
                     'hotelId': hotelId
                     }
    r = ''
    try:
        r = requests.post(requestApi, json=post_data)
    except:
        pass
    return r


@is_superuser
def get_outgoing_payments_json(request):
    content = ''
    starDate = None
    endDate = None
    hotelId = None

    if request.is_ajax():
        if request.method == 'POST':
            print('in outgoing_payments_json')
            raw_data = (request.POST)
            starDate = raw_data['startDate']
            endDate = raw_data['endDate']
            hotelId = raw_data['hotelId']
            print(' hotelId "%s"' % hotelId)
        content = get_outgoing_payments_from_api(starDate, endDate, hotelId).json()

    return HttpResponse(json.dumps(content), content_type="application/json")


# @is_superuser
def single_outgoing_payments(request, OutgoingPaymentId):
    """
    :param request:
    :param bookingConfirmation:
    :return:
    record matching the bookingConfirmation
    """
    print('OutgoingPaymentId')
    print(OutgoingPaymentId)
    # content = get_incoming_payments_from_api().json()
    # bookingConfirmation = 'B5f146eb8482c0a08b9bfa113'

    # import json

    # OutgoingPaymentId = 1
    # OutgoingPaymentId = 'not_available_5f82a2773f2e0923c206743f'
    # OutgoingPaymentId = 'not_available_5f82a99d3f2e0923c2067dcb'
    # OutgoingPaymentId = 'not_available_5f82abc13f2e0923c2067ecd'
    # OutgoingPaymentId = 'OMP5f8017072e38eb03d8d00a8a'
    # OutgoingPaymentId = 'OMP5f80171c2e38eb03d8d00a8d'
    # OutgoingPaymentId = 'OMP5f850db53f2e0923c2068416'
    OutgoingPaymentId = OutgoingPaymentId
    content = get_outgoing_payments_from_api().json()
    # print(content['data'])
    # data = {}
    # with open('static/outgoing_payments.json') as f:
    #     data = json.load(f)
    # print('data')
    # print(data)
    data = {}

    for c in content['data']:
        # print(c["hotelId"])
        if 'outgoingManualPaymentID' in c.keys():
            # print('in keys bhitra')
            # print(type(c['outgoingManualPaymentID']))
            # print(type(OutgoingPaymentId))
            if c['outgoingManualPaymentID'] == OutgoingPaymentId:
                data = c
                # address = {'address': c['hotel_address'][0]['address']}
                # contact1 = {'contact': c['hotel_address'][0]['contact1']}
                # # paymentRecordDetails = {'paymentRecordDetails'}
                # # paymentRecordDetails = {'paymentRecordDetails'}
                # print((c['paymentRecordDetails'][0]['paymentDetails']['Grand_total_cost']))
                # for i in range(0, len(c['paymentRecordDetails'])):
                #     cost_booking = {'cost_booking': c['paymentRecordDetails'][i]['paymentDetails']['Grand_total_cost']}
                #
                #
                # data.update(address)
                # data.update(contact1)

                # data['address'] = c['hotel_address'][0]['address']
                # print(c['hotel_address'][0]['address'])
    data['domain'] = FINANCE_MEDIA_BASE_SHIVAJI
    return render(request, 'payment/outgoing/show.html', context=data)


def renderdropzone(request):
    data = {}
    return render(request, 'payment/outgoing/dropzone.html', context=data)


def dropzoneuploads(request):
    if request.method == 'POST':
        files = [request.FILES.get('file[%d]' % i)
                 for i in range(0, len(request.FILES))]
        # text obtained from form is grabbed here, similarly other data can be gathered
        abc = request.POST['abc']
        # location where you want to upload your files
        folder = 'my_folder'
        fs = FileSystemStorage(location=folder)
        for f in files:
            filename = fs.save(f.name, f)
    data = {'status': 'success'}
    response = JsonResponse(data)
    return response
