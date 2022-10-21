from django.db import transaction

from rest_framework import serializers

from api.models import Person, Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            "id", "color", "model"
        )


class PersonSerializer(serializers.ModelSerializer):
    vehicles = VehicleSerializer(many=True, required=False)

    class Meta:
        model = Person
        fields = (
            "id", "name", "vehicles", "sales_opportunity"
        )

    @transaction.atomic
    def create(self, validated_data):
        vehicles = validated_data.pop('vehicles', [])

        created_person = super(PersonSerializer, self).create(validated_data)

        for vehicle in vehicles:
            create_vehicle(person=created_person, vehicle=vehicle)

        return created_person

    @transaction.atomic
    def update(self, instance, validated_data):
        vehicles = validated_data.pop('vehicles', [])

        updated_person = super(PersonSerializer, self).update(instance, validated_data)

        for vehicle in vehicles:
            create_vehicle(person=updated_person, vehicle=vehicle)

        return updated_person


def create_vehicle(person: Person, vehicle: dict) -> None:
    color = Vehicle.objects.filter(person=person).filter(color=vehicle["color"])
    model = Vehicle.objects.filter(person=person).filter(model=vehicle["model"])
    if color.count() == 0 and model.count() == 0:
        Vehicle.objects.create(person=person, **vehicle)
