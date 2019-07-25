from django.shortcuts import render, redirect
from .models import DaftarBarang
from .form import InputBarang


# Create your views here.
def HalamanHome(request):
    mentee = DaftarBarang.objects.all()
    return render(request, 'Home.html', {'daftar_barang': mentee})
def Halamanbase(request):
    return render(request, 'base/base.html')

def Input_barang(request):
    if request.method == "POST":
        form = InputBarang(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = InputBarang()
    return render(request, 'inputBarang.html', {'fromBarang': form})


def Detail(request, id_blog):
    hasil = DaftarBarang.objects.get(pk = id_blog)
    return render(request, 'detail.html', {'barang':hasil})