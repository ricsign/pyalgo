import tkinter as tk
window = tk.Tk()
window.title('Mine Swiper')
window.geometry('800x500')
for i in range(20):
    button = tk.Button(text = 'Hitme', width = 12, height = 3)
    button.pack()
window.mainloop()