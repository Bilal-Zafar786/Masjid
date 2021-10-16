from django.contrib import admin
from .models import Student_Registration,Student_Progress1,Monthly_Fee,Account_Record

class StudentRegistrationAdmin(admin.ModelAdmin):
	list_display=('roll_number','name','father_name','DOB','address','phone','addmission_date','promised_fee')
	list_editable = ('phone','promised_fee')
admin.site.register(Student_Registration,StudentRegistrationAdmin)

class Student_Progress1Admin(admin.ModelAdmin):
	list_display = ('roll','name','month')
admin.site.register(Student_Progress1,Student_Progress1Admin)


class Monthly_FeeAdmin(admin.ModelAdmin):
	list_display = ('roll_number','name','month','fee','discounted')
	list_editable = ('fee',)
admin.site.register(Monthly_Fee,Monthly_FeeAdmin)

# class Account_RecordAdmin(admin.ModelAdmin):
# 	list_display = ('date','total_income','total_expense','remaining')
# 	# list_editable = ('date','total_income','total_expense','remaining')
admin.site.register(Account_Record)

