from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', context={'users': users})

@login_required
def chatPage(request, username):  
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'main_chat.html', context={'users': users, 'chat_user': user_obj})


