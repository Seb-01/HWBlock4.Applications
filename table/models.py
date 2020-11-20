from django.db import models

# Create your models here.
class Table(models.Model):
    # имя
    name=models.CharField(max_length=50, unique=True)
    # width col
    col_width=models.IntegerField(default=5)
    # number
    serial_num=models.IntegerField(null=False)

    def __str__(self):
        return self.name

class CsvPath(models.Model):

    # путь к csv-файлу
    path=models.TextField(default='')


    def get_path(self):

        res=CsvPath.objects.first()
        return res.path


    def set_path(self, new_path_name):
        self.path=new_path_name
        super().save()

    def __str__(self):
        return self.path

