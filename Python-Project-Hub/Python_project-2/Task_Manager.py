def task_manager():
    tasks = []
    print("__________Welcome TO Task Manager Center__________")

    # Adding initial tasks
    total_tasks = int(input("Enter How many Tasks Do you want to add: "))
    for i in range(total_tasks):
        task_name = input(f"Enter Your Task No.{i + 1}: ")
        tasks.append(task_name)
    
    print(f"Today's Tasks are:\n{tasks}")

    while True:
        print("\nSelect an operation:")
        try:
            operation = int(input("1: Add Task\n2: Update Task\n3: Delete Task\n4: View Tasks\n5: Exit: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue  # Ask again for a valid operation

        if operation == 1:
            add_task = input("Enter Your Task you want to add: ")
            tasks.append(add_task)
            print(f"Task '{add_task}' added.")

        elif operation == 2:
            task_to_update = input("Enter the Task you want to update: ")
            if task_to_update in tasks:
                updated_task = input("Enter Your Updated Task: ")
                index = tasks.index(task_to_update)
                tasks[index] = updated_task
                print(f"Updated Task: '{task_to_update}' to '{updated_task}'.")
            else:
                print(f"Task '{task_to_update}' not found.")

        elif operation == 3:
            task_to_delete = input("Enter the Task you want to delete: ")
            if task_to_delete in tasks:
                tasks.remove(task_to_delete)
                print(f"Task '{task_to_delete}' deleted.")
            else:
                print(f"Task '{task_to_delete}' not found.")

        elif operation == 4:
            print(f"Current Tasks: {tasks}")

        elif operation == 5:
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid operation. Please select a valid option (1-5).")

task_manager()
