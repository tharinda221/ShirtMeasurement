__author__ = 'tharinda'

import Tkinter

class AddMeasureList:
    measureName=""
    measureSize=""
    row=""
    column=""
    def __init__(self,measureName,measureSize,row,column):
        self.measureName=measureName
        self.measureSize=measureSize
        self.row=row
        self.column=column
    def AddLabel(self,subframe):
        self.measureName = Tkinter.Entry(subframe)
        self.measureName.grid(row=self.row,column=self.column)

        self.measureSize = Tkinter.Entry(subframe)
        self.measureSize.grid(row=self.row,column=self.column+1)

        # measureButtonDel=Tkinter.Button(subframe, command=lambda:measureDelete(obj=self), text="delete")
        # measureButtonDel.grid(row=self.row,column=self.column+2)

# objList=[]
#
# for i in range (0,5):
#     objList.append(AddMeasureList("measureName"+str(i),"measureSize"+str(i)))
#
# for obj in objList:
#     print(obj.measureName+" "+obj.measureSize)