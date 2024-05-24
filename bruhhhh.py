import tkinter as tk

def on_button1_click():
    print("Button 1 clicked")

def on_button2_click():
    print("Button 2 clicked")

def on_button3_click():
    print("Button 3 clicked")

root = tk.Tk()
root.title("Our Form")

root.geometry("600x600")

root.configure(bg='#000000')

label = tk.Label(root, text="Выбор кнопки", fg='#ffffff', bg='#000000', font=("Arial", 24, "bold"))
label.pack(pady=55)

button_Anya = tk.Button(root, text="Аня", command=on_button1_click,font=("Arial", 18, "bold"),fg='#ffffff', bg='#ff0000',width=15,height=3)
button_Anya.pack(pady=13)

button_Sasha = tk.Button(root, text="Саша", command=on_button2_click,font=("Arial", 18, "bold"),fg='#ffffff', bg='#cc0000',width=15,height=3)
button_Sasha.pack(pady=13)

button_Vanya = tk.Button(root, text="Ваня", command=on_button3_click,font=("Arial", 18, "bold"),fg='#ffffff', bg='#660000',width=15,height=3)
button_Vanya.pack(pady=13)

root.mainloop()
