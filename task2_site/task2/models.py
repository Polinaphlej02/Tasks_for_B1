from django.db import models


class ExcelFiles(models.Model):
    id_file = models.AutoField(primary_key=True)
    excel_file = models.FileField(upload_to='media/', null=True)


class ClassTable(models.Model):
    id_class = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=150)


class BankAccount2(models.Model):
    id_bsch_2 = models.SmallIntegerField(primary_key=True)
    id_class = models.ForeignKey(ClassTable, on_delete=models.CASCADE)


class BankAccount4(models.Model):
    id_bsch_4 = models.AutoField(primary_key=True)
    bsch_ch = models.SmallIntegerField()
    id_bsch_2 = models.ForeignKey(BankAccount2, on_delete=models.CASCADE)


class Turnover(models.Model):
    id_bsch_4 = models.ForeignKey(BankAccount4, on_delete=models.CASCADE, primary_key=True)
    assets = models.FloatField()
    liabilities = models.FloatField()


class OpeningBalance(models.Model):
    id_bsch_4 = models.ForeignKey(BankAccount4, on_delete=models.CASCADE, primary_key=True)
    debit = models.FloatField()
    credit = models.FloatField()


