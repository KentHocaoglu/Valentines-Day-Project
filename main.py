import tkinter as tk
from math import sin, cos, pi
from PIL import Image, ImageDraw, ImageTk

WINDOW_SIZE_X = 720
WINDOW_SIZE_Y = 480
IMAGE_SIZE_X = 200
IMAGE_SIZE_Y = 200
SCALE = -5

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
    # Create a blank white image
    img = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#FCCCCC")
    draw = ImageDraw.Draw(img)
    draw.polygon(heart_coordiantes, fill="#ff2971", outline="black")
    return img


def display_heart():
    heart_img = create_heart_image()
    heart_photo = ImageTk.PhotoImage(heart_img)
    heart_label.config(image=heart_photo)
    heart_label.image = heart_photo  # Keep a reference to avoid garbage collection

    # Change the label text
    heart_label.config(text="Happy Valentine's Day!")

#Create window
font = ("Helvetica", 14)
window = tk.Tk()
window.title("Happy Valentine's Day")
window.geometry("720x480")
window.config(bg="#FCCCCC")

#Create label
heart_label = tk.Label(window, text="Click the button below", font=("Arial", 14),bg="#FCCCCC")
heart_label.pack(pady=100)

#Create button
button = tk.Button(window, text="Click Me", command=display_heart, bg="#aaa3ff")
button.pack()

if __name__ == '__main__':
    window.mainloop()



