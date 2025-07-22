from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login


def index_view(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'app/car_detail.html', {'car': car})

@login_required
def create_car(request): 
    if request.method == 'POST':
        title = request.POST.get('title')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        category_id = request.POST.get('category')  
        image = request.FILES.get('image')  
        description = request.POST.get('description')
        owner=request.user
        

        category = get_object_or_404(Category, id=category_id)

        Car.objects.create(
            title=title,
            model=model,
            year=year,
            price=price,
            image=image,
            category=category,
            description=description
        )

        return redirect('index')  

    categories = Category.objects.all()  
    return render(request, 'app/create_car.html', {'categories': categories})
@login_required
def update_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    
    if car.owner != request.user:
        return redirect('index')
    

    if request.method == 'POST':
        car.title = request.POST.get('title')
        car.model = request.POST.get('model')
        car.year = request.POST.get('year')
        car.price = request.POST.get('price')
        category_id = request.POST.get('category')
        car.description = request.POST.get('description')
        

        if request.FILES.get('image'):
            car.image = request.FILES['image']

        car.category = get_object_or_404(Category, id=category_id)
        car.save()

        return redirect('car_detail', pk=car.pk)

    categories = Category.objects.all()
    return render(request, 'app/update_car.html', {'car': car, 'categories': categories})

@login_required
def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    
    if car.owner != request.user:
        return redirect('index')
    

    if request.method == 'POST':
        car.delete()
        return redirect('index')

    return render(request, 'app/delete_car.html', {'car': car})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})