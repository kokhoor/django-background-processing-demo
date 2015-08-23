import time


def rq_task(data):
    print "[START] rq for: " + data.get("name","")
    time.sleep(10)
    print "[DONE] rq for: " + data.get("name","")