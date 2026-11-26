from django.db import models


class Xodim(models.Model):
    ismi = models.CharField(max_length=100, verbose_name="Ismi")
    familiyasi = models.CharField(max_length=100, verbose_name="Familiyasi")
    yoshi = models.PositiveIntegerField(verbose_name="Yoshi")
    kasbi = models.CharField(max_length=150, verbose_name="Kasbi")

    def __str__(self):
        return f"{self.ismi} {self.familiyasi}"

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"


from django.db import models

# Create your models here.
