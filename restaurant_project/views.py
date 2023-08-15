from django.shortcuts import redirect, render
from django.views.generic import *


from .forms import *
from django.contrib.auth import login, logout


from .models import * 
# Create your views here.


class MenuView(ListView):
  model = Menu 
  template_name = 'main.html'

  def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)
      context['menu_list'] = Menu.objects.all()
      context['category_menu'] = Category.objects.all()
      return context

def get_category_menu(request, category_id):
  menu_list = Menu.objects.filter(category_id=category_id)
  categories = Category.objects.all()
  category = Category.objects.get(pk=category_id)
  context = {
    'menu_list': menu_list,
    'categories': categories,
    'category': category 
  }
  return render(request, template_name='category_menu.html', context=context)

class View_Menu(DetailView):
  model = Menu 
  template_name='view_dish.html'
  context_object_name='dish_item'
  slug_field = 'url'


def about_us(request):
  return render(request, 'about_us.html')



def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('main')
  else:
    form = UserRegisterForm(request.FILES)
  return render(request, 'register.html', {'form': form})

def user_login(request):
  if request.method == 'POST':
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('main')
  else:
    form = UserLoginForm()
  return render(request, 'login.html', {'form': form})


def user_logout(request):
  logout(request)
  return redirect('main')

class Contacts(ListView):
  model = Review
  template_name = 'contact.html'
  context_object_name='review'


class AddReview(View):
  
  def post(self, request):
    if request.method == 'POST':
      form = ReviewForm(request.POST)
      if form.is_valid():
        form = form.save(commit=False)
        form.save()
    else:
      form = ReviewForm()
    return redirect('contacts')


  