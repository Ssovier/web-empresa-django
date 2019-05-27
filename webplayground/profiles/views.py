from django.shortcuts import render,get_object_or_404
from django.views.generic.detail import DetailView
from registration.models import Profile
from django.utils import timezone
from django.views.generic.list import ListView


class ProfileListView(ListView):
    template_name = 'profiles/profile_list.html'
    model = Profile
    paginate_by = 2


class ProfileDetailView(DetailView):
    template_name = 'profiles/profile_detail.html'
    model = Profile

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
        