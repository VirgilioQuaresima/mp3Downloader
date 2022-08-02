# import openpyxl and tkinter modules

from tkinter import *
from tkinter.filedialog import asksaveasfilename
from videoClass import Video
from threading import *
import logging

# globally declare wb and sheet variable


# create the sheet object



# Function to set focus (cursor)
def focus1(event):
    # set focus on the course_field box
    course_field.focus_set()


# Function to set focus
def focus2(event):
    # set focus on the sem_field box
    sem_field.focus_set()


# Function to set focus
def focus3(event):
    # set focus on the form_no_field box
    form_no_field.focus_set()


# Function to set focus
def focus4(event):
    # set focus on the contact_no_field box
    contact_no_field.focus_set()


# Function for clearing the
# contents of text entry boxes
def clear():

    # clear the content of text entry box
    name_field.delete(0, END)
    course_field.delete(0, END)
    sem_field.delete(0, END)
    form_no_field.delete(0, END)
    contact_no_field.delete(0, END)


# Function to take data from GUI
# window and write to an excel file
def click():

    # if user not fill any entry
    # then print "empty input"
    root.update()
    if (name_field.get() == "" and
        course_field.get() == "" and
        sem_field.get() == "" and
        form_no_field.get() == "" and
        contact_no_field.get() == ""):
        print("empty input")
    elif(course_field.get() == "" and
        sem_field.get() == "" and
        form_no_field.get() == "" and
        contact_no_field.get() == ""):
        file = asksaveasfilename()
        song = {
            'url': name_field.get(),
            'filename':file+'.',
            "start_min": "",
            "start_sec": "",
            "end_min": "",
            "end_sec": "",
            }
        video = Video(song)
        video.download() 
        if var1.get()==1:
            video.video_cutter()
    else:

        file = asksaveasfilename()
        
        song = {
            'url': name_field.get(),
            'filename':file+'.',
            "start_min": int(course_field.get()),
            "start_sec": int(sem_field.get()),
            "end_min": int(form_no_field.get()),
            "end_sec": int(contact_no_field.get()),
            }

        video = Video(song)
        video.download() 
        if var1.get()==1:
            video.video_cutter()
    # set focus on the name_field box
    name_field.focus_set()

    # call the clear() function
    clear()

def threading():
	# Call work function
	t1=Thread(target=click)
	t1.start()
    

# Driver code
if __name__ == "__main__":

    logging.basicConfig(filename="/Users/virgilio/Local_VxX/threaad test/log_xcv.log",format='%(asctime)s %(levelname)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S',filemode="w", level=logging.DEBUG)
    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background='green')

    # set the title of GUI window
    root.title("YouTube to mp3 Downloader")

    # set the configuration of GUI window
    root.geometry("500x300")
    var1 = IntVar()
    c1 = Checkbutton(root, text='taglia',variable=var1, onvalue=1, offvalue=0)
    c1.grid(row=9, column=1)
    # create a Form label
    heading = Label(root, text="Form", bg="light green")

    # create a Name label
    name = Label(root, text="URL", bg="light green")

    # create a Course label
    course = Label(root, text="Start Minutes", bg="light green")

    # create a Semester label
    sem = Label(root, text="Start Seconds", bg="light green")

    # create a Form No. label
    form_no = Label(root, text="End Minutes.", bg="light green")

    # create a Contact No. label
    contact_no = Label(root, text="End Seconds", bg="light green")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    name.grid(row=1, column=0)
    course.grid(row=2, column=0)
    sem.grid(row=3, column=0)
    form_no.grid(row=4, column=0)
    contact_no.grid(row=5, column=0)

    # create a text entry box
    # for typing the information
    name_field = Entry(root)
    course_field = Entry(root)
    sem_field = Entry(root)
    form_no_field = Entry(root)
    contact_no_field = Entry(root)

    # bind method of widget is used for
    # the binding the function with the events

    # whenever the enter key is pressed
    # then call the focus1 function
    name_field.bind("<Return>", focus1)

    # whenever the enter key is pressed
    # then call the focus2 function
    course_field.bind("<Return>", focus2)

    # whenever the enter key is pressed
    # then call the focus3 function
    sem_field.bind("<Return>", focus3)

    # whenever the enter key is pressed
    # then call the focus4 function
    form_no_field.bind("<Return>", focus4)

    # whenever the enter key is pressed
    # then call the focus6 function

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    name_field.grid(row=1, column=1, ipadx="100")
    course_field.grid(row=2, column=1, ipadx="100")
    sem_field.grid(row=3, column=1, ipadx="100")
    form_no_field.grid(row=4, column=1, ipadx="100")
    contact_no_field.grid(row=5, column=1, ipadx="100")

    # call excel function

    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=threading)
    submit.grid(row=8, column=1)

    # start the GUI
    root.mainloop()
