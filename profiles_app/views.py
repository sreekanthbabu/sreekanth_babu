import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from profiles_app.models import Profile
from django.core import serializers

# Create your views here.


@csrf_exempt
def create_profile(request):
    if request.method == "POST":
        # Converted request body into a dictionary
        data = json.loads(request.body)
        # fetching the value of key "name1" and assigning into a variable called "name"
        name1 = data['name']
        phone_number1 = data['phone']
        email1 = data['email']
        pincode1 = data['pincode']

        profile = Profile(name=name1, email=email1,
                          phone_number=phone_number1, pincode=pincode1)
        profile.save()
        return HttpResponse("Created!")
    else:
        return HttpResponseBadRequest('Invalid Method type!')


# @csrf_exempt
# def get_profiles(request):
#     if request.method == "GET":
#         profiles_queryset = Profile.objects.all()
#         profiles_json = serializers.serialize('json', profiles_queryset)
#         return HttpResponse(profiles_json, content_type='application/json')
#     else:
#         return HttpResponse('Invalid Method type!', status=400)
#         # return HttpResponseBadRequest('Invalid Method type!')

@csrf_exempt
def get_profiles(request):
    if request.method == "GET":
        profiles_queryset = Profile.objects.values(
            'id', 'name', 'email', 'phone_number', 'pincode')
        json_data = json.dumps(list(profiles_queryset))
        print(json_data, type(json_data))
        return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponse('Invalid Method type!', status=400)
        # return HttpResponseBadRequest('Invalid Method type!')


@csrf_exempt
def get_profile(request, profile_id):
    if request.method == 'GET':
        try:
            profile = Profile.objects.get(id=profile_id)
            profile_dictionary = {
                'id': profile.id,
                'name': profile.name,
                'email': profile.email,
                'phone_number': profile.phone_number,
                'pincode': profile.pincode,
            }
            profile_json = json.dumps(profile_dictionary)  # Dictonary to json
            return HttpResponse(profile_json, content_type='application/json')
        except Profile.DoesNotExist:
            return HttpResponse('Profile not found', status=404)
            # return HttpResponseNotFound('Profile not found')
    else:
        return HttpResponse('Invalid Method type!', status=400)


@csrf_exempt
def update_profile(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        # fetching the value of key "name1" and assigning into a variable called "name"
        id1 = data['id']
        name1 = data['name']
        phone_number1 = data['phone']
        email1 = data['email']
        pincode1 = data['pincode']

        profile = Profile.objects.get(id=id1)
        profile.name = name1
        profile.email = email1
        profile.phone_number = phone_number1
        profile.pincode = pincode1 
        profile.save()
        return HttpResponse("Updated!")
    else:
        return HttpResponseBadRequest('Invalid Method type!')


@csrf_exempt
def delete_profile(request, profile_id):
    if request.method == 'DELETE':
        try:
            profile = Profile.objects.get(id=profile_id)
            profile.delete()
            return HttpResponse('Deleted!')
        except Profile.DoesNotExist:
            return HttpResponse('Profile not found', status=404)
    else:
        return HttpResponse('Invalid Method type!', status=400)
