import json


def send_policies():
	cancellation_policies_list = [
		{
			'name': 'Non-refundable booking',
			'name_with_underscore': 'Non_refundable_booking',
			'guest_checkout': 'allowed',
			'login_required': False,
			'room_rate_operator': 'sub',
			'room_rate_number': 10,
			'cvc_code_required': True,
			'payment_hold': 'immediate',
			'vendor_payment_duration': 'after booking is made',
			'big_safar_amount_hold': False,
			'refundable_after_cancellation': False,
			'flag': '',
			'description':
				[
					'Payment Conditions: Guest checkout is allowed, login NOT essential'
					,
					
					'Room rate will be less by 10 % on base rate. i.e. room rate = base rate minus 10% $100-10 = $90'
					,
					
					'CVC CODE and immediate payment hold is essential for booking confirmation'
					,
					
					'Vendor’s Bank Account will be linked with this payment mode.'
					,
					
					'Payment will be made to the vendor’s account directly when such booking is made.'
					,
					
					'Bigsafar will NOT HOLD any amount at the time of booking – information to the client while booking is conformed as this payment will handle by the property itself.'
					,
					
					'If booking is cancelled after confirmation of booking then guest will NOT get any refund.'
				
				]
		},
		{
			'name': 'Partially-refundable booking',
			'name_with_underscore': 'Partially_refundable_booking',
			'guest_checkout': 'allowed',
			'login_required': False,
			'room_rate_operator': 'add',
			'room_rate_number': 15,
			'cvc_code_required': True,
			'payment_hold': 'immediate',
			'vendor_payment_duration': 'after booking is made',
			'big_safar_amount_hold': False,
			'refundable_after_cancellation': False,
			'flag': 'disabled',
			'description':
				[
					'Payment Conditions: Guest checkout is allowed, login NOT essential'
					,
					
					'Room rate will be less by 10 % on base rate. i.e. room rate = base rate minus 10% $100-10 = $90'
					,
					
					'CVC CODE and immediate payment hold is essential for booking confirmation'
					,
					
					'Vendor’s Bank Account will be linked with this payment mode.'
					,
					
					'Payment will be made to the vendor’s account directly when such booking is made.'
					,
					
					'Bigsafar will NOT HOLD any amount at the time of booking – information to the client while booking is conformed as this payment will handle by the property itself.'
					,
					
					'If booking is cancelled after confirmation of booking then guest will NOT get any refund.'
				
				]
		},
		{
			'name': 'Flexible booking',
			'name_with_underscore': 'Flexible_booking',
			'guest_checkout': 'allowed',
			'login_required': False,
			'room_rate_operator': 'add',
			'room_rate_number': 15,
			'cvc_code_required': True,
			'payment_hold': 'immediate',
			'vendor_payment_duration': 'after booking is made',
			'big_safar_amount_hold': False,
			'refundable_after_cancellation': False,
			'flag': 'disabled',
			'description':
				[
					'Payment Conditions: Guest checkout is allowed, login NOT essential'
					,
					
					'Room rate will be less by 10 % on base rate. i.e. room rate = base rate minus 10% $100-10 = $90'
					,
					
					'CVC CODE and immediate payment hold is essential for booking confirmation'
					,
					
					'Vendor’s Bank Account will be linked with this payment mode.'
					,
					
					'Payment will be made to the vendor’s account directly when such booking is made.'
					,
					
					'Bigsafar will NOT HOLD any amount at the time of booking – information to the client while booking is conformed as this payment will handle by the property itself.'
					,
					
					'If booking is cancelled after confirmation of booking then guest will NOT get any refund.'
				
				]
		},
		{
			'name': 'Pay at counter booking',
			'name_with_underscore': 'Pay_at_counter_booking',
			'guest_checkout': 'allowed',
			'login_required': False,
			'room_rate_operator': 'equal',
			'room_rate_number': 0,
			'cvc_code_required': True,
			'payment_hold': 'immediate',
			'vendor_payment_duration': 'after booking is made',
			'big_safar_amount_hold': True,
			'refundable_after_cancellation': False,
			'flag': 'disabled',
			'description':
				[
					'Payment Conditions: Guest checkout is allowed, login NOT essential'
					,
					
					'Room rate will be less by 10 % on base rate. i.e. room rate = base rate minus 10% $100-10 = $90'
					,
					
					'CVC CODE and immediate payment hold is essential for booking confirmation'
					,
					
					'Vendor’s Bank Account will be linked with this payment mode.'
					,
					
					'Payment will be made to the vendor’s account directly when such booking is made.'
					,
					
					'Bigsafar will NOT HOLD any amount at the time of booking – information to the client while booking is conformed as this payment will handle by the property itself.'
					,
					
					'If booking is cancelled after confirmation of booking then guest will NOT get any refund.'
				
				]
		}
	
	]
	final = json.dumps(cancellation_policies_list)
	return final


def send_booking():
	booking_list = [
		{
			"title": "Booking",
			"start": "2020-08-11",
			"end": "2020-08-13",
			"url": "",
			"customer": "Mr John Doe",
			"room_no": 3,
			"bookedPolicy": "Refundable",
			"paymentMethod": "Credit Card",
			"price": "101",
			"booking_id": "abcd1234"
		},
		{
			"title": "Booking",
			"start": "2020-08-11",
			"end": "2020-08-13",
			"url": "",
			"customer": "Mr John Doe",
			"room_no": 5,
			"bookedPolicy": "Refundable",
			"paymentMethod": "Credit Card",
			"price": "101",
			"booking_id": "abcd1234"
		},
		{
			"title": "Booking",
			"start": "2020-08-11",
			"end": "2020-08-13",
			"url": "",
			"customer": "Mr John Doe",
			"room_no": 7,
			"bookedPolicy": "Refundable",
			"paymentMethod": "Credit Card",
			"price": "101",
			"booking_id": "abcd1234"
		},
		{
			"title": "Booking",
			"start": "2020-08-11",
			"end": "2020-08-13",
			"url": "",
			"customer": "Mr John Doe",
			"room_no": 111,
			"bookedPolicy": "Refundable",
			"paymentMethod": "Credit Card",
			"price": "101",
			"booking_id": "abcd1234"
		}
	]
	final = json.dumps(booking_list)
	return final