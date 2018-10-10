from django.core.management.base import BaseCommand, CommandError

#### Step 1
from seeders.areas import AreaSeeder
from seeders.televisions import TelevisionSeeder
from seeders.machine_locations import MachineLocationSeeder


class Command(BaseCommand):
    help = 'Import area, television and machine location data'

    def handle(self, *args, **options):
        #### Step 1
        AreaSeeder()
        TelevisionSeeder()
        MachineLocationSeeder()
        self.stdout.write(self.style.SUCCESS('Import area, television and machine location data successfully'))
