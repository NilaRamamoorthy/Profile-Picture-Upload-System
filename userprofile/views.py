from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import UserProfile

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'userprofile/upload.html', {'form': form})

def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'userprofile/profile.html', {'profiles': profiles})
