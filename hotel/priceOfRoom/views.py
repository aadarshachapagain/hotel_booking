from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hotel.b2b.models import B2B
from hotel.child_supplement_policy.forms import ChildSupplementPolicyForm
from hotel.child_supplement_policy.models import ChildSupplementPolicy
from hotel.inventory.models import HotelInventory
from hotel.inventorygallery.models import InventoryGallery
from hotel.models import Hotels
from hotel.priceOfRoom.models import PriceInDiffSys
from hotel.priceOfRoom.forms import PriceInDiffSysForm
from hotel.inventory_bed_type.models import Inventory_Bed_Type
from hotel.mealPlan.models import MealPlan
from hotel.similarSystems.models import SimilarSystems
from hotel.priceOfRoom.forms import SysInfo
from decimal import Decimal
import json
from itertools import groupby
from collections import Counter


@method_decorator([login_required], name='dispatch')
class PriceOfDiffSystemCreate(SuccessMessageMixin, CreateView):
    template_name = 'pricefordiffsys/create.html'
    model = PriceInDiffSys
    form_class = PriceInDiffSysForm
    success_message = 'Information Added Successfully'

    def form_valid(self, form):
        bigsafarexists = SimilarSystems.objects.filter(name__startswith="Bigsafar").exists()
        if bigsafarexists:
            big_safar_id = SimilarSystems.objects.get(name__contains='Bigsafar').id
        epplanexists = MealPlan.objects.filter(plan__startswith="EP").exists()
        bbplanexists = MealPlan.objects.filter(plan__startswith="BB").exists()
        if epplanexists:
            ep_plan_id = MealPlan.objects.get(plan__contains='EP').id
        if bbplanexists:
            bb_plan_id = MealPlan.objects.get(plan__contains='BB').id
        other_systems = form.data.getlist('other_systems')
        meal_plans = form.data.getlist('meal_plans')
        price = form.data.getlist('price')
        inv_id = form.data['inventory']
        if 'adult_max' in form.data:
            adult_max = int(form.data['adult_max'])
        priceforadult = {}
        if (adult_max > 1):
            for j in range(0, adult_max - 1):
                keyadult = "adult" + str(j)
                if keyadult in form.data:
                    if form.data[keyadult] == '':
                        priceforadult[keyadult] = '0'
                    elif form.data[keyadult] != '':
                        priceforadult[keyadult] = form.data[keyadult]
        elif (adult_max == 1):
            priceforadult = '0'
        inv_instance = HotelInventory.objects.get(id=inv_id)
        listofSysInfo = []
        listofBsInfo = []

        ep_price = 0
        bb_price = 0

        if HotelInventory.objects.filter(id=inv_id).exists():
            ep_price = HotelInventory.objects.get(id=inv_id).european_plan
            bb_price = HotelInventory.objects.get(id=inv_id).bedandbreakfast_plan

        distinct_list = (Counter(meal_plans).keys())
        no_distict_mealplan = len(distinct_list)
        for index, item in enumerate(other_systems):
            obj = SysInfo()
            if int(big_safar_id) != int(other_systems[index]):
                obj.system = other_systems[index]
                obj.mealplan = meal_plans[index]
                if price[index]:
                    obj.price = Decimal(price[index])
                else:
                    obj.price = 0
                listofSysInfo.append(obj)
            elif int(big_safar_id) == int(other_systems[index]):
                obj.system = other_systems[index]
                obj.mealplan = meal_plans[index]
                if price[index]:
                    obj.price = Decimal(price[index])
                else:
                    obj.price = 0
                listofBsInfo.append(obj)
        grouped_by_meal_plan = []
        for item1 in distinct_list:
            arr = []
            for single in listofSysInfo:
                if int(single.mealplan) == int(item1):
                    arr.append(single)
            if len(arr) != 0:
                grouped_by_meal_plan.append(arr)
        # big safar ko check garna ko lagi
        bs_distinct_list_mp = []
        bs_sep_obj_by_mp = []
        for dl in distinct_list:
            bsarr = []
            for bsingle in listofBsInfo:
                if bsingle.mealplan == dl:
                    bs_distinct_list_mp.append(bsingle.mealplan)
                    bsarr.append(bsingle)
            if len(bsarr) != 0:
                bs_sep_obj_by_mp.append(bsarr)
        # big safar ko check garna ko lagi
        grouped_by_meal_plan_sorted_price = []
        for gbmp in grouped_by_meal_plan:
            brr = []
            brr = sorted(gbmp, key=lambda x: x.price, reverse=False)
            grouped_by_meal_plan_sorted_price.append(brr)
        final_price_bs = []
        final_price_othersys = []
        uniq_bs_list = []
        uniq_oths_list = []
        passed_mealplan = []
        failed_mealplan = []

        for si_of_bs in bs_sep_obj_by_mp:
            uiq_obj = SysInfo()
            uiq_obj.price = si_of_bs[0].price
            uiq_obj.mealplan = si_of_bs[0].mealplan
            uiq_obj.system = si_of_bs[0].system
            uniq_bs_list.append(uiq_obj)
            final_price_bs.append(si_of_bs[0].price)

        for si_of_others in grouped_by_meal_plan_sorted_price:
            uiq_obj2 = SysInfo()
            uiq_obj2.price = si_of_others[0].price
            uiq_obj2.mealplan = si_of_others[0].mealplan
            uiq_obj2.system = si_of_others[0].system
            uniq_oths_list.append(uiq_obj2)
        int_bs_distinct_list_mp = [int(l) for l in bs_distinct_list_mp]

        sorted_bs_distinct_list_mp = sorted(int_bs_distinct_list_mp, reverse=False)

        ubl_list = []
        uol_list = []

        # for mealplan that are only in either BS or other system
        for ubl in uniq_bs_list:
            ubl_list.append(ubl.mealplan)
        sorted_ubl_list = sorted(ubl_list, reverse=False)
        sorted_ubl_list = [int(h) for h in sorted_ubl_list]

        for uol in uniq_oths_list:
            uol_list.append(uol.mealplan)
        sorted_uol_list = sorted(uol_list, reverse=False)
        sorted_uol_list = [int(j) for j in sorted_uol_list]
        union_list = list(set(sorted_ubl_list).union(set(sorted_uol_list)))
        intersection = list(set(sorted_uol_list) & set(sorted_uol_list))
        a_compUb_comp = list(set(union_list) - set(intersection))

        only_in_others = list(set(sorted_uol_list) - set(sorted_ubl_list))
        # for mealplan that are only in other system

        for eachbs in uniq_bs_list:
            if len(uniq_oths_list) == 0:
                passed_mealplan.append(int(eachbs.mealplan))
            else:
                for eachos in uniq_oths_list:
                    if eachos.mealplan == '':
                        passed_mealplan.append(int(eachbs.mealplan))

                    if eachbs.mealplan == eachos.mealplan and eachbs.price <= eachos.price:
                        passed_mealplan.append(int(eachbs.mealplan))

        sorted_passed_mealplan = sorted(passed_mealplan, reverse=False)
        int_distinct_list = [int(i) for i in distinct_list]
        sorted_distinct_list = sorted(int_distinct_list, reverse=False)

        failed = list(set(sorted_bs_distinct_list_mp) - set(sorted_passed_mealplan))

        for acb in a_compUb_comp:
            if acb in failed:
                try:
                    failed.remove(acb)
                except:
                    print('cannot Remove')

        len_of_final_price_bs = len(final_price_bs)
        newlist = sorted(listofSysInfo, key=lambda x: x.price, reverse=False)
        newbslist = sorted(listofBsInfo, key=lambda x: x.price, reverse=False)

        for index, element in enumerate(newbslist):
            if int(element.system) == int(big_safar_id):
                if int(element.mealplan) == int(ep_plan_id):
                    ep_price = element.price
                if int(element.mealplan) == int(bb_plan_id):
                    bb_price = element.price

        pos = 1
        if len(failed) == 0:
            pos = 0
        else:
            pos = 1

        if pos != 0:
            msg = 'Please provide Lowest Possible rate for Bigsafar'
            form.add_error('price', msg)
            return super().form_invalid(form)
        elif pos == 0:
            for nl in newlist:
                # if int(nl.system) != int(big_safar_id):
                instance = PriceInDiffSys()
                system = SimilarSystems.objects.get(id=nl.system)
                mp = MealPlan.objects.get(id=nl.mealplan)
                instance.inventory = inv_instance
                instance.price = nl.price
                instance.other_systems = system
                instance.meal_plans = mp
                instance.status = True
                instance.save()
            inventory_instance = HotelInventory.objects.get(id=inv_id)
            inventory_instance.european_plan = ep_price
            inventory_instance.bedandbreakfast_plan = bb_price
            inventory_instance.priceforadult = json.dumps(priceforadult)
            inventory_instance.save()
            return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inv_id = self.kwargs['inv_id']
        hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
        adult_max = HotelInventory.objects.get(id=inv_id).adult_max
        context['inv_id'] = inv_id
        context['hotel_id'] = hotel_id
        context['adult_max'] = adult_max
        return context

    def get_success_url(self):
        inv_id = self.kwargs['inv_id']
        gallery = InventoryGallery.objects.filter(hotel_inventory_id=inv_id).count()
        if gallery <= 0:
            return reverse_lazy('hotel:inventorygallery-create', kwargs={'item_id': inv_id})
        else:
            return reverse_lazy('hotel:inventory-price-list', kwargs={'inv_id': inv_id})


