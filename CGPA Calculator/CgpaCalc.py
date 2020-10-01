

from tkinter import *
from tkinter import messagebox

class Home:
    def __init__(self, root):
        self.root = root
        self.header = Label(self.root, text="CGPA Calculator", font=("arial", 20, "bold"))
        self.header.grid(row=0,column=0,columnspan = 2,pady = 8, padx = 8)
        self.no_of_subs_label = Label(self.root, text="Number of Subjects")
        self.nos_entry = Entry(self.root, bg="honeydew", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white")
        self.button = Button(self.root, text="NEXT", bg="#50A8B0", fg="white",width= 25, command=self.add_sub)
        self.no_of_subs_label.grid(row=1,column=0,pady = 8, padx = 8)
        self.nos_entry.grid(row=1,column=1,pady = 8, padx = 8)
        self.button.grid(row=2,column=0,pady = 12,columnspan = 2, padx = 8)

        self.frame_1 = Frame(root,bg='grey')
        self.frame_1.grid(row=4,column=0,pady = 12,columnspan = 2, padx = 8)

        self.frame_2 = Frame(root)
        self.frame_2.grid(row=6, column=0, pady=12, columnspan=2, padx=8)

    def add_sub(self):
        if(self.nos_entry.get().isdigit()!=1):
            messagebox._show("Warning","Invalid Entry!!!")
        else:

            nos = int(self.nos_entry.get())
            self.grade_list_1 = []
            self.credit_list_1 = []
            self.cred_lb_1 = Label(self.frame_1, text="Semister 1",bg='grey', fg="white")
            self.grd_lb_1 = Label(self.frame_1, text="Semister 2",bg='grey', fg="white")
            self.cred_lb_1.grid(row=0, column=0,columnspan=2)
            self.grd_lb_1.grid(row=0, column=4,columnspan=2)
            self.cred_lb_1 = Label(self.frame_1, text="Credits :",bg='grey', fg="white")
            self.grd_lb_1 = Label(self.frame_1, text="Grade :",bg='grey', fg="white")
            self.cred_lb_1.grid(row=1, column=0)
            self.grd_lb_1.grid(row=1, column=1)
            self.grade_list_2 = []
            self.credit_list_2 = []
            self.cred_lb_2 = Label(self.frame_1, text="Credits :",bg='grey', fg="white")
            self.grd_lb_2 = Label(self.frame_1, text="Grade :",bg='grey', fg="white")
            self.cred_lb_2.grid(row=1, column=4)
            self.grd_lb_2.grid(row=1, column=5)
            for i in range(0,nos):
                self.credit_list_1.append(Spinbox(self.frame_1, values=(1, 2, 3, 4, 5),bg='grey', fg="white"))
                self.credit_list_1[i].grid(row=i + 2, column=0, padx=10, pady=10)

                self.grade_list_1.append(Spinbox(self.frame_1, values=("O","A+","A","B+","B","C+","C","D","E","F"),bg='grey', fg="white"))
                self.grade_list_1[i].grid(row=i + 2, column=1, padx=10, pady=10)

                self.credit_list_2.append(Spinbox(self.frame_1, values=(1, 2, 3, 4, 5),bg='grey', fg="white"))
                self.credit_list_2[i].grid(row=i + 2, column=4, padx=10, pady=10)

                self.grade_list_2.append(Spinbox(self.frame_1, values=("O", "A+", "A", "B+", "B", "C+", "C", "D", "E", "F"),bg='grey', fg="white"))
                self.grade_list_2[i].grid(row=i + 2, column=5, padx=10, pady=10)

            self.calc_btn = Button(self.frame_1, text="Calculate CGPA",bg="#50A8B0", fg="white",width= 25, command=self.calc_CG)
            self.calc_btn.grid(row=i + 3, column=0, padx=10, pady=10,columnspan=6)

    def calc_CG(self):
        print("Calculating !")
        credits_this_sem1 = 0
        units_this_sem1 = 0
        credits_this_sem2 = 0
        units_this_sem2 = 0
        nos = int(self.nos_entry.get())
        for j in range(0, nos):
            credits_this_sem1 = credits_this_sem1 + int(self.credit_list_1[j].get()) * ( self.grade(self.grade_list_1[j].get()))
            units_this_sem1 = units_this_sem1 + int(self.credit_list_1[j].get())
            credits_this_sem2 = credits_this_sem2 + int(self.credit_list_2[j].get()) * (self.grade(self.grade_list_2[j].get()))
            units_this_sem2 = units_this_sem2 + int(self.credit_list_2[j].get())

        final_cgpa1 = credits_this_sem1 / (units_this_sem1)
        final_cgpa2 = credits_this_sem2 / (units_this_sem2)
        final_cgpa = (final_cgpa1 + final_cgpa2) / 2

        self.lb1 = Label(self.frame_2, text="TGPA of Sem 1: ")
        self.lb2 = Label(self.frame_2, text="TGPA of Sem 1: ")
        self.lb3 = Label(self.frame_2, text="Total CGPA: ")
        self.cgpa1 = Label(self.frame_2, text=final_cgpa1)
        self.cgpa2 = Label(self.frame_2, text=final_cgpa2)
        self.tot = Label(self.frame_2, text=final_cgpa)

        self.lb1.grid(row=0, column=0)
        self.lb2.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)
        self.cgpa1.grid(row=0, column=1)
        self.cgpa2.grid(row=1, column=1)
        self.tot.grid(row=2, column=1)

    def grade(self, grd):
         dict_ = {"O":10, "A+":9, "A":8, "B+":7, "B":6, "C+":5, "C":4, "D":3, "E":2, "F":0}

         return dict_[grd]

root = Tk()
root.title("Calculator")
obj = Home(root)
root.mainloop()