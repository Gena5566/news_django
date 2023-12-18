# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import AllNews
from .forms import ContactForm, PostForm
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


class IndexView(View):
    template_name = 'mynewsapp/index.html'

    def get(self, request):
        posts = AllNews.objects.all()  # Здесь вы должны получить свои объекты постов
        return render(request, self.template_name, {'posts': posts})

class AllNewsView(LoginRequiredMixin, DetailView):
    template_name = 'mynewsapp/all_news.html'
    paginate_by = 5

    def get(self, request, id):
        #all_news_list = AllNews.objects.filter(is_active=True)
        #all_news_list = AllNews.objects.all().order_by('-time')
        #all_news_list = AllNews.active_objects.all()
        all_news_list = AllNews.objects.select_related('user').only('id', 'title', 'time', 'image', 'content',
                                                                    'user__username').all()
        paginator = Paginator(all_news_list, self.paginate_by)
        page = request.GET.get('page')
        try:
            all_news = paginator.page(page)
        except PageNotAnInteger:
            all_news = paginator.page(1)
        except EmptyPage:
            all_news = paginator.page(paginator.num_pages)

        # Изменим запрос, чтобы выбирать только необходимое количество новостей
        all_news_for_page = AllNews.objects.select_related('user').order_by('-time')[:5]

        post = get_object_or_404(AllNews, id=id)

        title = 'главная страница'
        # title = title.capitalize()
        #joke = 'Сайт создан с мною...2023'
        return render(request, self.template_name, {'post': post,
                                                    'all_news_list': all_news,
                                                    'image_present': post.image or post.image_url,
                                                    'all_news_for_page': all_news_for_page})  # 'joke': joke


class ContactView(LoginRequiredMixin, View):
    template_name = 'mynewsapp/contact.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            try:
                send_mail(
                    'Contact message',
                    f'Ваше сообщение: {message} принято',
                    'from@example.com',
                    ['viper101011@gmail.com'],
                    fail_silently=False,
                )
                return redirect('index')
            except Exception as e:
                # Логирование ошибки или добавление сообщения об ошибке
                print(f"Error sending email: {e}")
                return redirect('index')
        else:
            return render(request, self.template_name, context={'form': form})

@login_required
def create_post_view(request):
    template_name = 'mynewsapp/create.html'
    if request.method == 'POST':
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            try:
                form.instance.user = request.user
                form.save()
                return redirect(reverse('index'))
            except Exception as e:
                # Логирование ошибки или добавление сообщения об ошибке
                print(f"Error saving post: {e}")
    else:
        form = PostForm()
    return render(request, template_name, context={'form': form})

class SimpleMainAjax(TemplateView):
    template_name = 'mynewsapp/simple.html'












