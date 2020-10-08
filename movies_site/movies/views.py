from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Hall
from django.contrib.auth import authenticate, login
from .forms import VideoForm

# Create your views here.

def home(request):
    return render(request, 'movies/home.html')

def dashboard(request):
    return render(request, 'movies/dashboard.html')

def add_video(request, pk):
    form = VideoForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/add_video.html', context)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signupview.html'

    def form_valid(self, form):
        view = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

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
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateHall, self).form_valid(form)
        return redirect('home')

class DetailHall(generic.DetailView):
    model = Hall
    template_name = 'movies/detail_hall.html'

class UpdateHall(generic.UpdateView):
    model = Hall
    template_name = 'movies/update_hall.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')

class DeleteHall(generic.DeleteView):
    model = Hall
    template_name = 'movies/delete_hall.html'
    success_url = reverse_lazy('dashboard')