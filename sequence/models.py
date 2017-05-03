from django.db import models

from patient.models import Patient


class Sequence(models.Model):
    patient = models.ForeignKey(Patient, related_name='sequences', on_delete=models.CASCADE)
    sequence = models.CharField(max_length=1028)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __unicode__(self):
    #     return '%d: %d' % (self.id, self.sequence)
