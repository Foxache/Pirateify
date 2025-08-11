import random
import time
import os
import subprocess
import webbrowser
import threading
from pynput.keyboard import Key, Controller
import tkinter as tk
from PIL import Image, ImageTk

KEYBOARD = Controller()

TRIGGER_TEXTS = [
    "Thats not true! I Sent a text!",
    "I litteraly never talk about working in Blizzard",
    "Did you read that from a reddit thread",
    "This petition is absolutely shit",
    "My dad is one of the top employees for Blizzard",
    "I worked at Blizzard Entertainment for 7 Years",
    "My Dad IS the guy from South Park!",
    "They said I am the first Second Generation employee at Blizzard, and I love that shit I love that company",
    "Buy the demo",
    "See you in the unban requests",
    "I actively advise against Stop Killing Games",
    "I hope your Petition gets everything you asked for but nothing you wanted",
    "I have a very deep voice",
    "I worked at blizzard",
    "I cant do anything im out of Mana",
    "Yeah chat so today i was supposedly cursed hah I saw this woman breastfeeding her child in a non-optimal way so being the kind man I am I showed her how to do it correctly. I told her you should have the child latch at a thirty degree angle so that when the milk extrudes from the channel it will flow more rapidly with the babe's suction"
]

BATTLE_NET_PATH = r"C:\Program Files (x86)\Battle.net\Battle.net.exe"
CHECK_INTERVAL = random.randint(15,600)

def random_app_action():
    action = random.choice(["paint", "battle_net", "blizzard_website", "heartbound"])
    if action == "paint":
        subprocess.run(["start", "mspaint"], shell=True)
    elif action == "battle_net":
        subprocess.run(["start", BATTLE_NET_PATH], shell=True)
    elif action == "blizzard_website":
        webbrowser.open_new("https://www.blizzard.com/en-us/")
    elif action == "heartbound":
        webbrowser.open_new("https://store.steampowered.com/app/567380/Heartbound/")

def send_random_message():
    message = random.choice(TRIGGER_TEXTS)
    KEYBOARD.press(Key.enter)
    KEYBOARD.release(Key.enter)
    time.sleep(0.1)
    KEYBOARD.type(message)
    time.sleep(0.2)
    KEYBOARD.press(Key.enter)
    KEYBOARD.release(Key.enter)

def background_actions():
    while True:
        try:
            time.sleep(CHECK_INTERVAL)
            if random.choice([True, False]):
                random_app_action()
            else:
                print("Sending message...")
                send_random_message()
        except Exception as e:
            print(f"Error occurred: {e}")

def start_bouncing_window():
    root = tk.Tk()
    root.overrideredirect(True)  
    root.wm_attributes("-topmost", True) 
    
    img = f"{str(random.randint(1,4))}.png"
    
    image_path = os.path.join(os.path.dirname(__file__), img)
    img = Image.open(image_path)
    tk_img = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=tk_img, borderwidth=0, highlightthickness=0)
    label.pack()

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    img_w, img_h = img.size

    x, y = random.randint(0, screen_w - img_w), random.randint(0, screen_h - img_h)
    dx, dy = 3, 3

    def move():
        nonlocal x, y, dx, dy
        x += dx
        y += dy

        if x <= 0 or x + img_w >= screen_w:
            dx = -dx
        if y <= 0 or y + img_h >= screen_h:
            dy = -dy

        root.geometry(f"{img_w}x{img_h}+{x}+{y}")
        root.after(10, move)

    move()
    root.mainloop()

if __name__ == "__main__":
    threading.Thread(target=background_actions, daemon=True).start()
    start_bouncing_window()
