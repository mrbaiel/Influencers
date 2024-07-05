from django.urls import path

from . import views

urlpatterns = (
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('post/create/', views.create_post, name='add_page'),
    path('feedback/', views.contact, name='contact'),
    path('login/', views.login, name='login'),

)
