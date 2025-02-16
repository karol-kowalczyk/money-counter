from django.db import models
from datetime import datetime, timedelta

class ActionStatus(models.Model):
    date = models.DateField(unique=True)
    executed_at = models.DateTimeField(null=True, blank=True)
    
    def mark_as_executed(self):
        self.executed_at = datetime.now()
        self.save()

    @classmethod
    def was_action_executed_recently(cls):
        today = datetime.today().date()
        current_hour = datetime.now().hour  # Aktuelle Stunde des Tages
        
        try:
            action = cls.objects.get(date=today)
            if action.executed_at:
                # Überprüfe, ob die Aktion innerhalb der letzten `current_hour` Stunden durchgeführt wurde
                if datetime.now() - action.executed_at < timedelta(hours=current_hour):
                    return True  # Aktion wurde innerhalb der letzten `current_hour` Stunden ausgeführt
            return False
        except cls.DoesNotExist:
            return False
