import requests
from datetime import datetime, timedelta
from requests import exceptions


def api_call_for_booking_information(hotel_id):
    try:
        url = "http://128.199.22.231:8006/get_booking_calendar_by_hotelId/{hotel_id}".format(hotel_id=hotel_id)
        data_from_api = requests.get(url, timeout=1)
        data_from_api_json = data_from_api.json()
        for data in data_from_api_json:
            data['start'] = datetime.strptime(data['start'], "%m-%d-%Y").date()
            data['end'] = datetime.strptime(data['end'], "%m-%d-%Y").date()
        return data_from_api_json
    except exceptions.ConnectTimeout as e:
        data_from_api_json = ''
        return data_from_api_json
    except exceptions.ConnectionError as e:
        data_from_api_json = ''
        return data_from_api_json
