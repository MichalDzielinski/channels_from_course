from django.shortcuts import render
from .models import ChatRoom

def index(request):
    cr = ChatRoom.objects.all()
    context = {'cr':cr}
    return render(request, 'app/index.html', context)

def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    context = {'chatroom': chatroom}
    return render(request, 'app/room.html', context)










