from django.db import models

class Incident(models.Model):
    SEVERITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    country_issued = models.CharField(max_length=100)  # ← add this line
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.severity})"


