from crontab import CronTab

my_cron = CronTab(user='tbrody')

for job in my_cron:
    print(job)

job = my_cron.new(command='python /home/tbrody/test.py')
job.minute.every(1)
my_cron.write()

