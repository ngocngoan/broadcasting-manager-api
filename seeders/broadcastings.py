import datetime
import math
import random
from faker import Faker

from broadcasts.models import Broadcast
from contracts.models import Contract
from broadcasting_status.models import BroadcastingStatus
from time_ranges.models import TimeRange
from seeders.names import NAMES


class BroadcastingSeeder:
    def __init__(self):
        year = 2016
        now = datetime.datetime.now()
        start_day = datetime.date(year, 1, 1)
        broadcasts = Broadcast.objects.all()
        fake = Faker()
        broadcasts_by_contract = Broadcast.objects.filter(id__gt=11)

        while start_day < now.date():
            for broadcast in broadcasts:
                segments = broadcast.time_segment

                contract_start_date = broadcast.contract_start_date
                contract_end_date = broadcast.contract_end_date

                contract = Contract.objects.exclude(cancel_date=None).filter(broadcast=broadcast.pk).first()

                check = (start_day >= contract_start_date) \
                        and (start_day <= (contract_end_date + datetime.timedelta(days=1)))

                if contract is not None:
                    check = (start_day >= contract_start_date) \
                            and (start_day <= (contract_end_date + datetime.timedelta(days=1))) \
                            and (start_day <= contract.cancel_date + datetime.timedelta(days=1))

                if check:
                    if segments == 1:
                        broadcasting_status = BroadcastingStatus(
                            date=start_day,
                            power_T='500',
                            power_PX='5000',
                            reporter=self.generate_name(),
                            status=u'Bình thường',
                            broadcast=broadcast
                        )
                        broadcasting_status.save()

                        TimeRange(
                            type=1,
                            start_time=datetime.time.min,
                            end_time=datetime.time.max,
                            broadcasting_status=broadcasting_status
                        ).save()
                        print(broadcasting_status)

                    if segments == 2:
                        broadcasting_status = BroadcastingStatus(
                            date=start_day,
                            power_T='500',
                            power_PX='5000',
                            reporter=self.generate_name(),
                            status=u'Bình thường',
                            broadcast=broadcast
                        )
                        broadcasting_status.save()

                        TimeRange(
                            type=1,
                            start_time=datetime.time.min,
                            end_time=datetime.time(17, 0, 0),
                            broadcasting_status=broadcasting_status
                        ).save()

                        TimeRange(
                            type=1,
                            start_time=datetime.time(20, 0, 0),
                            end_time=datetime.time.max,
                            broadcasting_status=broadcasting_status
                        ).save()
                        print(broadcasting_status)

                    if segments == 3:
                        broadcasting_status = BroadcastingStatus(
                            date=start_day,
                            power_T='500',
                            power_PX='5000',
                            reporter=self.generate_name(),
                            status=u'Bình thường',
                            broadcast=broadcast
                        )
                        broadcasting_status.save()

                        TimeRange(
                            type=1,
                            start_time=datetime.time.min,
                            end_time=datetime.time(11, 0, 0),
                            broadcasting_status=broadcasting_status
                        ).save()

                        TimeRange(
                            type=1,
                            start_time=datetime.time(11, 40, 00),
                            end_time=datetime.time.max,
                            broadcasting_status=broadcasting_status
                        ).save()

                        TimeRange(
                            type=1,
                            start_time=datetime.time(21, 30, 00),
                            end_time=datetime.time.max,
                            broadcasting_status=broadcasting_status
                        ).save()
                        print(broadcasting_status)

            start_day += datetime.timedelta(days=1)

        # Nhập thông tin lỗi 100.000 lần
        for i in range(50000):
            start_time_string = fake.time(pattern="%H:%M:%S", end_datetime=None)
            end_time_string = fake.time(pattern="%H:%M:%S", end_datetime=None)

            start_time_list = start_time_string.split(':')
            end_time_list = end_time_string.split(':')

            start_time_day = datetime.datetime(
                now.year, now.month, now.day,
                int(start_time_list[0]), int(start_time_list[1]), 0
            )
            end_time_day = datetime.datetime(
                now.year, now.month, now.day,
                int(end_time_list[0]), int(end_time_list[1]), 0
            )
            time_delta = end_time_day - start_time_day

            if time_delta.total_seconds() <= 0:
                start_time = datetime.time(int(end_time_list[0]), int(end_time_list[1]), 0)
                end_time = datetime.time(int(start_time_list[0]), int(start_time_list[1]), 0)
            else:
                start_time = datetime.time(int(start_time_list[0]), int(start_time_list[1]), 0)
                end_time = datetime.time(int(end_time_list[0]), int(end_time_list[1]), 0)

            # Bắt đầu nhập
            broadcasting_status = BroadcastingStatus(
                date=fake.date_between_dates(date_start=datetime.date(year, 1, 1), date_end=None),
                power_T='500',
                power_PX='5000',
                reporter=self.generate_name(),
                status=u'Lỗi',
                broadcast=broadcasts_by_contract[random.randrange(0, len(broadcasts_by_contract), 1)]
            )
            broadcasting_status.save()

            TimeRange(
                type=math.floor(random.randrange(2, 4, 1)),
                start_time=start_time,
                end_time=end_time,
                broadcasting_status=broadcasting_status
            ).save()
            print(broadcasting_status)

    @staticmethod
    def generate_name():
        len_arr = len(NAMES) - 1
        first = NAMES[math.floor(random.randrange(0, len_arr, 1))]
        second = NAMES[math.floor(random.randrange(0, len_arr, 1))][0].upper()
        return u'{} {}.'.format(first, second)
