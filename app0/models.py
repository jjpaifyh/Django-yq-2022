from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle=models.CharField(max_length=50)
    bpub_date=models.DateField()
    bread=models.IntegerField()
    bcomnt=models.IntegerField()
    isDelete=models.BooleanField(default=False)

print('1')