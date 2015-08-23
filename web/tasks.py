import time

from background_task import background


@background(schedule=0)
def dbt_task(data):
    print "[START] django-background-tasks for: " + data.get("name","")
    time.sleep(10)
    print "[DONE] django-background-tasks for: " + data.get("name","")