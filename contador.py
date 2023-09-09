import tkinter as tk

def count_up():
  global count
  count += 1
  label.config(text=count)
  root.after(1000, count_up)

def count_down():
  global count
  count -= 1
  label.config(text=count)
  root.after(1000, count_down)
  
root = tk.Tk()
root.title("Contador")
count = 0
label = tk.Label(root, text=count)
label.pack()
button_up = tk.Button(root, text="Contar para cima", command=count_up)
button_up.pack()
button_down = tk.Button(root, text="Contar para baixo", command=count_down)
button_down.pack()
root.mainloop()
