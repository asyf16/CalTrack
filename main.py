from tkinter import *
import customtkinter
from PIL import Image
import cv2 as cv
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename
import os
import readdata
# Imports the Google Cloud client library
from google.cloud import vision
from datetime import datetime


customtkinter.set_appearance_mode("light")  # sets the color of the background
customtkinter.set_default_color_theme("/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/customtkinter/assets/themes/green.json")
root = customtkinter.CTk()  # create the root window
root.title("CalTrack")  # names the window
root.geometry("1200x800")
dark = True
home = customtkinter.CTkTabview(master=root, width=1200, height = 800, fg_color="transparent")
home.place(relx=0.5,rely=0.52,anchor=CENTER)
display = customtkinter.CTkTabview(master=root, width=1200, height = 800, fg_color="transparent")
calculate = customtkinter.CTkTabview(master=root, width=1200, height = 800, fg_color="transparent")
sex = "Female"
active = "Sedentary"
BMR = 0
home_bool = True
calc_bool = False
display_bool = False
total = 0
meterlevel = 0
dataset=readdata.getdata()
tot_array = []
time_array = []
# print(dataset.keys())


def updatemeter():
    cover = customtkinter.CTkButton(display, height=35, width= 250, state="disabled",text="",fg_color=("#F2E8D4","#183252"))
    cover.place(relx=0.2,rely=0.9,anchor='s')
    global total
    global meterlevel
    colors = "#635323"
    if BMR!=0:
        meterlevel = total/BMR
    else:
        meterlevel=0
    if meterlevel>1:
        meterlevel=1
        colors="#7B2D29"
    totalstring = str(total)+"/"+str(BMR)
    inside = customtkinter.CTkButton(display, height=550, width=250,border_color=("#35422E","#DEECFE"),border_width=4,corner_radius=0,text="", state="disabled",fg_color="transparent")
    meter = customtkinter.CTkButton(display, height=meterlevel*550, width=250,border_color=("#35422E","#DEECFE"),border_width=4,corner_radius=0,text="", state="disabled")
    trackedcal = customtkinter.CTkLabel(display, font=("Cordel",37),text_color=(colors,"#8ea3bf"), text=totalstring, fg_color="transparent")
    inside.place(relx=0.2,rely=0.83,anchor='s')
    meter.place(relx=0.2,rely=0.83,anchor='s')
    trackedcal.place(relx=0.2,rely=0.9,anchor='s')


def resetval():
    global total
    global tot_array
    total = 0
    tot_array.clear()
    textbox.place_forget()
    textbox.configure(state='normal')
    textbox.delete("0.0","end")
    textbox.configure(state='disabled')
    textbox.place(relx=0.65,rely=0.6, anchor=CENTER)
    updatemeter()

def switch_event():  # function to control the switch
    global dark
    if switch_var.get() == "off":  # if the switch is turned on
        customtkinter.set_appearance_mode("dark")  # changes the appearance mode to dark
        dark = True
    if switch_var.get() == "on":  # if the switch is turned off
        customtkinter.set_appearance_mode("light")  # changes the appearance mode to light
        dark = False


def getgender(choice):
    global sex
    sex = gender.get()
    print("optionmenu dropdown clicked:", sex)


def getactivity(choice):
    global active
    active = activity.get()
    print("optionmenu dropdown clicked:", active)


def updateinfo():
    if home_bool:
        infotext = "Upload your daily meals"
    if display_bool:
        infotext = "View your tracked meals"
    if calc_bool:
        infotext = "Calculate your calories"
    titlelabel = customtkinter.CTkLabel(master=tabview, text="Welcome", fg_color="transparent", font=("Corbel",30))
    bodylabel = customtkinter.CTkLabel(master=tabview, text=infotext, fg_color="transparent", font=my_font)
    titlelabel.place(relx=0.5, rely=0.3, anchor=CENTER)
    bodylabel.place(relx=0.5, rely=0.5, anchor=CENTER)

def showinfo():
    updateinfo()
    tabview.place(relx=0.75, rely=0.865, anchor=CENTER)
    exit = customtkinter.CTkButton(master=tabview, corner_radius=100, height=50, width=50, text="Ok",font=("Corbel", 20),anchor=CENTER, command=closeinfo)
    exit.place(relx=0.5,rely=0.78,anchor=CENTER)

def closeinfo():
    tabview.place_forget()


def showhome():
    global home_bool
    global calc_bool
    global display_bool
    home_bool = True
    calc_bool = False
    display_bool = False
    calculate.place_forget()
    display.place_forget()
    home.place(relx=0.5,rely=0.52,anchor=CENTER)
    closeinfo()


def showdisplay():
    global home_bool
    global calc_bool
    global display_bool
    home_bool = False
    calc_bool = False
    display_bool = True
    display.place(relx=0.5,rely=0.52,anchor=CENTER)
    home.place_forget()
    calculate.place_forget()
    closeinfo()
    updatemeter()
    

def showcalculate():
    global home_bool
    global calc_bool
    global display_bool
    home_bool = False
    calc_bool = True
    display_bool = False
    calculate.place(relx=0.5,rely=0.52,anchor=CENTER)
    home.place_forget()
    display.place_forget()
    closeinfo()


