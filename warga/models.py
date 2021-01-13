from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from django.urls import reverse, reverse_lazy



class DataWargaManager(models.Manager):
    def kepala_keluarga(self):
        qs = self.get_queryset().filter(kepala_keluarga=True)
        print(qs)
        return qs


class DataWarga(models.Model):
    KELAMIN = {
        ('LAKI-LAKI', 'LAKI-LAKI'),
        ('PEREMPUAN', 'PEREMPUAN'),
    }

    NIKAH = {
        ('NIKAH', 'NIKAH'),
        ('BELUM MENIKAH', 'BELUM MENIKAH')
    }
    no_kk = models.CharField(max_length=16, unique=True)
    nik = models.CharField(max_length=16)
    kepala_keluarga = models.BooleanField(blank=False, null=False)
    nama = models.CharField(max_length=50)
    agama = models.CharField(max_length=50)
    tempat_lahir = models.CharField(max_length=255)
    tgl_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=50, choices=KELAMIN)
    gol_darah = models.CharField(max_length=15, blank=True, null=True)
    alamat_ktp = models.CharField(max_length=255)
    alamat_sekarang = models.CharField(max_length=255, null=True, blank=True)
    status_perkawinan = models.CharField(max_length=50, choices=NIKAH)
    pendidikan = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=50)
    kewarganegaraan = models.CharField(max_length=50)
    no_telpon = models.CharField(max_length=25)

    objects = DataWargaManager()

    def __str__(self):
        return self.no_kk



def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    

class IuranWarga(models.Model):
    no_kk = models.OneToOneField(DataWarga, to_field='no_kk', on_delete=models.CASCADE, related_name='kk')
    kepala_keluarga = models.CharField(max_length=25)
    tahun = models.IntegerField(('year'), validators=[MinValueValidator(2020), max_value_current_year])
    januari = models.CharField(max_length=15, blank=True, null=True)
    februari = models.CharField(max_length=15, blank=True, null=True)
    maret = models.CharField(max_length=15, blank=True, null=True)
    april = models.CharField(max_length=15, blank=True, null=True)
    mei = models.CharField(max_length=15, blank=True, null=True)
    juni = models.CharField(max_length=15, blank=True, null=True)
    juli = models.CharField(max_length=15, blank=True, null=True)
    agustus = models.CharField(max_length=15, blank=True, null=True)
    september = models.CharField(max_length=15, blank=True, null=True)
    oktober = models.CharField(max_length=15, blank=True, null=True)
    november = models.CharField(max_length=15, blank=True, null=True)
    desember = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.kepala_keluarga




