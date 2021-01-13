from django import forms
import datetime
from .models import DataWarga, IuranWarga

KELAMIN=(
        ('NONE', 'NONE'),
        ('LAKI-LAKI', 'LAKI-LAKI'),
        ('PEREMPUAN', 'PEREMPUAN'),
)

NIKAH =(
        ('NONE', 'NONE'),
        ('NIKAH', 'NIKAH'),
        ('BELUM MENIKAH', 'BELUM MENIKAH')
)
class FormDataWarga(forms.ModelForm):
    jenis_kelamin = forms.ChoiceField(choices=KELAMIN,  label="Jenis Kelamin", initial='', widget=forms.Select(), required=True)
    status_perkawinan = forms.ChoiceField(choices=NIKAH, label="Status Perkawinan", widget=forms.Select(), required=True)
    kepala_keluarga = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    class Meta:
        model = DataWarga
        fields = ('no_kk', 'nik', 'nama', 'kepala_keluarga', 'agama', 'tempat_lahir', 'tgl_lahir', 'jenis_kelamin', 'gol_darah',
                 'alamat_ktp', 'alamat_sekarang', 'status_perkawinan', 'pendidikan', 'pekerjaan', 'kewarganegaraan',
                 'no_telpon')
        widgets = {
            'no_kk': forms.TextInput(attrs={'class': 'form-control'}),
            'nik': forms.TextInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'kepala_keluarga': forms.BooleanField(),
            'agama': forms.TextInput(attrs={'class': 'form-control'}),
            'tempat_lahir': forms.TextInput(attrs={'class': 'form-control'}),
            'tgl_lahir': forms.TextInput(attrs={'class': 'form-control fa fa-calender'}),
            'gol_darah': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat_ktp': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat_sekarang': forms.TextInput(attrs={'class': 'form-control'}),
            'pendidikan': forms.TextInput(attrs={'class': 'form-control'}),
            'pekerjaan': forms.TextInput(attrs={'class': 'form-control'}),
            'kewarganegaraan': forms.TextInput(attrs={'class': 'form-control'}),
            'no_telpon': forms.TextInput(attrs={'class': 'form-control'}),
              }


class FormUpdateIuranWarga(forms.ModelForm):
    class Meta:
        model = IuranWarga
        exclude = ('no_kk', 'kepala_keluarga',)

def current_year():
    return datetime.date.today().year

def year_choices():
    return [(r,r) for r in range(2020, datetime.date.today().year+1)]

# def kepala_keluarga():
#     qs = DataWarga.get_queryset().filter(kepala_keluarga=True)
#     return qs
# def kepala_keluarga(self, *args, **kwargs):
#     qs = DataWarga.objects.filter(kepala_keluarga=True)
#     return qs
class FormCreateIuranWarga(forms.ModelForm):

    no_kk = forms.ModelChoiceField(queryset=DataWarga.objects.filter(kepala_keluarga=True))
    tahun = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
    class Meta:
        model = IuranWarga
        fields = ('__all__')

