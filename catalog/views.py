from django.shortcuts import render
from .models import CustomerUser, Category, RequestDesing
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import CreateView

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_requests_in_progress = RequestDesing.objects.filter(status='h').count()

    completed_requests = RequestDesing.objects.filter(status='с').order_by('-date')[:4]

    context = {
        'num_requests_in_progress': num_requests_in_progress,
        'completed_requests': completed_requests,
    }

    return render(request, 'index.html', context=context)

class RegisterView(CreateView):
     form_class = CustomUserCreationForm
     template_name = 'registration/register.html'
     success_url = '/catalog/my_requests/' # Или используйте LOGIN_REDIRECT_URL

     def form_valid(self, form):
         response = super().form_valid(form)
         login(self.request, self.object) # Логиним после успешного создания
         return response