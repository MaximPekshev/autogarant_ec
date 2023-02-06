from django.urls import path
from .views import show_index
from .views import show_dvs_page
from .views import show_kpp_page
from .views import show_reductor_page
from .views import show_tnvd_page
from .views import show_forsunki_page
from .views import show_tachograph_page
from .views import show_other_page
from .views import show_contact_page
from .views import send_contact_form

urlpatterns = [

    path('', show_index, name='show_index'),
    path('dvs/', show_dvs_page, name='show_dvs_page'),
    path('kpp/', show_kpp_page, name='show_kpp_page'),
    path('reductor/', show_reductor_page, name='show_reductor_page'),
    path('tnvd/', show_tnvd_page, name='show_tnvd_page'),
    path('forsunki/', show_forsunki_page, name='show_forsunki_page'),
    path('tachograph/', show_tachograph_page, name='show_tachograph_page'),
    path('other/', show_other_page, name='show_other_page'),
    path('contact/', show_contact_page, name='show_contact_page'),
    path('send-contact-form/', send_contact_form, name='send_contact_form'),

]
