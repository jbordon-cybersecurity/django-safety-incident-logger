from django.shortcuts import render, redirect
from .models import Incident

def incident_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        category = request.POST.get("category")
        severity = request.POST.get("severity")
        country_issued = request.POST.get("country_issued")

        if title and description and category and severity and country_issued:
            Incident.objects.create(
                title=title,
                description=description,
                category=category,
                severity=severity,
                country_issued=country_issued
            )
            return redirect("incident_list")

    incidents = Incident.objects.all().order_by("-date_reported")
    return render(request, "incident_list.html", {"incidents": incidents})

