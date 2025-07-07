from datetime import datetime
taskList = []

def viewTask():
    for index,task in enumerate(taskList,start=1):
        string = f"{index}. Task Title: {task['Title']} | Task Due Date: {task['DueDate']}"
        if task['Status']:
            string += "| Task Status: Done"
        else:
            string += "| Task Status: Not Done"
        print(string)
    print("-------------------")

def get_completed_tasks(): #created a pure function instead of printing everything inside a function
    tempList = []
    for task in taskList:
        if(task['Status'] == True):
            tempList.append(task)
    return tempList        


def add_Task(title='',dueDate='',completeStatus = False):
    if(title == '' or dueDate == ''):
        print("Please Enter Valid Data")
        return

    tempList = {"Title": title,"DueDate": dueDate,"Status": completeStatus}
    taskList.append(tempList)

def mark_task_done(taskIndex):
    if checkTaskIndex(taskIndex) is False:
        return
    
    task = taskList[taskIndex-1]
    task['Status'] = True

def delete_task(taskIndex):
    if checkTaskIndex(taskIndex) is False:
        return
    taskList.pop(taskIndex -1)
    print(f"Task {taskIndex} deleted successfully")

def checkTaskIndex(taskIndex):
    lengthTaskList = len(taskList)
    if taskIndex <= 0 or taskIndex > len(taskList):
        print(f"Provide Valid Index Between 1 and {lengthTaskList}")
        return False
    return True


add_Task('add new task','11/12/25',True)
add_Task('','',True)
add_Task('2','',True)
add_Task('add new task','11/12/25',True)
add_Task('add new task','11/12/25',False)
add_Task('add new task','11/12/25',False)
add_Task('add new task','11/12/25',False)
viewTask()
mark_task_done(3)
viewTask()
delete_task(3)
viewTask()
print(get_completed_tasks())