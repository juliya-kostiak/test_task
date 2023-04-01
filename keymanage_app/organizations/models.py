from django.db import models


class Organization (models.Model):
    name = models.CharField("Название организации", max_length=500)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def get_absolute_url(self):
        return '/organizations'

    def __str__(self):
        return self.name


class Keys (models.Model):
    key = models.UUIDField("Ключ")
    start_date = models.DateField("Дата начала действия")
    end_date = models.DateField("Дата окончания действия")
    id_org = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE)
    block = models.BooleanField("Блокировка", default=True)

    class Meta:
        verbose_name = "Ключ"
        verbose_name_plural = "Ключи"

    def get_absolute_url(self):
        return '/keys'

