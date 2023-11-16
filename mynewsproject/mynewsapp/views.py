# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views import View
from .models import AllNews
from .forms import ContactForm, PostForm

class IndexView(View):
    template_name = 'mynewsapp/index.html'

    def get(self, request):
        posts = AllNews.objects.all()  # Здесь вы должны получить свои объекты постов
        return render(request, self.template_name, {'posts': posts})


class AllNewsView(LoginRequiredMixin, View):
    template_name = 'mynewsapp/all_news.html'


    def get(self, request, id):
        all_news_list = AllNews.objects.all().order_by('-time')
        post = get_object_or_404(AllNews, id=id)
        return render(request, self.template_name, {'post': post, 'all_news_list': all_news_list, 'image_present': post.image or post.image_url})

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

            send_mail(
                'Contact message',
                f'Ваше сообщение: {message} принято',
                'from@example.com',
                ['viper101011@gmail.com'],
                fail_silently=False,
            )

            return redirect('index')
        else:
            return render(request, self.template_name, context={'form': form})

@login_required
def create_post_view(request):
    template_name = 'mynewsapp/create.html'
    if request.method == 'POST':
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(reverse('index'))
    else:
        form = PostForm()
    return render(request, template_name, context={'form': form})










