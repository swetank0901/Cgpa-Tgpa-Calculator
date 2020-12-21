from tkinter import *
import tkinter.messagebox as boxx
z=[];
def tgpaf():
    cg1=2;
    cg2=4;
    def grade(g,c): 
        g=str(g);
        cc=int(c);
        if g=='O' and cc==2:
            return(10*2)
        elif g=="O" and cc==4:
            return(10*4)
        elif g=="A+" and cc==2:
            return(9*2)
        elif g=="A+" and cc==4:
            return(9*4)
        elif g=="A" and cc==2:
            return(8*2)
        elif g=="A" and cc==4:
            return(8*4)
        elif g=="B+" and cc==2:
            return(7*2)
        elif g=="B+" and cc==4:
            return(7*2)
        elif g=="B" and cc==2:
            return(6*2)
        elif g=="B" and cc==4:
            return(6*4)
        elif g=="C" and cc==2:
            return(5*2)
        elif g=="C" and cc==4:
            return(5*4)
    
    def tgpa22():
        to_point=0;
        subg21=ge21.get()
   # print(subg1)
        subc21=int(ce21.get())
        subgg21=grade(subg21,subc21)
        print(subgg21)
    #box.showinfo("showinfo",subg1)
        subg22=ge22.get()
        subc22=int(ce22.get())
        subgg22=grade(subg22,subc22)
        print(subgg22)
    
        subg23=ge23.get()
        subc23=int(ce23.get())
        subgg23=grade(subg23,subc23)
        print(subgg23)
    
        subg24=ge24.get()
        subc24=int(ce24.get())
        subgg24=grade(subg24,subc24)
        print(subgg24)
    
        subg25=ge25.get()
        subc25=int(ce25.get())
        subgg25=grade(subg25,subc25)
        print(subgg25)
    
        subg26=ge26.get()
        subc26=int(ce26.get())
        subgg26=grade(subg26,subc26)
        print(subgg26)

        to_point=subgg21+subgg22+subgg23+subgg24+subgg25+subgg26
        print(to_point)
        #aa=ce1.get()+ce2.get()+ce3.get()+ce4.get()+ce5.get()+ce6.get()
        #print(aa)
        to_cradit=subc21+subc22+subc23+subc24+subc25+subc26
        print(to_cradit)
        tg_pa2= to_point/to_cradit
        
        #boxx.showinfo("showinfo",tg_pa2)
        x.set(tg_pa2)
        return (tg_pa2);
    def tgpa11():
        to_point=0;
        subg1=ge1.get()
   # print(subg1)
        subc1=int(ce1.get())
        subgg1=grade(subg1,subc1)
        print(subgg1)
    #box.showinfo("showinfo",subg1)
        subg2=ge2.get()
        subc2=int(ce2.get())
        subgg2=grade(subg2,subc2)
        print(subgg2)
    
        subg3=ge3.get()
        subc3=int(ce3.get())
        subgg3=grade(subg3,subc3)
        print(subgg3)
    
        subg4=ge4.get()
        subc4=int(ce4.get())
        subgg4=grade(subg4,subc4)
        print(subgg4)
    
        subg5=ge5.get()
        subc5=int(ce5.get())
        subgg5=grade(subg5,subc5)
        print(subgg5)
    
        subg6=ge6.get()
        subc6=int(ce6.get())
        subgg6=grade(subg6,subc6)
        print(subgg6)

        to_point=subgg1+subgg2+subgg3+subgg4+subgg5+subgg6
        print(to_point)
    #aa=ce1.get()+ce2.get()+ce3.get()+ce4.get()+ce5.get()+ce6.get()
    #print(aa)
        to_cradit=subc1+subc2+subc3+subc4+subc5+subc6
        print(to_cradit)
        tg_pa1= to_point/to_cradit
        #boxx.showinfo("showinfo",tg_pa1)
        x1.set(tg_pa1)
        return(tg_pa1)

    
    def tg1():
        cg3=0;
        #print(cg1);
        cg3=tgpa11()
        print(cg3);
        z.append(cg3)
        print("tgpa1",z[0])
    def tg2():
       cg2=tgpa22()
       z.append(cg2)
       print("tgpa1",z[0])
       print("tgpa2",z[1])

    def cgpa():
        tgpa1=z[0];
        tgpa2=z[1];
        cgp=(tgpa1+tgpa2)/2
        print("tgpa1",tgpa1);
        print("tgpa2",tgpa2);
        print("cgpa",cgp);
        #boxx.showinfo("showinfo",cgp)
        x22.set(cgp)

    
    #from tkinter import *
    root=Tk()
    root.geometry("750x950")
    root.title('tgpa')
    root.configure(background="purple");
