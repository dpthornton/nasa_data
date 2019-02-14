from django.db import models


class Facility(models.Model):
    center = models.CharField(max_length=64, blank=True, null=True)
    center_search_status = models.CharField(max_length=64, blank=True, null=True)
    facility = models.CharField(max_length=64, blank=True, null=True)
    facility_url = models.URLField(blank=True, null=True)
    occupied = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    url_link = models.URLField(blank=True, null=True)
    record_date = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    contact = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    location_type = models.CharField(max_length=64, blank=True, null=True)
    location_zip = models.CharField(max_length=64, blank=True, null=True)
    location_x = models.DecimalField(max_digits=9, decimal_places=6)
    location_y = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=64, blank=True, null=True)
    zipcode = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'facility'

    def __str__(self):
        return self.center + ' - ' + self.facility