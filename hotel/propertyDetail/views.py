import json
import os

from PIL import Image
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from account.models import User
from hotel.models import Hotels
from hotel.propertyDetail.forms import PropertyDetailForm
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DetailView
from hotel.propertyDetail.models import PropertyDetail
from django.contrib import messages
from django.urls import reverse_lazy
from hotel.propertyDetail.models import Accomodation
from hotel.propertyDetail.forms import OwnerAndPropertyForm
from account.owner_profile.models import OwnerProfile
from hotel.Country.models import Country
from travel import settings
from travel.devsettings import MEDIA_ROOT
from account.owner_profile.forms import OwnerProfileForm


# class PropertyDetailCreateView(FormView):
@method_decorator([login_required], name='dispatch')
class PropertyDetailCreateView(SuccessMessageMixin, CreateView):
    form_class = PropertyDetailForm
    model = PropertyDetail
    template_name = 'propertyDetail/create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        list_of_accomodation = form.data.getlist('accomodation')
        prop_id = self.object.id
        prop_detail = PropertyDetail.objects.get(id=prop_id)
        for loa in list_of_accomodation:
            new_instance = Accomodation()
            new_instance.acc_name = loa
            new_instance.prop_det = prop_detail
            new_instance.save()
        return super(PropertyDetailCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)

        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        user = self.request.user.id
        context = super(PropertyDetailCreateView, self).get_context_data(**kwargs)
        context['user'] = user
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('PropertyDetail')


@method_decorator([login_required], name='dispatch')
class PropertyDetailListView(ListView):
    model = PropertyDetail
    # template_name = 'propertyDetail/index.html'
    template_name = 'propertyDetail/new_index.html'

    # context_object_name = 'all_items'

    def get_context_data(self, **kwargs):
        user = self.request.user
        all_items = PropertyDetail.objects.filter(user=user)
        context = super(PropertyDetailListView, self).get_context_data(**kwargs)
        context['all_items'] = all_items

        context['user'] = user
        statusFilters = {}
        statusFiltersList = []

        totalStatus = all_items.values('status').distinct()
        for status in totalStatus:
            stat = 'Verified' if status.get('status') == 'verified' else 'Pending'
            statusFilters.update({'value': stat})
            statusFilters.update({'name': 4})
            if statusFilters not in statusFiltersList:
                statusFiltersList.append(statusFilters)
            statusFilters = {}
        context['statusFilters'] = statusFiltersList
        return context


