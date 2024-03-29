from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')


@app.task
def add(x, y):
    return x + y


add.delay(4, 4)
