from rest_framework import serializers
from .models import ToPay, AlreadyPaid

class ToPaySerializer(serializers.ModelSerializer):
    # Füge eine benutzerdefinierte Methode hinzu, um amount als Zahl zurückzugeben
    amount_as_number = serializers.SerializerMethodField()

    class Meta:
        model = ToPay
        fields = ['amount_as_number']

    def get_amount_as_number(self, obj):
        # Wandelt amount in eine Zahl um (float oder int)
        return float(obj.amount)  # oder int(obj.amount), je nach Wunsch

class AlreadyPaidSerializer(serializers.ModelSerializer):
    amount_as_num = serializers.SerializerMethodField()

    class Meta:
        model = AlreadyPaid
        fields = ['amount_as_num']

    def get_amount_as_num(self, obj):
        # Wandelt amount in eine Zahl um (float oder int)
        return float(obj.amount)  # oder int(obj.amount), je nach Wunsch
