
import tkinter as tk
'''
root = tk.Tk()
label1 = tk.Label(root, text="Hello World!")
label1.pack()
label2 = tk.Label(root, text="This is a sample program!")
label2.pack()

root.mainloop()
'''

'''
#grid() 메소드는 위젯을 격자모양으로 배치한다. row와 column으로 위치 지정한다.
root = tk.Tk()

label1 = tk.Label(root, text="Hello World!")
label1.grid(row=0,column=0)
label2 = tk.Label(root, text="This is a sample program!")
label2.grid(row=1,column=1)

root.mainloop()
'''
#place() 메소드는 위젯을 지정된 좌표에 배치한다. x, u 좌표를 지정

root = tk.Tk()

label1 = tk.Label(root, text="Hello World!")
label1.place(x=10, y=10)
label2 = tk.Label(root, text="This is a sample program!")
label2.place(x=10,y=50)

root.mainloop()