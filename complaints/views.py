from django.shortcuts import render
from .models import Complaint


def home(request):
    return render(request, "home.html")


def register_complaint(request):

    if request.method == "POST":

        complaint = Complaint.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            description=request.POST.get("description")
        )

        return render(
            request,
            "success.html",
            {
                "complaint_id": complaint.complaint_id
            }
        )

    return render(request, "register_complaint.html")


def complaint_success(request):
    return render(request, "success.html")


def track_complaint(request):
    complaint = None

    if request.method == "POST":
        complaint_id = request.POST.get("complaint_id")
        complaint = Complaint.objects.filter(
            complaint_id=complaint_id
        ).first()

    return render(
        request,
        "track_complaint.html",
        {
            "complaint": complaint
        }
    )