import os
import sanitize
import getCoachData
os.chdir('D:/Python/python-git/begginger/2017-03-09/Program')

james=getCoachData.get_coach_data('james.txt')
julie=getCoachData.get_coach_data('julie.txt')
mikey=getCoachData.get_coach_data('mikey.txt')
sarah=getCoachData.get_coach_data('sarah.txt')


print(sorted(set([sanitize.sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize.sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize.sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize.sanitize(t) for t in sarah]))[0:3])