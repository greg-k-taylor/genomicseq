from rest_framework import serializers

from patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=128)
    address = serializers.CharField(max_length=255)
    date_of_birth = serializers.CharField(max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `Marker` instance, given the validated data.
        """
        return Patient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Marker` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.device_token)
        instance.address = validated_data.get('address', instance.prayer)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.prayer)
        instance.save()
        return instance

    class Meta:
        model = Patient
        fields = ('name', 'address', 'date_of_birth', 'created_at')
