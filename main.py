import sys
f = open('main.txt')


schedule = {}
iteration = ['Abbreviature','CourseType','CourseTitle',
'CreditsUS','CreditsECTS','StartDate','EndDate','WeekDays',
'Time','Enr','Cap','Prof','Room']


i = 0
counter = 0
abb = ""

for line in f:
	if i == 0:
		schedule[counter] = {}
	schedule[counter][iteration[i]] = line

	i = i + 1
	if i==13:
		i=0
		counter = counter+1


