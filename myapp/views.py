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

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JSONResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@csrf_exempt
def user_detail(request,pk):
	try:
		users = Users.objects.get(pk=pk)
 	except Users.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		user_detail_serializer = UsersSerializer(users)
		return user_detail_serializer.data

 	if request.method == 'PUT':
		user_data = JSONParser().parse(request)
    	user_serializer = UsersSerializer(users, data=user_data)
    	if user_serializer.is_valid():
    		user_serializer.save()
    		return JSONResponse(user_serializer.data)
    	return JSONResponse(user_serializer.errors, status=400)