@method_decorator([login_required], name='dispatch')
class PriceOfDiffSystemListView(SuccessMessageMixin, ListView):
    model = PriceInDiffSys
    template_name = 'pricefordiffsys/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PriceOfDiffSystemListView, self).get_context_data(**kwargs)
        inv_id = self.kwargs['inv_id']
        hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
        all_items = PriceInDiffSys.objects.filter(inventory_id=inv_id)
        ep_plan_id = MealPlan.objects.get(plan__contains='EP').id
        bb_plan_id = MealPlan.objects.get(plan__contains='BB').id
        message = ''
        ep_min_price = 0
        bb_min_price = 0
        inv_ep = HotelInventory.objects.get(id=inv_id).european_plan
        inv_bb = HotelInventory.objects.get(id=inv_id).bedandbreakfast_plan

        if PriceInDiffSys.objects.filter(inventory_id=inv_id).exists():
            items_same_inv_n_ep = PriceInDiffSys.objects.filter(inventory_id=inv_id, meal_plans_id=ep_plan_id).order_by(
                'price').first()
            items_same_inv_n_bb = PriceInDiffSys.objects.filter(inventory_id=inv_id, meal_plans_id=bb_plan_id).order_by(
                'price').first()
            if items_same_inv_n_ep:
                ep_min_price = items_same_inv_n_ep.price
                if ep_min_price < inv_ep:
                    message = 'Please provide lowest possible EP price for Bigsafar'

            if items_same_inv_n_bb:
                bb_min_price = items_same_inv_n_bb.price
                if bb_min_price < inv_bb:
                    message = 'Please provide lowest possible BB price for Bigsafar'

            if items_same_inv_n_ep and items_same_inv_n_bb:
                ep_min_price = items_same_inv_n_ep.price
                bb_min_price = items_same_inv_n_bb.price
                if ep_min_price < inv_ep and bb_min_price < inv_bb:
                    message = 'Please provide lowest possible EP and BB price for Bigsafar'
        context['message'] = message
        context['all_items'] = all_items
        context['inv_id'] = inv_id
        context['hotel_id'] = hotel_id
        return context


