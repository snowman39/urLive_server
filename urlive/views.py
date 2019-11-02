from django.shortcuts import render
import uuid
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from .models import Room, User

def home(request): #enter existing room
    return render(request, 'urlive/join.html')
    
def make(request): #make new room and enter
    if request.method == 'POST':
        room_name = request.POST['name']
        nickname = request.POST['nickname']
        pincode = uuid.uuid4().hex[:6]

        #방 이름, 초대코드를 넣어서 방 처음 생성 
        newRoom= Room.objects.create(
            name=room_name,
            pincode= pincode,
        ) 

        #받은 닉네임으로 방장 생성
        creator = User.objects.create(
			nickname=nickname,
			room = newRoom
		) 

        newRoom.save()
        creator.save()

        context = {}
        context['pincode'] = pincode
        context['creator'] = creator
        
        return HttpResponseRedirect('/{}/'.format(newRoom.id))
    else: 
        return HttpResponseNotAllowed(['POST'])

def room(request, room_id):
    if request.method == 'GET':
        context = {}
        context['room_id'] = room_id
        return render(request, 'urlive/room.html', context)
    elif request.method == 'POST':
        nickname = request.POST.get('nickname')
        pincode = request.POST.get('pincode')
        room = Room.objects.get(pincode= pincode)

        if room is not None:
            newUser = User.objects.create(nickname= nickname,room= room)
            return HttpResponseRedirect('/{}/'.format(room.id)) 
        else: 
            return HttpResponse(status = 400)
    else:
        return HttpResponse(status=400)

def new(request):
    return render(request, 'urlive/new.html')
	