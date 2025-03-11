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