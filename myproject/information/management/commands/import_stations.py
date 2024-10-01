import csv
from django.core.management.base import BaseCommand
from information.models import Station  # مطمئن شوید که مدل Station درست تعریف شده است

class Command(BaseCommand):
    help = 'Import stations from CSV'

    def handle(self, *args, **kwargs):
        with open('C:/Users/user/Desktop/csv/Tbl_Stations.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Station.objects.create(
                    Title=row['Title'],             # نام فیلدها باید با نام‌های مدل مطابقت داشته باشد
                    English_title=row['EnglishTitle'],
                    Line=row['Line'],
                    Address=row['Address'],
                    Lat=row['Lat'],
                    Lang=row['Lang'],
                    Description=row['Description']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
