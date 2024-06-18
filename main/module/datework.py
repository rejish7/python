import datetime
jobs =[
{'title':'Quality Assurance','company':'microsoft','exp_date':'2024-02-23'},
{'title':'Software Developer','company':'google','exp_date':'2025-02-23'},
{'title':'Data scientist','company':'TCS','exp_date':'2026-02-23'},
{'title':'Data Analyst','company':'Facebook','exp_date':'2023-02-23'}
]
    


for job in jobs:
    exp_date = datetime.datetime.strptime(job['exp_date'],"%Y-%m-%d")
    today  = datetime.datetime.now()
    if exp_date< today:
        exp_date = today- exp_date
        print(f"{job['title']} jobs in {job['company']} is expired {exp_date.days} days ago")
    else:
        active_days = exp_date-today
        print(f"{job['title']} jobs in {job['company']}{active_days} is active")