def captureimage():
    cam = cv.VideoCapture(0)

    if not cam.isOpened():
        print("Camera not accessible")
        return

    while True:
        # Show the live video stream in a window
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        cv.imshow('Press the spacebar to take a photo', frame)

        # Wait for a key press for 1 millisecond
        key = cv.waitKey(1)

        if key == ord('q'):  # Press 'q' to quit the program
            print("Exiting...")
            break
        elif key == 32:  
            # Save the image to a file
            filename = "Captured.png"
            # Get the current working directory where the file should be saved
            cwd = os.getcwd()
            taken_filepath = os.path.join(cwd, filename)
            cv.imwrite(taken_filepath, frame)  # This line saves the image
            print(f"Image saved at {taken_filepath}")
            cv.destroyWindow('Press the spacebar to take a photo')
            return (taken_filepath)
    
    # Release the camera resource
    cam.release()
    cv.destroyWindow('Press the spacebar to take a photo')


def captured_localobjects(path):
    current_time = datetime.now()
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision

    list = []

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations
    
    for object_ in objects:
        if object_.name in dataset.keys():
            upload_timestamp = current_time.strftime("%I:%M %p")
            print(f" The upload time is {upload_timestamp}")
            time_array.append (upload_timestamp)
            list.append(f"{object_.name}")
    print(list)
    return(list)

def capture():
    captured_filepath = captureimage()
    analysis(captured_localobjects(captured_filepath))

def upload_localobjects(path):
    from google.cloud import vision
    current_time = datetime.now()
    list = []

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations
    
    for object_ in objects:
        if object_.name in dataset.keys():
            upload_timestamp = current_time.strftime("%I:%M %p")
            print(f" The upload time is {upload_timestamp}")
            time_array.append (upload_timestamp)
            list.append(f"{object_.name}")
    print(list)
    return(list)

def uploadimage():
    global image_location
    filetypes = ([("Img Files", "*.png"), ("JPEG Files", "*.jpeg")])  # limits the filetypes to only CSV files
    image_location = fd.askopenfilename(  # gets the filepath for the uploaded file
        title='Open an image',  # title of the file dialog pop-up
        initialdir='/',
        filetypes=filetypes)
    if image_location != '':
        analysis(upload_localobjects(image_location))
        print(time_array)
        

def analysis(foods): # also needs to be provided the current 
    global tot_array
    global total
    textbox.configure(state='normal')
    for item in foods:
        total += dataset[item] # add the calories of the food to the tota
        line = str(len(tot_array) + 1) + ". " + item + " - " + str(dataset[item]) + " calories" + " @"f" {(time_array[len(tot_array)])}\n"
        textbox.insert("end", line)
        print(line)
        tot_array.append(line)
    textbox.configure(state='disabled')
    textbox.place(relx=0.65,rely=0.6, anchor=CENTER)
    

def getBMR():
    global BMR
    try:
        heavy=int(weight.get())
    except:
        heavy = int(60)
    try:
        old=int(age.get())
    except:
        old=int(30)
    try:
        tall=int(height.get())
    except:
        tall=int(170)

    if sex=="Female":
        BMR = 447.6 + (9.25 * heavy) + (3.10 * tall) - (4.33 *old)
    if sex=="Male":
        BMR = 88.4 + (13.4 * heavy) + (4.8 * tall) - (5.68 *old)
    if active == "Sedentary":
        BMR = BMR*1.2
    if active == "Moderate":
        BMR = BMR*1.375
    if active == "Active":
        BMR = BMR*1.55
    BMR=int(BMR)
    textbmr = "You are recommended to consume " + str(round(BMR,0)) + " calories daily."
    displaybmr = customtkinter.CTkLabel(calculate, text=textbmr, text_color=("#796C47","#8ea3bf"), font=bold_font, justify='left')
    displaybmr.place(relx=0.5, rely=0.75, anchor=CENTER)

#setup
my_font = customtkinter.CTkFont(family="Corbel", size=25)
bold_font = customtkinter.CTkFont(family="Corbel", size=35, weight="bold")
info_font = customtkinter.CTkFont(family="Times New Roman", size=25, slant="italic")

#navigation bar
navbar = customtkinter.CTkFrame(master=root, width=1300, height=100)
home_button = customtkinter.CTkButton(navbar, corner_radius=0, height=100, text="Home",font=my_font, fg_color="transparent",anchor=CENTER, command=showhome)
display_button = customtkinter.CTkButton(navbar, corner_radius=0, height=100, text="Display", font=my_font, fg_color="transparent", anchor=CENTER, command=showdisplay)
calc_button = customtkinter.CTkButton(navbar, corner_radius=0, height=100, text="Calculate",font=my_font, fg_color="transparent",border_width=2, border_color=("#65735e", "#687d96"),anchor=CENTER, command=showcalculate)
navbar.place(relx=0.5, rely=0, anchor=CENTER)  # places the switch
home_button.place(relx=0.59, rely=0.25)
display_button.place(relx=0.8, rely=0.25)
calc_button.place(relx=0.695, rely=0.25)

