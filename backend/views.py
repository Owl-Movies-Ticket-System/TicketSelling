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
    data = json.loads(request.body)
    # t = getattr(has,'member_id',-1)
    if Member.objects.filter(phone_number=data['phone_number'], password=data['password']).exists():
        # request.session['member_id'] = Member.objects.get(phone_number=data['phone_number'],password=data['password']).member_id
        token = generate_token(data['phone_number'])
        return JsonResponse({'result': 'ok', 'authorization': token})
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
    return HttpResponse("You're logged out.")


def movie_comment(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    data = json.loads(request.body)
    if certify_time(request.getHeader("Authorization")) == False:
        return JsonResponse({'error': 'You should log in.'})
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
    if certify_time(request.META.get("HTTP_AUTHOR")) == False:
        return JsonResponse({'error': 'You should log in.'})
    re = Movie.objects.filter(name__contains=data['name'])
    temp = []
    # return HttpResponse(json.dumps(re), content_type="application/json")
    for obj in re:
        cinemas = available_cinemas(obj.movie_id)
        temp.append({'name': obj.name,'id':obj.movie_id,'director':obj.director,"poster":str(obj.poster),'protagonist':obj.protagonist,'types':obj.types,'area':obj.area,'language':obj.language,'len':obj.len, 'rate': str(obj.rate), 'rate_people': obj.rate_people,
                     'introduction': obj.introduction, 'available': json.dumps(cinemas)})  ##其实不是返回这些，暂时先这样咯
    return HttpResponse(temp, content_type="application/json")


def movie_showall(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    data = json.loads(request.body)
    if certify_time(request.META.get("HTTP_AUTHOR")) == False:
        return JsonResponse({'error': 'You should log in.'})
    temp = []
    re = Movie.objects.all()
    for obj in re:
        temp.append({'name':obj.name,"director":obj.director,"poster":str(obj.poster),'protagonist':obj.protagonist,'types':obj.types,'area':obj.area,'language':obj.language,'len':obj.len, 'rate': str(obj.rate), 'rate_people': obj.rate_people, 
                     'introduction': obj.introduction})
    return HttpResponse(temp, content_type="application/json")

def get_img(request):
    #data = json.loads(request.body)
    #if certify_time(request.META.get("HTTP_AUTHOR")) == False:
    #   return JsonResponse({'error': 'You should log in.'})
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
    data = json.loads(request.body)
    if certify_time(request.META.get("HTTP_AUTHOR")) == False:
        return JsonResponse({'error': 'You should log in.'})
    id = token_getid(request.META.get("HTTP_AUTHOR"))
    member_id = Member.objects.get(phone_number=id)
    Order.models.create(member_id=member_id,movie_id=data['movie_id'],cinema_id=data['cinema_id']
                        ,stage=data['stage'],seat_row=data['seat_row'],seat_col=data['seat_col'])
    return JsonResponse({'result': 'ok'}) 


def getseats(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    data = json.loads(request.body)
    if certify_time(request.META.get("HTTP_AUTHOR")) == False:
        return JsonResponse({'error': 'You should log in.'})
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
    data = json.loads(request.body)
    if certify_time(request.META.get("HTTP_AUTHOR")) == False:
        return JsonResponse({'error': 'You should log in.'})
    re = Cinema.objects.filter(district__contains=data['district'])
    temp = []
    for obj in re:
        temp.append({'id': obj.cinema_id, 'name': obj.name, 'location': obj.location, 'phone_number': obj.phone_number})
    return HttpResponse(temp, content_type="application/json")


#show all movies in specific cinema
def available_movies_in_cinema(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    data = json.loads(request.body)
    if certify_time(request.META.get("HTTP_AUTHOR")) == False:
        return JsonResponse({'error': 'You should log in.'})
    id = data['id']
    objs = Cinema_Movie.objects.filter(cinema_id=id)
    re = []
    for obj in objs:
        movie = Movie.objects.get(movie_id=obj.id)
        re.append({'movie_id': obj.movie_id, 'name': movie.name, 'rate': movie.rate,
                   'rate_people': movie.rate_people, 'poster': movie.poster,
                   'price': obj.price, 'on_time': obj.on_time, 'stage': obj.stage})
    return HttpResponse(re, content_type="application/json")


#get specific movie stage information in specific cinema
def get_stage_info(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    data = json.loads(request.body)
    if certify_time(request.META.get("HTTP_AUTHOR")) == False:
        return JsonResponse({'error': 'You should log in.'})
    re = Cinema_Movie.objects.filter(cinema_id=data['cinema_id']).filter(movie_id=data['movie_id'])
    temp = []
    for obj in re:
        temp.append({'on_time': obj.on_time, 'stage': obj.stage})
    return HttpResponse(temp, content_type="application/json")


#show all food suppliers in specific cinema
def available_food_suppliers_in_cinema(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'method should be POST'})
    data = json.loads(request.body)
    if certify_time(request.META.get("HTTP_AUTHOR")) == False:
        return JsonResponse({'error': 'You should log in.'})
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
    data = json.loads(request.body)
    if certify_time(request.META.get("HTTP_AUTHOR")) == False:
        return JsonResponse({'error': 'You should log in.'})
    id = data['id']
    objs = Food_Service.objects.filter(supplier_id=id)
    re = []
    for obj in objs:
        re.append({'service_id': obj.serve_id, 'name': obj.name, 'introduction': obj.introduction})
    return HttpResponse(re, content_type="application/json")


def generate_token(key, expire=3600):
    r'''
        @Args:
            key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
            expire: int(最大有效时间，单位为s)
        @Return:
            state: str
    '''
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str + ':' + sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")


def certify_token(key, token):
    r'''
        @Args:
            key: str
            token: str
        @Returns:
            boolean
    '''
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return False
        # token certification success
    return True


def certify_time(token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return False
    return True


def token_getid(token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    return token_list[1]