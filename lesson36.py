class Jira:

    def __init__(self, ticket_number, creation_date):
        self.ticket_number = ticket_number
        self.creation_date = creation_date


class TaskType(Jira):

    def __init__(self, ticket_name, ticket_number, creation_date, ticket_type,
                 status='To do', ticket_author=None, ticket_executor=None, comment_after_closing=None):
        super().__init__(ticket_number, creation_date)
        self.ticket_name = ticket_name
        self.ticket_author = ticket_author
        self.ticket_executor = ticket_executor
        self.ticket_type = ticket_type
        self.statuts = status
        self.comment_after_closing = comment_after_closing

    def get_task_status(self):
        return self.status

    def set_task_status(self, new_status):
        self.status = new_status

    def set_executor_to_task(self, user_role):
        self.ticket_executor = user_role.last_name

    def __str__(self):
        return (f'Task: {self.ticket_name}, Type: {self.ticket_type}, Status: {self.status}, Author: {self.ticket_author}, '
                f'Executor: {self.ticket_executor}, Comment: {self.comment_after_closing}')


class User:

    def __init__(self, first_name, last_name, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id


class UserRole(User):
    def __init__(self, first_name, last_name, user_id, user_role):
        super().__init__(first_name, last_name, user_id)
        self.user_role = user_role
        self.tasks = []

    def create_task(self, ticket_name, ticket_number, creation_date, ticket_type):
        task = TaskType(ticket_name, ticket_number, creation_date, ticket_type, ticket_author=self.last_name)
        return task

    def take_task_in_progress(self, task):
        task.status = 'In Progress'
        task.ticket_executor = self.last_name
        self.tasks.append(task)

    def closing_task(self, task):
        task.status = 'Closed'
        task.comment_after_closing = input('Comment: ')
        self.tasks.remove(task)

    def __str__(self):
        task_string = ""
        for i in self.tasks:
            task_string += f'{str(i)}\n'
        return f"{self.last_name} {self.first_name}: \n{task_string}"



ruslan = UserRole('Ruslan', 'Zaslotskyi', 1, 'Developer')
nastya = UserRole('Anastasiia', 'Vaskina', 2, 'Business Analyst')
bug_1 = nastya.create_task("Bug1", 1, "03.06.2024", 'Bug')
improve_1 = nastya.create_task("Improvement1", 2, "03.06.2024", 'Improvement')
print(bug_1)
ruslan.take_task_in_progress(bug_1)
print(bug_1)
bug_1.set_task_status('Ready for Development')
print(bug_1)
print(ruslan)
