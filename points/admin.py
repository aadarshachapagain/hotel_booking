from django.contrib import admin
from points.reward_point.models import RewardPoint
from points.credit_point.models import CreditPoint
from points.virtual_point.models import VirtualPoint
from points.membership_plan.models import Membership_plan
from points.point_setting.models import PointSetting

# Register your models here.
admin.site.register(RewardPoint)
admin.site.register(CreditPoint)
admin.site.register(VirtualPoint)
admin.site.register(Membership_plan)
admin.site.register(PointSetting)

