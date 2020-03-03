from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm

path_to_app_static = "admin/app/"
car_prefix = "car/"
review_prefix = "review/"

def review_count(obj):
    return obj.review_count()


class CarAdmin(admin.ModelAdmin):
    readonly_fields = ["review_count"]
    list_display = ("brand", "model", review_count)
    # change_list_template = path_to_app_static + car_prefix + "change_list.html"
    search_fields = ("brand", "model")
    # list_filter = ("brand", "model")
    fields = ("brand", "model", "review_count")
    ordering = ["id"]
    def review_count(self, obj):
        return obj.review_count()

class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ("car", "title")
    # change_list_template = path_to_app_static + review_prefix + "change_list.html"


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
