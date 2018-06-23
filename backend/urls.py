from django.urls import path
import backend.views as backend_view

urlpatterns = [
    path('login', backend_view.login),
    path('logup', backend_view.logup),
    path('logout', backend_view.logout),
    path('movie/comment', backend_view.movie_comment),
    path('movie/search', backend_view.movie_search),
    path('movie/all', backend_view.movie_showall),
    path('cinema/search', backend_view.cinema_search),
    path('cinema/available_movies', backend_view.available_movies_in_cinema),
    path('cinema/get_stage_info', backend_view.get_stage_info),
    path('cinema/available_food_suppliers', backend_view.available_food_suppliers_in_cinema),
    path('food_suppliers/available_services', backend_view.available_food_services_by_supplier),
    path('ticket/post',backend_view.tiket_post),
    path('ticket/seat',backend_view.getseats)
]
