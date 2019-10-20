from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'home'
urlpatterns = [
    path('home', views.home_index, name='home'),
    path('products', views.ProductsIndexView.as_view(), name='products'),
    # path('products', views.home_products, name='products'),
    # path('', views.IndexView.as_view(), name='index'),
    path('details/<int:pk>', views.ProductDetailsView.as_view(), name='details')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
