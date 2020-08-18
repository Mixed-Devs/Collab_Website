from django.urls import path


from . import views

urlpatterns = [
    path('home/',views.HomePageView.as_view(), name='home'),
    path('test/',views.TestPageView.as_view(), name='test'),

]