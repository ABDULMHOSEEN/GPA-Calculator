#  Import
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import filedialog

# make a root
root = Tk()
# put a  title
root.title("GPA Calculator")
# make a font
title_font = Font(family="Berlin Sans FB Demi", size=20)
sub_title = Font(family="Tempus Sans ITC", size=15)
write_font = Font(family="Segoe UI Historic", size=10)
# define a function that will get the number of the points
def Count_points():
    # define the total points
    total_points = 0
    # define the total hour
    total_hour = 0
    # put the student information inside a diec
    data = {GradesShow1.get(): Credits_Hours1.get(), GradesShow2.get(): Credits_Hours2.get(), GradesShow3.get():Credits_Hours3.get(), GradesShow4.get(): Credits_Hours4.get(), GradesShow5.get(): Credits_Hours5.get(), GradesShow6.get(): Credits_Hours6.get()}
    # delete the empty places
    for i in range(5):
        if '' in data:
            data.pop('')
    if data != {}:
        # take each grade and got its point
        for grade, credit in data.items():
            # make the number of credit as integer
            credit = int(credit)
            # collect the hours
            total_hour += credit
            # do the process to get the number of pints
            if grade == "A+":
                total_points += (credit * 4)
            elif grade == "A":
                total_points += (credit * 3.75)
            elif grade == "B+":
                total_points += (credit * 3.5)
            elif grade == "B":
                total_points += (credit * 3)
            elif grade == "C+":
                total_points += (credit * 2.5)
            elif grade == "C":
                total_points += (credit * 2)
            elif grade == "D+":
                total_points += (credit * 1.5)
            elif grade == "D":
                total_points += (credit * 1)
            elif grade == "F":
                total_points += (credit * 0)

        total_GPA(total_hour, total_points)

# define a function that will calculate the GPA
def total_GPA(total_hour, total_points):
    # display the GPA
    GPA = round((total_points/total_hour), 3)
    label5 = Label(root,font = title_font, text="Your GPA in semester %s is %.3f" % (semester.get(), GPA)).grid(row=11, column=1,columnspan=3)
    return GPA
#### design of the app

# put a label that ask for information
label1= Label(root,font = title_font,text ="Enter the semester number").grid(row=1,column = 1,columnspan=3)
# put an entry to get the data (number of the semester)
semester = Entry(root, font = sub_title,justify = "center")
semester.grid(row=2,column = 1, columnspan=3)

# ask for the course name
label2 = Label(root,font = sub_title,text="Course Name").grid(row=3,column=1, padx = 10, pady = 10)
# put an entry to get data
Course_Name1 = Entry(root,font = write_font,justify = "center").grid(row=4,column = 1,padx=10,pady=10)

# ask for the number of credits
label3 = Label(root,font = sub_title,text="Credits Hours").grid(row=3,column=2)
# entry
Credits_Hours1 = Entry(root,font = write_font,justify = "center")
Credits_Hours1.grid(row=4,column = 2, padx = 10, pady = 10)

# ask for the grade
label4 = Label(root,font = sub_title,text="Your Grade").grid(row=3,column=3)
# get choice
Grades = ["A+","A","B+","B","C+","C","D+","D","F","None"]
GradesShow1 = ttk.Combobox(root,values=Grades,font = write_font,justify = "center")
GradesShow1.grid(row=4,column=3, padx = 5, pady = 10)

# take the information from all of the entry
button = Button(root, text = "Count GPA",font = sub_title, padx=15, pady=15, bg="#14adf5", command = lambda: Count_points()).grid(row=10, column=2, pady=20)

#### design of the app END

# repeated stuff
Course_Name2 = Entry(root,font = write_font,justify = "center").grid(row=5,column = 1, padx = 5, pady = 10)
Credits_Hours2 = Entry(root,font = write_font,justify = "center")
Credits_Hours2.grid(row=5,column = 2, padx = 5, pady = 10)
GradesShow2 = ttk.Combobox(root,values=Grades,font = write_font,justify = "center")
GradesShow2.grid(row=5,column=3, padx = 5, pady = 10)

Course_Name3 = Entry(root,font = write_font,justify = "center").grid(row=6,column = 1, padx = 5, pady = 10)
Credits_Hours3 = Entry(root,font = write_font,justify = "center")
Credits_Hours3.grid(row=6,column = 2, padx = 5, pady = 10)
GradesShow3 = ttk.Combobox(root,values=Grades,font = write_font,justify = "center")
GradesShow3.grid(row=6,column=3, padx = 5, pady = 10)

Course_Name4 = Entry(root,font = write_font,justify = "center").grid(row=7,column = 1, padx = 5, pady = 10)
Credits_Hours4 = Entry(root,font = write_font,justify = "center")
Credits_Hours4.grid(row=7,column = 2, padx = 5, pady = 10)
GradesShow4 = ttk.Combobox(root,values=Grades,font = write_font,justify = "center")
GradesShow4.grid(row=7,column=3, padx = 5, pady = 10)

Course_Name5 = Entry(root,font = write_font,justify = "center").grid(row=8,column = 1, padx = 10, pady = 10)
Credits_Hours5 = Entry(root,font = write_font,justify = "center")
Credits_Hours5.grid(row=8,column = 2, padx = 5, pady = 10)
GradesShow5 = ttk.Combobox(root,values=Grades,font = write_font,justify = "center")
GradesShow5.grid(row=8,column=3, padx = 5, pady = 10)

Course_Name6 = Entry(root,font = write_font,justify = "center").grid(row=9,column = 1, padx = 5, pady = 10)
Credits_Hours6 = Entry(root,font = write_font,justify = "center")
Credits_Hours6.grid(row=9,column = 2, padx = 5, pady = 10)
GradesShow6 = ttk.Combobox(root,values=Grades,font = write_font,justify = "center")
GradesShow6.grid(row=9,column=3, padx = 5, pady = 10)
root.mainloop()