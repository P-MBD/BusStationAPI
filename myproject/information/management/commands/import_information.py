import csv
from django.core.management.base import BaseCommand
from information.models import Information, Station

class Command(BaseCommand):
    help = 'Import information from CSV'

    def handle(self, *args, **kwargs):
        with open('C:/Users/user/Desktop/csv/Tbl_Information.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                station = Station.objects.get(id=row['Id_Station'])
                Information.objects.create(
                    station=station,
                    day=row['day'],
                    Time=row['Time']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
