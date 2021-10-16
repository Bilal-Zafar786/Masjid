from django.db import models

# Create your models here.
class Student_Registration(models.Model):
    roll_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    DOB = models.DateField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=30)
    addmission_date = models.DateField()
    promised_fee = models.IntegerField()
    class Meta:
        db_table = 'student_registration'

    def __str__(self):
        return str(self.roll_number)



class Student_Progress1(models.Model):
    roll_number = models.ForeignKey(Student_Registration,on_delete=models.CASCADE)
    print("Roll Number is: ",roll_number)
    name = models.CharField(max_length=300)
    month = models.DateField()

    def __str__(self):
        return self.roll_number.name

    def roll(self):
        return self.roll_number.name

    class Meta:
        db_table = 'student_progress1'

class Monthly_Fee(models.Model):
    roll_number = models.ForeignKey(Student_Registration, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    month = models.DateField()
    fee = models.IntegerField()
    discounted = models.BooleanField(default=False)

    class Meta:
        db_table = 'fee_record'

class Account_Record(models.Model):
    date = models.DateField()
    total_income = models.IntegerField()
    total_expense = models.IntegerField()
    remaining = models.IntegerField()

    class Meta:
        db_table = 'account_record'
