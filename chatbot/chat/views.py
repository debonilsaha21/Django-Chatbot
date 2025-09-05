from django.shortcuts import render, redirect
from django.http import JsonResponse 
from groq import Groq
from decouple import config
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone

client = Groq(api_key=config("API_KEY"))
# Create your views here.
def chatbot(request):
    user = request.user if request.user.is_authenticated else None
    chat_history = Chat.objects.filter(user=user) if user else []

    if user:
        chat_history = Chat.objects.filter(user=user)
        if request.method == "POST":
            message = request.POST.get('message')
            get_data = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant.  Keep all responses under 75 words."},
                    {"role": "user", "content": message}
                ]
            )
            # print(get_data)
            response = get_data.choices[0].message.content
            chat = Chat(user= request.user, message= message, response = response)
            chat.save()
            return JsonResponse({"message": message, "response": response})
    else:
        if request.method == "POST":
            message = request.POST.get('message')
            get_data = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant.  Keep all responses under 75 words."},
                    {"role": "user", "content": message}
                ]
            )
            # print(get_data)
            response = get_data.choices[0].message.content
            return JsonResponse({"message": message, "response": response})
    #handle get request
    return render(request, "chat_page.html", {"chat_history": chat_history})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username= username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("chatbot")
        else:
            return render(request, "login.html", {"error_message": "Invalid Username/Password"})
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(request, "register.html", {"error_message": "Passwords don't match!"})

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error_message": "Username already taken!"})

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error_message": "Email already registered!"})
        try:
            user = User.objects.create_user(
                username = username, 
                email = email, 
                password= password1
                )
            print("got user data")
            user.save()
            auth.login(request, user)
            return redirect("chatbot")
        except Exception as e:
            return render(request, "register.html", {"error_message": f"Error: {e}"})
        
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect("login")