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
        Plant.objects.create(garden_bed=garden_bed, name="Test Plant 1", description="Test Plant Description 1")
        Plant.objects.create(garden_bed=garden_bed, name="Test Plant 2", description="Test Plant Description 2")
        Plant.objects.create(garden_bed=garden_bed, name="Test Plant 3", description="Test Plant Description 3")

    def test_number_of_garden_beds(self):
        """Number of garden beds for garden is correct."""
        garden = Garden.objects.get(name="Test Garden")
        beds = GardenBed.objects.filter(garden=garden)

        self.assertEqual(len(beds), 1)

    def test_number_of_plants(self):
        """Number of plants for garden bed is correct."""
        garden = Garden.objects.get(name="Test Garden")
        beds = GardenBed.objects.filter(garden=garden)
        plants = Plant.objects.filter(garden_bed=beds[0])

        self.assertEqual(len(plants), 3)
