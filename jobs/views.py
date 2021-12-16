from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, job_title):

    if job_title.lower() == "neural decoding":
        return render(request, 'jobs/neuraldecoding.html')
    elif job_title.lower() == "emg decoding":
        return render(request, 'jobs/motiondecoding.html')
    elif job_title.lower() == "car rental app":
        return render(request, 'jobs/carapp.html')
    elif job_title.lower() == "board game app":
        return render(request, 'jobs/gameapp.html')
    elif job_title.lower() == "pta":
        return render(request, 'jobs/pta.html') 
    else:
        return render(request, 'jobs/home.html')