#info button
info_button = customtkinter.CTkButton(root, width = 30, height = 40, corner_radius=100, text = "i", font=info_font, border_spacing= 0, command=showinfo)
tabview = customtkinter.CTkTabview(master=root, width=400, height = 180, fg_color=("#D4C9A8","#2d4a6e"), border_width=0)
info_button.place(relx=0.95, rely=0.95, anchor=CENTER)  # places the switch

#light switch
switch_var = customtkinter.StringVar(value="on")  # creates the value of the switch
dark_switch = customtkinter.CTkSwitch(master=root, switch_width=50, switch_height=30, text="Dark", text_color=("#635323","#8ea3bf"), font=("Corbel", 25), command=switch_event, variable=switch_var, onvalue="on", offvalue="off")  # initializes the switch
dark_switch.place(relx=0.1, rely=0.95, anchor=CENTER)  # places the switch

#home area
my_image = customtkinter.CTkImage(light_image=Image.open("Images/title1.png"),dark_image=Image.open("Images/title2.png"),size=(850, 250))
image_label = customtkinter.CTkLabel(home, image=my_image, text="")
image_label.place(relx=0.5, rely=0.31, anchor=CENTER)
upload_button = customtkinter.CTkButton(home, width = 180, height = 60, corner_radius=100, text = "Upload",text_color=("#635323","#8ea3bf"), font=my_font, command=uploadimage, fg_color=("#D4C9A8","#436791"),hover_color=("#c9bb91","#36567d"))
photo_button = customtkinter.CTkButton(home, width = 180, height = 60, corner_radius=100, text = "Capture", text_color=("#635323","#8ea3bf"), font=my_font, command=capture, fg_color=("#D4C9A8","#436791"),hover_color=("#c9bb91","#36567d") )
upload_button.place(relx=0.5, rely=0.55, anchor=CENTER)
photo_button.place(relx=0.5, rely=0.65, anchor=CENTER)

#calculate area
Labels = customtkinter.CTkLabel(calculate, text="Gender\n\nAge (years)\n\nWeight (kg)", text_color=("#796C47","#8ea3bf"), font=bold_font, justify='left')
Labels2 = customtkinter.CTkLabel(calculate, text="Height (cm)\n\nActivity", text_color=("#796C47","#8ea3bf"), font=bold_font, justify='left')
age = customtkinter.CTkEntry(calculate, placeholder_text="22", height = 45, width = 240, font=my_font)
weight = customtkinter.CTkEntry(calculate, placeholder_text="60", height = 45, width = 240, font=my_font)
height = customtkinter.CTkEntry(calculate, placeholder_text="170", height = 45, width = 240, font=my_font)
gender = customtkinter.CTkOptionMenu(calculate, values=["Female", "Male"], command=getgender, height = 45, width = 240, font=my_font)
activity = customtkinter.CTkOptionMenu(calculate, values=["Sedentary", "Moderate", "Active"], command=getactivity, height = 45, width = 240, font=my_font)
calc_button = customtkinter.CTkButton(calculate, width = 240, height = 60, corner_radius=100, text = "Calculate",text_color=("#4c5e42","#8ea3bf"), font=my_font, command=getBMR, fg_color=("#a8bd9d","#436791"),hover_color=("#92ab85","#36567d"))
Labels.place(relx=0.17,rely=0.50,anchor=CENTER)
Labels2.place(relx=0.57,rely=0.435,anchor=CENTER)
gender.place(relx=0.37, rely=0.40, anchor=CENTER)
age.place(relx=0.37, rely=0.50, anchor=CENTER)
weight.place(relx=0.37, rely=0.60, anchor=CENTER)
height.place(relx=0.77, rely=0.40, anchor=CENTER)
activity.place(relx=0.77, rely=0.50, anchor=CENTER)
calc_button.place(relx=0.77, rely=0.61, anchor=CENTER)
calc_img = customtkinter.CTkImage(light_image=Image.open("Images/calc1.png"),dark_image=Image.open("Images/calc2.png"),size=(900, 165))
calc_label = customtkinter.CTkLabel(calculate, image=calc_img, text="")
calc_label.place(relx=0.5, rely=0.23, anchor=CENTER)

#display area
display_img = customtkinter.CTkImage(light_image=Image.open("Images/track1.png"),dark_image=Image.open("Images/track2.png"),size=(550, 290))
display_label = customtkinter.CTkLabel(display, image=display_img, text="")
textbox = customtkinter.CTkTextbox(display,text_color=("#695737","#8ea3bf"), border_width=5,border_color=("#B6A77A","#8ea3bf"),border_spacing=6, height = 375, width=650, font=("Corbel", 30), state="disabled")
textbox.place(relx=0.65,rely=0.6, anchor=CENTER)
display_label.place(relx=0.6, rely=0.23, anchor=CENTER)
reset_button = customtkinter.CTkButton(display, width = 200, height = 50, corner_radius=100, text = "Reset",font=my_font,command=resetval)
reset_button.place(relx=0.5, rely=0.92, anchor=CENTER)
updatemeter()

root.mainloop()