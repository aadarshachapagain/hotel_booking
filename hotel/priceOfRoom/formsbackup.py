from django import forms
from hotel.mealPlan.models import MealPlan
from hotel.priceOfRoom.models import PriceInDiffSys
from hotel.similarSystems.models import SimilarSystems
from hotel.mealPlan.models import MealPlan
from hotel.priceOfRoom.models import PriceInDiffSys
from collections import Counter
from hotel.inventory.models import HotelInventory
from decimal import Decimal
import json
from itertools import groupby
import numpy as np


class PriceInDiffSysForm(forms.ModelForm):
    other_systems = forms.ModelChoiceField(
        queryset=SimilarSystems.objects.all(),
        widget=forms.Select(attrs={'class': "form-control custom-input-box myselect"}),
        help_text="Select Systems from dropdown below.",
        empty_label=None,
    )

    meal_plans = forms.ModelChoiceField(
        queryset=MealPlan.objects.all(),
        widget=forms.Select(attrs={'class': "form-control custom-input-box myselect"}),
        help_text="Select MealPlan from dropdown below.",
        empty_label=None,

    )

    inventory = forms.ModelChoiceField(
        queryset=HotelInventory.objects.all(),
        empty_label=None,
    )

    # price = forms.DecimalField(
    #     label='Price',
    #     help_text="Price",
    #     required=False
    # )
    price = forms.CharField(label='Price',
                            widget=forms.TextInput(attrs={'placeholder': 'Price'}),
                            required=False
                            )
    status = forms.BooleanField(
        label='Status',
        required=False,
    )

    class Meta:
        model = PriceInDiffSys
        fields = [
            "inventory",
            "other_systems",
            "meal_plans",
            "price",
        ]

        widgets = {
            'inventory': forms.HiddenInput()
        }

    def clean(self):
        # a = [2, 3, 4, 5, 6, 7, 8]
        # b = [3, 4, 5, 6]
        # c = []
        # d = []
        # print('d.index(False)')
        # if 'False' not in d:
        #     print('False doesnot exist in array d')
        #
        # print('np.less_equal(c, d)')
        # print(np.less_equal(d, d))
        # len_of_b = len(b)
        # len_of_a = len(a)
        # diff_in_length = len_of_b - len_of_a
        # print('diff_in_length')
        # print(diff_in_length)
        # if diff_in_length < 0:
        #     abs_length = abs(diff_in_length)
        #     for j in range(0, abs_length):
        #         a.pop()
        # print('a after poping')
        # print(a)

        # for i in range(len_of_b, len_of_a):
        #     print('a[i-1]')
        #     print(a[i - 1])
        # print('np.less_equal(a, b)')
        # print(np.less_equal(a, b))
        bigsafarexists = SimilarSystems.objects.filter(name__startswith="Bigsafar").exists()
        if bigsafarexists:
            big_safar_id = SimilarSystems.objects.get(name__contains='Bigsafar').id

        epplanexists = MealPlan.objects.filter(plan__startswith="EP").exists()
        bbplanexists = MealPlan.objects.filter(plan__startswith="BB").exists()
        if epplanexists:
            ep_plan_id = MealPlan.objects.get(plan__contains='EP').id
        if bbplanexists:
            bb_plan_id = MealPlan.objects.get(plan__contains='BB').id

        other_systems = self.data.getlist('other_systems')
        meal_plans = self.data.getlist('meal_plans')
        price = self.data.getlist('price')
        inv_id = self.data['inventory']

        if 'adult_max' in self.data:
            adult_max = int(self.data['adult_max'])
        priceforadult = {}

        if (adult_max > 1):
            for j in range(0, adult_max - 1):
                keyadult = "adult" + str(j)
                if keyadult in self.data:
                    if self.data[keyadult] == '':
                        priceforadult[keyadult] = '0'
                    elif self.data[keyadult] != '':
                        priceforadult[keyadult] = self.data[keyadult]
        elif (adult_max == 1):
            priceforadult = '0'

        inv_instance = HotelInventory.objects.get(id=inv_id)
        listofSysInfo = []
        listofBsInfo = []

        ep_price = 0
        bb_price = 0
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

        print('listofBsInfo')
        print(listofBsInfo)

        grouped_by_meal_plan = []
        for item1 in distinct_list:
            arr = []
            for single in listofSysInfo:
                if int(single.mealplan) == int(item1):
                    arr.append(single)
            if len(arr) != 0:
                grouped_by_meal_plan.append(arr)
        # print('grouped_by_meal_plan')
        # print(grouped_by_meal_plan)
        # print('len(grouped_by_meal_plan)')
        # print(len(grouped_by_meal_plan))

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
                # grouped_by_meal_plan.append(bsarr)
                bs_sep_obj_by_mp.append(bsarr)
        print('bs_distinct_list_mp')
        print(bs_distinct_list_mp)

        print('bs_sep_obj_by_mp')
        print(bs_sep_obj_by_mp)
        # big safar ko check garna ko lagi

        grouped_by_meal_plan_sorted_price = []

        for gbmp in grouped_by_meal_plan:
            brr = []
            brr = sorted(gbmp, key=lambda x: x.price, reverse=False)
            grouped_by_meal_plan_sorted_price.append(brr)

            # for g in range(len(gbmp)):
            #     brr = sorted(gbmp[g], key=lambda x: x.price, reverse=False)
            # grouped_by_meal_plan_sorted_price.append(brr)

        print('grouped_by_meal_plan_sorted_price')
        print(grouped_by_meal_plan_sorted_price)

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
            print('si_of_bs[0].price')
            print(si_of_bs[0].price)
            final_price_bs.append(si_of_bs[0].price)

        for si_of_others in grouped_by_meal_plan_sorted_price:
            uiq_obj2 = SysInfo()
            uiq_obj2.price = si_of_others[0].price
            uiq_obj2.mealplan = si_of_others[0].mealplan
            uiq_obj2.system = si_of_others[0].system
            uniq_oths_list.append(uiq_obj2)

        int_bs_distinct_list_mp = [int(l) for l in bs_distinct_list_mp]
        print('int_bs_distinct_list_mp')
        print(int_bs_distinct_list_mp)

        sorted_bs_distinct_list_mp = sorted(int_bs_distinct_list_mp, reverse=False)
        print('sorted_bs_distinct_list_mp')
        print(sorted_bs_distinct_list_mp)

        for eachbs in uniq_bs_list:
            if len(uniq_oths_list) == 0:
                passed_mealplan.append(int(eachbs.mealplan))
            else:
                for eachos in uniq_oths_list:
                    if eachos.mealplan == '':
                        passed_mealplan.append(int(eachbs.mealplan))

                    if eachbs.mealplan == eachos.mealplan and eachbs.price <= eachos.price:
                        passed_mealplan.append(int(eachbs.mealplan))

        print('passed mealplans')
        print(passed_mealplan)
        print('failed_mealplan')
        print(failed_mealplan)
        sorted_passed_mealplan = sorted(passed_mealplan, reverse=False)
        #
        # print('si_of_others[0].price')
        # print(si_of_others[0].price)
        # final_price_othersys.append(si_of_others[0].price)

        print('distinct_list')
        print(distinct_list)
        int_distinct_list = [int(i) for i in distinct_list]
        sorted_distinct_list = sorted(int_distinct_list, reverse=False)
        print('sorted_distinct_list')
        print(sorted_distinct_list)
        print('sorted_passed_mealplan')
        print(sorted_passed_mealplan)
        print('sorted_bs_distinct_list_mp')
        print(sorted_bs_distinct_list_mp)

        # result = all(
        #     [sorted_passed_mealplan[m] == sorted_bs_distinct_list_mp[m] for m in
        #      range(len(sorted_bs_distinct_list_mp))])
        # print('result:')
        # print(result)

        failed = list(set(sorted_bs_distinct_list_mp) - set(sorted_passed_mealplan))
        print('failed')
        print(failed)

        # # makes both array of same length
        #     diff_in_length = len(final_price_bs) - len(final_price_othersys)
        #     abs_length = abs(diff_in_length)
        #     if diff_in_length < 0:
        #         for j in range(0, abs_length):
        #             final_price_othersys.pop()
        #     elif diff_in_length > 0:
        #         for k in range(0, abs_length):
        #             final_price_bs.pop()
        #     # makes both array of same length

        len_of_final_price_bs = len(final_price_bs)

        # print('result from numpy')
        # result_array = np.less_equal(final_price_bs, final_price_othersys)
        # if len(result_array) == 0 or 'False' not in result_array:
        #     pos = 0
        #
        # pos = 1
        # print(np.less_equal(final_price_bs, final_price_othersys))
        #
        # # sorted(r, key=lambda x: x.price, reverse=False)
        # # Group by#
        #
        # # sorting in ascending order
        newlist = sorted(listofSysInfo, key=lambda x: x.price, reverse=False)
        newbslist = sorted(listofBsInfo, key=lambda x: x.price, reverse=False)

        # for index, element in enumerate(newlist):
        #     if int(element.system) == int(big_safar_id):
        #         pos = index
        #         break
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
            self.add_error('price', msg)
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

    def save(self, commit=True):
        instance = super(PriceInDiffSysForm, self).save(commit=False)
        return instance

    def __init__(self, *args, **kwargs):
        super(PriceInDiffSysForm, self).__init__(*args, **kwargs)


class SysInfo:
    def __init__(self):
        self.system = 0
        self.mealplan = 0
        self.price = 0
