from tkinter import *
count=0
a=0
b=None
def countFun(lbl,type):   
    global count,a,b
    if type=='0':
        count=0
        lbl.config(text=str(count))
    elif type=='1':
        count=1
        lbl.config(text=str(count))
    elif type=='2':
        count=2
        lbl.config(text=str(count))
    elif type=='3':
        count=3
        lbl.config(text=str(count))
    elif type=='4':
        count=4
        lbl.config(text=str(count))
    elif type=='5':
        count=5
        lbl.config(text=str(count))
    elif type=='6':
        count=6
        lbl.config(text=str(count))
    elif type=='7':
        count=7
        lbl.config(text=str(count))
    elif type=='8':
        count=8
        lbl.config(text=str(count))
    elif type=='9':
        count=9
        lbl.config(text=str(count))
    
    if type=='+':
        b='+'
        a = count  
        count = 0
        lbl.config(text=str(b))
    elif type=='-':
        b='-'
        a = count  
        count = 0
        lbl.config(text=str(b))
    elif type=='*':
        b='*'
        a = count  
        count = 0
        lbl.config(text=str(b))
    elif type=='/':
        b='/'
        a = count  
        count = 0
        lbl.config(text=str(b))
        
    if type=='=':
        if b is not None:
            if b=='+':
                count=a+count
                lbl.config(text=str(count))
                b=None
            elif b=='-':
                count=a-count
                lbl.config(text=str(count))
                b=None
            elif b=='*':
                count=a*count
                lbl.config(text=str(count))
                b=None
            elif b=='/':
                if count!=0:
                    count=round(a/count)
                    
                else:
                    count=0  
                lbl.config(text=str(count))
                b=None
            
            
    if type=='C': 
        count=0
        a=0
        lbl.config(text="0")
        
    
    
if __name__=="__main__":
    root=Tk()
    root.title("計算機")
    root.geometry("375x140+100+50")
    
    lbl=Label(root,width=20,height=2,bg="#ccddff",
              font=("Times New Roman",20,"bold"),
              text="0",justify=RIGHT)
    lbl.grid(row=0,column=0,sticky=NSEW,pady=5,padx=3,columnspan=50)
    
    divBtn=Button(root,text="/",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="black",
                  command=lambda:countFun(lbl,"/"))
    divBtn.grid(row=1,column=3,sticky=W,pady=5,padx=3)
    
    multBtn=Button(root,text="*",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="black",
                  command=lambda:countFun(lbl,"*"))
    multBtn.grid(row=2,column=3,sticky=W,pady=5,padx=3)
    
    subBtn=Button(root,text="-",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="black",
                  command=lambda:countFun(lbl,"-"))
    subBtn.grid(row=3,column=3,sticky=W,pady=5,padx=3)
    
    addBtn=Button(root,text="+",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="black",
                  command=lambda:countFun(lbl,"+"))
    addBtn.grid(row=4,column=3,sticky=W,pady=5,padx=3)
    
    
    oneBtn=Button(root,text="1",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="blue",
                  command=lambda:countFun(lbl,"1"))
    oneBtn.grid(row=1,column=0,sticky=W,pady=5,padx=3)
    
    twoBtn=Button(root,text="2",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="blue",
                  command=lambda:countFun(lbl,"2"))
    twoBtn.grid(row=1,column=1,sticky=W,pady=5,padx=3)
    
    thrBtn=Button(root,text="3",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="blue",
                  command=lambda:countFun(lbl,"3"))
    thrBtn.grid(row=1,column=2,sticky=W,pady=5,padx=3)
    
    forBtn=Button(root,text="4",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="blue",
                  command=lambda:countFun(lbl,"4"))
    forBtn.grid(row=2,column=0,sticky=W,pady=5,padx=3)
    
    fivBtn=Button(root,text="5",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="blue",
                  command=lambda:countFun(lbl,"5"))
    fivBtn.grid(row=2,column=1,sticky=W,pady=5,padx=3)
    
    sixBtn=Button(root,text="6",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="blue",
                  command=lambda:countFun(lbl,"6"))
    sixBtn.grid(row=2,column=2,sticky=W,pady=5,padx=3)
    
    sevBtn=Button(root,text="7",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="blue",
                  command=lambda:countFun(lbl,"7"))
    sevBtn.grid(row=3,column=0,sticky=W,pady=5,padx=3)
    
    eigBtn=Button(root,text="8",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="blue",
                  command=lambda:countFun(lbl,"8"))
    eigBtn.grid(row=3,column=1,sticky=W,pady=5,padx=3)
    
    nineBtn=Button(root,text="9",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="blue",
                  command=lambda:countFun(lbl,"9"))
    nineBtn.grid(row=3,column=2,sticky=W,pady=5,padx=3)
    
    zeroBtn=Button(root,text="0",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="blue",
                  command=lambda:countFun(lbl,"0"))
    zeroBtn.grid(row=4,column=1,sticky=W,pady=5,padx=3)


    noneBtn=Button(root,text="C",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="black",
                  command=lambda:countFun(lbl,"C"))
    noneBtn.grid(row=4,column=0,sticky=W,pady=5,padx=3)

    resBtn=Button(root,text="=",bg="#ffcc99",
                  font=("Times New Roman",20,"bold"),
                  width=8,height=2,fg="black",
                  command=lambda:countFun(lbl,"="))
    resBtn.grid(row=4,column=2,sticky=W,pady=5,padx=3)   
    
    root.mainloop()