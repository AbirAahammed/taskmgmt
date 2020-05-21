task = {
    'NOT_STARTED': 'NOT_STARTED',
    'STARTED': 'STARTED',
    'HALTED': 'HALTED',
    'COMPLETED': 'COMPLETED'
}

"""
    Create a task object with.
    Parameter : 
        compulsory : taskname
        optional : taskDetails, start, end, 
"""
class Task:

    def __init__(self, taskName, isSubTask, taskDetails='', taskinterval=0, start=None, end=None):
        self._taskName = taskName
        self.taskDetails = taskDetails
        self._taskinterval = taskinterval
        self._start = start
        self._end = end
        self._status = task['NOT_STARTED']
        self._subTask = []
        self.isSubTask = isSubTask
    """
    Start a task that just has been created.
    parameter : takes no parameter.
    """
    def startTask(self):
        self._status = task['STARTED']

    def haltTask(self):
        self._status = task['HALTED']

    def completeTask(self):
        self._status = task['COMPLETED']
    
    def addSubTask(self, subTask):
        subTask.isSubTask = True
        self._subTask.append(subTask)
