from Tkconstants import RIDGE, NSEW, END
from AddCustomer import AddCustomer
from AddInVoice import AddInVoice
from AddMeasure import AddMeasure
from AddMeasureDetails import AddMeasureDetails
import Tkinter
import ttk
from tkFileDialog import askopenfilename
from mainClass import mainClass
from AddMeasureList import AddMeasureList
Measurecount = 2
MeasureList=[]

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def getNames(event):
    result=AddInVoice.getFLNames()
    fname4Entry.set(result[0][0])
    lname4Entry.set(result[0][1])
    IIDEntry.set(result[0][2])
    SearchFrmIID.insert(END,result[0][2])
def OpenImageBox():
    name = askopenfilename()
    filePathEntry.insert(END, name)
def getDataToInVoice(event):
    result=AddCustomer.getDataInVoice()
    CIDEntry.set(result[0][0])
    fnameEntry.set(result[0][1])
    lnameEntry.set(result[0][2])

def saveCustomer():
    if firstnameText.get()!="" and lastnameText.get()!="" and ageV.get()!="" and contactnumberText.get()!="" and addressText.get()!="":
        if hasNumbers(firstnameText.get()) or hasNumbers(lastnameText.get()):
            ErrorMsg.set("Please enter your name with letters")
        else :
            if contactnumberText.get().isdigit():
                if len(contactnumberText.get())==10:
                    ErrorMsg.set("")
                    AddCustomer.firstname = firstnameText.get()
                    AddCustomer.lastname = lastnameText.get()
                    AddCustomer.age = ageV.get()
                    AddCustomer.contactnumber = contactnumberText.get()
                    AddCustomer.address = addressText.get()

                    AddCustomer.saveToDB()
                    dbUpdate.set("Successfully added")
                else :
                    ErrorMsg.set("Telephone Number should be included with 10 digits")
            else :
                ErrorMsg.set("Telephone Number should be included with integer values")
    else:
        ErrorMsg.set("Cannot have Empty Entries!")

def ClearCustomer():
    firstnameText.delete(0, 'end')
    lastnameText.delete(0, 'end')
    contactnumberText.delete(0, 'end')
    addressText.delete(0, 'end')

def searchInVoice():
    goRows=10
    result = AddInVoice.InVoiceList()
    rows = []
    cols = []
    colnames = ["IID", "firstname", "lastname", "Submit Date", "Require Date", "quantity", "price"]
    for k in range(6):
        e = Tkinter.Entry(subframe3, relief=RIDGE)
        e.grid(row=goRows, column=k, sticky=NSEW)
        e.insert(END, colnames[k])
        cols.append(e)
    rows.append(cols)
    goRows = goRows + 1

    rows = []
    for i in range(len(result)):
        cols = []
        for j in range(len(result[0])):
            e = Tkinter.Entry(subframe3, relief=RIDGE)
            e.grid(row=goRows, column=j, sticky=NSEW)
            e.insert(END, result[i][j])
            cols.append(e)
        rows.append(cols)
        goRows = goRows + 1

def searchCustomer():
    # fullname=customerName.get()
    # AddCustomer.firstname=fullname.split( )[0]
    # AddCustomer.lastname =fullname.split( )[1]
    goRows = 15

    result = AddCustomer.searchCustomers()
    rows = []
    cols = []
    colnames = ["CID", "firstname", "lastname", "age", "contactnumber", "address"]
    for k in range(6):
        e = Tkinter.Entry(subframe1, relief=RIDGE)
        e.grid(row=goRows, column=k, sticky=NSEW)
        e.insert(END, colnames[k])
        cols.append(e)
    rows.append(cols)
    goRows = goRows + 1

    rows = []
    for i in range(len(result)):
        cols = []
        for j in range(len(result[0])):
            e = Tkinter.Entry(subframe1, relief=RIDGE)
            e.grid(row=goRows, column=j, sticky=NSEW)
            e.insert(END, result[i][j])
            cols.append(e)
        rows.append(cols)
        goRows = goRows + 1
