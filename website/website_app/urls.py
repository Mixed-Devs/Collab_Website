from django.urls import path


from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(), name='home'),
    path('tan/',views.Tanwebsite.as_view(), name='tan_page'),
    path('daniil/',views.Daniilwebsite.as_view(),name='daniil_page')
]