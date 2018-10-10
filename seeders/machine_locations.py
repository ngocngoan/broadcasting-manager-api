from machine_locations.models import MachineLocation

LOCARIONS = [
    {
        'name': 'Địa điểm đặt máy cùng với Đài địa phương',
        'owner': 'Đài Truyền hình Quốc gia'
    },
    {
        'name': 'Địa điểm đặt máy đặc biệt khó khăn',
        'owner': 'Đài Truyền hình Quốc gia'
    },
    {
        'name': 'Cụm máy phát độc lập của Đài Truyền hình Quốc gia',
        'owner': 'Đài Truyền hình Quốc gia'
    },
    {
        'name': 'Địa điểm đặt máy bình thường',
        'owner': 'Đài Truyền hình Địa phương'
    },
    {
        'name': 'Địa điểm đặt máy đặc biệt khó khăn',
        'owner': 'Đài Truyền hình Địa phương'
    },
]


class MachineLocationSeeder:
    def __init__(self):
        MachineLocation.objects.all().delete()
        for location in LOCARIONS:
            new_location = MachineLocation(name=location['name'], owner=location['owner'])
            new_location.save()
