from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=64, verbose_name = "Author's first name")
    last_name = models.CharField(max_length=64, verbose_name = "Author's last name")
    birthday_year = models.PositiveIntegerField(verbose_name = "Author's birthday year")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.birthday_year}"