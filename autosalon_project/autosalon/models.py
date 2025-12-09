from django.db import models

# Модель для автомобилей
class Car(models.Model):
    BRAND_CHOICES = [
        ('Toyota', 'Toyota'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
        ('Audi', 'Audi'),
        ('Hyundai', 'Hyundai'),
        ('Kia', 'Kia'),
        ('Lexus', 'Lexus'),
        ('Mazda', 'Mazda'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название автомобиля")
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, verbose_name="Марка")
    model = models.CharField(max_length=100, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    mileage = models.IntegerField(verbose_name="Пробег (км)")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='cars/', verbose_name="Фото", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False, verbose_name="Продан")
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    
    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

# Модель для услуг
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    duration = models.CharField(max_length=50, verbose_name="Длительность")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

# Модель для поставщиков запчастей
class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название компании")
    contact_person = models.CharField(max_length=100, verbose_name="Контактное лицо")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Адрес")
    specialization = models.CharField(max_length=200, verbose_name="Специализация")
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Рейтинг")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

# Модель для заявок на тест-драйв
class TestDriveRequest(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    preferred_date = models.DateField(verbose_name="Предпочтительная дата")
    message = models.TextField(verbose_name="Сообщение", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False, verbose_name="Обработано")
    
    def __str__(self):
        return f"Заявка на {self.car} от {self.name}"
    
    class Meta:
        verbose_name = "Заявка на тест-драйв"
        verbose_name_plural = "Заявки на тест-драйв"