from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
import decimal
import json
import time
import base64
import hmac
import sys
import matplotlib.pylab as plt


# Create your views here.
# test git
def login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    if request.session.get('log_in', None):
        return JsonResponse({'error':'repeated login'})
    data = json.loads(request.body)
    # t = getattr(has,'member_id',-1)
    if Member.objects.filter(phone_number=data['phone_number'], password=data['password']).exists():
        # request.session['member_id'] = Member.objects.get(phone_number=data['phone_number'],password=data['password']).member_id
        # token = generate_token(data['phone_number'])
        request.session['log_in'] = True
        request.session['user_id'] = data['phone_number']
        request.session['password'] = data['password']
        return JsonResponse({'result': 'ok'})
    else:
        return JsonResponse({'result': 'Your username and password did not match.'})


def logup(request):
    if request.method != 'POST':
        return JsonResponse({"error": 'method should be POST'})
    data = json.loads(request.body)
    if Member.objects.filter(phone_number=data['phone_number']).exists():
        return JsonResponse({'result': 'the phone_number has been used.'})
    Member.objects.create(phone_number=data['phone_number'], password=data['password'],
                          nickname=data['nickname'], sex=data['sex'], birth=data['birth'])
    return JsonResponse({'result': 'ok'})


def logout(request):
    # 浏览器清除token
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'you haven\'t log in'})
    request.session.flush()
    return JsonResponse({'result':'log out ok'})

def movie_comment(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    data = json.loads(request.body)
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    if Movie.objects.filter(movie_id=data['movie_id']).exists() == False:
        return JsonResponse({'error': 'movie is not exist.'})
    ob = Movie.objects.get(movie_id=data['movie_id'])
    new_rate = decimal.Decimal(float(data['rate']))
    rate_people = decimal.Decimal(int(ob.rate_people))
    ob.rate = (ob.rate * rate_people + new_rate) / (rate_people + 1)
    ob.rate_people = ob.rate_people + 1
    ob.save()
    return JsonResponse({'result': 'ok', 'rate_people': ob.rate_people})


def movie_search(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    data = json.loads(request.body)
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    re = Movie.objects.filter(name__contains=data['name'])
    temp = []
    # return HttpResponse(json.dumps(re), content_type="application/json")
    for obj in re:
        cinemas = available_cinemas(obj.movie_id)
        temp.append({'name': obj.name,'id':obj.movie_id,'director':obj.director,"poster":str(obj.poster),'protagonist':obj.protagonist,'types':obj.types,'area':obj.area,'language':obj.language,'len':obj.len, 'rate': str(obj.rate), 'rate_people': obj.rate_people,
                     'introduction': obj.introduction, 'available': json.dumps(cinemas)})  
    return HttpResponse(temp, content_type="application/json")


def movie_showall(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    print(request.session.get('user_id','no'))
    print(request.session.get('log_in',None))
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    data = json.loads(request.body)
    temp = []
    re = Movie.objects.all()
    for obj in re:
        temp.append({'name':obj.name,"director":obj.director,"poster":str(obj.poster),'protagonist':obj.protagonist,'types':obj.types,'area':obj.area,'language':obj.language,'len':obj.len, 'rate': str(obj.rate), 'rate_people': obj.rate_people, 
                     'introduction': obj.introduction})

    print("movie_showall successfully.")
    return HttpResponse(json.dumps(temp), content_type="application/json")

def get_img(request):
    #data = json.loads(request.body)
    #if certify_time(request.META.get("HTTP_AUTHOR")) == False:
    #   return JsonResponse({'error': 'You should log in.'})
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    p = request.GET.get('img')
    print(sys.path[0])
    f = open(str(p),"rb+")
    img = f.read() 
    f.close()
    return HttpResponse(img, content_type="image/jpeg")

def available_cinemas(id):
    objs = Cinema_Movie.objects.filter(movie_id=id)
    re = []
    for obj in objs:
        temp = Cinema.objects.get(cinema_id=obj.id)
        re.append({'name':temp.name,'id':temp.cinema_id})
    return re


def tiket_post(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})   
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    data = json.loads(request.body)
    id = token_getid(request.META.get("HTTP_AUTHOR"))
    print(id)
    member_id = Member.objects.get(phone_number=data['phone_num'])
    movie_id = Movie.objects.get(movie_id=data['movie_id'])
    cinema_id = Cinema_Movie.objects.get(cinema_id=data['cinema_id'])
    Order.objects.create(member_id=member_id,movie_id=movie_id,cinema_id=cinema_id
                        ,stage=data['stage'],
                        seat_row=data['seat_row'],
                        seat_col=data['seat_col'])
    return JsonResponse({'result': 'ok'}) 


def getseats(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    data = json.loads(request.body)
    re = Order.objects.filter(movie_id=data['movie_id'],cinema_id=data['cinema_id'],stage=data['stage'])
    temp = []
    for ob in re:
        t = (ob.seat_row,ob.seat_col)
        temp.append(t)
    return HttpResponse(temp, content_type="application/json")


#search cinemas using district
def cinema_search(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    data = json.loads(request.body)
    re = Cinema.objects.filter(district__contains=data['district'])
    temp = []
    for obj in re:
        temp.append({'id': obj.cinema_id, 'name': obj.name,'photo':str(obj.cinema_photo), 'location': obj.location, 'phone_number': obj.phone_number})
    return HttpResponse(temp, content_type="application/json")


#show all movies in specific cinema
def available_movies_in_cinema(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    data = json.loads(request.body)
    id = data['id']
    objs = Cinema_Movie.objects.filter(cinema_id=id)
    re = []
    for obj in objs:
        movie = Movie.objects.get(movie_id=obj.id)
        re.append({'movie_id': str(obj.id), 'name': str(movie.name), 'rate': str(movie.rate),
                   'rate_people': str(movie.rate_people), 'poster': str(movie.poster),
                   'price': str(obj.price), 'on_time': str(obj.on_time), 'stage': str(obj.stage)})
    return HttpResponse(re, content_type="application/json")


#get specific movie stage information in specific cinema
def get_stage_info(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    data = json.loads(request.body)
    re = Cinema_Movie.objects.filter(cinema_id=data['cinema_id']).filter(movie_id=data['movie_id'])
    temp = []
    for obj in re:
        temp.append({'on_time': obj.on_time, 'stage': obj.stage})
    return HttpResponse(temp, content_type="application/json")


#show all food suppliers in specific cinema
def available_food_suppliers_in_cinema(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    data = json.loads(request.body)
    id = data['id']
    objs = Food_Supplier.objects.filter(cinema_id=id)
    re = []
    for obj in objs:
        re.append({'name': obj.name, 'id': obj.supplier_id})
    return HttpResponse(re, content_type="application/json")


#show all food services provided by specific suppliers
def available_food_services_by_supplier(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    if request.session.get('log_in',None) == None:
        return JsonResponse({'error':'log in'})
    data = json.loads(request.body)
    id = data['id']
    objs = Food_Service.objects.filter(supplier_id=id)
    re = []
    for obj in objs:
        re.append({'service_id': obj.serve_id, 'name': obj.name, 'introduction': obj.introduction})
    return HttpResponse(re, content_type="application/json")