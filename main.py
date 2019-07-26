import sys
f = open('schedule.txt')


schedule = {}
iteration = ['Abbreviature','CourseType','CourseTitle',
'CreditsUS','CreditsECTS','StartDate','EndDate','WeekDays',
'Time','Enr','Cap','Prof','Room']


i = 0
counter = 0
abb = ""

for line in f:
	line = line.strip('\n')
	if i == 0:
		schedule[counter] = {}
	
	schedule[counter][iteration[i]] = line

	i = i + 1
	if i==13:
		i=0
		counter = counter+1

course = input()
for index, value in enumerate(schedule): 
	if schedule[value]['Abbreviature'] == course or schedule[value]['Abbreviature'] == " "+course:
		for i in schedule[value]:
			print(i+ "  " + schedule[value][i])
		print('\n')