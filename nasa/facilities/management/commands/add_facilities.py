from django.core.management.base import BaseCommand
from facilities.models import Facility
import requests
from datetime import timezone
from datetime import datetime


class Command(BaseCommand):
    help = 'Adds new NASA facilities to the database'


    def get_json_value(self, data, key):

        value = None

        try:
            value = data[key]
        except KeyError as e:
            pass

        return value

    def handle(self, *args, **options):

        url = "https://data.nasa.gov/resource/9g7e-7hzz.json"

        r = requests.get(url)
        facilities = r.json()

        new_facility_count = 0
        total_facilities = len(facilities)

        for f in facilities:

            location_type = None
            location_x = None
            location_y  = None

            location = self.get_json_value(f, 'location')

            if location:
                location_type = self.get_json_value(location, 'type')
                location_x = location['coordinates'][0]
                location_y = location['coordinates'][1]


            center = self.get_json_value(f, 'center')
            center_search_status = self.get_json_value(f, 'center_search_status')
            facility = self.get_json_value(f, 'facility')
            facility_url = self.get_json_value(f, 'facilityurl')
            occupied = self.get_json_value(f, 'occupied')
            status = self.get_json_value(f, 'status')
            url_link = self.get_json_value(f, 'url_link')
            record_date = self.get_json_value(f, 'record_date')
            last_update = self.get_json_value(f, 'last_update')
            country = self.get_json_value(f, 'country')
            contact = self.get_json_value(f, 'contact')
            phone = self.get_json_value(f, 'phone')
            location_zip = self.get_json_value(f, 'location_zip')
            location_type = location_type
            location_x = location_x
            location_y = location_y
            city = self.get_json_value(f, 'city')
            state = self.get_json_value(f, 'state')
            zipcode = self.get_json_value(f, 'zipcode')

            if occupied:
                occupied = datetime.strptime(occupied, '%Y-%m-%dT%H:%M:%S.%f').replace(tzinfo=timezone.utc)

            if record_date:
                record_date = datetime.strptime(record_date, '%Y-%m-%dT%H:%M:%S.%f').replace(tzinfo=timezone.utc)

            if last_update:
                last_update = datetime.strptime(last_update, '%Y-%m-%dT%H:%M:%S.%f').replace(tzinfo=timezone.utc)

            obj, created = Facility.objects.get_or_create(center=center,
                                                          center_search_status=center_search_status,
                                                          facility=facility,
                                                          facility_url=facility_url,
                                                          occupied=occupied,
                                                          status=status,
                                                          url_link=url_link,
                                                          record_date=record_date,
                                                          last_update=last_update,
                                                          country=country,
                                                          contact=contact,
                                                          phone=phone,
                                                          location_type=location_type,
                                                          location_zip = location_zip,
                                                          location_x=location_x,
                                                          location_y=location_y,
                                                          city=city,
                                                          state=state,
                                                          zipcode=zipcode
                                                        )
            if created:
                new_facility_count += 1

        facilities_count = Facility.objects.count()

        print('Loaded ' + str(new_facility_count) + ' new facility records')
        print('There are now ' + str(facilities_count) +  ' facility records stored')
        print('There were ' + str(total_facilities) + ' facility records available from the NASA API')