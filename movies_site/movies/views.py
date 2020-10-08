from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Hall

# Create your views here.

def home(request):
    return render(request, 'movies/home.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signupview.html'

# def crate_hall(request):
#     if request.method == 'POST':
#         # get the form data
#         # validate form data
#         # create hall
#         # save Hall
#     else:
#         # Create a form for a hall
#         # return the template

class CreateHall(generic.CreateView):
    model = Hall
    fields = ['title']
    template_name = 'movies/create_hall.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateHall, self).form_valid(form)
        return redirect('home')