from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Job
from django.db.models import Q


def home(request):
    # Search query pakadne ke liye
    query = request.GET.get('q')
    
    if query:
        # Agar koi search kar raha hai toh filter karein
        # job_title, vacancy_name ya category_details mein word dhoondein
        latest_jobs = Job.objects.filter(
            Q(job_title__icontains=query) | 
            Q(vacancy_name__icontains=query),
            show_in_latest_job=True
        ).order_by('-created_at')
        
        results = Job.objects.filter(
            Q(result_title__icontains=query) | 
            Q(job_title__icontains=query),
            show_in_result=True
        ).order_by('-created_at')
        
        admit_cards = Job.objects.filter(
            Q(admit_title__icontains=query) | 
            Q(job_title__icontains=query),
            show_in_admit_card=True
        ).order_by('-created_at')
    else:
        # Agar search khali hai toh normal data dikhayein
        latest_jobs = Job.objects.filter(show_in_latest_job=True).order_by('-created_at')
        results = Job.objects.filter(show_in_result=True).order_by('-created_at')
        admit_cards = Job.objects.filter(show_in_admit_card=True).order_by('-created_at')

    return render(request, 'home.html', {
        'latest_jobs': latest_jobs,
        'results': results,
        'admit_cards': admit_cards,
        'query': query # Isse search bar mein word bacha rahega
    })


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'job_detail.html', {'job': job})

def magic_entry_view(request):
    return render(request, 'admin/magic_entry.html')

def about_us(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact.html')

@csrf_exempt
def fast_entry_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            job = Job.objects.create(
                show_in_latest_job=data.get('show_in_latest_job', True),
                job_title=data.get('job_title'),
                show_in_result=data.get('show_in_result', False),
                show_in_admit_card=data.get('show_in_admit_card', False),
                vacancy_name=data.get('vacancy_name', 'Various Posts'),
                start_date=data.get('start_date'),
                fee_gen=data.get('fee_gen'),
                age_limit=data.get('age_limit'),
                total_posts=data.get('total_posts'),
                category_details=data.get('category_details'), # Isme Eligibility bhi hai
                important_links=data.get('important_links'),
                physical_details=data.get('physical_details', ''),
                selection_mode=data.get('selection_mode', ''),
                has_physical_standards=data.get('has_physical_standards', False),
                has_selection_mode=data.get('has_selection_mode', False),
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error'})