class Task(object):
    def __init__(self, task_id, dependencies):
        self.dependencies = dependencies
        self.done = False
        self.task_id = task_id
    def run(self):
        self.done = True

class Scheduler(object):
    def __init__(self, tasks):
        self.tasks = tasks

    def run(self):
        tasks_to_run = self.tasks.copy()
        while tasks_to_run:
            for task in tasks_to_run:
                print (task.task_id)
                if all(dependency.done for dependency in task.dependencies):
                     task.run()
                     tasks_to_run.remove(task)
                     break
        print("All tasks have been completed.")


def test_question_four():
    task_one = Task(1, [])
    task_two = Task(2, [task_one])
    task_four = Task(4, [task_two])
    task_three = Task(3, [task_four])
    s = Scheduler([   task_one,
                      task_two,
                      task_three,
                      task_four])
    s.run()

test_question_four()