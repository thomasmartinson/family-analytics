from datetime import date, timedelta
import json

DAYS_IN_YEAR = 365.24

today = date.today()

with open('template.json') as f:
    bdays = json.load(f)
    
# print ages
for person in bdays:
    bday = date.fromisoformat(bdays[person])
    print('{:>9}: {:5.2f} years old'.format(person, (today - bday).days / DAYS_IN_YEAR))

# store ages
ages_in_days = [(today - date.fromisoformat(i)).days for i in bdays.values()]

# avg age difference
total_days = 0
total_diffs = 0
for i in range(len(ages_in_days)):
    for j in range(i+1, len(ages_in_days)):
        total_days += abs(ages_in_days[i] - ages_in_days[j])
        total_diffs += 1
print("avg age difference: {:.2f} years".format((total_days / total_diffs) / DAYS_IN_YEAR))

# avg adj age difference
print('avg adjacent age diff: {:.2f} years'.format((ages_in_days[0] - ages_in_days[-1]) / (DAYS_IN_YEAR * (len(bdays) - 1))))

# avg birthdate
avg_age = sum(ages_in_days) / len(ages_in_days)
print("avg age: {:.2f} years old".format(avg_age / DAYS_IN_YEAR))
print("avg birthday: {}".format(today - timedelta(days=avg_age)))

# avg calendar birthday
total_days = sum([(today - date.fromisoformat('2019{}'.format(i[4:]))).days for i in bdays.values()])
avg_days = total_days / len(bdays)
avg_cal_date = today - timedelta(days=avg_days)
print("avg calendar date: {}".format(avg_cal_date.strftime('%m-%d'))) 

