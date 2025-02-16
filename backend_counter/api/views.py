from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ToPay, AlreadyPaid
from .serializers import ToPaySerializer, AlreadyPaidSerializer


class ToPayAmountView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Hole den einzigen Eintrag
            to_pay_entry = ToPay.objects.first()
            if to_pay_entry:
                # Serialisiere den Eintrag und gib die Antwort zurück
                serializer = ToPaySerializer(to_pay_entry)
                return Response(serializer.data)
            else:
                return Response({"message": "No data available"}, status=404)
        except ToPay.DoesNotExist:
            return Response({"message": "No data available"}, status=404)


class AlreadyPaidView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            already_paid = AlreadyPaid.objects.latest('created_at')  # Holt den neuesten Eintrag
            serializer = AlreadyPaidSerializer(already_paid)
            return Response(serializer.data)
        except AlreadyPaid.DoesNotExist:
            return Response({"message": "No data available"}, status=404)

    def post(self, request, *args, **kwargs):
        # Hole den neuen Wert aus der Anfrage
        new_amount = request.data.get('amount_as_num')

        if new_amount is not None:
            # Erstelle ein neues AlreadyPaid-Objekt oder aktualisiere den Wert
            already_paid_entry = AlreadyPaid(amount=new_amount)
            already_paid_entry.save()

            return Response({'message': 'AlreadyPaid successfully updated'}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No amount provided"}, status=status.HTTP_400_BAD_REQUEST)