@method_decorator([login_required], name='dispatch')
class PriceOfDiffSystemDelete(SuccessMessageMixin, DeleteView):
    model = PriceInDiffSys
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item_id = self.object.id
        inv_id = PriceInDiffSys.objects.get(id=item_id).inventory_id
        return reverse_lazy('hotel:inventory-price-list', kwargs={'inv_id': inv_id})

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


@method_decorator([login_required], name='dispatch')
class PriceOfDiffSystemUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'pricefordiffsys/edit.html'
    model = PriceInDiffSys
    form_class = PriceInDiffSysForm
    success_message = 'Information Updated Successfully'
    queryset = PriceInDiffSys.objects.all()

    # def form_valid(self, form):
    #     # self.hotel = form.data.get('hotel')
    #     item = form.save(commit=False)
    #     print('item')
    #     print(item)
    #     item.price = form.data['price']
    #     item.mealplan = form.data['meal_plans']
    #     # item.save()
    #
    #     # print('form.data')
    #     # print(form.data)
    #     # return super().form_valid(form)
    #     return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(PriceOfDiffSystemUpdate, self).get_context_data(**kwargs)
        item_id = self.kwargs['pk']
        inv_id = PriceInDiffSys.objects.get(id=item_id).inventory_id
        hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
        context['inv_id'] = inv_id
        context['hotel_id'] = hotel_id
        return context

    def get_success_url(self):
        item_id = self.object.id
        inv_id = PriceInDiffSys.objects.get(id=item_id).inventory_id
        cancel = Inventory_Bed_Type.objects.filter(inventory_id=inv_id).count()
        if cancel <= 0:
            return reverse_lazy('hotel:inv-bed-type-create', kwargs={'item_id': inv_id})

        else:
            return reverse_lazy('hotel:inventory-price-list', kwargs={'inv_id': inv_id})


