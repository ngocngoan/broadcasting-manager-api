from contracts.models import Contract
from broadcasts.models import Broadcast
from unit_prices.models import UnitPrice

CONTRACTS = [
    {
        'contract_number': "39/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=43),
        'unit_price': UnitPrice.objects.get(pk=39),
    },
    {
        'contract_number': "33/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=44),
        'unit_price': UnitPrice.objects.get(pk=41),
    },
    {
        'contract_number': "44/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=45),
        'unit_price': UnitPrice.objects.get(pk=42),
    },
    {
        'contract_number': "04/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=46),
        'unit_price': UnitPrice.objects.get(pk=9),
    },
    {
        'contract_number': "05/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=47),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "46/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=48),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "18/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=49),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "01/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=50),
        'unit_price': UnitPrice.objects.get(pk=9),
    },
    {
        'contract_number': "22/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=51),
        'unit_price': UnitPrice.objects.get(pk=42),
    },
    {
        'contract_number': "03/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=52),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "03/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=53),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "38/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=54),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "49/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=55),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "01/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=56),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "40/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=57),
        'unit_price': UnitPrice.objects.get(pk=24),
    },
    {
        'contract_number': "39/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=58),
        'unit_price': UnitPrice.objects.get(pk=21),
    },
    {
        'contract_number': "50/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=59),
        'unit_price': UnitPrice.objects.get(pk=24),
    },
    {
        'contract_number': "46/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=60),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "59/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=61),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "44/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=62),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "28/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=63),
        'unit_price': UnitPrice.objects.get(pk=47),
    },
    {
        'contract_number': "60/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=64),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "18/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=65),
        'unit_price': UnitPrice.objects.get(pk=9),
    },
    {
        'contract_number': "32/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=66),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "39/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=67),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "42/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=68),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "35/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=69),
        'unit_price': UnitPrice.objects.get(pk=9),
    },
    {
        'contract_number': "30/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=70),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "09/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=71),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "02/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=72),
        'unit_price': UnitPrice.objects.get(pk=9),
    },
    {
        'contract_number': "50/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=73),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "24/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=74),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "19/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=75),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "38/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=76),
        'unit_price': UnitPrice.objects.get(pk=45),
    },
    {
        'contract_number': "30/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=77),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "42/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=78),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "03/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=79),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "06/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=80),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "07/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=81),
        'unit_price': UnitPrice.objects.get(pk=7),
    },
    {
        'contract_number': "19/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=82),
        'unit_price': UnitPrice.objects.get(pk=10),
    },
    {
        'contract_number': "02/2016/HĐKT/THQG_So",
        'sign_date': "2016-02-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=83),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "23/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=84),
        'unit_price': UnitPrice.objects.get(pk=35),
    },
    {
        'contract_number': "24/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=85),
        'unit_price': UnitPrice.objects.get(pk=34),
    },
    {
        'contract_number': "34/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=86),
        'unit_price': UnitPrice.objects.get(pk=34),
    },
    {
        'contract_number': "21/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=87),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "34/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=88),
        'unit_price': UnitPrice.objects.get(pk=47),
    },
    {
        'contract_number': "43/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=89),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "54/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=90),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "14/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=91),
        'unit_price': UnitPrice.objects.get(pk=10),
    },
    {
        'contract_number': "20/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=92),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "08/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=93),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "43/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=94),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "54/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=95),
        'unit_price': UnitPrice.objects.get(pk=47),
    },
    {
        'contract_number': "21/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=96),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "17/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=97),
        'unit_price': UnitPrice.objects.get(pk=10),
    },
    {
        'contract_number': "40/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=98),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "09/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=99),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "05/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=100),
        'unit_price': UnitPrice.objects.get(pk=10),
    },
    {
        'contract_number': "13/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=101),
        'unit_price': UnitPrice.objects.get(pk=10),
    },
    {
        'contract_number': "55/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=102),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "05/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=103),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "10/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=104),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "48/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=105),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "05/2016/HĐKT/THQG_So",
        'sign_date': "2016-02-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=106),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "11/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=107),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "51/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=108),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "67/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=109),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "14/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=110),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "52/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=111),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "61/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=112),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "22/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=113),
        'unit_price': UnitPrice.objects.get(pk=7),
    },
    {
        'contract_number': "45/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=114),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "62/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=115),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "19/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=116),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "04/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=117),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "63/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=118),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "12/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=119),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "36/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=120),
        'unit_price': UnitPrice.objects.get(pk=47),
    },
    {
        'contract_number': "64/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=121),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "22/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=122),
        'unit_price': UnitPrice.objects.get(pk=48),
    },
    {
        'contract_number': "24/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=123),
        'unit_price': UnitPrice.objects.get(pk=9),
    },
    {
        'contract_number': "49/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=124),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "23/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=125),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "06/2016/HĐKT/THQG_So",
        'sign_date': "2016-02-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=126),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "25/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=127),
        'unit_price': UnitPrice.objects.get(pk=9),
    },
    {
        'contract_number': "37/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=128),
        'unit_price': UnitPrice.objects.get(pk=10),
    },
    {
        'contract_number': "48/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=129),
        'unit_price': UnitPrice.objects.get(pk=10),
    },
    {
        'contract_number': "33/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=130),
        'unit_price': UnitPrice.objects.get(pk=9),
    },
    {
        'contract_number': "47/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=131),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "65/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=132),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "29/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=133),
        'unit_price': UnitPrice.objects.get(pk=9),
    },
    {
        'contract_number': "14/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=134),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "38/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=135),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "34/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=136),
        'unit_price': UnitPrice.objects.get(pk=20),
    },
    {
        'contract_number': "41/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=137),
        'unit_price': UnitPrice.objects.get(pk=60),
    },
    {
        'contract_number': "37/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=138),
        'unit_price': UnitPrice.objects.get(pk=22),
    },
    {
        'contract_number': "28/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=139),
        'unit_price': UnitPrice.objects.get(pk=20),
    },
    {
        'contract_number': "26/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=140),
        'unit_price': UnitPrice.objects.get(pk=22),
    },
    {
        'contract_number': "36/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=141),
        'unit_price': UnitPrice.objects.get(pk=22),
    },
    {
        'contract_number': "20/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=142),
        'unit_price': UnitPrice.objects.get(pk=42),
    },
    {
        'contract_number': "06/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=143),
        'unit_price': UnitPrice.objects.get(pk=42),
    },
    {
        'contract_number': "41/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=144),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "40/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=145),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "51/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=146),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "15/2016/HĐKT/THQG6",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=147),
        'unit_price': UnitPrice.objects.get(pk=45),
    },
    {
        'contract_number': "15/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=148),
        'unit_price': UnitPrice.objects.get(pk=9),
    },
    {
        'contract_number': "31/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=149),
        'unit_price': UnitPrice.objects.get(pk=35),
    },
    {
        'contract_number': "21/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=150),
        'unit_price': UnitPrice.objects.get(pk=34),
    },
    {
        'contract_number': "31/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=151),
        'unit_price': UnitPrice.objects.get(pk=35),
    },
    {
        'contract_number': "16/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=152),
        'unit_price': UnitPrice.objects.get(pk=21),
    },
    {
        'contract_number': "27/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=153),
        'unit_price': UnitPrice.objects.get(pk=22),
    },
    {
        'contract_number': "58/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=154),
        'unit_price': UnitPrice.objects.get(pk=60),
    },
    {
        'contract_number': "17/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=155),
        'unit_price': UnitPrice.objects.get(pk=21),
    },
    {
        'contract_number': "30/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=156),
        'unit_price': UnitPrice.objects.get(pk=20),
    },
    {
        'contract_number': "42/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=157),
        'unit_price': UnitPrice.objects.get(pk=22),
    },
    {
        'contract_number': "53/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=158),
        'unit_price': UnitPrice.objects.get(pk=22),
    },
    {
        'contract_number': "04/2016/HĐKT/THQG_So",
        'sign_date': "2016-02-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=159),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "26/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=160),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "25/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=161),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "35/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=162),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "01/2016/HĐKT/THQG_So",
        'sign_date': "2016-02-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=163),
        'unit_price': UnitPrice.objects.get(pk=12),
    },
    {
        'contract_number': "18/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Tiếp Phát",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=164),
        'unit_price': UnitPrice.objects.get(pk=38),
    },
    {
        'contract_number': "36/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=165),
        'unit_price': UnitPrice.objects.get(pk=32),
    },
    {
        'contract_number': "35/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=166),
        'unit_price': UnitPrice.objects.get(pk=10),
    },
    {
        'contract_number': "18/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=167),
        'unit_price': UnitPrice.objects.get(pk=10),
    },
    {
        'contract_number': "27/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=168),
        'unit_price': UnitPrice.objects.get(pk=8),
    },
    {
        'contract_number': "31/2016/HĐKT/THQG2",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=169),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "43/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 5,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=170),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
    {
        'contract_number': "37/2016/HĐKT/THQG1",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=171),
        'unit_price': UnitPrice.objects.get(pk=7),
    },
    {
        'contract_number': "66/2016/HĐKT/THQG3",
        'sign_date': "2016-01-01",
        'contract_type': "Khai Thác",  # 0 = Khai Thác, 1 = Tiếp Phát
        'tax': 10,
        'cancel_date': None,
        'broadcast': Broadcast.objects.get(pk=172),
        'unit_price': UnitPrice.objects.get(pk=11),
    },
]


class ContractSeeder:
    def __init__(self):
        Contract.objects.all().delete()
        for contract in CONTRACTS:
            new_contract = Contract(contract_number=contract['contract_number'],
                                    sign_date=contract['sign_date'],
                                    contract_type=contract['contract_type'],
                                    tax=contract['tax'],
                                    cancel_date=contract['cancel_date'],
                                    broadcast=contract['broadcast'],
                                    unit_price=contract['unit_price'],
                                    )
            new_contract.save()