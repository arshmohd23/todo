from django.shortcuts import render, redirect


# Create your views here.

from .models import TO_DO
from .forms import todoForm

# Create your views here.


def home(request):
    text = TO_DO.objects.all()
    form = todoForm()

    if request.method == 'POST':
        form = todoForm(request.POST)
        # text = request.POST.get('text')

        if form.is_valid():
            form.save()

        return redirect('home')

    context = {'text': text, 'form': form}
    return render(request, 'main.html', context)


def updatetask(request, id):
    updated = TO_DO.objects.get(id=id)
    form = todoForm(instance=updated)
    if request.method == 'POST':
        form = todoForm(request.POST, instance=updated)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def deletetask(request, id):
    item = TO_DO.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('home')

    context = {
        'item': item
    }
    return render(request, 'delete.html', context)


def deleteall(request):
    item = TO_DO.objects.all()
    if request.method == 'POST':
        item.delete()
        return redirect('home')

    # return render(request, 'deleteall.html')
