import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="", # add your pw
    database="" # add your Database name
)

cursor = db.cursor()

def addTask(task, time, Date):
    """
    add a new task to the Database/Table
    """

    date = f"{Date[0]}-{Date[1]}"
    cursor.execute("INSERT INTO Tasks (date, time, task) VALUES (%s, %s, %s)", (date, time, task))
    db.commit()
    cursor.execute("SELECT * FROM Tasks")

def getTaskofDay(DATE):
    """
    get the tasks of the day DATE
    """

    cursor.execute("SELECT * FROM Tasks ORDER BY ID DESC")

    List = cursor.fetchall()
    list3 = []
    for i in List:
        list2 = []
        list2.append(i[0])
        list2.append(i[1])
        list2.append(i[2])
        list2.append(i[3])
        list3.append(list2)

    List = list3
    newList = []
    check = []

    for i in List:
        try:
            check = []
            for x in newList:
                check.append(x[0])
        except:
            pass
        try:
            if i[0] not in check:
                newList.append(i)
        except:
            newList.append(i)

    tasks = []

    for i in newList:
        if i[1] == DATE:
            task_save = []
            task_save.append(i[0])
            task_save.append(i[2])
            tasks.append(task_save)
    return tasks