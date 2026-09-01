
print(r"""
  _____       ____          _     _     _   
 |_   _|__   |  _ \  ___   | |   (_)___| |_ 
   | |/ _ \  | | | |/ _ \  | |   | / __| __|
   | | (_) | | |_| | (_) | | |___| \__ \ |_ 
   |_|\___/  |____/ \___/  |_____|_|___/\__|
                                            


""")

List = []
while True:
    print(r"""
    [1] Add task
    [2] View tasks
    [3] Remove task
    [4] Exit
    
    Choose an option:
    
    """)

    choice = int(input("Enter your choice: "))
    if choice == 1:
        t = input("Enter your task: ")
        List.append(t)
    elif choice == 2:
        print(List)
    elif choice == 3:
        print(List)
        di = int(input("Enter the number of the task (Starting from 0): "))
        List.pop(di)
    else:
        break


