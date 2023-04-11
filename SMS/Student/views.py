from django.shortcuts import render, redirect
from .forms import StudentForm, StudentModel, StudentUpdateForm
from django import views
from django.http import HttpResponse


class CreateStudent(views.View):
    template_name = 'Student/create_student.html'
    def get(self, request):
        form = StudentForm()
        context = {"form": form}
        return render(request, template_name=self.template_name, context=context)
    
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            rn =  form.cleaned_data.get("rn")
            fnm =  form.cleaned_data.get("fnm")
            lnm =  form.cleaned_data.get("lnm")
            mk =  form.cleaned_data.get("mk")

            student = StudentModel(rn=rn,fnm=fnm,lnm=lnm,mk=mk)
            student.save()
            return HttpResponse("<style={'color':'green'}>Data daved</style=>")
        
class ListStudentView(views.View):
    template_name = 'Student/list_student_view.html'

    def get(self, request):
        objs = StudentModel.objects.all()
        context = {'objs': objs}
        return render(request, template_name=self.template_name, context=context)
    
class UpdateStudentView(views.View):
    
    def get(self, request, pk=None):
        template_name = 'Student/update_student.html'
        obj = StudentModel.objects.get(id=pk)
        form = StudentUpdateForm(instance=obj)
        return render(request, template_name=template_name, context={'form':form})
    
    def post(self, request, pk=None):
        obj = StudentModel.objects.get(id=pk)
        form = StudentUpdateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list_student_url')
    
class DeleteStudentView(views.View):

    def delete(self, request, pk=None):
        template_name = 'Student/delete_student.html'
        obj = StudentModel.objects.get(id=pk)
        if request.method == 'POST':
            obj.delete()
            return redirect('list_student_url')
        return render(request, template_name=template_name, context={'obj':obj})
    
        