@method_decorator([login_required], name='dispatch')
class PropertyDetailUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'propertyDetail/create.html'
    model = PropertyDetail
    form_class = PropertyDetailForm
    success_message = 'Information Updated Successfully'

    def get_success_url(self):
        item = self.object

        # return redirect('PropertyDetail-show', item.id)
        return reverse_lazy('PropertyDetail-show', kwargs={'pk': item.id})

    def form_valid(self, form):
        propDet = form.save(commit=False)
        print('form.data')
        prop_id = self.object.id
        prop_detail = PropertyDetail.objects.get(id=prop_id)
        Accomodation.objects.filter(prop_det_id=prop_id).delete()
        list_of_accomodation = form.data.getlist('accomodation')
        for loa in list_of_accomodation:
            new_instance = Accomodation()
            new_instance.acc_name = loa
            new_instance.prop_det = prop_detail
            new_instance.save()
        return super(PropertyDetailUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(PropertyDetailUpdate, self).get_context_data(**kwargs)
        user = self.request.user.id
        accomodations = Accomodation.objects.filter(prop_det_id=self.object.id)
        list_acc = []
        for accomodation in accomodations:
            if accomodation not in list_acc:
                list_acc.append(accomodation.acc_name)
        list_of_acc = json.dumps(list_acc)
        context['user'] = user
        context['accomodations'] = list_of_acc
        return context


#
# legal_name = models.CharField(max_length=200, blank=True, null=True)
# business_name = models.CharField(max_length=200, blank=True, null=True)
# business_reg_date = models.CharField(max_length=60, null=True, blank=True)
# comm_open_date = models.CharField(max_length=60, null=True, blank=True)
# prop_history = models.CharField(max_length=200, blank=True, null=True)
# corp_address = models.CharField(max_length=200, blank=True, null=True)
# business_address = models.CharField(max_length=200, blank=True, null=True)
# comp_reg_name = models.CharField(max_length=200, blank=True, null=True)
# comp_reg_no = models.CharField(max_length=200, blank=True, null=True)
# bus_reg_no = models.CharField(max_length=200, blank=True, null=True)
# type_of_inc = models.CharField(max_length=200, blank=True, null=True)
# pan_number = models.CharField(max_length=60, null=True, blank=True)
# name_on_pancard = models.CharField(max_length=60, null=True, blank=True)
# vat_number = models.CharField(max_length=60, null=True, blank=True)
# busn_reg_cert = models.FileField(blank=True, default='default.png', upload_to=busn_reg_cert_path, max_length=100)
# busn_lcn_cert = models.FileField(blank=True, default='default.png', upload_to=busn_lcn_cert_path, max_length=100)
# pan_card_cert = models.FileField(blank=True, default='default.png', upload_to=pan_card_cert_path, max_length=100)
# vat_cert = models.FileField(blank=True, default='default.png', upload_to=vat_cert_path, max_length=100)
# car_rental = models.BooleanField(default=False)
# transport_company = models.BooleanField(default=False)
# travel_agency = models.BooleanField(default=False)
# food_deliver_agent = models.BooleanField(default=False)
# restaurant_bar_lounge = models.BooleanField(default=False)
# tour_operator = models.BooleanField(default=False)
# ticketing_agent = models.BooleanField(default=False)
# travel_agent = models.BooleanField(default=False)
# trekking_company = models.BooleanField(default=False)
# expedition_company = models.BooleanField(default=False)
# date = models.CharField(max_length=60, null=True, blank=True)
# applicant_name = models.CharField(max_length=10, blank=True, null=True)
# created_at = models.DateTimeField(default=datetime.now, blank=True)
# user = models.ForeignKey(User, on_delete=models.CASCADE)


@method_decorator([login_required], name='dispatch')
class OwnerNPropertyDetailView(FormView):
    template_name = 'propertyDetail/owernnproperty.html'
    form_class = OwnerAndPropertyForm

    def get_success_url(self):
        prop_id = self.prop_id
        if self.form.data['register'] == 'Save and Exit':
            url = reverse_lazy('PropertyDetail-show', kwargs={'pk': prop_id})
        else:
            url = reverse_lazy('PropertyDetail-show', kwargs={'pk': prop_id})
        return url
        # return reverse_lazy('dashboard')

    def form_valid(self, form):
        self.form = form
        print('form.data')
        print(form.data)
        new_owner = OwnerProfile.objects.get(user_id=self.request.user.id)
        country = Country.objects.get(id=form.data['Country'])
        new_owner.name = form.data['name']
        new_owner.Country = country
        new_owner.contact = form.data['contact']
        new_owner.email = form.data['email']
        new_owner.image = self.request.FILES['image'] if 'image' in self.request.FILES else 'default.png'
        new_owner.address = form.data['address']
        user = User.objects.get(id=form.data['user'])
        new_owner.user = user
        new_owner.is_owner = form.data['is_owner'] if 'is_owner' in form.data else 0
        new_owner.is_manager = form.data['is_manager'] if 'is_manager' in form.data else 0
        new_owner.document_type = form.data['document_type']
        new_owner.document = self.request.FILES['document'] if 'document' in self.request.FILES else 'default.png'
        new_owner.save()

        photo = new_owner
        if new_owner.image != 'default.png':
            # x = float(form.data['x']) if form.data['x'] != '' else 0
            # y = float(form.data['y']) if form.data['y'] != '' else 0
            # w = float(form.data['width']) if form.data['width'] != '' else 0
            # h = float(form.data['height']) if form.data['height'] != '' else 0

            x = float(form.data['x']) if form.data['x'] != '' else 0
            y = float(form.data['y']) if form.data['y'] != '' else 0
            w = float(form.data['width']) if form.data['width'] != '' else 0
            h = float(form.data['height']) if form.data['height'] != '' else 0

            if x != None:
                image = Image.open(photo.image)
                cropped_image = image.crop((x, y, w + x, h + y))
                cropped_image.save(photo.image.path)

            # image = Image.open(photo.image)
            # cropped_image = image.crop((x, y, w + x, h + y))
            # cropped_image.save(photo.image.path)

        new_prop = PropertyDetail()
        new_prop.legal_name = form.data['legal_name']
        new_prop.business_name = form.data['business_name']
        new_prop.business_reg_date = form.data['business_reg_date']
        new_prop.comm_open_date = form.data['comm_open_date']
        new_prop.prop_history = form.data['prop_history']
        new_prop.corp_address = form.data['corp_address']
        new_prop.business_address = form.data['business_address']
        new_prop.type_of_inc = form.data['type_of_inc']
        # new_prop.pan_number = form.data['pan_number']
        new_prop.name_on_pancard = form.data['name_on_pancard']
        new_prop.vat_number = form.data['vat_number']
        new_prop.busn_reg_cert = self.request.FILES[
            'busn_reg_cert'] if 'busn_reg_cert' in self.request.FILES else 'default.png'
        new_prop.busn_lcn_cert = self.request.FILES[
            'busn_lcn_cert'] if 'busn_lcn_cert' in self.request.FILES else 'default.png'
        new_prop.pan_card_cert = self.request.FILES[
            'pan_card_cert'] if 'pan_card_cert' in self.request.FILES else 'default.png'
        new_prop.vat_cert = self.request.FILES['vat_cert'] if 'vat_cert' in self.request.FILES else 'default.png'
        new_prop.car_rental = form.data['car_rental'] if 'car_rental' in form.data else 0
        new_prop.transport_company = form.data['transport_company'] if 'transport_company' in form.data else 0
        new_prop.travel_agency = form.data['travel_agency'] if 'travel_agency' in form.data else 0
        new_prop.food_deliver_agent = form.data['food_deliver_agent'] if 'food_deliver_agent' in form.data else 0
        new_prop.restaurant_bar_lounge = form.data[
            'restaurant_bar_lounge'] if 'restaurant_bar_lounge' in form.data else 0
        new_prop.tour_operator = form.data['tour_operator'] if 'tour_operator' in form.data else 0
        new_prop.ticketing_agent = form.data['ticketing_agent'] if 'ticketing_agent' in form.data else 0
        new_prop.travel_agent = form.data['travel_agent'] if 'travel_agent' in form.data else 0
        new_prop.trekking_company = form.data['trekking_company'] if 'trekking_company' in form.data else 0
        new_prop.expedition_company = form.data['expedition_company'] if 'expedition_company' in form.data else 0
        new_prop.date = form.data['date']
        new_prop.applicant_name = form.data['applicant_name']
        new_prop.user = user
        new_prop.save()
        list_of_accomodation = form.data.getlist('accomodation')
        for loa in list_of_accomodation:
            new_instance = Accomodation()
            new_instance.acc_name = loa
            new_instance.prop_det = new_prop
            new_instance.save()
        self.prop_id = new_prop.id
        return super(OwnerNPropertyDetailView, self).form_valid(form)

        # return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print('from from_invalid')
        print(form.data)
        print('form-errors')
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        countries = Country.objects.all()
        context = super(OwnerNPropertyDetailView, self).get_context_data(**kwargs)
        context['countries'] = countries
        return context


@method_decorator([login_required], name='dispatch')
class PropertyDetailShow(DetailView):
    model = PropertyDetail
    template_name = 'propertyDetail/show.html'
    queryset = PropertyDetail.objects.all()

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['pk']
        context = super(PropertyDetailShow, self).get_context_data(**kwargs)
        context['accomodations'] = Accomodation.objects.filter(prop_det_id=item_id)
        prop_status = PropertyDetail.objects.get(id=item_id).status
        hotel_already_created = Hotels.objects.filter(prop_id_id=item_id).exists()

        if prop_status == 'verified' or prop_status == 'active':
            if Hotels.objects.filter(prop_id_id=item_id).exists():
                context['hotel_id_id'] = Hotels.objects.filter(prop_id_id=item_id).first().id
                if hotel_already_created:
                    context['hotel_already_created'] = hotel_already_created

        return context


@login_required
def PropList(request):
    if request.user.is_superuser:
        all_items = PropertyDetail.objects.all()
    else:
        all_items = PropertyDetail.objects.filter(user_id=request.user.id)

    statusFilters = {}
    statusFiltersList = []

    totalStatus = all_items.values('status').distinct()
    for status in totalStatus:
        stat = 'Verified' if status.get('status') == 'verified' else 'Pending'
        statusFilters.update({'value': stat})
        statusFilters.update({'name': 4})
        if statusFilters not in statusFiltersList:
            statusFiltersList.append(statusFilters)
        statusFilters = {}

    context = {
        'all_items': all_items,
        'statusFilters': statusFiltersList,
    }
    return render(request, 'propertyDetail/new_index.html', context)


# @login_required
def verify_single_prop(request, item_id):
    PropertyDetail.objects.filter(id=item_id).update(is_verified=True)
    return redirect('proplist')
    # return render(request, 'propertyDetail/new_index.html')
    # return reverse_lazy('proplist')


from account.models import Account_Type


@login_required
def change_prop_status(request, item_id, status):
    PropertyDetail.objects.filter(id=item_id).update(status=status)
    user_id = PropertyDetail.objects.get(id=item_id).user_id
    hotel_owner = User.objects.get(id=user_id)
    is_hotel_owner = False
    hotel_owner_type = Account_Type.objects.get(type='hotel_owner')
    existing_account_type = hotel_owner.account_type.all()
    if hotel_owner_type in existing_account_type:
        is_hotel_owner = True

    # add hotel_owner permisions
    # all_permissions = Permission.objects.filter(content_type__model='hotels')
    if is_hotel_owner:
        permission1 = Permission.objects.get(name='Can add hotels')
        permission2 = Permission.objects.get(name='Can change hotels')
        permission3 = Permission.objects.get(name='Can view hotels')
        hotel_owner.user_permissions.add(permission1)
        hotel_owner.user_permissions.add(permission2)
        hotel_owner.user_permissions.add(permission3)

    if status == 'submitted':
        return redirect('proplist')

    return redirect('proplist')


def pdf_view(request, prop_id, type):
    user_id = PropertyDetail.objects.filter(id=prop_id).first().user_id
    owner_directory = 'user_' + str(user_id) + '/document/prop_' + str(prop_id) + '/'
    # directory_path = os.path.join(settings.MEDIA_ROOT, owner_directory)
    file_name = str(type) + str(user_id) + '.pdf'
    final_path = owner_directory + file_name
    file_path = os.path.join(settings.MEDIA_ROOT, final_path)
    # with open('/app/../Test.pdf', 'r') as pdf:
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=some_file.pdf'
        return response
    pdf.closed

# return 'user_{user_id}/{dir_name}/prop_{instance_id}/{renamed_file}{ext}'.format(user_id=user_id,
#                                                                            basename=basefilename,
#                                                                            dir_name=dir_name,
#                                                                            instance_id=instance_id,
#                                                                            renamed_file=renamed_file,
#                                                                            ext=file_extension)
