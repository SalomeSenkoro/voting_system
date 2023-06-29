from tkinter import*
root=Tk()
root.geometry("500x400")

# Expose endpoints
# /register


def getvals():
   print("Accepted")


#Heading
Label(root, text= "Voting Registration System",font= "ar 15 bold").grid(row=0,column=3)

#Fields name
name = Label(root, text="Name")
gender = Label(root, text="Gender")
age = Label(root, text = "Age")
nationality = Label(root, text="Nationality")
id = Label(root, text="ID")
phone = Label(root, text="Phone")
email = Label(root, text = "Email")
adress = Label(root, text = "Adress")


#Packing Fields
name.grid(row=1,column=2)
gender.grid(row=2,column=2)
age.grid(row=3,column=2)
nationality.grid(row=4,column=2)
id.grid(row=5,column=2)
phone.grid(row=6,column=2)
email.grid(row = 7, column=2)
adress.grid(row=8,column=2)


#Variables for Installing data
namevalue = StringVar
gendervalue = StringVar
agevalue = StringVar
nationalityvalue = StringVar
idvalue = StringVar
phonevalue = StringVar
emailvalue = StringVar
adressvalue = StringVar
checkvalue = IntVar

#Creating entry field
nameentry = Entry(root,textvariable = namevalue)
genderentry = Entry(root,textvariable = gendervalue)
ageentry = Entry(root,textvariable = agevalue)
nationalityentry = Entry(root,textvariable = nationalityvalue)
identry = Entry(root,textvariable =idvalue)
phoneentry = Entry(root,textvariable = phonevalue)
emailentry = Entry(root,textvariable = emailvalue)
adressentry = Entry(root,textvariable = adressvalue)


#Packing entry field
nameentry.grid(row=1,column=3)
genderentry.grid(row=2,column=3)
ageentry.grid(row=3,column=3)
nationalityentry.grid(row=4,column=3)
identry.grid(row=5,column=3)
phoneentry.grid(row=6,column=3)
emailentry.grid(row=7,column=3)
adressentry.grid(row=8,column=3)


#Creating chechbox
checkbtn = Checkbutton(text="Sign Up", variable=checkvalue).grid(row=9,column=3)


#Submit button
Button(text="Submit", command=getvals).grid(row=10,column=3)



root.mainloop()
