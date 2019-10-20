from django.contrib import admin
from .models import CompanyData, FourInfo

# Register your models here.


class CompanyDataAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_add', 'company_phone_nub', 'company_email', 'company_key_word')
    fieldsets = [
        ("公司名字", {'fields': ['company_name']}),
        ("公司地址", {'fields': ['company_add']}),
        ("公司电话", {'fields': ['company_phone_nub']}),
        ("公司邮箱", {'fields': ['company_email']}),
        ("SEO推广词", {'fields': ['company_key_word']})
    ]


admin.site.register(FourInfo)
admin.site.register(CompanyData, CompanyDataAdmin)


