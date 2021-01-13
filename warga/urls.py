from django.urls import path, include
from django.conf.urls import (handler400 , handler403, handler404, handler500)

from django.conf import settings
from .views import (home, DataWargaView, CreateDataWargaView, UpdataDataWargaView, DeleteDataWargaView,
                    SearchView, load_kepala_keluarga,
                    IuranWargaView, CreateIuranWargaView, UpdateIuranWargaView, DeleteIuranWargaView)

handler400 = 'warga.views.bad_request'
handler403 = 'warga.views.permission_denied'
handler404 = 'warga.views.page_not_found'
handler500 = 'warga.views.server_error'



app_name = 'warga'
urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('warga/delete/<int:pk>', DeleteDataWargaView.as_view(), name='delete-data-warga'),
    path('warga/update/<int:pk>', UpdataDataWargaView.as_view(), name='update-data-warga'),
    path('warga/create/', CreateDataWargaView.as_view(), name='create-data-warga'),
    path('warga/<str:page>', DataWargaView.as_view(), name='list-data-warga'),
    path('warga/iuran/<str:page>', IuranWargaView.as_view(), name='list-iuran-warga'),
    path('warga/iuran/create/', CreateIuranWargaView.as_view(), name='create-iuran-warga'),
    path('warga/iuran/update/<int:pk>', UpdateIuranWargaView.as_view(), name='update-iuran-warga'),
    path('warga/iuran/delete/<int:pk>', DeleteIuranWargaView.as_view(), name='delete-iuran-warga'),
    path('', home),
    path('ajax/load-kepala-keluarga/', load_kepala_keluarga, name='ajax-load-kepala-keluarga'),
]
