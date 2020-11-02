from django.shortcuts import render, redirect
from .models import Member
from django.contrib.auth import authenticate, login, logout
from .Form import CreateUserForm, MemberForm


def index(request):
    member = Member.objects.get(user=request.user)
    return render(request, 'member/index.html', {'member': member})


def details(request, id):
    member = Member.objects.get(pk=id)
    return render(request, 'member/details.html', {'member': member})


def l_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    context = {}
    return render(request, 'member/login.html', context)


def logoutt(request):
    logout(request)
    return l_login(request)


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {"form": form}
    return render(request, 'member/register.html', context)


def settings(request, id):
    member = Member.objects.get(pk=id)
    form = MemberForm(instance=member)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'member/settings.html', context)
