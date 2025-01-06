import tkinter as tk
from tkinter import font
from math import sin, cos, pi
from PIL import Image, ImageDraw, ImageTk

WINDOW_SIZE_X = 800
WINDOW_SIZE_Y = 600
IMAGE_SIZE_X = 300
IMAGE_SIZE_Y = 300
SCALE = -9
flower_index = 0

#Use parametric equations to model the heart
heart_x = lambda t : 16*sin(t)**3
heart_y = lambda t : 13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t)
#flower_x = lambda t : 6*sin(15*t)*cos(3.7*t)
#flower_y = lambda t : 6*sin(15*t)*sin(3.7*t)

flower_parametrics = [(lambda t : 6*sin(15*t)*cos(3.7*t), lambda t : 6*sin(15*t)*sin(3.7*t)), 
                (lambda t : 6*sin(16*t)*cos(3.7*t), lambda t : 6*sin(16*t)*sin(3.7*t)),
                (lambda t : 10*sin(17*t)*cos(14*t), lambda t : 10*sin(14*t)*sin(17*t)),
                (lambda t : 10*sin(12*t)*cos(14*t), lambda t : 10*sin(14*t)*sin(12*t)),
                (lambda t : 10*sin(2*t*t)*cos(2*t), lambda t : 10*sin(2*t*t)*sin(2*t)),
                (lambda t : -10*sin(1*t)*cos(14*t), lambda t : -5*sin(7*t)*sin(21*t)),
                (lambda t : 10*sin(5*t)*cos(8*t), lambda t : 5*sin(8*t)*sin(24*t))
                ]



def get_heart_coordinates():
    # Return coordinates for heart   
    heart_coordinates = []
    n = 150
    theta = 0
    while(theta<2*pi):
        heart_coordinates.append(( IMAGE_SIZE_X/2 + heart_x(theta)*SCALE, IMAGE_SIZE_Y/2 + heart_y(theta)*SCALE ))
        theta += 2*pi/n
    return heart_coordinates
    

def get_flower_coordinates(index = 0):
    # Return flower coordinates
    n = 300
    theta = 0
    flower_x, flower_y = flower_parametrics[index][0], flower_parametrics[index][1]
    flower_coordinates = []
    while(theta<2*pi):
        flower_coordinates.append(( IMAGE_SIZE_X/2 + flower_x(theta)*-15, IMAGE_SIZE_Y/2 + flower_y(theta)*-15 ))
        theta += 2*pi/n
    return flower_coordinates

def create_heart_image():
    #Create the heart
    img = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#FCCCCC")
    draw = ImageDraw.Draw(img)
    draw.polygon(get_heart_coordinates(), fill="#ff2971", outline="black")
    text = "Awww, I love you too <3"
    text_offset = draw.textlength(text)/2
    text_position = (IMAGE_SIZE_X/2-text_offset, IMAGE_SIZE_Y/2)
    draw.text(text_position, text, fill="white")
    return img

def create_image(coordinates, text = ""):
    #Create the heart
    img = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#FCCCCC")
    draw = ImageDraw.Draw(img)
    draw.polygon(coordinates, outline="black")
    text_offset = draw.textlength(text)/2
    text_position = (IMAGE_SIZE_X/2-text_offset, IMAGE_SIZE_Y/2)
    draw.text(text_position, text, fill="white")
    return img


def display_heart():
    #Turn the heart image into a label
    heart_img = create_heart_image()
    heart_photo = ImageTk.PhotoImage(heart_img)
    heart_label.config(image=heart_photo)
    heart_label.image = heart_photo  # Keep a reference to avoid garbage collection

def display_flower(index):
    flower_img = create_image(get_flower_coordinates(index))
    flower_photo = ImageTk.PhotoImage(flower_img)
    heart_label.config(image=flower_photo)
    heart_label.image = flower_photo

def sad_text():
    heart_label.config(text="Oh... Okay")

def hide_bad_button():
    bad_button.grid_forget()

def hide_buttons():
    bad_button.grid_forget()
    good_button.grid_forget()

def show_next_button():
    next_button.grid(row=1, column=1)

def next_view():
    #heart_label.pack_forget()
    #next_button.grid_forget()
    global flower_index
    display_flower(flower_index)
    if flower_index < len(flower_parametrics)-1:
        flower_index += 1
    else:
        next_button.grid_forget()

#Create window
window = tk.Tk()
window.title("Happy Valentine's Day")
window.geometry(f"{WINDOW_SIZE_X}x{WINDOW_SIZE_Y}")
window.config(bg="#FCCCCC")

font = font.Font(family = "Sylfaen", size = 24)

#Create label
heart_label = tk.Label(window, text="Happy Valentine's Day", fg = "#ff2971", font=font, bg="#FCCCCC")
heart_label.pack(pady=30)

#Create a frame for the buttons
button_frame = tk.Frame(window, bg="#FCCCCC")
button_frame.pack(pady=50)

#Create button
good_button = tk.Button(button_frame, text="You Love Me", command=lambda:[display_heart(), hide_buttons(), show_next_button()], bg="#aaa3ff")
good_button.grid(row=0, column=0, padx=10)
bad_button = tk.Button(button_frame, text="You Don't Love Me", command= lambda:[sad_text(), hide_bad_button()], bg="#aaa3ff")
bad_button.grid(row=0, column=2, padx=10)
next_button = tk.Button(button_frame, text="Next", command=next_view, bg="#Faa3ff")


if __name__ == '__main__':
    window.mainloop()



