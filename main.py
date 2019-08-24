import sys
import json
import re

CREDUND = "\33[41m\33[4m"
BOLD = '\33[1m'
CEND = '\33[0m'


schedule = json.load(open('schedule.json'))


iteration = ['Abbreviation','CourseType','CourseTitle',
'CreditsUS','CreditsECTS','StartDate','EndDate',
'WeekDays','Time','Enr','Cap','Prof','Room']

course = input("Course:")
Ctype = input("Course Type:")

for index, value in enumerate(schedule): 
	#course abb
	abb = schedule[value]['Abbreviation'].lower()
	course = course.lower()
	CourseType = schedule[value]['CourseType'].lower()
	Ctype = Ctype.lower()

	if (abb == course or\
	abb.split(' ')[0] == course):
		print(BOLD+30*'-' + CEND)
		for i in schedule[value]:
			print('',end='   ')
			if i=='CourseTitle' or i=='Prof':
				print(i+ " "+CREDUND+schedule[value][i]+CEND)
			elif i=='WeekDays' or i=='Time':
				print(i+ " "+BOLD+schedule[value][i]+CEND)

			else:
				print(i+ "  " + schedule[value][i])
		print('\n')
