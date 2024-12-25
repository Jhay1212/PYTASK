class Task:
    def __init__(self, task, status):
        self._task = task
        self._status = status



    @property
    def task(self):
        return self._task   
    
    @property
    def status(self):
        return self._status
    
    @task.setter
    def task(self, value):
        self._task = value

    @status.setter
    def status(self, value):
        self._status = value

    def add(self):
        pass