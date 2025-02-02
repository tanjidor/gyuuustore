from django.shortcuts import render, get_object_or_404 
from .models import Produk, Review, Attachment
from django.db.models import Q
from django.core.paginator import Paginator
import random


def index(request):
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
    context = {
        'data_list': data_list,
        'query': query,
        'home': True,
    }
    if query:
        random_list = list(Produk.objects.all())
        context['random_list'] = random.sample(random_list, 5)
        return render(request, 'template1/search.html', context)
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
    query = request.GET.get('q')
    context = {
        'kontak': True,
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
    return render(request, 'template1/kontak.html', context)