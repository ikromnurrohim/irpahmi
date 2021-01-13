from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Q
from .models import DataWarga, IuranWarga
from .forms import FormDataWarga, FormUpdateIuranWarga, FormCreateIuranWarga
from .filter import SearchWarga
from django.template import RequestContext

# HTTP Error 404
def page_not_found(request, exception):
    response = render('404.html', context_instance=RequestContext(request))
    response.status_code = 404

    return response

# HTTP Error 500
def server_error(request):
    response = render('500.html', context_instance=RequestContext(request))
    response.status_code = 500

    return response

def permission_denied(request, exception):
    response = render('403.html', context_instance=RequestContext(request))
    response.status_code = 403
    return response

def bad_request(request, exception):
    response = render('400.html', context_instance=RequestContext(request))
    response.status_code = 400
    return response




def home(request):
    return render(request, 'index.html')

class SearchView(TemplateView):
    template_name = 'data_warga.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = DataWarga.objects.filter(Q(no_kk__icontains=q) |
                                                Q(nik__icontains=q) |
                                                Q(nama__icontains=q)
                                                )
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(object_list=self.results, **kwargs)

class DataWargaView(ListView):
    model = DataWarga
    template_name = 'data_warga.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kepala_keluarga'] = DataWarga.objects.kepala_keluarga()
        return context


class CreateDataWargaView(CreateView):
    model = DataWarga
    template_name = 'form_warga.html'
    form_class = FormDataWarga
    success_url = '/warga/1'

class UpdataDataWargaView(UpdateView):
    model = DataWarga 
    form_class = FormDataWarga
    template_name = 'update_warga.html'
    success_url = '/warga/1'

class DeleteDataWargaView(DeleteView):
    model = DataWarga
    template_name = 'delete_warga.html'
    success_url = '/warga/1'


class IuranWargaView(ListView):
    model = IuranWarga
    template_name = 'iuran_warga.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        iuran_warga = IuranWarga.objects.all()
        context["object_list"] = iuran_warga
        return context

class CreateIuranWargaView(CreateView):
    model = IuranWarga
    form_class = FormCreateIuranWarga
    template_name = 'form_iuran_warga.html'
    success_url = '/warga/iuran/1'

class UpdateIuranWargaView(UpdateView):
    model = IuranWarga
    form_class = FormUpdateIuranWarga
    template_name = 'update_iuran_warga.html'
    success_url = '/warga/iuran/1'

class DeleteIuranWargaView(DeleteView):
    model = IuranWarga
    template_name = 'delete_iuran_warga.html'
    success_url = '/warga/iuran/1'

def get_warga_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        data_warga = DataWarga.objects.filter(
            Q(no_kk__icontains=q)|
            Q(nik__icontains=q) |
            Q(nama__icontains=q)
            ).distinct()
        for warga in data_warga:
            queryset.append(warga)
    return list(set(queryset))


def load_kepala_keluarga(request):
    no_kk = request.GET.get('no_kk')
    print(no_kk)
    iuran = DataWarga.objects.get(id=no_kk)
    print(iuran)
    return JsonResponse(iuran.nama, safe=False)