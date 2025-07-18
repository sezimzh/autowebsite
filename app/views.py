from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Category

def index_view(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'app/car_detail.html', {'car': car})


def create_car(request): 
    if request.method == 'POST':
        title = request.POST.get('title')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        category_id = request.POST.get('category')  
        image = request.FILES.get('image')  
        description = request.POST.get('description')

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
