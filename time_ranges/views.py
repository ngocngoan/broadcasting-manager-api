from datetime import datetime

from django.db import connection
from django.db.models.aggregates import Sum
from django.db.models import DurationField, ExpressionWrapper, F
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend

from time_ranges.models import TimeRange
from time_ranges.serializers import TimeRangeSerializers, TimeRangeMonthlyReportSerializers, TimeRangeBillSerializers


class TimeRangeList(generics.ListCreateAPIView):
    queryset = TimeRange.objects.all().order_by('-id')
    serializer_class = TimeRangeSerializers
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('broadcasting_status',)
    filter_fields = ('broadcasting_status',)


class TimeRangeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeRange.objects.all().order_by('-id')
    serializer_class = TimeRangeSerializers
    renderer_classes = (JSONRenderer,)


@api_view(['GET'])
def time_range_by_month(request, *args, **kwargs):
    month = int(kwargs['month'])
    if month > 12:
        return

    year = int(kwargs['year'])
    response = TimeRange.objects \
        .filter(broadcasting_status__date__month=month, broadcasting_status__date__year=year,
                broadcasting_status__broadcast__is_by_region=False) \
        .values('broadcasting_status__broadcast__station_id', 'broadcasting_status__broadcast_id', 'type') \
        .annotate(duration=Sum(ExpressionWrapper(F('end_time') - F('start_time'), output_field=DurationField()))) \
        .order_by('broadcasting_status__broadcast__name', 'broadcasting_status__broadcast__station_id', 'type')
    return Response(list(response))


class TimeRangeByMonthReport(generics.ListAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = TimeRangeMonthlyReportSerializers

    def get_queryset(self):
        month = int(self.kwargs['month'])
        if month > 12:
            return

        year = int(self.kwargs['year'])
        query_set = TimeRange.objects \
            .filter(broadcasting_status__date__month=month, broadcasting_status__date__year=year,
                    broadcasting_status__broadcast__is_by_region=False) \
            .values('broadcasting_status__broadcast_id') \
            .annotate(duration=Sum(ExpressionWrapper(F('end_time') - F('start_time'), output_field=DurationField()))) \
            .order_by('broadcasting_status__broadcast__name', 'broadcasting_status__broadcast__station_id', 'type')
        # query_set = query_set.prefetch_related('broadcast', 'broadcast__status', 'broadcast__status__time_range')
        return query_set


class TimeRangeReport(generics.ListAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = TimeRangeMonthlyReportSerializers

    def get_queryset(self):
        start_date_param = self.request.query_params.get('date_gte', None)
        end_date_param = self.request.query_params.get('date_lte', None)
        by_region = self.request.query_params.get('is_by_region', None)

        if start_date_param is None and end_date_param is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if by_region == 'True' or by_region == 'true':
            is_by_region = True
        else:
            is_by_region = False

        start_date = datetime.strptime(start_date_param, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_param, '%Y-%m-%d').date()

        query_set = TimeRange.objects \
            .filter(broadcasting_status__date__range=(start_date, end_date),
                    broadcasting_status__broadcast__is_by_region=is_by_region) \
            .values('broadcasting_status__broadcast_id', 'type') \
            .annotate(duration=Sum(ExpressionWrapper(F('end_time') - F('start_time'), output_field=DurationField()))) \
            .order_by('broadcasting_status__broadcast__name', 'broadcasting_status__broadcast__station_id', 'type')
        return query_set


def dict_fetch_all(cursor):
    """
    Return all rows from a cursor as a dict
    :param cursor:
    :return list:
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class TimeRangeBillReport(generics.ListAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = TimeRangeBillSerializers

    def get_queryset(self):
        date_gte = self.request.query_params.get('date_gte', None)
        date_lte = self.request.query_params.get('date_lte', None)
        tax = self.request.query_params.get('tax', None)

        sql = "select televisions.id as television_id, broadcasts.id AS broadcast_id, contracts.id as contract_id, " +\
              "unit_prices.id as unit_price_id, time_ranges.type, sum(end_time - start_time) as duration " +\
              "from televisions " +\
              "inner join stations on televisions.id = stations.television_id " +\
              "inner join broadcasts on stations.id = broadcasts.station_id " +\
              "inner join contracts on broadcasts.id = contracts.broadcast_id " +\
              "inner join unit_prices on contracts.unit_price_id = unit_prices.id " +\
              "join broadcasting_status on broadcasts.id = broadcasting_status.broadcast_id " +\
              "join time_ranges on broadcasting_status.id = time_ranges.broadcasting_status_id " +\
              "where tax = %s " +\
              "and broadcasts.contract_start_date <= %s " +\
              "and broadcasts.contract_end_date >= %s " +\
              "and broadcasting_status.date BETWEEN %s and %s " +\
              "group by televisions.id, broadcasts.id, contracts.id, unit_prices.id, time_ranges.type " +\
              "order by televisions.id, broadcasts.id, contracts.id, unit_prices.id, time_ranges.type"

        with connection.cursor() as cursor:
            cursor.execute(sql, [tax, date_gte, date_lte, date_gte, date_lte])
            rows = dict_fetch_all(cursor)

        if len(rows) == 0:
            return []

        bills = []
        idx = 0
        tel_id = rows[0]["television_id"]

        for i in range(0, len(rows)):
            if len(bills) == 0:
                bills.append({
                    "television": rows[i]["television_id"],
                    "payments": [{
                        "broadcast": rows[i]["broadcast_id"],
                        "contract": rows[i]["contract_id"],
                        "unit_price": rows[i]["unit_price_id"],
                        "duration": rows[i]["duration"],
                    }]})
                continue
            elif tel_id == rows[i]["television_id"] and rows[i]["type"] == 4:
                continue
            elif tel_id == rows[i]["television_id"] and rows[i]["type"] == 1:
                bills[idx]["payments"].append({
                    "broadcast": rows[i]["broadcast_id"],
                    "contract": rows[i]["contract_id"],
                    "unit_price": rows[i]["unit_price_id"],
                    "duration": rows[i]["duration"],
                })
            elif tel_id == rows[i]["television_id"] and rows[i]["type"] == 2 or rows[i]["type"] == 3:
                payments_len = len(bills[idx]["payments"])
                bills[idx]["payments"][payments_len - 1]["duration"] -= rows[i]["duration"]
            else:
                tel_id = rows[i]["television_id"]
                idx += 1
                bills.append({
                    "television": rows[i]["television_id"],
                    "payments": [{
                        "broadcast": rows[i]["broadcast_id"],
                        "contract": rows[i]["contract_id"],
                        "unit_price": rows[i]["unit_price_id"],
                        "duration": rows[i]["duration"],
                    }]})

        return bills

