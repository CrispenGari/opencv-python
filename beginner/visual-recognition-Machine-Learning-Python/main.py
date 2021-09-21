
""""
Author: Crispen Gari
"""
import json
from tkinter import *
from tkinter import messagebox, scrolledtext
import tkinter.ttk as ttk
import keys as key
try:
    from PIL import ImageTk, Image
    from ibm_watson import VisualRecognitionV3

    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
except ImportError as err:
    from pip._internal import main as install
    install(["install", "ibm-watson>=4.0.1"])
    install(["install", "Pillow"])
finally:
    pass
root = Tk()
root.title("Visual Recognition")
width, height = 900, 500
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
position_top, postion_right = int(screen_height/2 - height/2), int(screen_width/2 - width/2)
root.geometry(f'{width}x{height}+{postion_right}+{position_top}')
root.resizable(False, False)
root.iconbitmap('main.ico')
label_img = ImageTk.PhotoImage(Image.open("icon.ico"))

# Configuring the visual recogniser
version = '2018-03-19',
authenticator = IAMAuthenticator(apikey=f'{key.apikey}')
visual_recognition = VisualRecognitionV3(version=version, authenticator=authenticator)
visual_recognition.set_service_url(f'{key.url}')
# Functions
def close():
    val = messagebox.askyesnocancel("Closing the Visual Recognition", "Are you sure you want to close the Visual "
                                                                      "Recognition APP?")
    return root.quit() if val else root.focus()
classfire_ids =["food", 'cars']
def detect():

    image_url = image_.get()
    if image_url:
        # class_results = visual_recognition.classify(url=image_url, classifier_ids=classfire_ids).get_result()
        scrollable_text["state"] = NORMAL
        scrollable_text.delete('0.0', END)
        try:
            class_results = visual_recognition.classify(url=image_url).get_result()
            objects = class_results["images"][0]["classifiers"][0]["classes"]
            scrollable_text.insert(END, f"\tObjects Class Detected {len(objects)} classes object(s)\n")
            scrollable_text.insert(END, key.line)
            for classified_object in objects:
                # display them on a scrolltext
                scrollable_text.insert(END, f"\t{classified_object['class']} ({classified_object['score']})\n")
        except Exception:
            messagebox.showerror("Visual Recognition", "An error Occoured Make sure you are connected to internet or your API is working")
        # print(json.dumps(class_results, indent=2))
        scrollable_text["state"] = DISABLED
    return
# UI
Label(root, text="Visual Recognition App", font=("Arial", 15, "bold"), fg="lightseagreen",
      image=label_img, compound=RIGHT).grid(row=0, column=0, pady=15,  padx=5, columnspan=5)
label = Label(root, text="Paste Image URL", font=("Arial", 11))
label.grid(row=1, column=0, sticky=W, padx=5)
image_ = ttk.Entry(root, width=50, font=("arial", 14))
image_.grid(row=1, column=1, sticky=W)
btn = Button(root, font=("arial", 12),text="DETECT",activebackground="green", relief=SOLID,bg="lightseagreen",
             fg="white", bd=1,
        width=20, command = detect)
btn.grid(row=1, column=2, sticky=W)
Label(root, text="Results", font=("Arial", 15, "bold"), fg="lightseagreen", compound=RIGHT).grid(row=3, column=0, pady=15,  padx=5, columnspan=5)
scrollable_text = scrolledtext.ScrolledText(root, width=95, height=10,font=("arial", 12) , state=DISABLED)
scrollable_text.grid(row=4, column=0,  padx=5, columnspan=5)

btn2 = Button(root, font=("arial", 12),text="Close",activebackground="red", relief=SOLID,bg="orange",
             fg="white", bd=1,
        width=10, command=close)
btn2.grid(row=5, column=0, sticky=W, padx=5, pady=10)
root.mainloop(0)
