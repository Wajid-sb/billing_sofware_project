import tkinter
from tkinter import*
import random,os
from tkinter import messagebox
import  mysql.connector
os.chdir(r"D:\my_codings\python_projects")
class bill_app:
    def __init__(self,root):# root is the our windows name
        self.root=root
        self.root.geometry("1350x700+0+0") #selttig geometry 
        self.root.title("billing software ")
        bg_color='#074463'
        title=Label(self.root,text='BILLING SOFTWARE ',bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",27,"bold"),pady=2)
        title.pack(fill=X)

        #-------------------customer detail---------------------------
        frame1=LabelFrame(self.root,text='customer detail',font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=8)
        frame1.place(x=0,y=70,relwidth=1) #y is 80 because relwidth = 1 because it will take equal to the parent width
        
        customer_label=Label(frame1,text="Customer_Name :",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        customer_label.grid(row=0,column=0,padx=20,pady=5)

        self.name_var=StringVar()
        customer_entry=Entry(frame1,width=20,font="arial 15",bd=7,textvariable=self.name_var,relief=SUNKEN)
        customer_entry.grid(row=0,column=1,padx=10,pady=5)

        phone_label=Label(frame1,text="phone :",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        phone_label.grid(row=0,column=2,padx=10,pady=5)

        self.phone_var=IntVar()
        phone_entry=Entry(frame1,width=20,font="arial 15",bd=7,textvariable=self.phone_var,relief=SUNKEN)
        phone_entry.grid(row=0,column=3,padx=10,pady=5)

        bill_number_label=Label(frame1,text="Bill number :",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        bill_number_label.grid(row=0,column=4,padx=10,pady=5)
        self.bill_number_var=IntVar()
        x=random.randint(1000, 9999)
        self.bill_number_var.set(x)
        bill_number_entry=Entry(frame1,width=20,font="arial 15",bd=7,textvariable=self.bill_number_var,relief=SUNKEN)
        bill_number_entry.grid(row=0,column=5,padx=10,pady=5)

        bill_btn=Button(frame1,text="search",width=10,bd=7,font="arial 12 bold",command=self.find_bill)
        bill_btn.grid(row=0,column=6,padx=5,pady=5)
    
    #------------------------cosmetic deatail-------------
        cosatics_frame=LabelFrame(self.root,text="cosmetic detail",bd=7,relief=GROOVE,font=("arial 12 bold",15,"bold"),bg=bg_color,fg="yellow")
        cosatics_frame.place(x=5,y=160,width=325,height=380)
        

        # bath_soap=Label(cosatics_frame,text="Bath Soap",)
        cosmatics_names=['Bath soaps','Face Cream','Face Wash','Hair Spray','Hair get','body Loshan']
        self.cosmetic_entry={
            "bath_soap":IntVar(),
            "Face_soap":IntVar(),
            "Face_wash":IntVar(),
            "Hair_-spray":IntVar(),
            "Hair_gel":IntVar(),
            "Body_spray":IntVar()
        }
        count=0
        for i in range(len(cosmatics_names)):
            labels='label'+str(i)
            labels=Label(cosatics_frame,text=cosmatics_names[i],fg="white",font=("times new roman",15,"bold"),bg=bg_color)
            labels.grid(row=i,column=0,padx=15,pady=10,sticky="W")
       

        for i in self.cosmetic_entry:
            entry_labels="entry"+i
            entry_labels=Entry(cosatics_frame,width=10,font="arial 15",bd=7,relief=SUNKEN,textvariable=self.cosmetic_entry[i])
            entry_labels.grid(row=count,column=1,padx=15,pady=10,sticky="W")
            count+=1
            
        #----------------grocery frame---------------------------
        grocery_frame=LabelFrame(self.root,text="Geocery",bd=7,relief=GROOVE,font=("arial 12 bold",15,"bold"),bg=bg_color,fg='yellow')
        grocery_frame.place(x=340,y=160,width=325,height=380)

        grocery_names=['Rice','Food Oil','Daal','Wheat','sugar','Tea']
        for i in range(len(grocery_names)):
            grocery_labels='lables'+str(i)
            grocery_labels=Label(grocery_frame,text=grocery_names[i],bg=bg_color,font=("times new roman",15,"bold"),fg="white")
            grocery_labels.grid(row=i,column=0,padx=15,pady=15,sticky='W')
        
        self.grocery_entyr={
            "Rice":IntVar(),
            "Food oil":IntVar(),
            "Daal":IntVar(),
            "Wheat":IntVar(),
            "Sugar":IntVar(),
            "Tea":IntVar()
        }
        count=0
        for i in self.grocery_entyr:
            entry_labels=i.strip()
            entry_labels=Entry(grocery_frame,width=10,font="arial 15",bd=7,relief=SUNKEN,textvariable=self.grocery_entyr[i])
            entry_labels.grid(row=count,column=1,padx=25,pady=5)
            count+=1

        #-------------cold detail frame----------------------
        cold_frame=LabelFrame(self.root,text="Geocery",bd=7,relief=GROOVE,font=("arial 12 bold",15,"bold"),bg=bg_color,fg='yellow')
        cold_frame.place(x=675,y=160,width=325,height=380)

        cold_names=['Maza','Thumbs up','Sprite','7up','Pepsi','String']
        for i in range(len(cold_names)):
            cold_labels='lables'+str(i)
            cold_labels=Label(cold_frame,text=cold_names[i],bg=bg_color,font=("times new roman",15,"bold"),fg="white")
            cold_labels.grid(row=i,column=0,padx=15,pady=15,sticky='W')
        
        self.cold_entyr={
            "Maza":IntVar(),
            "thums up":IntVar(),
            "Sprite":IntVar(),
            "7up":IntVar(),
            "Pepsi":IntVar(),
            "String":IntVar()
        }
        count=0
        for i in self.cold_entyr:
            entry_labels=i
            entry_labels=Entry(cold_frame,width=10,font="arial 15",bd=7,relief=SUNKEN,textvariable=self.cold_entyr[i])
            entry_labels.grid(row=count,column=1,padx=25,pady=5)
            count+=1

        #------------bill area--------------
        Bill_frame=Frame(self.root,relief=GROOVE,bd=7)
        Bill_frame.place(x=1010,y=160,width=325,height=380)
        bill_title=Label(Bill_frame,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE)
        bill_title.pack(fill=X)
        
        self.textarea=Text(Bill_frame)
        scroll_bar=Scrollbar(Bill_frame,orient=VERTICAL)
        scroll_bar.pack(side=RIGHT,fill=Y)
        scroll_bar.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=scroll_bar.set)
        self.textarea.pack(fill=BOTH,expand=1)

        # 3---------------billing menu--------------------
        billing_menu=LabelFrame(self.root,text="Billing menu",bg=bg_color,bd=7,fg="yellow",font="arial 15 bold")
        billing_menu.place(x=0,y=545,relwidth=1,height=150)

        cosmetic_price=Label(billing_menu,text="total cosmetic price",bg=bg_color,fg="white",font=("times new roman",15,'bold'))
        cosmetic_price.grid(row=0,column=0,padx=15,pady=2,sticky="W")
        
        cosmetic_price=Label(billing_menu,text="total Grocery price",bg=bg_color,fg="white",font=("times new roman",15,'bold'))
        cosmetic_price.grid(row=1,column=0,padx=15,pady=2,sticky="W")

        cosmetic_price=Label(billing_menu,text="total Cold Drink price",bg=bg_color,fg="white",font=("times new roman",15,'bold'))
        cosmetic_price.grid(row=2,column=0,padx=15,pady=2,sticky="W")
        
        self.price_vars={
            'cosmatic_price':IntVar(),
            'grocery_price':IntVar(),
            'cold_drink_price':IntVar()
        }

        count=0
        for i in self.price_vars:
            billing_price_entry="billing_price"+str(i)
            billing_price_entry=Entry(billing_menu,width=25,bd=7,relief=SUNKEN,textvariable=self.price_vars[i])
            billing_price_entry.grid(row=count,column=1,padx=15,pady=2)
            count+=1

        tax_names=['Cesmatic tax',"grocery tax",'Cold Drink tax']
        for i in range(len(tax_names)):
            label_tax=tax_names[i].strip()+'_labels'
            label_tax=Label(billing_menu,text=tax_names[i],bg=bg_color,fg="white",font=("times new roman",15,"bold"))
            label_tax.grid(row=i,column=2,padx=15,pady=2,sticky="W")
        
        self.tax_vars={
            'cosmatic_tax':IntVar(),
            'grocery_tax':IntVar(),
            'cold_drink_tax':IntVar()
        }

        count=0
        for i in self.tax_vars:
            billing_tax_entry="billing_tax"+str(i)
            billing_tax_entry=Entry(billing_menu,width=25,bd=7,relief=SUNKEN,textvariable=self.tax_vars[i])
            billing_tax_entry.grid(row=count,column=3,padx=15,pady=2)
            count+=1

        btn_frames=Frame(billing_menu,relief=GROOVE,bd=7)
        btn_frames.place(x=770,y=0,width=560,height=105)

        total_btn=Button(btn_frames,text="Total",bg="cadetblue",fg="white",pady=13,width=11,font="arail 12 bold",bd=5,command=self.total)
        total_btn.grid(row=0,column=0,padx=5,pady=2)

        generate_b_btn=Button(btn_frames,text="Generat bill",command=self.bill_area,bg="cadetblue",fg="white",pady=13,width=11,font="arail 12 bold",bd=5)
        generate_b_btn.grid(row=0,column=1,padx=5,pady=2)
        
        Clear_btn=Button(btn_frames,text="Clear",command=self.clear,bg="cadetblue",fg="white",pady=13,width=11,font="arail 12 bold",bd=5)
        Clear_btn.grid(row=0,column=2,padx=5,pady=2)

        Exit_btn=Button(btn_frames,text="Exit",command=self.add,bg="cadetblue",fg="white",pady=13,width=11,font="arail 12 bold",bd=5)
        Exit_btn.grid(row=0,column=3,padx=5,pady=2)
        
        self.welcome_bill()
    

        # -------------funtionality of all widgets-----------------
        # for i in self.cosmetic_entry:
        #     # cosmetic_vars=str(i)+'var'
        #     cosmetic_vars=self.cosmetic_entry[i].get()
        
        # for i in self.grocery_entyr:
        #     grocery_var=self.grocery_entyr[i].get()

        #functionality for the tax removing from the total amount
    def cosmatic_sum(self):
        self.cosmatics_prices=[40,120,60,180,140,100]
        self.sum=0
        self.cosmaics_itmes=[]
        count=0
        for i in self.cosmetic_entry:
            self.cosmaics_itmes.append(self.cosmatics_prices[count]*self.cosmetic_entry[i].get())
            count+=1
        for j in range(len(self.cosmaics_itmes)):
            self.sum=self.sum+self.cosmaics_itmes[j]
        # self.cosmatic_total()
        self.sum=float(self.sum)
        self.price_vars['cosmatic_price'].set(str(self.sum))
        self.tax_vars['cosmatic_tax'].set(str(round((self.sum*0.05),2)))
        # print(self.sum)
    # def cosmatic_total(self):
    def grocery_sum(self):
        self.grocery_rate=[120,34,12,453,213,123]
        self.sum_grocery=0
        self.grocey_values=[]
        count=0
        for i in self.grocery_entyr:
            self.grocey_values.append(self.grocery_rate[count]*self.grocery_entyr[i].get())
            count+=1
        for j in range(len(self.grocey_values)):
            self.sum_grocery=self.sum_grocery+self.grocey_values[j]
        # print(self.sum_grocery)
        # print(self.grocey_values)
        self.sum_grocery=float(self.sum_grocery)
        self.price_vars['grocery_price'].set(str(self.sum_grocery))
        self.tax_vars['grocery_tax'].set(str(round((self.sum_grocery*0.05),2)))
        

    def total(self):
        # global price_vars
        
        # for i in self.cosmetic_entry:
            # self.cosmaics_itmes.append(self.cosmetic_entry.get()*self.cosmatics_prices[i])
        # for i in self.cosmaics_itmes:
        #     # self.sum=self.sum+cosmaics_itmes
        #     self.sum=sum(self.cosmaics_itmes)
        # for i in self.cosmetic_entry:
        #     self.sum=self.sum+self.cosmetic_entry[i].get()
        # print(self.sum)
        
        # for j in self.cosmatics_prices:
        self.cosmatic_sum()
        # self.cosmatics_prices=[40,120,60,180,140,100]
        # self.sum=0
        # self.cosmaics_itmes=[]
        # self.sum=float(self.sum)
        # count=0
        # for i in self.cosmetic_entry:
        #     self.cosmaics_itmes.append(self.cosmatics_prices[count]*self.cosmetic_entry[i].get())
        #     count+=1


        # for j in range(len(self.cosmaics_itmes)):
        #     self.sum=self.sum+self.cosmaics_itmes[j]
        # # print(self.sum)
        
        # self.price_vars['cosmatic_price'].set(str(self.sum))
        # self.tax_vars['cosmatic_tax'].set(str(round((self.sum*0.05),2)))
        
        self.grocery_sum()
        #get the all vlaus from the grocery 
        # self.grocery_rate=[120,34,12,453,213,123]
        # self.grocey_values=[]
        # self.sum_grocery=0
        # count=0
        # for i in self.grocery_entyr:
        #     self.grocey_values.append(self.grocery_rate[count]*self.grocery_entyr[i].get())
        #     count+=1
        # for j in range(len(self.grocey_values)):
        #     self.sum_grocery=self.sum_grocery+self.grocey_values[j]
        # # print(self.sum_grocery)
        # # print(self.grocey_values)
        # self.sum_grocery=float(self.sum_grocery)
        # self.price_vars['grocery_price'].set(str(self.sum_grocery))
        # self.tax_vars['grocery_tax'].set(str(round((self.sum_grocery*0.05),2)))
        # print(self.sum_grocery)
        # print(self.grocey_values)
        #---getting cold drink vlaues
        self.cold_drink_rate=[12,432,12,43,123,2]
        self.cold_drink_values=[]
        self.sum_coldrink=0
        self.sum_coldrink=float(self.sum_coldrink)
        count=0
        for i in self.cold_entyr:
            self.cold_drink_values.append(self.cold_drink_rate[count]*self.cold_entyr[i].get())
            count+=1
        for j in range(len(self.cold_drink_rate)):
            self.sum_coldrink=self.sum_coldrink+self.cold_drink_values[j]
        self.price_vars["cold_drink_price"].set(str(self.sum_coldrink))
        self.tax_vars['cold_drink_tax'].set(str(round((self.sum_coldrink*0.05),2)))
        # self.total_bill()

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome webcode detail\n")
        self.textarea.insert(END, f"\n Bill number :{self.bill_number_var.get()}")
        self.textarea.insert(END, f"\n Customer name :{self.name_var.get()}")
        self.textarea.insert(END, f"\n Phone number :{self.phone_var.get()}")
        self.textarea.insert(END,"\n************************************")
        self.textarea.insert(END,"\n Products\t\tQTY\tPrice")
        self.textarea.insert(END,"\n************************************")

    def bill_area(self):
        self.cosmatics_prices=[40,120,60,180,140,100]
        self.grocery_rate=[120,34,12,453,213,123]
        self.cold_drink_rate=[12,432,12,43,123,2]
        if self.name_var.get()=='' or self.phone_var.get()=="":
            messagebox.showwarning("warning","please enter both phone number and customer name")

        elif self.price_vars['cosmatic_price'].get()==0 and self.price_vars['grocery_price'].get()==0 and self.price_vars['cold_drink_price'].get()==0:
            messagebox.showwarning('warning',"no product has selected ")
        else:
            self.welcome_bill()
            count=0
            #get the value from the dictionary and print it in the textarea
            self.cosmatic_ttl=0
            for i in self.cosmetic_entry:
                #print only if the values are not 
                if self.cosmetic_entry[i].get()!=0:
                    self.textarea.insert(END,f"\n{i}\t\t{self.cosmetic_entry[i].get()}\t{self.cosmatics_prices[count]*self.cosmetic_entry[i].get()}")
                    self.cosmatic_ttl+=self.cosmatics_prices[count]*self.cosmetic_entry[i].get()
                count+=1
            count=0
            self.textarea.insert(END,'\n**********************************')
            self.grocery_ttl=0
            for i in self.grocery_entyr:
                if self.grocery_entyr[i].get()!=0:
                    self.textarea.insert(END,f"\n{i}\t\t{self.grocery_entyr[i].get()}\t{self.grocery_rate[count]*self.grocery_entyr[i].get()}")
                    self.grocery_ttl+=self.grocery_rate[count]*self.grocery_entyr[i].get()
                count+=1
            count=0
            self.textarea.insert(END,'\n**********************************')
            self.cold_sum=0
            for i in self.cold_entyr:
                if self.cold_entyr[i].get()!=0:
                    self.textarea.insert(END,f"\n{i}\t\t{self.cold_entyr[i].get()}\t{self.cold_drink_rate[count]*self.cold_entyr[i].get()}")
                    self.cold_sum+=self.cold_drink_rate[count]*self.cold_entyr[i].get()
                count+=1
            # self.total_bill()
            self.textarea.insert(END,f"\n********************************")
            self.textarea.insert(END,f"\ncosmatic_total\t\t{self.total_bill()}\t{self.cosmatic_ttl+(self.cosmatic_ttl*5)/100}")
            self.textarea.insert(END,f"\ngrocery total\t\t{self.total_bill1()}\t{self.grocery_ttl+(self.grocery_ttl*5)/100}")
            self.textarea.insert(END,f"\ncold total\t\t{self.total_bill2()}\t{self.cold_sum+(self.cold_sum*5)/100}")
            self.save_file()
    def total_bill(self):
        # self.total_amount=self.sum+self.sum_grocery+self.sum_coldrink
        # self.textarea.insert(END,f"\n{-}\t\t{2}\t{}")
        # self.r1=self.cosmatic_sum()
        self.sum=0
        for i in self.cosmetic_entry:
            if self.cosmetic_entry[i].get()!=0:
                # break
                self.sum+=self.cosmetic_entry[i].get()
        return self.sum
    def total_bill1(self):
        # self.total_amount=self.sum+self.sum_grocery+self.sum_coldrink
        # self.textarea.insert(END,f"\n{-}\t\t{2}\t{}")
        # self.r1=self.grocery_sum()
        self.sum=0
        for i in self.grocery_entyr:
            if self.grocery_entyr[i].get()!=0:
                # break
                self.sum+=self.grocery_entyr[i].get()
        return self.sum
    def total_bill2(self):
        # self.total_amount=self.sum+self.sum_grocery+self.sum_coldrink
        # self.textarea.insert(END,f"\n{-}\t\t{2}\t{}")
        # self.r1=self.cold_sum()
        self.sum=0
        for i in self.cold_entyr:
            if self.cold_entyr[i].get()!=0:
                # break
                self.sum+=self.cold_entyr[i].get()
        return self.sum
    
    
    def save_file(self):
        ask_yn=messagebox.askyesno("save file","do you want to save the file")
        if ask_yn>0:
            self.get_data=self.textarea.get('1.0',END)
            f1=open(f"bills/{self.bill_number_var.get()}.txt",'w')
            f1.write(self.get_data)
            f1.close()
            messagebox.showinfo("saves",f"your file {self.bill_number_var.get()} saved successfully")
        else:
            return

    def find_bill(self):
        self.present=False
        for i in os.listdir("bills/"):
            # print(i.split('.')[0])
            # print(self.bill_number_var.get())
            if int(i.split('.')[0])==self.bill_number_var.get():
                self.present=True
                # f1=open(f"bills/{i}","r")
                # self.textarea.delete('1.0',END)
                # for data in f1:
                #     self.textarea.insert(END,data)
                # f1.close()
                with open(f"bills/{i}",'r') as rf:
                    self.textarea.delete('1.0',END)
                    for i in rf:
                        self.textarea.insert(END,i)

                
        if self.present==False:
            messagebox.showerror("error","file not found")

    def clear(self):
        for i in self.cosmetic_entry:
            self.cosmetic_entry[i].set(0)
        
        for j in self.grocery_entyr:
            self.grocery_entyr[j].set(0)
        
        for k in self.cold_entyr:
            self.cold_entyr[k].set(0)
        
        self.name_var.set(0)
        self.phone_var.set(0)
        self.bill_number_var.set(0)
        for i in self.price_vars:
            self.price_vars[i].set(0)
        for j in self.tax_vars:
            self.tax_vars[j].set(0)
        self.textarea.delete('1.0',END)
        self.welcome_bill()

    def exit(self):
        op=messagebox.askyesno("Exit","do you really want to exit ")
        if op>0:
            self.root.destroy()

    def add(self,event=""):
        
        try:
            # print(self.entry_vars[i].get())
            conn=mysql.connector.connect(host="localhost",username="root",password="root@wajid123",database="customer_detail")
            my_curser=conn.cursor()
            my_curser.execute("insert into bills values(%s,%s,%s)",tuple([str(self.name_var),self.phone_var,self.bill_number_var]))
            conn.commit()
            # self.fetch_data()
            conn.close()
            messagebox.showinfo("success","you data is successfully added")
        except Exception as es:
                messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)



root=Tk()
obj=bill_app(root)
root.mainloop()