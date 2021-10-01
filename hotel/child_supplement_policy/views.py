from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hotel.b2b.models import B2B
from hotel.child_supplement_policy.forms import ChildSupplementPolicyForm
from hotel.child_supplement_policy.models import ChildSupplementPolicy
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels


class childSupplementListView(ListView):
    model = ChildSupplementPolicy
    template_name = 'childSupplementPolicy/index.html'
    context_object_name = 'all_items'

    def get_context_data(self, **kwargs):
        context = super(childSupplementListView, self).get_context_data(**kwargs)
        hotel_id = self.kwargs.get('item_id')
        all_items = ChildSupplementPolicy.objects.filter(hotel=hotel_id, hotelInventory=None)
        context.update({'hotel_id': hotel_id})
        context.update({'all_items': all_items})
        return context


@method_decorator([login_required], name='dispatch')
class childSupplementCreate(SuccessMessageMixin, CreateView):
    template_name = 'childSupplementPolicy/create.html'
    model = ChildSupplementPolicy
    form_class = ChildSupplementPolicyForm
    success_message = 'Information Added Successfully'

    def form_valid(self, form):
        self.form = form
        form.save(commit=False)
        hotel = form.data.get('hotel')
        age_category = form.data.getlist('age_category')
        age_start = form.data.getlist('age_start')
        age_end = form.data.getlist('age_end')
        cost_status = form.data.getlist('cost_status')
        cost = form.data.getlist('cost')
        unit = form.data.getlist('unit')
        season_start_date = form.data.getlist('season_start_date')
        season_end_date = form.data.getlist('season_end_date')
        day = form.data.getlist('day')
        DayCount = form.data.getlist('DayCount')
        seperator = ","
        for index, age_cat in enumerate(age_category):
            instance = ChildSupplementPolicy()
            instance.hotel = Hotels.objects.get(pk=hotel)
            instance.age_category = age_cat
            instance.age_start = age_start[index]
            instance.age_end = age_end[index]
            instance.cost_status = cost_status[index]
            instance.cost = cost[index] or 0.0
            instance.unit = None if cost_status[index] == 'Free' else unit[index]
            instance.change_status = 'new'
            instance.season_start_date = season_start_date[index] or None
            instance.season_end_date = season_end_date[index] or None
            a = seperator.join(day[:int(DayCount[index])])
            del day[0:int(DayCount[index])]
            instance.day = a or None
            instance.save()

            inventories = HotelInventory.objects.filter(hotel_id=hotel)
            for inventory in inventories:
                cancel = ChildSupplementPolicy()
                cancel.hotelInventory = HotelInventory.objects.get(id=inventory.pk)
                cancel.parent = instance
                cancel.hotel = Hotels.objects.get(id=HotelInventory.objects.get(id=inventory.pk).hotel_id)
                cancel.change_status = 'assigned'
                cancel.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        print(form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(childSupplementCreate, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):

        if self.form.data['register'] == 'Save and Exit':
            url = reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': self.kwargs.get('item_id')})
        else:
            url = reverse_lazy('hotel:extraBedPolicy-create', kwargs={'item_id': self.kwargs.get('item_id')})
        return url
        # return reverse_lazy('hotel:childSupplement', kwargs={'item_id': self.kwargs.get('item_id')})

    def get_form_kwargs(self):
        kwargs = super(childSupplementCreate, self).get_form_kwargs()
        hotel_id = self.kwargs.get('item_id')
        kwargs['action'] = 'create'
        kwargs['hotel'] = hotel_id
        return kwargs


@method_decorator([login_required], name='dispatch')
class childSupplementUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'childSupplementPolicy/create.html'
    model = ChildSupplementPolicy
    form_class = ChildSupplementPolicyForm
    success_message = 'Information Updated Successfully'
    queryset = ChildSupplementPolicy.objects.all()

    def form_valid(self, form):
        self.hotel = form.data.get('hotel')
        form.save(commit=False)
        data = form.cleaned_data
        hotel = data.get('hotel')
        instance = ChildSupplementPolicy.objects.get(pk=self.kwargs['pk'])
        # instance.hotel = Hotels.objects.get(pk=hotel)
        instance.age_category = data.get('age_category')
        instance.age_start = data.get('age_start')
        instance.age_end = data.get('age_end')
        instance.cost_status = data.get('cost_status')
        instance.cost = data.get('cost') or 0.0
        instance.unit = None if data.get('cost_status') == 'Free' else data.get('unit')
        instance.change_status = 'new'
        instance.season_start_date = data.get('season_start_date') or None
        instance.season_end_date = data.get('season_end_date') or None
        temp = ""
        for d in data.get('day'):
            if temp:
                temp = temp + ',' + d
            else:
                temp = d
        instance.day = temp or None
        instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(childSupplementUpdate, self).get_context_data(**kwargs)
        arrayDay = self.model.objects.get(pk=self.kwargs['pk']).day
        daysOfWeekList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = {}
        objList = []
        if arrayDay:
            spilted = arrayDay.split(',')
            # spilted.pop(0)
            context['day'] = spilted

            for d in daysOfWeekList:
                day.update({'day': d})
                if d in spilted:
                    day.update({'status': 'checked'})
                else:
                    day.update({'status': 'unchecked'})
                objList.append(day)
                day = {}
        context['dayObj'] = objList
        return context

    def get_form_kwargs(self):
        kwargs = super(childSupplementUpdate, self).get_form_kwargs()
        pk = self.kwargs.get('pk')
        hotel_id = ChildSupplementPolicy.objects.get(pk=pk).hotel_id
        kwargs['hotel'] = hotel_id
        kwargs['action'] = 'edit'
        return kwargs

    def get_success_url(self):
        hotel_id = self.hotel
        return reverse_lazy('hotel:childSupplement', kwargs={'item_id': hotel_id})


@method_decorator([login_required], name='dispatch')
class childSupplementUpdateInv(SuccessMessageMixin, UpdateView):
    template_name = 'childSupplementPolicy/create.html'
    model = ChildSupplementPolicy
    form_class = ChildSupplementPolicyForm
    success_message = 'Information Updated Successfully'
    queryset = ChildSupplementPolicy.objects.all()

    def form_valid(self, form):
        self.hotel = form.data.get('hotel')
        temp = form.save(commit=False)
        hotel_id = self.model.objects.get(id=self.kwargs.get('pk')).hotel_id
        previous = self.model.objects.get(id=self.kwargs.get('pk'))
        previous.save()
        data = form.cleaned_data
        instance = ChildSupplementPolicy()
        hotel = get_object_or_404(Hotels, pk=hotel_id)
        instance.hotel = hotel
        instance.hotelInventory = HotelInventory.objects.get(id=self.kwargs.get('inventory_id'))
        instance.age_category = data.get('age_category')
        instance.age_start = data.get('age_start')
        instance.age_end = data.get('age_end')
        instance.cost_status = data.get('cost_status')
        instance.cost = data.get('cost') or 0.0
        instance.unit = None if data.get('cost_status') == 'Free' else data.get('unit')
        instance.season_start_date = data.get('season_start_date') or None
        instance.season_end_date = data.get('season_end_date') or None
        temp = ""
        for d in data.get('day'):
            if temp:
                temp = temp + ',' + d
            else:
                temp = d
        instance.day = temp or None
        instance.change_status = 'copied'
        instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(childSupplementUpdateInv, self).get_context_data(**kwargs)
        parent_id = self.model.objects.get(pk=self.kwargs.get('pk')).parent_id
        if not parent_id:
            parent_id = self.model.objects.get(pk=self.kwargs.get('pk')).pk
        arrayDay = self.model.objects.get(pk=parent_id).day
        daysOfWeekList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = {}
        objList = []
        if arrayDay:
            spilted = arrayDay.split(',')
            # spilted.pop(0)
            context['day'] = spilted

            for d in daysOfWeekList:
                day.update({'day': d})
                if d in spilted:
                    day.update({'status': 'checked'})
                else:
                    day.update({'status': 'unchecked'})
                objList.append(day)
                day = {}
        context['dayObj'] = objList
        return context

    def get_form_kwargs(self):
        kwargs = super(childSupplementUpdateInv, self).get_form_kwargs()
        pk = self.kwargs.get('pk')
        hotel_id = ChildSupplementPolicy.objects.get(pk=pk).hotel_id
        kwargs['hotel'] = hotel_id
        kwargs['action'] = 'edit'
        return kwargs

    def get_success_url(self):
        return reverse_lazy('hotel:inventoryPolicies-create',
                            kwargs={'model': 'childsupplement', 'operation': 'list', 'id': self.hotel,
                                    'inv_id': self.kwargs.get('inventory_id')})

    def get_object(self, queryset=None):
        parent_id = self.model.objects.get(pk=self.kwargs.get('pk')).parent_id

        if not parent_id:
            parent_id = self.model.objects.get(pk=self.kwargs.get('pk')).pk

        return self.model.objects.get(pk=parent_id)


@method_decorator([login_required], name='dispatch')
class childSupplementDelete(SuccessMessageMixin, DeleteView):
    model = ChildSupplementPolicy

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted.")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item_id = self.object.id
        hotel_id = ChildSupplementPolicy.objects.get(id=item_id).hotel_id
        return reverse_lazy('hotel:childSupplement', kwargs={'item_id': hotel_id})

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


@method_decorator([login_required], name='dispatch')
class childSupplementDeleteInv(SuccessMessageMixin, DeleteView):
    model = ChildSupplementPolicy

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted.")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item_id = self.object.id
        hotel = ChildSupplementPolicy.objects.get(id=item_id).hotel_id
        inventory = ChildSupplementPolicy.objects.get(id=item_id).hotelInventory_id
        return reverse_lazy('hotel:inventoryPolicies-create',
                            kwargs={'model': 'childsupplement', 'operation': 'list', 'id': hotel, 'inv_id': inventory})

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
