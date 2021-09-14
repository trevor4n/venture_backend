from django.db import models

class Trip(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    # todo - implement layovers, secondary destinations, & timeline
    description = models.TextField()
    # iata_code = models.CharField(max_length=3)
    photo_url = models.TextField()
    
    def __str__(self):
        return self.name

class Guideline(models.Model):
    trip = models.ForeignKey(
        Trip, 
        on_delete=models.CASCADE, 
        related_name='guidelines'
    )
    # ref - https://developers.travelperk.com/docs/sandbox-environment-1#travel-restrictions
    location_type = models.CharField(max_length=100, default='country_code')
    location = models.CharField(max_length=3, default='DE')

    def __str__(self):
        return self.title

class Restriction(models.Model):
    trip = models.ForeignKey(
        Trip, 
        on_delete=models.CASCADE, 
        related_name='restrictions'
    )
    # ref - https://developers.travelperk.com/docs/sandbox-environment-1#local-summary
    destination_type = models.CharField(max_length=100, default='country_code')
    destination = models.CharField(max_length=3, default='ES')
    origin_type = models.CharField(max_length=100, default='country_code')
    origin = models.CharField(max_length=3, default='DE')
    arrival_date = models.DateField(default='2020-10-15')

    def __str__(self):
        return self.title

class Airline(models.Model):
    trip = models.ForeignKey(
        Trip, 
        on_delete=models.CASCADE, 
        related_name='airlines'
    )
    # ref - https://developers.travelperk.com/docs/sandbox-environment-1#airline-safety-measures
    iata_code = models.CharField(max_length=3, default='LH')

    def __str__(self):
        return self.title