def searchMeasureDeatils():
    goRows = 10

    result = AddMeasureDetails.searchMeasureDeatils(SearchFrmIID.get())
    rows = []
    cols = []
    colnames = ["Measure Name", "distance"]
    for k in range(2):
        e = Tkinter.Entry(subframe4, relief=RIDGE)
        e.grid(row=goRows, column=k, sticky=NSEW)
        e.insert(END, colnames[k])
        cols.append(e)
    rows.append(cols)
    goRows = goRows + 1

    rows = []
    for i in range(len(result)):
        cols = []
        for j in range(len(result[0])):
            e = Tkinter.Entry(subframe4, relief=RIDGE)
            e.grid(row=goRows, column=j, sticky=NSEW)
            e.insert(END, result[i][j])
            cols.append(e)
        rows.append(cols)
        goRows = goRows + 1

def printInVoice():
    if submitdateEntry.get()!="" and expiredateEntry.get()!="" and QuantityEntry.get()!="" and PriceEntry.get()!="":
        IIDErrorMsg.set("")
        obj=AddInVoice(CIDEntry.get(),submitdateEntry.get(),expiredateEntry.get(),QuantityEntry.get(),PriceEntry.get())
        AddInVoice.saveInVoice(obj)

        generateTXT(CIDEntry.get(),obj.getIID(),fnameEntry.get(),lnameEntry.get(),submitdateEntry.get(),expiredateEntry.get(),QuantityEntry.get(),PriceEntry.get())
        InVoiceUpdate.set("InVoice Updated")
        GetIID.set("Your IID is :"+obj.getIID())
    else :
        IIDErrorMsg.set("Cannot have Empty Entries!")

def generateTXT(cid,iid,fname,lname,submitdate,requiredate,amount,price):
    with open("InVoice.txt", "w") as text_file:
        text_file.write("CID : %s \n" % (cid))
        text_file.write("IID : %s \n" % (iid))
        text_file.write("Customer Name : %s %s \n" % (fname,lname))
        text_file.write("Issued Date : %s \n" % (submitdate))
        text_file.write("Required Date  : %s \n" % (requiredate))
        text_file.write("Amount : %s \n" % (amount))
        text_file.write("Price : %s \n" % (price))
        text_file.close()
def measureSave():
    global MeasureList
    MeasureObj=AddMeasure(IIDEntry.get())
    AddMeasure.SaveMeasure(MeasureObj)
    measureId=AddMeasure.getMeasureId(MeasureObj)
    for obj in MeasureList:
        MeasureDetails=AddMeasureDetails(measureId,obj.measureName.get(),obj.measureSize.get())
        AddMeasureDetails.saveMeasureDetails(MeasureDetails)
    MeasureUpdated.set("Measurements successfully saved")
def measureDelete(obj):
    global MeasureList
    MeasureList.remove(obj)
    for object in MeasureList:
        object.AddLabel(subframe4,measureDelete)



def MeasureAddToLabel():
    global Measurecount,MeasureList
    obj=AddMeasureList("measureName"+str(Measurecount-1),"measureSize"+str(Measurecount-1),Measurecount,5)
    MeasureList.append(obj)
    obj.AddLabel(subframe4)

    Measurecount=Measurecount+1

def AddMeasurement(mainClass):
    if filePathEntry.get()!="":
        measure=mainClass.mainMethod(filePathEntry.get())
        measurement.set("Your Measurement Distance is "+measure)
        MeasureAddToLabel()
    else :
        AddMeasureError.set("Please add image path")

window = Tkinter.Tk()
window.title("Shirt Measurement")
notebook = ttk.Notebook(window, width=1000, height=1000)
notebook.pack()
subframe1 = Tkinter.Frame(window)
subframe3 = Tkinter.Frame(window)
subframe4 = Tkinter.Frame(window)
subframe1.pack()
subframe3.pack()
notebook.add(subframe1, text="Add Customer", state="normal")
notebook.add(subframe3, text="InVoice", state="normal")
notebook.add(subframe4, text="Take Measurements", state="normal")


