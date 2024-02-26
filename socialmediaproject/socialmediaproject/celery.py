import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','socialmediaproject.settings')
app=Celery('socialmediaproject')
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings')


app.conf.beat_schedule={
"share":{
'task':'socialmediaapp.task.post_on_facebook',#note this task specify in task.py
'schedule':10.0,#means 5 seconds
"args": ["this is pranav page"],

}
}
app.conf.beat_scheduler='django_celery_beat.schedulers.DatabaseScheduler'


app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'request:{self.request!r}')
