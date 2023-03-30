from django.db import models


class Organization (models.Model):
    name = models.CharField("Название организации", max_length=500)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.name


class Keys (models.Model):
    key = models.UUIDField()
    start_date = models.DateField()
    end_date = models.DateField()
    id_org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    block = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Ключ"
        verbose_name_plural = "Ключи"

    def __str__(self):
        return self.key

