from django.db import models
import datetime


# Create your models here.
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(u'手机号码', max_length=20, db_index=True)
    password = models.CharField(u'密码', max_length=50)
    nickname = models.CharField(u'昵称', max_length=50)
    sex = models.CharField(u'性别', max_length=1)
    birth = models.DateField(u'生日日期')


class Cinema(models.Model):
    cinema_id = models.AutoField(primary_key=True)
    name = models.CharField(u'影院名称', max_length=20)
    province = models.CharField(u'省', max_length=20)
    city = models.CharField(u'市', max_length=20)
    district = models.CharField(u'区', max_length=20)
    location = models.CharField(u'影院地址', max_length=20)
    phone_number = models.CharField(u'影院电话', max_length=20)


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(u'电影名称', max_length=50)
    poster = models.ImageField(u'电影海报', default='posters/default.jpg')
    rate = models.DecimalField(u'电影评分', decimal_places=2, max_digits=3)
    rate_people = models.IntegerField(u'评价人数', default=0)
    introduction = models.TextField(u'电影简介', max_length=200, default=u'暂无简介')


class Cinema_Movie(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    price = models.DecimalField(u'影票价格', decimal_places=2, max_digits=5)
    on_time = models.DateField(u'上映日期')
    stage = models.CharField(u'场次',max_length=10,default='null')


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    create_date = models.DateField(u'订单日期', default=datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S"))
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_id = models.ForeignKey(Cinema_Movie, on_delete=models.CASCADE)
    stage = models.CharField(u'场次',max_length=10,default='null')
    seat_row = models.IntegerField(u'座位行数',default=0)
    seat_col = models.IntegerField(u'座位列数',default=0)


class Food_Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(u'餐饮供应商名称', max_length=50)
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)


class Food_Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(u'餐饮服务名称', max_length=50)
    introduction = models.TextField(u'电影简介', max_length=200, default=u'暂无简介')
    supplier_id = models.ForeignKey(Food_Supplier, on_delete=models.CASCADE)