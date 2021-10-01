from django import forms
from points.point_setting.models import PointSetting



class PointSettingForm(forms.ModelForm):
    class Meta:
        model = PointSetting
        fields = [

                    "frompoint",
                    "topoint",
                    "conversion_ratio",
                    "maturity_time",
                    "created_at",
                    "status",
        ]
