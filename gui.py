import tkinter as tk

def message(status):
    field = tk.Tk()
    field.title("File Categorizer")
    field.geometry("300x100")
    if not status: # False
        message = tk.Label(master=field, text = 'Incorrect Address...')
    elif status:   # True
        message = tk.Label(master=field, text = 'Program has been completed...')
    message.pack()
    field.after(3000, lambda: field.destroy())
    field.mainloop()
