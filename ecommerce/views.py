from django.shortcuts import render, get_object_or_404, redirect
from .models import Produk, Review, Attachment
from django.db.models import Q
from django.core.paginator import Paginator
import random
from django.urls import reverse
from django.http import HttpResponse


def index(request):
    data_list = Produk.objects.all().order_by('-id')
    paginator = Paginator(data_list, 8)
    page = request.GET.get('page')
    data_list = paginator.get_page(page)
    context = {
        'data_list': data_list,
        'home': True,
    }
    return render(request, 'template1/index.html', context)


def detail(request, slug):
    query = request.GET.get('q')
    data = get_object_or_404(Produk, slug=slug)
    reviews = Review.objects.filter(produk=data)
    attachment = Attachment.objects.filter(produk=data)
    random_list = list(Produk.objects.all())
    context = {
        'data': data,
        'reviews': reviews,
        'attachment': attachment,
        'detail': True,
        'random_list': random.sample(random_list, 5),
    }
    if query:
        data_list = Produk.objects.all().order_by('-id')
        query = request.GET.get('q')
        if query:
            data_list = data_list.filter(
                Q(nama_produk__icontains=query) |
                Q(deskripsi1__icontains=query) |
                Q(deskripsi2__icontains=query)
            ).distinct()
        paginator = Paginator(data_list, 8)
        page = request.GET.get('page')
        data_list = paginator.get_page(page)
        context['data_list'] = data_list
        return render(request, 'template1/search.html', context)
    return render(request, 'template1/detail_produk.html', context)


def about(request):
    query = request.GET.get('q')
    context = {
        'about': True,
    }
    if query:
        data_list = Produk.objects.all().order_by('-id')
        query = request.GET.get('q')
        if query:
            data_list = data_list.filter(
                Q(nama_produk__icontains=query) |
                Q(deskripsi1__icontains=query) |
                Q(deskripsi2__icontains=query)
            ).distinct()
        paginator = Paginator(data_list, 8)
        page = request.GET.get('page')
        data_list = paginator.get_page(page)
        random_list = list(Produk.objects.all())
        context['random_list'] = random.sample(random_list, 5)
        context['data_list'] = data_list
        return render(request, 'template1/search.html', context)
    return render(request, 'template1/about.html', context)


def kontak(request):
    return render(request, 'template1/kontak.html', {'kontak': True})


def search(request):
    query = request.GET.get('q')
    if query:
        context = {}
        data_list = Produk.objects.all().order_by('-id')
        query = request.GET.get('q')
        if query:
            data_list = data_list.filter(
                Q(nama_produk__icontains=query) |
                Q(deskripsi1__icontains=query) |
                Q(deskripsi2__icontains=query)
            ).distinct()
        paginator = Paginator(data_list, 8)
        page = request.GET.get('page')
        data_list = paginator.get_page(page)
        random_list = list(Produk.objects.all())
        context['random_list'] = random.sample(random_list, 5)
        context['data_list'] = data_list
    return render(request, 'template1/search.html', context)