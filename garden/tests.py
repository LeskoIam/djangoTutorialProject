from django.test import TestCase

from garden.models import Garden, GardenBed, Plant


class MyFirstTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        garden = Garden.objects.create(name="Test Garden", description="Test Garden Description")
        garden_bed = GardenBed.objects.create(
            garden=garden, name="Test Garden Bed", description="Test Garden Bed Description 1"
        )

        for plant_i in range(3):
            p = Plant(name=f"Test Plant {plant_i}", description=f"Test Plant Description{plant_i}")
            p.save()
            p.garden_bed.add(garden_bed)

    def test_number_of_garden_beds(self):
        """Number of garden beds for garden is correct."""
        garden = Garden.objects.get(name="Test Garden")
        beds = GardenBed.objects.filter(garden=garden)

        assert len(beds) == 1

    def test_number_of_plants(self):
        """Number of plants for garden bed is correct."""
        garden = Garden.objects.get(name="Test Garden")
        beds = GardenBed.objects.filter(garden=garden)
        plants = Plant.objects.filter(garden_bed=beds[0])

        assert len(plants) == 3
