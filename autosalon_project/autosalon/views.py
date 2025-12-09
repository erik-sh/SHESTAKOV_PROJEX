from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Service, Supplier
from .forms import TestDriveForm
from django.contrib import messages

def home(request):
    """Главная страница"""
    cars = Car.objects.filter(is_sold=False)[:6]  # 6 последних автомобилей
    services = Service.objects.all()[:4]  # 4 услуги для показа на главной
    return render(request, 'autosalon/home.html', {
        'cars': cars,
        'services': services
    })

def cars_list(request):
    """Список всех автомобилей"""
    cars = Car.objects.filter(is_sold=False)
    brands = Car.objects.values_list('brand', flat=True).distinct()
    
    # Фильтрация по марке
    brand_filter = request.GET.get('brand')
    if brand_filter:
        cars = cars.filter(brand=brand_filter)
    
    return render(request, 'autosalon/cars_list.html', {
        'cars': cars,
        'brands': brands,
        'selected_brand': brand_filter
    })

def car_detail(request, car_id):
    """Детальная информация об автомобиле"""
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            test_drive = form.save(commit=False)
            test_drive.car = car
            test_drive.save()
            messages.success(request, 'Заявка на тест-драйв отправлена! Мы свяжемся с вами в ближайшее время.')
            return redirect('car_detail', car_id=car.id)
    else:
        form = TestDriveForm(initial={'car': car})
    
    return render(request, 'autosalon/car_detail.html', {
        'car': car,
        'form': form
    })

def services(request):
    """Страница услуг"""
    services_list = Service.objects.all()
    return render(request, 'autosalon/services.html', {
        'services': services_list
    })

def suppliers(request):
    """Страница поставщиков"""
    suppliers_list = Supplier.objects.all()
    return render(request, 'autosalon/suppliers.html', {
        'suppliers': suppliers_list
    })

def about(request):
    """Страница "О нас" (добавил от себя)"""
    return render(request, 'autosalon/about.html')

def contact(request):
    """Страница контактов (добавил от себя)"""
    if request.method == 'POST':
        # Здесь можно добавить обработку формы обратной связи
        messages.success(request, 'Сообщение отправлено! Мы ответим вам в течение 24 часов.')
        return redirect('contact')
    
    return render(request, 'autosalon/contact.html')