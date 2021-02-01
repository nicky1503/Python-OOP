
class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        task_list = [task for task in self.tasks if task.name == task_name]
        if not task_list:
            return f"Could not find task with the name {task_name}"
        task_list[0].completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks = [task for task in self.tasks if task.completed]
        self.tasks = [task for task in self.tasks if not task.completed]
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += task.details() + "\n"
        return result

