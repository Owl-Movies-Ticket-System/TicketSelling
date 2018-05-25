from django.urls import path
import backend.views as backend_view

urlpatterns = [
    path('login', backend_view.login),
]