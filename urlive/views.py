from django.shortcuts import render
import uuid
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from .models import Room, User
import json
    
def make(request): #make new room and enter
    if request.method == 'POST':
        req_data = json.loads(request.body.decode())
        room_name = req_data['name']
        nickname = req_data['nickname']
        uid = req_data['uid']

        pincode = uuid.uuid4().hex[:6]
        encrypt = uuid.uuid4().hex[:20]
        #방 이름, 초대코드를 넣어서 방 처음 생성 
        # pre_room = Room.objects.filter(is_selected = True)
        # for room in pre_room:
        #     pre_room.is_selected = False

        newRoom= Room.objects.create(
            name=room_name,
            pincode= pincode,
            encrypt= encrypt,
            # is_selected = True,
        )

        #받은 닉네임으로 방장 생성
        creator = User.objects.create(
			nickname=nickname,
			room = newRoom,
            uid = uid,
		) 

        newRoom.save()
        creator.save()

        context = {}
        context['room_name'] = newRoom.name
        context['pincode'] = pincode
        context['nickname'] = creator.nickname
        context['uid'] = creator.uid
        context['encrypt'] = newRoom.encrypt
        print(context)
        context = json.dumps(context)
        return HttpResponse(status=200, content=context)
        # return HttpResponseRedirect('/{}/'.format(newRoom.encrypt))
    else: 
        return HttpResponseNotAllowed(['POST'])

def enter(request):
    if request.method == 'POST':
        req_data = json.loads(request.body.decode())
        pincode = req_data['pincode']
        nickname = req_data['nickname']
        uid = req_data['uid']
       
        # pre_room = Room.objects.filter(is_selected = True)
        # for room in pre_room:
        #     pre_room.is_selected = False

        room = Room.objects.get(pincode= pincode)

        if room is not None:
            newUser = User.objects.create(
                nickname= nickname,
                room= room,
                uid = uid,
            )
            newUser.save()

            context = {}
            context['room_name'] = room.name
            context['pincode'] = pincode
            context['nickname'] = newUser.nickname
            context['uid'] = newUser.uid
            context['encrypt'] = room.encrypt
            
            print(context)
            context = json.dumps(context)
            return HttpResponse(status=200, content=context)

            # return HttpResponseRedirect('/{}/'.format(room.encrypt)) 
        else: 
            return HttpResponse(status = 400)
    else:
        return HttpResponse(status=400)

def room(request, encrypt):
    if request.method == 'GET':
        room= Room.objects.get(encrypt=encrypt)
        users= User.objects.filter(room= room.id)
        
        user_str = ''
        for user in users:
            user_str += user.nickname + '/'

        uid_str = ''
        for user in users:
            print(user.uid)
            uid_str += user.uid + '/'
        
        context = {}
        context['room_name'] = room.name
        context['pincode']=room.pincode
        # context['is_selected']=room.is_selected
        context['users_uid']=uid_str
        context['encrypt']=room.encrypt
        context['users_str']=user_str
        context = json.dumps(context)
        print(context)
        return HttpResponse(status=200, content=context)

    else:
        return HttpResponse(status=400)
	
def list(request, uid):
    if request.method == 'GET':
        print(uid)
        me = User.objects.filter(uid = uid) #다양한 방에 속한 나들 [별명1, 별명2,,,,]
        print(me)
        room_name_arr=''
        room_url_arr=''
        room_participant=''

        for user in me: 
            room= user.room
            
            room_name= room.name
            room_name_arr += room_name + '/'

            room_url= room.encrypt
            room_url_arr += room_url +'/'

            users= User.objects.filter(room= room.id)
            for participant in users:
                room_participant += participant.nickname + '='
            room_participant += '/'
            
        
        context = {}
        context['room_name_arr']=room_name_arr
        context['room_url_arr']=room_url_arr
        context['room_part_arr']=room_participant
        context = json.dumps(context)
        print(context)
        return HttpResponse(status=200, content=context)

    else:
        return HttpResponse(status=400)