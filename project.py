import tkinter as tk
import pyttsx3

# بحول النص للكلام
engine = pyttsx3.init()

def play_text():
    text = entry.get()
    if text:
        engine.say(text)
        engine.runAndWait()

def exit_program():
    root.destroy()

def clear_text():
    entry.delete(0, tk.END)

# بنشاء نافذه للبرنامج
root = tk.Tk()
root.title("Text to Speech")
rate = engine.getProperty('rate')  
engine.setProperty('rate', 120)  # بعدل علي مستوي السرعه
# اضافه العناصر ال هتظهر علي الواجهه
label = tk.Label(root, text="Enter your text:")
label.grid(row=0, column=0, columnspan=3, pady=10)

entry = tk.Entry(root, width=50)
entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

play_button = tk.Button(root, text="Play", command=play_text, width=10)
play_button.grid(row=2, column=0, padx=5, pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_program, bg="red", width=10) 
exit_button.grid(row=2, column=1, padx=5, pady=10)

set_button = tk.Button(root, text="Set", command=clear_text, width=10)
set_button.grid(row=2, column=2, padx=5, pady=10)

# تشغيل واجهه البرنامج
root.mainloop()