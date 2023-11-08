from django.shortcuts import render, get_object_or_404, redirect
from .models import AllNews
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContactForm

def index(request):
    # Ваш код для главной страницы
    return render(request, 'mynewsapp/index.html')

def all_news(request, id):
    all_news_list = AllNews.objects.all().order_by('-time')  # Изменили имя переменной
    post = get_object_or_404(AllNews, id=id)
    return render(request, 'mynewsapp/all_news.html', {'post': post, 'all_news_list': all_news_list})  # Изменили имена переменных в контексте

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из формы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail(
                'Contact message',
                f'Ваше сообщение: {message} принято',
                'from@example.com',  # Адрес отправителя (можете заменить на свой)
                ['viper101011@gmail.com'],  # Адрес получателя (ваш адрес)
                fail_silently=False,
            )

            return redirect('index')  # Вернуться на главную страницу
    else:
        form = ContactForm()  # Если GET-запрос, создать пустую форму

    return render(request, 'mynewsapp/contact.html', context={'form': form})







