from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.mail import send_mail
from django.urls import reverse
from .models import AllNews
from .forms import ContactForm, PostForm

class IndexView(View):
    template_name = 'mynewsapp/index.html'

    def get(self, request):
        # Ваш код для главной страницы
        return render(request, self.template_name)

class AllNewsView(View):
    template_name = 'mynewsapp/all_news.html'

    def get(self, request, id):
        all_news_list = AllNews.objects.all().order_by('-time')  # Изменили имя переменной
        post = get_object_or_404(AllNews, id=id)
        return render(request, self.template_name, {'post': post, 'all_news_list': all_news_list})  # Изменили имена переменных в контексте

class ContactView(View):
    template_name = 'mynewsapp/contact.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
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
            return render(request, self.template_name, context={'form': form})

class CreatePostView(View):
    template_name = 'mynewsapp/create.html'

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            return render(request, self.template_name, context={'form': form})