#line=canvas.create_line(1,90,208900,390,fill='black',width=2)
#l1=Label(root,text="SVS COLLEGE OF ENGINEERING",width=30,font=("bold",20))
#l1.place(x=10,y=49)
    sem1=Label(root,text="SEM 1",width=10,font=("bold",15),fg="black",bg="grey")
    sem1.place(x=250,y=10)
    g1=Label(root,text="GRADE",width=10,font=("bold",15),fg="yellow",bg="purple")
    g1.place(x=200,y=50)
    g1=Label(root,text="CREDIT",width=10,font=("bold",15),fg="yellow",bg="purple")
    g1.place(x=380,y=50)
    sub1=Label(root,text="1.PHYSICS",width=10,font=("bold",15),fg="white",bg="purple")
    sub1.place(x=20,y=100)
    ge1=Entry(root)
    ge1.place(x=200,y=105)
    ce1=Entry(root)
    ce1.place(x=380,y=105)

    sub2=Label(root,text="2.C",width=5,font=("bold",15),fg="white",bg="purple")
    sub2.place(x=20,y=140)
    ge2=Entry(root) 
    ge2.place(x=200,y=140)
    ce2=Entry(root)
    ce2.place(x=380,y=140)

    sub3=Label(root,text="3.MATHS",width=10,font=("bold",15),fg="white",bg="purple")
    sub3.place(x=20,y=180)
    ge3=Entry(root)
    ge3.place(x=200,y=180)
    ce3=Entry(root)
    ce3.place(x=380,y=180)

    sub4=Label(root,text="4.ELECTRONICS",width=15,font=("bold",15),fg="white",bg="purple")
    sub4.place(x=25,y=215)
    ge4=Entry(root)
    ge4.place(x=200,y=220)
    ce4=Entry(root)
    ce4.place(x=380,y=220)


    sub5=Label(root,text="5.ENGLISH",width=10,font=("bold",15),fg="white",bg="purple")
    sub5.place(x=25,y=255)
    ge5=Entry(root)
    ge5.place(x=200,y=255)
    ce5=Entry(root)
    ce5.place(x=380,y=255)

    sub6=Label(root,text="6.C LAB",width=10,font=("bold",15),fg="white",bg="purple")
    sub6.place(x=13,y=290)
    ge6=Entry(root)
    ge6.place(x=200,y=295)
    ce6=Entry(root)
    ce6.place(x=380,y=295)

    tgpa1=Button(root,text="TGPA1",width=6,font=("bold",10),fg="white",bg="brown",command=tg1)
    tgpa1.place(x=537,y=215)
    x1=StringVar()
    E1=Entry(root,textvariable=x1)
    E1.place(x=620,y=225)

    sem2=Label(root,text="SEM 2",width=10,font=("bold",15),fg="black",bg="grey")
    sem2.place(x=250,y=350)
    g2=Label(root,text="GRADE",width=10,font=("bold",15),fg="yellow",bg="purple")
    g2.place(x=200,y=390)
    g2=Label(root,text="CREDIT",width=10,font=("bold",15),fg="yellow",bg="purple")
    g2.place(x=380,y=390)
    sub21=Label(root,text="1.CHE110",width=10,font=("bold",15),fg="white",bg="purple")
    sub21.place(x=20,y=435)
    ge21=Entry(root)
    ge21.place(x=200,y=440)
    ce21=Entry(root)
    ce21.place(x=380,y=440)

    sub22=Label(root,text="2. CSE202",width=10,font=("bold",15),fg="white",bg="purple")
    sub22.place(x=20,y=470)
    ge22=Entry(root)
    ge22.place(x=200,y=470)
    ce22=Entry(root)
    ce22.place(x=380,y=470)

    sub23=Label(root,text="3.CSE326(LAB)",width=15,font=("bold",15),fg="white",bg="purple")
    sub23.place(x=15,y=505)
    ge23=Entry(root)
    ge23.place(x=200,y=507)
    ce23=Entry(root)
    ce23.place(x=380,y=507)

    sub24=Label(root,text="4.ECE213",width=10,font=("bold",15),fg="white",bg="purple")
    sub24.place(x=15,y=545)
    ge24=Entry(root)
    ge24.place(x=200,y=547)
    ce24=Entry(root)
    ce24.place(x=380,y=547)


    sub25=Label(root,text="5.MEC107",width=10,font=("bold",15),fg="white",bg="purple")
    sub25.place(x=17,y=580)
    ge25=Entry(root)
    ge25.place(x=200,y=580)
    ce25=Entry(root)
    ce25.place(x=380,y=580)

    sub26=Label(root,text="6.ECE216(LAB)",width=15,font=("bold",15),fg="white",bg="purple")
    sub26.place(x=13,y=620)
    ge26=Entry(root)
    ge26.place(x=200,y=624)
    ce26=Entry(root)
    ce26.place(x=380,y=624)

    tgpa2=Button(root,text="TGPA2",width=7,font=("bold",10),fg="white",bg="brown",command=tg2)
    tgpa2.place(x=537,y=530)
    x=StringVar()
    E2=Entry(root,textvariable=x)
    E2.place(x=620,y=540)

    tgpa2=Button(root,text="CGPA",width=7,font=("bold",10),fg="white",bg="brown",command=cgpa)
    tgpa2.place(x=250,y=650)
    x22=StringVar()
    E22=Entry(root,textvariable=x22)
    E22.place(x=324,y=650)
    root.mainloop()
tgpaf()
