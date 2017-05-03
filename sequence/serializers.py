from rest_framework import serializers

from patient.models import Patient
from sequence.models import Sequence


class SequenceSerializer(serializers.ModelSerializer):
    sequence = serializers.CharField(max_length=1028)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    def create(self, validated_data):
        """
        Create and return a new `Marker` instance, given the validated data.
        """
        return Sequence.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Sequence` instance, given the validated data.
        """
        instance.patient_id = validated_data.get('patient_id', instance.patient_id)
        instance.sequence = validated_data.get('sequence', instance.sequence)
        instance.save()
        return instance

    class Meta:
        model = Sequence
        fields = ('sequence', 'created_at', 'patient')
