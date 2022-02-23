from tkinter import *
import database

class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title('Daily Planner')

        self.window_width = 650
        self.window_height = 550

        # get the screen dimension
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # find the center point
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')

        # add Labels for the day
        # Time
        self.myLabel_title_border = Label(self.root, borderwidth=2, relief="ridge", height=35, width=15, bg="white").place(x=30, y=3)

        self.myLabel_title = Label(self.root, text="Time", font="bold", bg="white").place(x=50, y=10)

        self.time_0 = Label(self.root, text="0-1", bg="white").place(x=50, y=40)
        self.time_1 = Label(self.root, text="1-2", bg="white").place(x=50, y=60)
        self.time_2 = Label(self.root, text="2-3", bg="white").place(x=50, y=80)
        self.time_3 = Label(self.root, text="3-4", bg="white").place(x=50, y=100)
        self.time_4 = Label(self.root, text="4-5", bg="white").place(x=50, y=120)
        self.time_5 = Label(self.root, text="5-6", bg="white").place(x=50, y=140)
        self.time_6 = Label(self.root, text="6-7", bg="white").place(x=50, y=160)
        self.time_7 = Label(self.root, text="7-8", bg="white").place(x=50, y=180)
        self.time_8 = Label(self.root, text="8-9", bg="white").place(x=50, y=200)
        self.time_9 = Label(self.root, text="9-10", bg="white").place(x=50, y=220)
        self.time_10 = Label(self.root, text="10-11", bg="white").place(x=50, y=240)
        self.time_11 = Label(self.root, text="11-12", bg="white").place(x=50, y=260)
        self.time_12 = Label(self.root, text="12-13", bg="white").place(x=50, y=280)
        self.time_13 = Label(self.root, text="13-14", bg="white").place(x=50, y=300)
        self.time_14 = Label(self.root, text="14-15", bg="white").place(x=50, y=320)
        self.time_15 = Label(self.root, text="15-16", bg="white").place(x=50, y=340)
        self.time_16 = Label(self.root, text="16-17", bg="white").place(x=50, y=360)
        self.time_17 = Label(self.root, text="17-18", bg="white").place(x=50, y=380)
        self.time_18 = Label(self.root, text="18-19", bg="white").place(x=50, y=400)
        self.time_19 = Label(self.root, text="19-20", bg="white").place(x=50, y=420)
        self.time_20 = Label(self.root, text="20-21", bg="white").place(x=50, y=440)
        self.time_21 = Label(self.root, text="21-22", bg="white").place(x=50, y=460)
        self.time_22 = Label(self.root, text="22-23", bg="white").place(x=50, y=480)
        self.time_23 = Label(self.root, text="23-24", bg="white").place(x=50, y=500)

        # Task
        self.myLabel_task_border = Label(self.root, borderwidth=2, relief="ridge", height=35, width=15, bg="white").place(x=180, y=3)

        self.myLabel_title_2 = Label(self.root, text="Task", font="bold", bg="white").place(x=200, y=10)

        self.task_0 = StringVar()
        self.task_1 = StringVar()
        self.task_2 = StringVar()
        self.task_3 = StringVar()
        self.task_4 = StringVar()
        self.task_5 = StringVar()
        self.task_6 = StringVar()
        self.task_7 = StringVar()
        self.task_8 = StringVar()
        self.task_9 = StringVar()
        self.task_10 = StringVar()
        self.task_11 = StringVar()
        self.task_12 = StringVar()
        self.task_13 = StringVar()
        self.task_14 = StringVar()
        self.task_15 = StringVar()
        self.task_16 = StringVar()
        self.task_17 = StringVar()
        self.task_18 = StringVar()
        self.task_19 = StringVar()
        self.task_20 = StringVar()
        self.task_21 = StringVar()
        self.task_22 = StringVar()
        self.task_23 = StringVar()

        self.list_Task = [self.task_0, self.task_1, self.task_2, self.task_3, self.task_4, self.task_5, self.task_6, self.task_7, self.task_8, self.task_9,
                          self.task_10, self.task_11, self.task_12, self.task_13, self.task_14, self.task_15, self.task_16, self.task_17, self.task_18,
                          self.task_19, self.task_20, self.task_21, self.task_22, self.task_23]


        self.show_task_0 = Label(self.root, textvariable=self.task_0, bg="white").place(x=200, y=40)
        self.show_task_1 = Label(self.root, textvariable=self.task_1, bg="white").place(x=200, y=60)
        self.show_task_2 = Label(self.root, textvariable=self.task_2, bg="white").place(x=200, y=80)
        self.show_task_3 = Label(self.root, textvariable=self.task_3, bg="white").place(x=200, y=100)
        self.show_task_4 = Label(self.root, textvariable=self.task_4, bg="white").place(x=200, y=120)
        self.show_task_5 = Label(self.root, textvariable=self.task_5, bg="white").place(x=200, y=140)
        self.show_task_6 = Label(self.root, textvariable=self.task_6, bg="white").place(x=200, y=160)
        self.show_task_7 = Label(self.root, textvariable=self.task_7, bg="white").place(x=200, y=180)
        self.show_task_8 = Label(self.root, textvariable=self.task_8, bg="white").place(x=200, y=200)
        self.show_task_9 = Label(self.root, textvariable=self.task_9, bg="white").place(x=200, y=220)
        self.show_task_10 = Label(self.root, textvariable=self.task_10, bg="white").place(x=200, y=240)
        self.show_task_11 = Label(self.root, textvariable=self.task_11, bg="white").place(x=200, y=260)
        self.show_task_12 = Label(self.root, textvariable=self.task_12, bg="white").place(x=200, y=280)
        self.show_task_13 = Label(self.root, textvariable=self.task_13, bg="white").place(x=200, y=300)
        self.show_task_14 = Label(self.root, textvariable=self.task_14, bg="white").place(x=200, y=320)
        self.show_task_15 = Label(self.root, textvariable=self.task_15, bg="white").place(x=200, y=340)
        self.show_task_16 = Label(self.root, textvariable=self.task_16, bg="white").place(x=200, y=360)
        self.show_task_17 = Label(self.root, textvariable=self.task_17, bg="white").place(x=200, y=380)
        self.show_task_18 = Label(self.root, textvariable=self.task_18, bg="white").place(x=200, y=400)
        self.show_task_19 = Label(self.root, textvariable=self.task_19, bg="white").place(x=200, y=420)
        self.show_task_20 = Label(self.root, textvariable=self.task_20, bg="white").place(x=200, y=440)
        self.show_task_21 = Label(self.root, textvariable=self.task_21, bg="white").place(x=200, y=460)
        self.show_task_22 = Label(self.root, textvariable=self.task_22, bg="white").place(x=200, y=480)
        self.show_task_23 = Label(self.root, textvariable=self.task_23, bg="white").place(x=200, y=500)

        # add a task
        self.myLabel_new_task_border = Label(self.root, borderwidth=2, relief="ridge", height=5, width=41, bg="#2C3333").place(x=322, y=3)

        self.new_task_date = Entry(self.root, width=20, borderwidth=2, relief="ridge")
        self.new_task_date.insert(0, "Enter a day")
        self.new_task_date.place(x=330, y=10)

        self.new_task_time = Entry(self.root, width=20, borderwidth=2, relief="ridge")
        self.new_task_time.insert(0, "Enter a time")
        self.new_task_time.place(x=480, y=10)

        self.new_task = Entry(self.root, width=20, borderwidth=2, relief="ridge")
        self.new_task.insert(0, "Enter a task")
        self.new_task.place(x=330, y=50)

        self.new_task_submit = Button(self.root, text="Submit", borderwidth=2, relief="ridge", bg="#141E27", fg="white", command=self.add_task)
        self.new_task_submit.place(x=520, y=45)

        # get day input
        self.myLabel_date_border = Label(self.root, borderwidth=2, relief="ridge", height=5, width=41, bg="#2C3333").place(x=322, y=100)

        # show date
        self.date = StringVar()
        self.date.set(f"current date: ")
        self.show_date = Label(self.root, borderwidth=2, relief="ridge", bg="white", fg="black", textvariable=self.date)
        self.show_date.place(x=330, y=140)
        self.show_date.pack_forget()

        self.date_field = Entry(self.root, width=20, borderwidth=2, relief="ridge")
        self.date_field.insert(0, "Enter a day")
        self.date_field.place(x=330, y=110)

        self.btn_date_input = Button(self.root, text="Select Date", borderwidth=2, relief="ridge", bg="#141E27", fg="white", command=self.get_user_date)
        self.btn_date_input.place(x=480, y=108)

        self.root.mainloop()


    def check_time(self, time_input):
        """
        analyze if time is a real time or if the user selected a wrong time
        """

        if len(time_input) < 2:
            return False

        if int(time_input[0]) > 23 or int(time_input[1]) > 24:
            return False

        if int(time_input[0]) != int(time_input[1])-1:
            return False
        return True


    def check_date(self, date_input):
        """
        analyze if date is a real date or if the user selected a wrong date
        """

        self.new_data_input = []
        for i in date_input:
            if i != ".":
                self.new_data_input.append(i)

        # only numbers
        for i in self.new_data_input:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return False

        # day
        if int(self.new_data_input[2]) == 0 and int(self.new_data_input[3]) in [1, 3, 5, 7, 8] or int(self.new_data_input[2]) == 1 and int(self.new_data_input[3]) in [0, 2]:
            if int(self.new_data_input[0]) == 3 and int(self.new_data_input[1]) > 1 or int(self.new_data_input[0]) > 3:
                return False

        elif int(self.new_data_input[2]) == 0 and int(self.new_data_input[3]) in [4, 6, 9] or int(self.new_data_input[2]) == 1 and int(self.new_data_input[3]) == 1:
            if int(self.new_data_input[0]) == 3 and int(self.new_data_input[1]) > 0 or int(self.new_data_input[0]) > 3:
                return False

        elif int(self.new_data_input[2]) == 0 and int(self.new_data_input[3]) == 2:
            if int(self.new_data_input[0]) == 2 and int(self.new_data_input[1]) > 8 or int(self.new_data_input[0]) > 2:
                return False

        # month
        if int(self.new_data_input[2]) == 0 and int(self.new_data_input[3]) == 0 or int(self.new_data_input[2]) >= 1 and int(self.new_data_input[3]) > 2 or int(self.new_data_input[2]) > 1:
            return False

        # year
        if int(self.new_data_input[4]) < 2 or int(self.new_data_input[5]) < 0 or int(self.new_data_input[6]) < 2 or int(self.new_data_input[7]) < 2:
            return False
        return True


    def add_task(self):
        """
        user can add a new task
        """
        self.date_input = self.new_task_date.get()
        self.real_date = self.check_date(self.date_input)
        self.task = self.new_task.get()

        self.time_input = self.new_task_time.get().split("-")
        self.real_time = self.check_time(self.time_input)
        if self.real_date != False and self.real_time != False:
            database.addTask(self.task, self.date_input, self.time_input)


    def show_task(self, tasks):
        """
        show the tasks of the day (day -> user input)
        """

        for i in tasks:
            self.time = list(i[0].split("-"))
            self.time = int(self.time[0])
            self.task = i[1]

            self.list_Task[self.time].set(self.task)

    def reset_task(self):
        """
        reset the tasks
        """

        for i in self.list_Task:
            i.set("")


    def get_user_date(self):
        """
        shows the new date
        """

        self.date_input = self.date_field.get()
        self.real_date = self.check_date(self.date_input)
        if self.real_date != False:
            self.date.set(f"current date: {self.date_field.get()}")
            self.tasks = database.getTaskofDay(self.date_field.get())
            self.reset_task()
            self.show_task(self.tasks)

if __name__ == "__main__":
    GUI()