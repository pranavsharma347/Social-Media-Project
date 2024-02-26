Here we are creating a project  user get all posts using facebook graphql api,send the post in facebook using celery and provide analytics of facebook page using facebookgraph api

1.click on Home on navbar =>we get all posts facebook
2.click on PostReschddule on navbar =>In the form we provide time and date to send post using celery ahd provide message go to celery.py in args
3.click on Facebook Page analytics on navbar =>we get the analytics of facebook Page



Before using an application first activate the python environment Desktop/socialmedia$ source socialmediaenv/bin/activate
For running celery run both command in different terminal after activate the python environment /Desktop/socialmedia/socialmediaproject$ celery -A socialmediaproject worker --loglevel=INFO
and /Desktop/socialmedia/socialmediaproject$ celery -A socialmediaproject beat --loglevel=INFO

I did not get Instagram data beacuse they does not give permission to make a test app.Without test app we can use its api.

Python version =>3.8.10

Required packages for run this application ==>

amqp==5.2.0
asgiref==3.7.2
async-timeout==4.0.3
backports.zoneinfo==0.2.1
billiard==4.2.0
celery==5.3.6
certifi==2024.2.2
charset-normalizer==3.3.2
click==8.1.7
click-didyoumean==0.3.0
click-plugins==1.1.1
click-repl==0.3.0
cron-descriptor==1.4.3
Django==4.2.10
django-admin==2.0.2
django-celery-beat==2.5.0
django-celery-results==2.5.1
django-excel-response2==3.0.6
django-six==1.0.5
django-timezone-field==6.1.0
excel-base==1.0.4
facebook-sdk==3.1.0
idna==3.6
isoweek==1.3.3
kombu==5.3.5
prompt-toolkit==3.0.43
python-crontab==3.0.0
python-dateutil==2.8.2
redis==5.0.1
requests==2.31.0
screen==1.0.1
six==1.16.0
sqlparse==0.4.4
TimeConvert==3.0.13
typing_extensions==4.9.0
tzdata==2024.1
tzlocal==5.2
urllib3==2.2.1
vine==5.1.0
wcwidth==0.2.13
xlwt==1.3.0

