import sys
import json
import re

CREDUND = "\33[41m\33[4m"
BOLD = '\33[1m'
CEND = '\33[0m'


schedule = json.load(open('schedule.json'))


iteration = ['Abbreviature','CourseType','CourseTitle',
'CreditsUS','CreditsECTS','StartDate','EndDate',
'WeekDays','Time','Enr','Cap','Prof','Room']

course = input("Course:")

for index, value in enumerate(schedule): 
	if schedule[value]['Abbreviature'] == course or\
	schedule[value]['Abbreviature'].split(' ')[0] == course:
		for i in schedule[value]:
			if i=='CourseTitle' or i=='Prof':
				print(i+ " "+CREDUND+schedule[value][i]+CEND)
			elif i=='WeekDays':
				print(i+ " "+BOLD+schedule[value][i]+CEND)
			else:
				print(i+ "  " + schedule[value][i])
		print('\n')
