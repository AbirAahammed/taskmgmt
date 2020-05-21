import task
def main():
    task1 = task.Task('Fist task', False, 'This is the first task')
    subtask1_1 = task.Task('subtask1_1 task', True, 'This is the first sub task')
    task1.addSubTask(subtask1_1)
    subtask1_1.taskDetails = 'Changed'
    print(task1)

if __name__ == "__main__":
    main()