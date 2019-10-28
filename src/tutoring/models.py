from django.db import models
import json

class Tutor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    form = models.CharField(max_length=20)
    subjects = models.CharField(max_length=300)
    available_times = models.CharField(max_length=1000)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

    def set_subjects(self, subjects):
        self.subjects = json.dumps(subjects)

    def get_subjects(self):
        return json.loads(self.subjects)
    
    def set_available_times(self, available_times):
        self.available_times = json.dumps(available_times)

    def get_available_times(self):
        return json.loads(self.available_times)

class Tutee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    form = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")