# ########tab1#add#customer######################
ageV = Tkinter.StringVar()

AddCustomer = AddCustomer()
firstname = Tkinter.Label(subframe1, text="First Name")
firstname.grid(row=1,column=0)
firstnameText = Tkinter.Entry(subframe1)
firstnameText.grid(row=1,column=1)

lastname = Tkinter.Label(subframe1, text="Last Name")
lastname.grid(row=2,column=0)
lastnameText = Tkinter.Entry(subframe1)
lastnameText.grid(row=2,column=1)

age = Tkinter.Label(subframe1, text="Age")
age.grid(row=3,column=0)
ageR1 = Tkinter.Radiobutton(subframe1, variable=ageV, value="6-18", text="6-18")
ageR1.grid(row=3,column=1)
ageR2 = Tkinter.Radiobutton(subframe1, value="19-30", variable=ageV, text="19-30")
ageR2.grid(row=3,column=2)
ageR3 = Tkinter.Radiobutton(subframe1, value="31-50", variable=ageV, text="31-50")
ageR3.grid(row=3,column=3)

contactnumber = Tkinter.Label(subframe1, text="Contact Number")
contactnumber.grid(row=4,column=0)
contactnumberText = Tkinter.Entry(subframe1)
contactnumberText.grid(row=4,column=1)

address = Tkinter.Label(subframe1, text="Address")
address.grid(row=5,column=0)
addressText = Tkinter.Entry(subframe1)
addressText.grid(row=5,column=1)

button = Tkinter.Button(subframe1, command=saveCustomer, text="save")
button.grid(row=6,column=3)

button = Tkinter.Button(subframe1, command=ClearCustomer, text="cancel")
button.grid(row=6,column=4)

dbUpdate = Tkinter.StringVar()
dbUpdateLabel = Tkinter.Label(subframe1, textvariable=dbUpdate)
dbUpdateLabel.grid(row=6,column=5)

ErrorMsg = Tkinter.StringVar()
ErrorMsgLabel = Tkinter.Label(subframe1, textvariable=ErrorMsg)
ErrorMsgLabel.grid(row=6,column=6)
# #######################################

#########tab1#View#customers######################

customerName = Tkinter.Entry(subframe1)
customerName.grid(row=7,column=2)
button = Tkinter.Button(subframe1, command=searchCustomer, text="search")
button.grid(row=7,column=1)

###############################################

#########tab3#InVoice################

CID = Tkinter.Label(subframe3, text="CID")
CID.grid(row=0, column=0)
CIDEntry = Tkinter.StringVar()
CIDEntryLabel = Tkinter.Label(subframe3, textvariable=CIDEntry)
CIDEntryLabel.grid(row=0,column=1)

fname = Tkinter.Label(subframe3, text="First Name")
fname.grid(row=1, column=0)
fnameEntry = Tkinter.StringVar()
fnameEntryLabel = Tkinter.Label(subframe3, textvariable=fnameEntry)
fnameEntryLabel.grid(row=1,column=1)

lname = Tkinter.Label(subframe3, text="Last Name")
lname.grid(row=2, column=0)
lnameEntry = Tkinter.StringVar()
lnameEntryLabel = Tkinter.Label(subframe3, textvariable=lnameEntry)
lnameEntryLabel.grid(row=2,column=1)

submitdate = Tkinter.Label(subframe3, text="Submit Date")
submitdate.grid(row=3, column=0)
submitdateEntry = Tkinter.Entry(subframe3)
submitdateEntry.grid(row=3, column=1)

expiredate = Tkinter.Label(subframe3, text="Expire Date")
expiredate.grid(row=4, column=0)
expiredateEntry = Tkinter.Entry(subframe3)
expiredateEntry.grid(row=4, column=1)

