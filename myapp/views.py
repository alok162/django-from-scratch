from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from myapp.models import Users
from myapp.serializers import UsersSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return JSONResponse(users_serializer.data)

    # elif request.method == 'POST':
    #     game_data = JSONParser().parse(request)
    #     game_serializer = GameSerializer(data=game_data)
    #     if game_serializer.is_valid():
    #         game_serializer.save()
    #         return JSONResponse(game_serializer.data, status=status.HTTP_201_CREATED)
    #     return JSONResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
