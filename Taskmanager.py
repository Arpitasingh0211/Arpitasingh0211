def task():
    tasks = []
    print("-----Welcome to Task Manager App-----")

    total_task = int(input("Enter how many task you want to do = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's task are...\n{tasks} ")  

    while True:
        operations = int(input("If you want to change something in task then ENTER---\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))  
        if(operations == 1):
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif(operations == 2):
            update = input("Enter the task name you want to update = ")
            if update in tasks:
                up = input("Enter the new task = ")
                ind = tasks.index(update)
                tasks[ind] = up
                print(f"Updated the Task {up}")

        elif(operations == 3):
            del_val = input("Enter the task you want to Delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted")

        elif(operations == 4):
            print(f"These are the task....\n{tasks} ")  

        elif(operations == 5):
            print("Closing the program.....")    
            break      
        
        else:
            print("Invalid Input")

task()
