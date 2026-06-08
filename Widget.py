import Repetitive_Grothendieck_Groups as rg
import tkinter as tk

from Repetitive_Grothendieck_Groups import rep_cluster_K0

root = tk.Tk()
root.title("Grothendieck Groups of Repetitive Cluster Category")
root.geometry("800x500")

frame = tk.Frame(root)

def clicked():
    my_type.config(text=f'Dynkin Type:{var.get()}')

def compute():
    #Delete previous entry
    hidden_label.config(text='')
    # Output new entries
    hidden_label.config(text=f'{rg.rep_cluster_K0(var.get(),int(n_entry.get()),int(p_entry.get()))}')

var = tk.StringVar()

#Create Radio Buttons for Dynkin type

radio1 = tk.Radiobutton(root,text = "A", variable = var, value = "A", command=clicked)
radio1.pack(pady =(40,10))

radio2 = tk.Radiobutton(root,text = "D", variable = var, value = "D", command=clicked)
radio2.pack(pady =(40,10))

#set default radio button
var.set("A")

# Define which Dynkin type is used

my_type = tk.Label(root,text = "Dynkin type:",font = ('Helvetica', 24))
my_type.pack(pady =10)

#Create labels and entry boxes for variables n and p

nlabel = tk.Label(root, text = "n",font = ('Helvetica', 24))
nlabel.pack(pady =20,padx=30)

n_entry = tk.Entry(root)
n_entry.pack(padx=20)

plabel = tk.Label(root, text = "p",font = ('Helvetica', 24))
plabel.pack(pady =20,padx=30)

p_entry = tk.Entry(root)
p_entry.pack(padx=20)

#Create answer button to run function

answer = tk.Button(root,text = "Compute", font = ('Helvetica', 24),command = compute)
answer.pack(pady =20)

#Produces answer when called

hidden_label = tk.Label(root, text = "",font = ('Helvetica', 24))
hidden_label.pack(pady =20)


root.mainloop()