from django.shortcuts import render
# from django.http import JsonResponse
# from django.contrib.auth import authenticate, login
# import json
# Create your views here.

def home(request):
    return render(request,"home.html")

def room(request,room_name):
    return render(request,"room.html",{"roomname":room_name})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             # Generate token
#             token = generate_token_for_user(user)
#             return JsonResponse({'token': token})
#         else:
#             return JsonResponse({'error': 'Invalid credentials'}, status=400)
