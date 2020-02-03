from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

def index(request):
    return render(request, 'index.html')

def display_pens(request):
    items = Pen.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)  # 3 arguments

def display_notebooks(request):
    items = Notebook.objects.all()
    context = {
        'items': items,
        'header': 'Notebooks',
    }
    return render(request, 'index.html', context)

def display_pencilcases(request):
    items = Pencilcase.objects.all()
    context = {
        'items': items,
        'header': 'Pencilcases',
    }
    return render(request, 'index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})

def add_pen(request):
    return add_item(request, PenForm)

def add_notebook(request):
    return add_item(request, NotebookForm)

def add_pencilcase(request):
    return add_item(request, PencilcaseForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = PenForm(instance=item)

    return render(request, 'edit_item.html', {'form': form})

def edit_pen(request, pk):
    return edit_item(request, pk, Pen, PenForm)

def edit_notebook(request, pk):
    return edit_item(request, pk, Notebook, NotebookForm)

def edit_pencilcase(request, pk):
    return edit_item(request, pk, Pencilcase, PencilcaseForm)

def delete_pen(request, pk):

    Pen.objects.filter(id=pk).delete()

    items = Pen.objects.all()

    context = {
        'items': items
    }

    return render(request, 'index.html', context)


def delete_notebook(request, pk):
    Notebook.objects.filter(id=pk).delete()

    items = Notebook.objects.all()

    context = {
        'items': items
    }

    return render(request, 'index.html', context)


def delete_pencilcase(request, pk):
    Pencilcase.objects.filter(id=pk).delete()

    items = Pencilcase.objects.all()

    context = {
        'items': items
    }

    return render(request, 'index.html', context)
