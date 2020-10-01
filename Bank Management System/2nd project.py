

import tkinter as tk

name1='Avdhoot Patil'
pinc1=1234
bal=23556
acc_no1=123456789
acc2_no=123456788
#1    
root= tk.Tk()

canvas=tk.Canvas(root,height=500,width=650,bg='#99ccff')
canvas.pack()

mlabel=tk.Label(root,text="Enter PIN",font=("impact",30),bg='#00004d',fg='White')
mlabel.place(relx=0.3,rely=0.3,relwidth=0.60,relheight=0.1)

epin=tk.Entry(root)
epin.place(relx=0.3,rely=0.5,relwidth=0.40,relheight=0.1)

compute=tk.Button(root,text="enter",font="impact",bg='red',fg='White',bd=2,command=lambda:pin(int(epin.get())))
compute.place(relx=0.7,rely=0.7,relwidth=0.2,relheight=0.12)
 
root.mainloop()
def main():
    #1      
    broot= tk.Tk()

    canvas=tk.Canvas(broot,height=500,width=650,bg='#99ccff')
    canvas.pack()

    mlabel=tk.Label(broot,text="Enter PIN",font=("impact",30),bg='#00004d',fg='White')
    mlabel.place(relx=0.3,rely=0.3,relwidth=0.60,relheight=0.1)

    epin=tk.Entry(broot)
    epin.place(relx=0.3,rely=0.5,relwidth=0.40,relheight=0.1)

    compute=tk.Button(broot,text="enter",font="impact",bg='red',fg='White',bd=2,command=lambda:pin(int(epin.get())))
    compute.place(relx=0.7,rely=0.7,relwidth=0.2,relheight=0.12)

    broot.mainloop()

def pin(p):
    a=bal
    if p==pinc1:
        
        #3
        options(a)

        
    else:
        #2
        aroot= tk.Tk()

        canvas=tk.Canvas(aroot,height=500,width=650,bg='red')
        canvas.pack()
        alabel=tk.Label(aroot,text=(f"Wrong Password"),font=("impact",30),bg='#00004d',fg='White')
        alabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        acompute=tk.Button(aroot,text="return",font="impact",bg='red',fg='White',bd=2,command=lambda:main())
        acompute.place(relx=0.3,rely=0.8,relwidth=0.2,relheight=0.12)


        aroot.mainloop()





def options(bal):
    #3
    proot= tk.Tk()

    canvas=tk.Canvas(proot,height=500,width=650,bg='#99ccff')
    canvas.pack()

    bcompute=tk.Button(proot,text="Withdraw",font="impact",bg='red',fg='White',bd=2,command=lambda:withdrawl(bal))#4
    bcompute.place(relx=0.4,rely=0.3,relwidth=0.2,relheight=0.12)
    ccompute=tk.Button(proot,text="Mini Statement",font="impact",bg='red',fg='White',bd=2,command=lambda:Mini_Statement(bal))#6
    ccompute.place(relx=0.4,rely=0.4,relwidth=0.2,relheight=0.12)
    dcompute=tk.Button(proot,text="Transfer",font="impact",bg='red',fg='White',bd=2,command=lambda:Transfer(bal))#7
    dcompute.place(relx=0.4,rely=0.5,relwidth=0.2,relheight=0.12)
    c=tk.Button(proot,text="back",font="impact",bg='red',fg='White',bd=2,command=lambda:main())
    c.place(relx=0.7,rely=0.7,relwidth=0.2,relheight=0.12)
    
    proot.mainloop()

        
def withdrawl(bal):
    
    
    #4
    wroot= tk.Tk()
    canvas=tk.Canvas(wroot,height=500,width=650,bg='#99ccff')
    canvas.pack()
    
    label=tk.Label(wroot,text=(f"available amount :{bal}"),font=("impact",30),bg='#00004d',fg='White')
    label.place(relx=0.1,rely=0.2,relwidth=0.60,relheight=0.1)

    ecompute=tk.Button(wroot,text="Submit",font="impact",bg='red',fg='White',bd=2,command=lambda:withdrawl_check(bal,int(amount.get())))
    ecompute.place(relx=0.7,rely=0.7,relwidth=0.2,relheight=0.12)
    
    c=tk.Button(wroot,text="return",font="impact",bg='red',fg='White',bd=2,command=lambda:options(bal))
    c.place(relx=0.3,rely=0.7,relwidth=0.2,relheight=0.12)


    flabel=tk.Label(wroot,text="Enter Amount",font=("impact",30),bg='#00004d',fg='White')
    flabel.place(relx=0.3,rely=0.3,relwidth=0.60,relheight=0.1)

    amount=tk.Entry(wroot)
    amount.place(relx=0.3,rely=0.5,relwidth=0.40,relheight=0.1)

    wroot.mainloop()
    

    
