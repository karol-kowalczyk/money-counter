from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from backend_counter.api.models import AlreadyPaid

class PerformActionView(APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.today().date()
        
        # Überprüfen, ob heute der 20. ist
        if today.day == 16:
            # Überprüfen, ob der Wert bereits für diesen Monat erhöht wurde
            # Angenommen, wir speichern ein `created_at`-Feld für jedes `AlreadyPaid`-Objekt
            latest_payment = AlreadyPaid.objects.filter(created_at__month=today.month).first()
            
            if latest_payment:  # Wenn bereits ein Eintrag für diesen Monat existiert
                return Response({"message": "Der Wert wurde bereits diesen Monat erhöht."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Erhöhe den Wert (nehmen wir an, der Wert beträgt 100)
            new_amount = 100  # Hier könnte eine Logik kommen, um den Wert dynamisch zu berechnen
            AlreadyPaid.objects.create(amount=new_amount)
            
            return Response({"message": "Der Wert wurde erfolgreich erhöht."}, status=status.HTTP_200_OK)
        
        # Wenn es nicht der 20. ist, Fehlermeldung mit aktuellem Datum zurückgeben
        return Response({
            "message": f"Sorry, heute ist der {today.day}. und nicht der 20."
        }, status=status.HTTP_400_BAD_REQUEST)