Quantity = Tkinter.Label(subframe3, text="Quantity")
Quantity.grid(row=5, column=0)
QuantityEntry = Tkinter.Entry(subframe3)
QuantityEntry.grid(row=5, column=1)

Price = Tkinter.Label(subframe3, text="Price")
Price.grid(row=6, column=0)
PriceEntry = Tkinter.Entry(subframe3)
PriceEntry.grid(row=6, column=1)

button = Tkinter.Button(subframe3, command=printInVoice, text="save")
button.grid(row=7, column=2)

GetIID = Tkinter.StringVar()
GetIIDLabel = Tkinter.Label(subframe3, textvariable=GetIID)
GetIIDLabel.grid(row=9,column=3)

InVoiceUpdate = Tkinter.StringVar()
InVoiceUpdateUpdateLabel = Tkinter.Label(subframe3, textvariable=InVoiceUpdate)
InVoiceUpdateUpdateLabel.grid(row=9,column=4)

IIDErrorMsg = Tkinter.StringVar()
IIDErrorMsgLabel = Tkinter.Label(subframe3, textvariable=IIDErrorMsg)
IIDErrorMsgLabel.grid(row=9,column=5)

customerName = Tkinter.Entry(subframe3)
customerName.grid(row=9,column=2)
button = Tkinter.Button(subframe3, command=searchInVoice, text="search Invoice")
button.grid(row=9,column=1)

#########tab4#MeasurementDetails################
measurement = Tkinter.StringVar()
measurementLabel = Tkinter.Label(subframe4, textvariable=measurement)
measurementLabel.grid(row=0, column=5)
IID = Tkinter.Label(subframe4, text="IID")
IID.grid(row=0, column=0)
IIDEntry = Tkinter.StringVar()
IIDEntryLabel = Tkinter.Label(subframe4, textvariable=IIDEntry)
IIDEntryLabel.grid(row=0,column=1)

fname4 = Tkinter.Label(subframe4, text="First Name")
fname4.grid(row=1, column=0)
fname4Entry = Tkinter.StringVar()
fname4EntryLabel = Tkinter.Label(subframe4, textvariable=fname4Entry)
fname4EntryLabel.grid(row=1,column=1)

lname4 = Tkinter.Label(subframe4, text="Last Name")
lname4.grid(row=2, column=0)
lname4Entry = Tkinter.StringVar()
lname4EntryLabel = Tkinter.Label(subframe4, textvariable=lname4Entry)
lname4EntryLabel.grid(row=2,column=1)

filePath = Tkinter.Label(subframe4, text="Enter your image")
filePath.grid(row=3, column=0)
filePathEntry = Tkinter.Entry(subframe4)
filePathEntry.grid(row=3, column=1)
filePathButton = Tkinter.Button(subframe4, command=OpenImageBox, text="Choose")
filePathButton.grid(row=3, column=2)
button = Tkinter.Button(subframe4, command=lambda:AddMeasurement(mainClass=mainClass()), text="Add Measurement")
button.grid(row=7, column=2)
measureSaveButton=Tkinter.Button(subframe4, command=measureSave, text="save")
measureSaveButton.grid(row=8,column=2)

SearchFrmIID = Tkinter.Entry(subframe4)
SearchFrmIID.grid(row=9,column=2)
SearchFrmIIDbutton = Tkinter.Button(subframe4, command=searchMeasureDeatils, text="search")
SearchFrmIIDbutton.grid(row=9,column=1)

AddMeasureError=Tkinter.StringVar()
AddMeasureErrorLabel=Tkinter.Label(subframe4, textvariable=AddMeasureError)
AddMeasureErrorLabel.grid(row=9,column=4)

MeasureUpdated=Tkinter.StringVar()
MeasureUpdatedLabel=Tkinter.Label(subframe4, textvariable=MeasureUpdated)
MeasureUpdatedLabel.grid(row=9,column=4)

window.bind('<Return>', getNames)
window.bind('<Up>', getDataToInVoice)
if __name__ == "__main__":
    window.minsize(1000, 1000)
    window.mainloop()