def withdrawl_check(bal,amount):
    #5
    oroot= tk.Tk()
   
    canvas=tk.Canvas(oroot,height=500,width=650,bg='red')
    canvas.pack()
    if ((bal-amount)<0):
        glabel=tk.Label(oroot,text=(f"insufficient balance"),font=("impact",30),bg='#00004d',fg='White')
       
    else:
        glabel=tk.Label(oroot,text=(f"Available balance : {bal-amount}"),font=("impact",30),bg='#00004d',fg='White')
        bal=bal-amount
    
    c=tk.Button(oroot,text="return",font="impact",bg='red',fg='White',bd=2,command=lambda:options(bal))
    c.place(relx=0.3,rely=0.7,relwidth=0.2,relheight=0.12)
    glabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    
    
    oroot.mainloop()
    
    
def Mini_Statement(bal):
    #6
    croot= tk.Tk()
    canvas=tk.Canvas(croot,height=500,width=650,bg='#99ccff')
    canvas.pack()

    hlabel=tk.Label(croot,text=(f"Name :{name1}"),font=("impact",20),bg='#00004d',fg='White')
    hlabel.place(relx=0.3,rely=0.3,relwidth=0.60,relheight=0.1)
    ilabel=tk.Label(croot,text=(f"account No. :{acc_no1}"),font=("impact",20),bg='#00004d',fg='White')
    ilabel.place(relx=0.3,rely=0.4,relwidth=0.60,relheight=0.1)
    jlabel=tk.Label(croot,text=(f"Balance :{bal}"),font=("impact",20),bg='#00004d',fg='White')
    jlabel.place(relx=0.3,rely=0.5,relwidth=0.60,relheight=0.1)    
    c=tk.Button(croot,text="return",font="impact",bg='red',fg='White',bd=2,command=lambda:options(bal))
    c.place(relx=0.3,rely=0.7,relwidth=0.2,relheight=0.12)  
    
    croot.mainloop()

    
def Transfer(bal):
    #7
    droot= tk.Tk()
    canvas=tk.Canvas(droot,height=500,width=650,bg='#99ccff')
    canvas.pack()

    klabel=tk.Label(droot,text="Account no.",font=("impact",30),bg='#00004d',fg='White')
    klabel.place(relx=0.3,rely=0.2,relwidth=0.60,relheight=0.1)

    acc_no=tk.Entry(droot)
    acc_no.place(relx=0.3,rely=0.3,relwidth=0.40,relheight=0.1)
    
    llabel=tk.Label(droot,text="Amount",font=("impact",30),bg='#00004d',fg='White')
    llabel.place(relx=0.3,rely=0.4,relwidth=0.60,relheight=0.1)

    ammount=tk.Entry(droot)
    ammount.place(relx=0.3,rely=0.5,relwidth=0.40,relheight=0.1)
    
  
    
    c=tk.Button(droot,text="proceed",font="impact",bg='red',fg='White',bd=2,command=lambda:check_transfer(bal,int(acc_no.get()),int(ammount.get())))
    c.place(relx=0.3,rely=0.7,relwidth=0.2,relheight=0.12)


    
    
    droot.mainloop()   
    
     
def check_transfer(bal,acc,amt):
    #8
    
    if acc==acc2_no and amt<=bal:
        eroot= tk.Tk()
        canvas=tk.Canvas(eroot,height=500,width=650,bg='blue')
        canvas.pack()
        nlabel=tk.Label(eroot,text=(f"sucessfully transfer"),font=("impact",30),bg='#00004d',fg='White')
        olabel=tk.Label(eroot,text=(f"Available balance : {bal-amt}"),font=("impact",20),bg='#00004d',fg='White')
        nlabel.place(relx=0.1,rely=0.2,relwidth=0.4,relheight=0.1)
        olabel.place(relx=0.3,rely=0.4,relwidth=0.4,relheight=0.1)
        c=tk.Button(eroot,text="return",font="impact",bg='red',fg='White',bd=2,command=lambda:options(bal-amt))
        c.place(relx=0.3,rely=0.7,relwidth=0.2,relheight=0.12)
    
        eroot.mainloop()
       
    else:
        eroot= tk.Tk()
        canvas=tk.Canvas(eroot,height=500,width=650,bg='blue')
        canvas.pack()
        plabel=tk.Label(eroot,text=(f"wrong input"),font=("impact",30),bg='#00004d',fg='White')
        plabel.place(relx=0.1,rely=0.4,relwidth=0.5,relheight=0.1)
        
        c=tk.Button(eroot,text="previous",font="impact",bg='red',fg='White',bd=2,command=lambda:Transfer(bal))
        c.place(relx=0.3,rely=0.7,relwidth=0.4,relheight=0.12)
        c=tk.Button(eroot,text="return",font="impact",bg='red',fg='White',bd=2,command=lambda:options(bal))
        c.place(relx=0.7,rely=0.7,relwidth=0.4,relheight=0.12)
    
        eroot.mainloop()





