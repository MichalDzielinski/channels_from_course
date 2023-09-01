from django.shortcuts import render
from .models import ChatRoom, ChatMessage

def index(request):
    cr = ChatRoom.objects.all()
    context = {'cr':cr}
    return render(request, 'app/index.html', context)

def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]
    context = {'chatroom': chatroom, 'messages': messages}
    return render(request, 'app/room.html', context)










