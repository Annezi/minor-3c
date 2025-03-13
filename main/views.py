from django.shortcuts import render

# Главная страница
def home(request):
    return render(request, 'home.html')

# Страница "О программе"
def about(request):
    data = {
        "student": {
            "name": "Анна Ахматова",
            "photo": "images/student.jpg",
            "email": "aaguschina_1@edu.hse.ru",
            "phone": "+79991234567",
        },
        "program": {
            "name": "Программа разработки веб-приложений",
            "description": "Эта программа обучает студентов созданию современных веб-приложений.",
            "manager": {
                "name": "Петр Петров",
                "photo": "images/manager.jpg",
                "email": "petr@edu.hse.ru",
            },
            "leader": {
                "name": "Сидор Сидоров",
                "photo": "images/leader.jpg",
                "email": "sidor@edu.hse.ru",
            },
        },
        "classmates": [
            {"name": "Анна", "photo": "images/anna.jpg", "email": "anna@edu.hse.ru", "phone": "+79991112233"},
            {"name": "Мария", "photo": "images/maria.jpg", "email": "maria@edu.hse.ru", "phone": "+79994445566"},
        ],
    }
    return render(request, 'about.html', {'data': data})

# Страница с алгоритмической задачей
def task(request):
    return render(request, 'task.html')

# Страницы о каллиграфии, живописи и фарфоре
def calligraphy(request):
    return render(request, 'calligraphy.html')

def painting(request):
    return render(request, 'painting.html')

def porcelain(request):
    return render(request, 'porcelain.html')

# Задачи 

def task(request):
    result_task1 = None
    result_task2 = None

    if request.method == 'POST':
        if 'task1-submit' in request.POST:
            # Первая задача
            countries = request.POST.get('countries').split()
            gdp_per_capita = list(map(float, request.POST.get('gdp_per_capita').split()))
            threshold = float(request.POST.get('threshold'))

            result_task1 = [
                country for country, gdp in zip(countries, gdp_per_capita)
                if gdp >= threshold
            ]
            if not result_task1:
                result_task1 = "Нет стран, удовлетворяющих условию."

        elif 'task2-submit' in request.POST:
            # Вторая задача
            year = int(request.POST.get('year'))

            is_leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

            century = (year - 1) // 100 + 1

            result_task2 = {
                'year': year,
                'is_leap_year': is_leap_year,
                'century': century,
            }

    return render(request, 'task.html', {
        'result_task1': result_task1,
        'result_task2': result_task2,
    })
