from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('bizkimiz/', views.about, name='about'),
    path('iletisim/', views.contact, name='contact'),
    path('kargo_islemleri/', views.cargo_operations, name='cargo_operations'),
    path('adres_ekle/', views.new_address, name='new_address'),
    path('delete/<uuid:address_id>', views.delete_address, name="delete_address"),
    path('kargo_gonder/<uuid:address_id>', views.send_cargo, name="send_cargo")
]