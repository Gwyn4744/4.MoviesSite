from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Hall, Video
from django.contrib.auth import authenticate, login
from .forms import VideoForm, SearchForm
from  django.http import Http404, JsonResponse
import urllib
import requests
from django.forms.utils import ErrorList

YOUTUBE_API_KEY = 'AIzaSyAKsVcz9Qa1S2Qd-_LKFuiduKdIGUowb7A'

# Create your views here.

def home(request):
    return render(request, 'movies/home.html')

def dashboard(request):
    return render(request, 'movies/dashboard.html')

def add_video(request, pk):
    form = VideoForm()
    search_form = SearchForm()
    hall = Hall.objects.get(pk=pk)
    if not hall.user == request.user:
        raise Http404
    if request.method == 'POST':
        # Create
        form = VideoForm(request.POST)
        if form.is_valid():
            video = Video()
            video.hall = hall
            video.url = form.cleaned_data['url']
            parsed_url = urllib.parse.urlparse(video.url)
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
            if video_id:
                video.youtube_id = video_id[0]
                response = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={ video_id[0] }&key={YOUTUBE_API_KEY}')
                json = response.json()
                title = json['items'][0]['snippet']['title']
                video.title = title
                video.save()
                return redirect('detail_hall', pk)
            else:
                errors = form._errors.setdefault('url', ErrorList())
                errors.append('Needs to be a YouTube URL')
    context = {
        'form': form,
        'search_form': search_form,
        'hall': hall,
    }
    return render(request, 'movies/add_video.html', context)

def video_search(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        return JsonResponse({'Hello': search_form.cleaned_data['search_tern']})
    return JsonResponse({'Hello': 'Not working'})

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