from django.contrib import admin
from .models import ProductsList, ClientInfo, MyCompanyInfo
# Register your models here.


admin.site.site_header = 'J.P. Created'
admin.site.site_title = 'J.P. Created 后台'
admin.site.register(ProductsList)
admin.site.register(ClientInfo)
admin.site.register(MyCompanyInfo)
