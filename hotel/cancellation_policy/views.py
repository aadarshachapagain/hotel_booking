"""
cancellation_policy views.py
----------------------------------
"""
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.views import View

from hotel.bankDetail.models import BankDetail
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from hotel.cancellation_policy.models import Cancellation_Policy
from hotel.cancellation_policy.forms import CancellationForm
from datetime import datetime

from travel.businessPolicies import send_policies

__author__ = "Aashish Paudel"


@method_decorator([login_required], name="dispatch")
class Cancellation_PolicyListView(ListView):
    model = Cancellation_Policy
    template_name = "cancellation_policy/index.html"
    context_object_name = "all_items"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Cancellation_PolicyListView, self).get_context_data(**kwargs)
        item_id = self.kwargs["item_id"]
        cancel = Cancellation_Policy.objects.filter(hotel=item_id, hotelInventory=None)
        context["all_items"] = cancel
        context["item_id"] = item_id
        return context


@method_decorator([login_required], name="dispatch")
class Cancellation_PolicyDelete(SuccessMessageMixin, DeleteView):
    model = Cancellation_Policy
    pk_url_kwarg = "include_id"

    def get(self, request, *args, **kwargs):
        """
        this is demo
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item_id = self.object.id
        x = Cancellation_Policy.objects.get(id=item_id)
        return reverse_lazy("hotel:cancelindex", kwargs={"item_id": x.hotel.id})

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


@method_decorator([login_required], name="dispatch")
class Cancellation_PolicyDetail(DetailView):
    model = Cancellation_Policy
    template_name = "cancellation_policy/show.html"
    queryset = Cancellation_Policy.objects.all().values()

    def get_context_data(self, **kwargs):
        context = super(Cancellation_PolicyDetail, self).get_context_data(**kwargs)
        policy_id = self.kwargs["pk"]
        hotel = Cancellation_Policy.objects.get(pk=policy_id).hotel_id
        policy = Cancellation_Policy.objects.get(pk=policy_id)
        context["hotel"] = hotel
        context["all_items"] = policy
        return context


@method_decorator([login_required], name="dispatch")
class Cancellation_PolicyCreate(SuccessMessageMixin, CreateView):
    template_name = "cancellation_policy/create.html"
    model = Cancellation_Policy
    form_class = CancellationForm
    success_message = "Information Added Successfully"

    def get_success_url(self, **kwargs):
        hotel_id = self.kwargs.get("item_id")
        if self.form.data['register'] == 'Save and Exit':
            url = reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': hotel_id})
        elif self.form.data['register'] == 'Save and Add New':
            url = reverse_lazy('hotel:cancelcreate', kwargs={'item_id': hotel_id})
        else:
            url = reverse_lazy('hotel:childSupplement-create', kwargs={'item_id': hotel_id})
        return url

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        hotel_id = self.kwargs.get("item_id")
        return self.render_to_response(
            self.get_context_data(object=form.data, hotel_id=hotel_id)
        )

    def form_valid(self, form):
        form.save(commit=False)
        data = form.cleaned_data
        hotel = get_object_or_404(Hotels, pk=self.kwargs.get("item_id"))
        cancel = Cancellation_Policy()
        cancel.hour = data.get("hour") or None
        cancel.cancellation_type = data.get("cancellation_type")
        cancel.price = data.get("price") or None
        cancel.hotel = hotel
        cancel.no_show = data.get("no_show") or None
        cancel.cancel_allow = data.get("cancel_allow")
        cancel.charge_cancel = data.get("charge_cancel") or None
        cancel.modification_allow = data.get("modification_allow")
        cancel.charge_modification = data.get("charge_modification") or None
        cancel.cvc_required = data.get("cvc_required")
        cancel.card_detail_required = data.get("card_detail_required")
        cancel.season_start_date = data.get("season_start_date") or None
        cancel.season_end_date = data.get("season_end_date") or None
        temp = ""
        for day in data.get("day"):
            if temp:
                temp = temp + "," + day
            else:
                temp = day
        cancel.day = temp or None
        cancel.change_status = "new"
        cancel.save()

        inventories = HotelInventory.objects.filter(hotel_id=hotel)
        for inventory in inventories:
            instance = Cancellation_Policy()
            instance.hotelInventory = HotelInventory.objects.get(id=inventory.pk)
            instance.parent = cancel
            instance.hotel = Hotels.objects.get(
                id=HotelInventory.objects.get(id=inventory.pk).hotel_id
            )
            instance.change_status = "assigned"
            instance.save()
        self.form = form
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Cancellation_PolicyCreate, self).get_context_data(**kwargs)
        package_id = self.kwargs["item_id"]
        temp = send_policies()
        y = json.loads(temp)
        x = Hotels.objects.get(id=package_id).pk
        context["policies"] = y
        context["hotel_id"] = x
        context["form"] = self.form_class
        return context


@method_decorator(login_required, name="dispatch")
class Cancellation_PolicyUpdate(SuccessMessageMixin, UpdateView):
    template_name = "cancellation_policy/create.html"
    model = Cancellation_Policy
    form_class = CancellationForm

    def get_success_url(self):
        item = self.hotel
        return reverse_lazy("hotel:cancelindex", kwargs={"item_id": item})

    def form_valid(self, form):
        hotel_id = self.model.objects.get(id=self.kwargs.get("pk")).hotel_id
        temp = form.save(commit=False)
        previous = self.model.objects.get(id=self.kwargs.get("pk"))
        previous.end_date = datetime.now()
        previous.save()
        data = form.cleaned_data
        hotel = get_object_or_404(Hotels, pk=hotel_id)
        cancel = Cancellation_Policy()
        cancel.hour = data.get("hour") or None
        cancel.cancellation_type = data.get("cancellation_type")
        cancel.price = data.get("price") or None
        cancel.hotel = hotel
        cancel.no_show = data.get("no_show") or None
        cancel.cancel_allow = data.get("cancel_allow")
        cancel.charge_cancel = data.get("charge_cancel") or None
        cancel.modification_allow = data.get("modification_allow")
        cancel.charge_modification = data.get("charge_modification") or None
        cancel.cvc_required = data.get("cvc_required")
        cancel.card_detail_required = data.get("card_detail_required")
        cancel.season_start_date = data.get("season_start_date") or None
        cancel.season_end_date = data.get("season_end_date") or None
        temp = ""
        for day in data.get("day"):
            if temp:
                temp = temp + "," + day
            else:
                temp = day
        cancel.day = temp or None
        cancel.change_status = "new"
        cancel.save()

        inventories = HotelInventory.objects.filter(hotel_id=hotel)
        for inventory in inventories:
            instance = Cancellation_Policy()
            instance.hotelInventory = HotelInventory.objects.get(id=inventory.pk)
            instance.parent = cancel
            instance.hotel = Hotels.objects.get(
                id=HotelInventory.objects.get(id=inventory.pk).hotel_id
            )
            instance.change_status = "assigned"
            instance.save()

        self.form = form
        self.hotel = hotel_id
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        item = self.model.objects.get(id=self.kwargs["pk"]).hotel_id
        return self.render_to_response(
            self.get_context_data(object=form.data, item=item)
        )

    def get_context_data(self, **kwargs):
        context = super(Cancellation_PolicyUpdate, self).get_context_data(**kwargs)
        arrayDay = self.model.objects.get(pk=self.kwargs["pk"]).day
        daysOfWeekList = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        day = {}
        objList = []
        if arrayDay:
            spilted = arrayDay.split(",")
            context["day"] = spilted

            for d in daysOfWeekList:
                day.update({"day": d})
                if d in spilted:
                    day.update({"status": "checked"})
                else:
                    day.update({"status": "unchecked"})
                objList.append(day)
                day = {}
        context["dayObj"] = objList
        context["hotel_id"] = self.model.objects.get(id=self.kwargs.get("pk")).hotel_id
        return context


@method_decorator(login_required, name="dispatch")
class Cancellation_PolicyUpdateInv(SuccessMessageMixin, UpdateView):
    template_name = "cancellation_policy/create.html"
    model = Cancellation_Policy
    form_class = CancellationForm

    def get_success_url(self):
        return reverse_lazy(
            "hotel:inventoryPolicies-create",
            kwargs={
                "model": "cancellation",
                "operation": "list",
                "id": self.hotel,
                "inv_id": self.kwargs.get("inventory_id"),
            },
        )

    def form_valid(self, form):
        hotel_id = self.model.objects.get(id=self.kwargs.get("pk")).hotel_id
        temp = form.save(commit=False)
        previous = self.model.objects.get(id=self.kwargs.get("pk"))
        previous.save()
        data = form.cleaned_data
        hotel = get_object_or_404(Hotels, pk=hotel_id)
        cancel = Cancellation_Policy()
        cancel.hour = data.get("hour") or None
        cancel.cancellation_type = data.get("cancellation_type")
        cancel.price = data.get("price") or None
        cancel.hotel = hotel
        cancel.hotelInventory = HotelInventory.objects.get(
            id=self.kwargs.get("inventory_id")
        )
        cancel.no_show = data.get("no_show") or None
        cancel.cancel_allow = data.get("cancel_allow")
        cancel.charge_cancel = data.get("charge_cancel") or None
        cancel.modification_allow = data.get("modification_allow")
        cancel.charge_modification = data.get("charge_modification") or None
        cancel.cvc_required = data.get("cvc_required")
        cancel.card_detail_required = data.get("card_detail_required")
        cancel.season_start_date = data.get("season_start_date") or None
        cancel.season_end_date = data.get("season_end_date") or None
        temp = ""
        for day in data.get("day"):
            if temp:
                temp = temp + "," + day
            else:
                temp = day
        cancel.day = temp or None
        cancel.change_status = "copied"
        cancel.save()
        self.form = form
        self.hotel = hotel_id
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(Cancellation_PolicyUpdateInv, self).get_context_data(**kwargs)

        parent_id = self.model.objects.get(pk=self.kwargs.get("pk")).parent_id
        if not parent_id:
            parent_id = self.model.objects.get(pk=self.kwargs.get("pk")).pk

        arrayDay = self.model.objects.get(pk=parent_id).day
        daysOfWeekList = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        day = {}
        objList = []
        if arrayDay:
            spilted = arrayDay.split(",")
            context["day"] = spilted

            for d in daysOfWeekList:
                day.update({"day": d})
                if d in spilted:
                    day.update({"status": "checked"})
                else:
                    day.update({"status": "unchecked"})
                objList.append(day)
                day = {}
        context["dayObj"] = objList
        context["hotel_id"] = self.model.objects.get(id=self.kwargs.get("pk")).hotel_id
        return context

    def get_object(self, queryset=None):
        parent_id = self.model.objects.get(pk=self.kwargs.get("pk")).parent_id

        if not parent_id:
            parent_id = self.model.objects.get(pk=self.kwargs.get("pk")).pk

        return self.model.objects.get(pk=parent_id)


@method_decorator([login_required], name="dispatch")
class Cancellation_PolicyDeleteInv(SuccessMessageMixin, DeleteView):
    model = Cancellation_Policy

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item_id = self.object.id
        hotel = Cancellation_Policy.objects.get(id=item_id).hotel_id
        inventory = Cancellation_Policy.objects.get(id=item_id).hotelInventory_id
        return reverse_lazy(
            "hotel:inventoryPolicies-create",
            kwargs={
                "model": "cancellation",
                "operation": "list",
                "id": hotel,
                "inv_id": inventory,
            },
        )

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


def editsingle(request, item_id):
    items = Cancellation_Policy.objects.get(id=item_id)
    data = {
        "item": items,
    }
    return render(request, "cancellation_policy/editsingle.html", data)


def updateinclude(request):
    if request.method == "POST":
        form = CancellationForm(request.POST or None, request.FILES)
        if form.is_valid():
            x = form.data.get("inventory")
            form = form.save(commit=False)
            cancelId = request.POST.get("cancelId")
            day = request.POST.get("day")
            price = request.POST.get("price")
            inventory = HotelInventory.objects.get(id=x)
            instance = Cancellation_Policy.objects.get(id=cancelId)
            instance.day = day
            instance.price = price
            instance.inventory = inventory
            instance.save()
            return redirect("hotel:cancelindex", inventory)
        else:
            return HttpResponse("KAAM vayena")
    else:
        return HttpResponse(request.form.errors)


class getCancellationPolicy(View):
    
    def get(self, request):
        temp = send_policies()
        y = json.loads(temp)
        print(type(y))
        return HttpResponse(y)
