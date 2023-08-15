from django.urls import path, include

from .views import * 


urlpatterns = [
  path('main/', MenuView.as_view(), name='main'),   
  path('category_menu/<int:category_id>/', get_category_menu, name='get_category_menu'),

  path('view_dish/<slug:slug>/', View_Menu.as_view(), name='view_dish'),
  path('about_us/', about_us, name='about_us'),

  path('register/', register, name='register'),
  path('login/', user_login, name='login'),
  path('logout/', user_logout, name='logout'),

  path('review/', AddReview.as_view(), name='add_review'),
  path('contacts/', Contacts.as_view(), name='contacts'),
]



