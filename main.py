import tkinter as tk
from tkinter import font
from math import sin, cos, pi
from PIL import Image, ImageDraw, ImageTk

WINDOW_SIZE_X = 720
WINDOW_SIZE_Y = 480
IMAGE_SIZE_X = 200
IMAGE_SIZE_Y = 200
SCALE = -6


#Use parametric equations to model the heart
x = lambda t : 16*sin(t)**3
y = lambda t : 13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t)

#Create coordinates for heart
heart_coordiantes = []
n = 200
theta = 0
while(theta<2*pi):
    heart_coordiantes.append(( IMAGE_SIZE_X/2 + x(theta)*SCALE, IMAGE_SIZE_Y/2 + y(theta)*SCALE ))
    theta += 2*pi/n
#print(heart_coordiantes)
    

def create_heart_image():
    #Create the heart
    img = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#FCCCCC")
    draw = ImageDraw.Draw(img)
    draw.polygon(heart_coordiantes, fill="#ff2971", outline="black")
    text = "Awww, I love you too <3"
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

 
#Create window
window = tk.Tk()
window.title("Happy Valentine's Day")
window.geometry("720x480")
window.config(bg="#FCCCCC")

font = font.Font(family = "Sylfaen", size = 24)

#Create label
heart_label = tk.Label(window, text="Happy Valentine's Day", fg = "#ff2971", font=font, bg="#FCCCCC")
heart_label.pack(pady=100)

#Create a frame for the buttons
button_frame = tk.Frame(window, bg="#FCCCCC")
button_frame.pack(pady=50)

#Create button
good_button = tk.Button(button_frame, text="You Love Me", command=display_heart, bg="#aaa3ff")
good_button.grid(row=0, column=0, padx=10)
bad_button = tk.Button(button_frame, text="You Don't Love Me", bg="#aaa3ff")
bad_button.grid(row=0, column=1, padx=10)


if __name__ == '__main__':
    window.mainloop()



