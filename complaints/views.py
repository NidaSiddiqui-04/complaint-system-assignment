from django.shortcuts import render,redirect
from .form import Complaintform
from django.contrib.auth import models
from .models import Complaint
from django.contrib.auth.decorators import user_passes_test,login_required
from django.shortcuts import get_object_or_404



# Create your views here.
def add_complaint(request):

    if request.method=='POST':
        form=Complaintform(request.POST,request.FILES)
        
        if form.is_valid():
            complaint = form.save(commit=False)  
            complaint.user = request.user         
            complaint.save()    
            return redirect('complaint:user_dashboard')
        
    form=Complaintform()
    return render(request,'complaint/complaint_form.html',{'form':form})




def my_complaints(request):
    complaint=Complaint.objects.filter(user=request.user)
    return render(request,'complaint/my_complaint.html',{'complaint':complaint})


from django.db.models import Count

def is_user(user):
    return user.is_authenticated and user.role=='user'



@user_passes_test(is_user)
@login_required
def user_dashboard(request):
     complaints = Complaint.objects.filter(user=request.user)

     total = complaints.count()

     status_summary = complaints.values('status').annotate(count=Count('status'))

     return render(request, 'complaint/user_dashboard.html', {
        'total': total,                       
        'status_summary': status_summary, 
        'complaints':complaints,   
    })

def is_admin(user):
    return user.is_authenticated and user.role=='admin'

@user_passes_test(is_admin)
def all_complaints(request):
    complaint=Complaint.objects.all()
    return render(request,'complaint/complaint_list.html',{'complaint':complaint})
    



@user_passes_test(is_admin)
def update_status(request,id):
    complaint = get_object_or_404(Complaint, id=id)
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(Complaint.STATUS_CHOICES).keys():
            complaint.status = new_status
            complaint.save()
        return redirect("complaint:all_complaints")
    return render(request, "complaint/update_status.html", {"complaint": complaint})

 

@user_passes_test(is_admin)
def admin_dashboard(request):
    # complaints को category के हिसाब से group करें
    category_summary = Complaint.objects.values('category').annotate(count=Count('category'))

    # unresolved complaints (Pending या In Progress)
    unresolved = Complaint.objects.exclude(status='Resolved')

    return render(request, 'complaint/admin_dashboard.html', {
        'category_summary': list(category_summary),
        'unresolved': unresolved,
    })