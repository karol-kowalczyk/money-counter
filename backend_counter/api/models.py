from django.db import models

class ToPay(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Wenn es schon einen Eintrag gibt, wird der alte gelöscht
        if ToPay.objects.exists():
            ToPay.objects.all().delete()  # Alle löschen (nur eine Zeile darf existieren)
        super().save(*args, **kwargs)

class AlreadyPaid(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"AlreadyPaid: {self.amount} on {self.created_at}"

