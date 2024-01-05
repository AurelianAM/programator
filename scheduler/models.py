from django.db import models

# Create your models here.


class Medic(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=30, null=False, unique=True)
    firstName = models.CharField(max_length=50, null=True, blank=True)
    lastName = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.nickname}"

class Scheduler(models.Model):
    date = models.DateField(primary_key=True)
    tura1 = models.ForeignKey(Medic, related_name='+', on_delete=models.CASCADE, null=True, default = "", blank=True)
    tura2 = models.ForeignKey(Medic, related_name='+', on_delete=models.CASCADE, null=True, default = "", blank=True)
    tura3 = models.ForeignKey(Medic, related_name='+', on_delete=models.CASCADE, null=True, default = "", blank=True)

    def __str__(self):
        return f"{self.date}-{self.tura1}-{self.tura2}-{self.tura3}"

    # tura1 = models.CharField(max_length=30, null=True, default=None)
    # tura2 = models.CharField(max_length=30, null=True, default=None)
    # tura3 = models.CharField(max_length=30, null=True, default=None)



    # tura1 = models.ForeignKey(Medic, to_field='nickname', related_name='tura1', on_delete=models.CASCADE, null=True)
    # tura2 = models.ForeignKey(Medic, to_field='nickname', on_delete=models.CASCADE, null=True)
    # tura3 = models.ForeignKey(Medic, to_field='nickname', on_delete=models.CASCADE, null=True)