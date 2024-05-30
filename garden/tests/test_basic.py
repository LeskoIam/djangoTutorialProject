# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import pytest

from garden import models


@pytest.fixture(scope="module", autouse=True)
def _prepare_db(django_db_setup, django_db_blocker):
    # Set up non-modified objects used by all test methods
    with django_db_blocker.unblock():
        garden = models.Garden.objects.create(name="Test Garden", description="Test Garden Description")
        garden_bed = models.GardenBed.objects.create(
            garden=garden, name="Test Garden Bed", description="Test Garden Bed Description 1"
        )

        for plant_i in range(3):
            p = models.Plant(name=f"Test Plant {plant_i}", description=f"Test Plant Description{plant_i}")
            p.save()
            p.garden_bed.add(garden_bed)


@pytest.mark.django_db()
def test_numer_of_garden_beds():
    """Number of garden beds for garden is correct."""
    garden = models.Garden.objects.get(name="Test Garden")
    beds = models.GardenBed.objects.filter(garden=garden)

    assert len(beds) == 1


@pytest.mark.django_db()
def test_number_of_plants():
    """Number of plants for garden bed is correct."""
    garden = models.Garden.objects.get(name="Test Garden")
    beds = models.GardenBed.objects.filter(garden=garden)
    plants = models.Plant.objects.filter(garden_bed=beds[0])

    assert len(plants) == 3
