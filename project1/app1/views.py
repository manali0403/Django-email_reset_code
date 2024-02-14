from django.shortcuts import render,redirect
from .forms import Student,StudentForm

# Create your views here.

def add_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'app1/add.html'
    context = {'form':form}
    return render(request,template_name,context)


def show_view(request):
    obj = Student.objects.all()
    template_name = 'app1/show.html'
    context = {'form':obj}
    return render(request,template_name,context)


def update_view(request,pk):
    obj = Student.objects.get(id=pk)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'app1/add.html'
    context = {'form':form}
    return render(request,template_name,context)



def delete_view(request,pk):
    obj = Student.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'app1/delete.html'
    context = {'form':obj}
    return render(request,template_name,context)
