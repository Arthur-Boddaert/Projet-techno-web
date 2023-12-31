from django.db import models

# Create your models here.


class Multi_fasta(models.Model):
    file = models.FileField(upload_to='')