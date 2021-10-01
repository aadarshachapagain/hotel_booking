from django import forms

from booking.business_partners.models import BusinessPartners


class BusinessPartnersForm(forms.ModelForm):
	class Meta:
		model = BusinessPartners
		fields = [
			"type",
			"setupcost",
			"renewalcost",
			"acctransferable",
			"refundable",
			"flightexcludedCb",
			"flightincludedCb",
			"flightincludedVb",
			"package_worth",
			"count",
			"return_ticket_worth",
			"countforreturnticket"
		]
