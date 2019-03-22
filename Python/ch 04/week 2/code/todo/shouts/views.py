from django.shortcuts import render, redirect
from .models import Shout
from .forms import ShoutModelForm

# Create your views here.
def home(request):
    shouts = Shout.objects.all()
    return render(request, 'shouts/home.html', {'shouts':shouts})

def create(request):
    if request.method == "POST":
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shouts:home')
    else:
        form = ShoutModelForm()
        return render(request, 'shouts/form.html', {"form":form})


def update(request, shout_id):
    shout = Shout.objects.get(pk=shout_id)
    if request.method == "POST": # 수정하기
        form = ShoutModelForm(request.POST, instance=shout)
        if form.is_valid():
            form.save()
        return redirect('shouts:home')
    else: # 수정 html
        form = ShoutModelForm(instance=shout)
        context = {
            'form':form
        }
        return render(request, 'shouts/form.html', context)
