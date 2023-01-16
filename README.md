# dfs

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
# task id
# liste des dépendances

<code>
class Task(object):
    def __init__(self, task_id, dependencies):
        self.dependencies = dependencies
        self.done = False
        self.task_id = task_id

    def run(self):
        self.done = True

class Scheduler(object):
    def __init__(self, tasks: List[Task]):
        self.tasks = tasks

    def run(self):
        

def test_question_three():
    task_one = Task(1, [])
    task_two = Task(2, [task_one])
    task_three = Task(3, [task_two])
    s = SchedulerRun([task_one,
                      task_two,
                      task_three])
    s.run()
</code>

