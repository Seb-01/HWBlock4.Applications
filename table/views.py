import csv

from django.shortcuts import render
from table.models import Table, CsvPath


def table_view(request):
    template = 'table.html'

    #в БД есть запись о пути к csv-файлу
    path=CsvPath()
    file_name=path.get_path()

    # загружаем из БД настройки полей для выводимой таблицы
    columns=list(Table.objects.order_by('serial_num').values('name','col_width'))

    with open(file_name, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:

                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': columns,
            'table': table,
            'csv_file': file_name
        }
        result = render(request, template, context)
    return result
