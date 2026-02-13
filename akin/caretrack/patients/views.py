from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient


def home(request):
    patients = Patient.objects.all()
    return render(request, 'patients/home.html', {'patients': patients})



def add_patient(request):
    if request.method == 'POST':
        Patient.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            gender=request.POST['gender'],
            phone=request.POST['phone'],
            diagnosis=request.POST['diagnosis'],
        )
        return redirect('home')
    return render(request, 'patients/add_patient.html')


def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.age = request.POST['age']
        patient.gender = request.POST['gender']
        patient.phone = request.POST['phone']
        patient.diagnosis = request.POST['diagnosis']
        patient.save()
        return redirect('home')
    return render(request, 'patients/edit_patient.html', {'patient': patient})


def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('home')

# Create your views here.
