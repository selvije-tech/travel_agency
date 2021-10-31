from django.db import models



class Continent(models.Model):
    CONTINENT_CHOICES = (
    ('North America', 'North America'),
    ('South America', 'South America'),
    ('Europe', 'Europe'),
    ('Asia', 'Asia'),
    ('Antartica', 'Antartica'),
    ('Africa', 'Africa'),
    ('Oceania', 'Oceania'))

    name = models.CharField(max_length=255,choices=CONTINENT_CHOICES)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    continent_of_country = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name='continent_of_country')

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    country_of_city = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_of_city')

    def __str__(self):
        return self.name

class Hotel(models.Model):
    START_CHOICES = (
        ('1', '1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'))
        
    name = models.CharField(max_length=255, null=False, blank=False)
    standard = models.CharField(max_length=255 ,choices=START_CHOICES)
    description = models.TextField(blank=True, null=True)
    city_of_hotel = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_of_hotel')

    def __str__(self):
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    city_of_airport = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_of_airport')

    def __str__(self):
        return self.name

class Trip(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    ACCOMODATION_CHOICES = (
        ('bed & breakfast' , 'BB'),
        ('half board', 'HB'),
        ('full board' , 'FB'),
        ('all inclusive' , 'AI'))
        

    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city')
    from_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='from_airport')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city')
    to_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='to_hotel')
    to_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='to_airport')
    date_of_departure = models.DateTimeField()
    date_of_return = models.DateTimeField()
    number_of_days = models.IntegerField()
    type_of_accomodation = models.CharField(max_length=255,choices=ACCOMODATION_CHOICES)
    price_for_an_adult = models.DecimalField(max_digits=10, decimal_places=2)
    price_for_a_chield = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_places_for_adults = models.IntegerField()
    number_of_places_for_children = models.IntegerField()

    def __str__(self):
        return self.name

class Purchase(models.Model):
    purchase_trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='purchase_trip')
    participiant_details = models.CharField(max_length=255,blank=False, null=False)
    amount = models.IntegerField()

