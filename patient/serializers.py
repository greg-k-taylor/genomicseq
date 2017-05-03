from rest_framework import serializers
from patient.models import Patient
from sequence.serializers import SequenceSerializer


class PatientSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=128)
    address = serializers.CharField(max_length=255)
    date_of_birth = serializers.CharField(max_length=255)

    sequences = SequenceSerializer(many=True, read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Patient` instance, given the validated data.
        """
        return Patient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Patient` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance

    class Meta:
        model = Patient
        fields = ('name', 'address', 'date_of_birth', 'created_at', 'sequences')
        # fields = ('name', 'address', 'date_of_birth', 'created_at')
