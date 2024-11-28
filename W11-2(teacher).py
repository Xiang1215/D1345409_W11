from tkinter import *
op=0
val1=0
opCount=0
def btn_click(btn):
    global op,val1,opCount
    if btn['text'] in ['+','-','*','/']:
        val1=float(labl['text'])
        opCount=1
        op=1 if btn['text']=='+' else 2 if btn['text']=='-'else 3 if btn['text']=='*' else 4
    elif btn['text']=='=':
        if op==1:
            val1+=float(labl['text'])
            labl.config(text=str(val1))
        elif op==2:
            val1-=float(labl['text'])
            labl.config(text=str(val1))
        elif op==3:
            val1*=float(labl['text'])
            labl.config(text=str(val1))
        elif op==4:
            val1/=float(labl['text'])
            labl.config(text=str(val1))
        op=0   
    else: 
        if op!=0 :
            if opCount==1:
                labl.config(text=btn['text'])
                opCount=0
            else:
                labl.config(text=labl['text']+btn['text'])
        else:
            if labl['text']=="0":
                labl.config(text=btn['text'])
            else:
                labl.config(text=labl['text']+btn['text'])           

if __name__=="__main__":
    root=Tk()
    root.title("Calculator")
    root.geometry("300x400+200+100")
    
    for i in range (4):
        root.grid_rowconfigure(i,weight=1)
        root.grid_columnconfigure(i,weight=1)
    root.grid_rowconfigure(4,weight=1)   
    
    labl=Label(root,text="0",
               font=('Arial',20),
               bg="#ffcc99",
               justify=RIGHT,anchor=E)
    labl.grid(row=0,column=0,columnspan=4,sticky=NSEW)
    btn_labs=["7","8","9","/",
              "4","5","6","*",
              "1","2","3","-",
              "0",".","=","+"]
    
    btns=[]
    for i in range(4):
        for j in range(4):
            btns.append(Button(root,text=btn_labs[i*4+j],
                               font=('Arial',20)))
            btns[-1].config(command=lambda btn=btns[-1]:btn_click(btn))
            btns[-1].grid(row=i+1,column=j,sticky=NSEW)
            
    root.resizable(0,0)
    root.mainloop()