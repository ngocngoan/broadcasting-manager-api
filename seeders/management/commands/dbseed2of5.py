from django.core.management.base import BaseCommand, CommandError

#### Step 2
from seeders.unit_prices import UnitPriceSeeder
from seeders.stations import StationSeeder


class Command(BaseCommand):
    help = 'Import unit price and base-station data'

    def handle(self, *args, **options):
        #### Step 2
        UnitPriceSeeder()
        StationSeeder()
        self.stdout.write(self.style.SUCCESS('Import unit price and base-station data successfully'))