from hotel.priceOfRoom.forms import PriceForAllSysForm


class PriceOfRoom(FormView):
    template_name = 'pricefordiffsys/new_create.html'
    # model = PriceInDiffSys
    # form_class = PriceInDiffSysForm
    form_class = PriceForAllSysForm
    success_message = 'Information Added Successfully'

    def get_success_url(self):
        inv_id = self.kwargs['inv_id']
        gallery = InventoryGallery.objects.filter(hotel_inventory_id=inv_id).count()
        if gallery <= 0:
            return reverse_lazy('hotel:inventorygallery-create', kwargs={'item_id': inv_id})
        else:
            return reverse_lazy('hotel:showinvdetail', kwargs={'pk': inv_id})

    def get_context_data(self, **kwargs):
        context = super(PriceOfRoom, self).get_context_data(**kwargs)
        hotel_inv_id = self.kwargs['inv_id']
        hotel_id = HotelInventory.objects.get(id=hotel_inv_id).hotel.id
        similar_sys = SimilarSystems.objects.all()
        meal_plans = MealPlan.objects.all()
        context['similar_sys'] = similar_sys
        context['hotel_inv_id'] = hotel_inv_id
        context['hotel_id'] = hotel_id
        existingfeature = MealPlan.objects.all()
        meal_plan_list = []
        for ef in existingfeature:
            dict = model_to_dict(ef)
            del dict['created_at']
            meal_plan_list.append(dict)
        context['meal_plans'] = json.dumps(meal_plan_list)
        return context

    def form_valid(self, form):
        ep = form.data['EP'] if form.data['EP'] != '' else 0.00
        bb = form.data['BB'] if form.data['BB'] != '' else 0.00
        HotelInventory.objects.filter(id=form.data['inventory']).update(european_plan=ep, bedandbreakfast_plan=bb)
        meal_plans = form.data.getlist('meal_plans')
        dist_mp = []
        for mp in meal_plans:
            if mp not in dist_mp:
                dist_mp.append(mp)

        if 'price' in form.data:
            k = -1
            for index, othersys in enumerate(form.data.getlist('other_systems')):
                for jndex, meal_plan in enumerate(dist_mp):
                    k = k + 1
                    obj = PriceInDiffSys()
                    obj.meal_plans = MealPlan.objects.get(id=meal_plan)
                    obj.other_systems = SimilarSystems.objects.get(id=othersys)
                    obj.price = form.data.getlist('price')[k] if form.data.getlist('price')[k] != '' else 0.00
                    obj.inventory = HotelInventory.objects.get(id=form.data['inventory'])
                    obj.status = True
                    obj.save()
        return super(PriceOfRoom, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
