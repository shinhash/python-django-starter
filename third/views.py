from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from third.models import Restaurant, Review
from third.forms import RestaurantForm, ReviewForm, UpdateRestaurantForm
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Count, Avg
import json

from third.utils import image_path_rename


# Create your views here.
def list(request, page_num):
    restaurant_list = (Restaurant.objects.all()
                       .annotate(reviews_count=Count('review'))
                       .annotate(reviews_avg=Avg('review__point')))
    paginator = Paginator(restaurant_list, 3)
    page = page_num
    items = paginator.get_page(page)
    context = {
        'restaurant_list' : items
    }
    return render(request, 'third/list.html', context)


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        print(form)
        if form.is_valid():
            # new_item = form.save()
            print("")
        return HttpResponseRedirect('/third/list/page/1')
    form = RestaurantForm()
    return render(request, 'third/create.html', {'form':form})


def update(request, restaurant_id):
    if request.method == 'POST' and restaurant_id is not None:
        password = request.POST.get('password', '')

        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        form = UpdateRestaurantForm(request.POST, instance=item)
        if form.is_valid() and password == item.password:
            item = form.save()
    elif request.method == 'GET':
        # item = Restaurant.objects.get(pk=request.GET.get('id'))
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form':form})
    return HttpResponseRedirect('/third/list/page/1')


def detail(request, restaurant_id):
    if restaurant_id is not None:
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/detail.html', {'item':item, 'reviews':reviews})
    return HttpResponseRedirect('/third/list/page/1')


def delete(request, restaurant_id):
    if restaurant_id is not None:
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        item.delete()
    return HttpResponseRedirect('/third/list/page/1')


def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurant-detail', restaurant_id=restaurant_id)
    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant': item})
    return render(request, 'third/review_create.html', {'form':form, 'item':item})


def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()
    return redirect('restaurant-detail', restaurant_id=restaurant_id)


def review_list(request):
    reviews = Review.objects.all().select_related().order_by('-create_at')
    paginator = Paginator(reviews, 5)

    page = request.GET.get('page_num')
    items = paginator.get_page(page)

    context = {
        'reviews' : items
    }
    return render(request, 'third/review_list.html', context)


## API LINE
def api_rest_create(request):
    result = 'FALSE'
    if request.method == 'POST':

        my_file = request.FILES['image']
        fs = FileSystemStorage(location='media/images/', base_url='media/images/')

        file_origin_name = my_file.name
        file_trance_name = image_path_rename(my_file.name)
        filename = fs.save(file_trance_name, my_file)

        restaurant = Restaurant(
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            password=request.POST.get('password'),
            image_origin_name=file_origin_name,
            image_trance_name=file_trance_name,
            image_view_path='/media/images/'+file_trance_name
        )

        if restaurant is not None:
            restaurant.save()
            result = 'SUCCESS'

    context = {
        'result' : result
    }
    return JsonResponse(context)


def api_rest_delete(request):
    result = 'FALSE'
    if request.method == 'POST':
        post_data = json.loads(request.body)
        restaurant_id = post_data.get('restaurant_id')
        if restaurant_id is not None:
            item = get_object_or_404(Restaurant, pk=restaurant_id)
            item.delete()
            result = 'SUCCESS'

    context = {
        'result' : result
    }
    return JsonResponse(context)


def api_rest_update(request):
    result = 'FALSE'
    if request.method == 'POST':
        restaurant_id = request.POST.get('restaurant_id')
        # form = UpdateRestaurantForm(request.POST, request.FILES, instance=item)
        # print('form : ', form)
        # if form.is_valid():
        #     item = form.save()
        #     result = 'SUCCESS'

        restaurant = Restaurant.objects.filter(id=restaurant_id)

        if 'image' in request.FILES:
            my_file = request.FILES['image']
            fs = FileSystemStorage(location='media/images/', base_url='media/images/')

            file_origin_name = my_file.name
            file_trance_name = image_path_rename(my_file.name)
            filename = fs.save(file_trance_name, my_file)
            if restaurant is not None:
                restaurant.update(
                    image_origin_name=file_origin_name,
                    image_trance_name=file_trance_name,
                    image_view_path='/media/images/' + file_trance_name
                )
                result = 'SUCCESS'

        if restaurant is not None:
            restaurant.update(
                name=request.POST.get('name'),
                address=request.POST.get('address'),
                password=request.POST.get('password')
            )
            result = 'SUCCESS'

    context = {
        'result': result
    }
    return JsonResponse(context)