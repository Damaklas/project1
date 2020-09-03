from tkinter import *
from datetime import date
#from PIL import ImageTk, Image

root = Tk()
root.geometry("900x700")
# root.iconbitmap("C:/Users/gerge/Desktop/Python/CODEMY/TKINTER/aeromexico-logo.png")

"""def send():
    #fill it up later
def save():
    #fill it up later"""

today = date.today()
today_string = today.strftime('%Y-%m-%d')

title = Label(root, text="AEROMEXICO")
subTitle = Label(root, text="REPORT")

# Labels

reportType = Label(root, text="REPORT TYPE")  # dropdown menu
date_text = Label(root, text="Date")
today_text = Label(root, text=today)
crew_text = Label(text="Crew", )  # two different box and fomrat after
aircraftType_text = Label(text="A/C type", )  # flight number/route/reg connect together
flightNunber_text = Label(text="Flight Number", )  # flight number with search engine //
route_text = Label(text="Route", )  #
registration_text = Label(text="Registration", )  #
jClass_text = Label(text="J", )
yClasst_text = Label(text="Y", )
area_text = Label(text="AREA", )
zoneA_text = Label(text="ZONE A", )
zoneB_text = Label(text="ZONE B", )
zoneC_text = Label(text="ZONE C", )
total_text = Label(text="TOTAL", )
adult_text = Label(text="ADULT", )
child_text = Label(text="CHILD", )
infant_text = Label(text="INFANT", )
lirEdno_text = Label(text="LIR EDNO", )
xqContainerMessage_text = Label(text="BAGGAIGE CONTAINER MESSAGE", )  # + icon to add new line for AKE if needed
totalXqInAke_text = Label(text="TOTAL BAGS IN AKE", )
container_text = Label(text="CONTAINER", )
position_text = Label(text="POSITION", )
nunmberOfXq_text = Label(text="NUMBER OF BAGS", )
typeXq_text = Label(text="TYPE", )
horizontalSpace = Label(root, text="         ")
verticalSpace1 = Label(root, text="   ")
bulk_text = Label(text="BULK", )
stroller_text = Label(text="STROLLER", )
wchr_text = Label(text="WCHR", )
localBag_text = Label(text="LOCAL BAG", )
transferBag_text = Label(text="TRANSFER BAG", )
priorityBag_text = Label(text="PRIORITY BAG", )
totalBulkBag_text = Label(text="TOTAL BAGS IN BULK", )
totalBagsOb_text = Label(text="TOTAL BAGS ON BOARD", )
totalBagWeight_text = Label(text="TOTAL WEIGHT OF BAGS", )
captain_text = Label(text="CAP", )
h2o_text = Label(text="H2O", )
flightPlan_text = Label(text="FLIGHT PLAN", )
runway_text = Label(text="TAKE OFF RUNWAY", )
runwayCondition_text = Label(text="RUNWAY CONDITION", )
fuel_text = Label(text="FINAL FUEL", )
damagedBags_text = Label(text="DAMAGED BAG", )
remarks_text = Label(text="REMARKS", )

# Buttons

sendButton = Button(root, text="SEND", padx=50, pady=5)
saveButton = Button(root, text="SAVE", padx=50, pady=5)
exitButton = Button(root, text="EXIT", command=root.quit)

###################################################################xx

# Label Placement

title.grid(row=0, column=0)
subTitle.grid(row=1, column=0)
reportType.grid(row=2, column=0, sticky=W)
reportType_entry.grid(row=2, column=1, sticky=W)
date_text.grid(row=3, column=0, sticky=W)
today_text.grid(row=3, column=1, sticky=W)
flightNunber_text.grid(row=2, column=2, sticky=W)
route_text.grid(row=3, column=2, sticky=W)
registration_text.grid(row=4, column=2, sticky=W)
aircraftType_text.grid(row=5, column=2, sticky=W)
crew_text.grid(row=6, column=2, sticky=W)
jClass_text.grid(row=8, column=0, sticky=W)
yClasst_text.grid(row=8, column=2, sticky=W)
area_text.grid(row=9, column=0, sticky=W)
zoneA_text.grid(row=10, column=0, sticky=W)
zoneB_text.grid(row=11, column=0, sticky=W)
zoneC_text.grid(row=12, column=0, sticky=W)
total_text.grid(row=13, column=0, sticky=W)
adult_text.grid(row=9, column=1)
child_text.grid(row=9, column=2)
infant_text.grid(row=9, column=3)
lirEdno_text.grid(row=15, column=0, sticky=W)
xqContainerMessage_text.grid(row=16, column=0, columnspan=2, sticky=W)
totalXqInAke_text.grid(row=16, column=2, sticky=W)
container_text.grid(row=18, column=0, sticky=W)
position_text.grid(row=18, column=1, sticky=W)
nunmberOfXq_text.grid(row=18, column=2, sticky=W)
typeXq_text.grid(row=18, column=3, sticky=W)
horizontalSpace.grid(row=2, column=4)
bulk_text.grid(row=2, column=6, sticky=W)
stroller_text.grid(row=3, column=6, sticky=W)
wchr_text.grid(row=4, column=6, sticky=W)
localBag_text.grid(row=5, column=6, sticky=W)
transferBag_text.grid(row=6, column=6, sticky=W)
priorityBag_text.grid(row=7, column=6, sticky=W)
totalBulkBag_text.grid(row=8, column=6, sticky=W)
totalBagsOb_text.grid(row=9, column=6, sticky=W)
totalBagWeight_text.grid(row=10, column=6, sticky=W)
captain_text.grid(row=12, column=6, sticky=W)
h2o_text.grid(row=13, column=6, sticky=W)
flightPlan_text.grid(row=14, column=6, sticky=W)
runway_text.grid(row=15, column=6, sticky=W)
runwayCondition_text.grid(row=16, column=6, sticky=W)
fuel_text.grid(row=17, column=6, sticky=W)
damagedBags_text.grid(row=18, column=6, sticky=W)
remarks_text.grid(row=19, column=6, sticky=W)

#########################################################################



crew = StringVar()
aircraftType = StringVar()
registration = StringVar()
route = StringVar()
flightNumber = StringVar()
jClass = StringVar()
yClass = StringVar()
zoneAA = StringVar()
zoneAC = StringVar()
zoneAI = StringVar()
zoneBA = StringVar()
zoneBC = StringVar()
zoneBI = StringVar()
zoneCA = StringVar()
zoneCC = StringVar()
zoneCI = StringVar()
# total = StringVar()  # here comes the total ob formula
lirEdno = StringVar()
totalXqInAke = StringVar()  # here comes the totl bags in AKE formula
container = StringVar()
position = StringVar()
number_of_xq = StringVar()
type_xq = StringVar()
container2 = StringVar()
position2 = StringVar()
number_of_xq2 = StringVar()
type_xq2 = StringVar()
container3 = StringVar()
position3 = StringVar()
number_of_xq3 = StringVar()
type_xq3 = StringVar()
container4 = StringVar()
position4 = StringVar()
number_of_xq4 = StringVar()
type_xq4 = StringVar()
container5 = StringVar()
position5 = StringVar()
number_of_xq5 = StringVar()
type_xq5 = StringVar()
container6 = StringVar()
position6 = StringVar()
number_of_xq6 = StringVar()
type_xq6 = StringVar()
container7 = StringVar()
position7 = StringVar()
number_of_xq7 = StringVar()
type_xq7 = StringVar()
container8 = StringVar()
position8 = StringVar()
number_of_xq8 = StringVar()
type_xq8 = StringVar()

stroller = StringVar()
wchr = StringVar()
localBag = StringVar()
transferBag = StringVar()
priorityBag = StringVar()
totalBulkBag = StringVar()  # here comes the total bulk bags
totalBagsOb = StringVar()  # here comes the total on board bags
totalBagWeight = StringVar()
captain = StringVar()
h2o = StringVar()
flightPlan = StringVar()
runway = StringVar()
runwayCondition = StringVar()
fuel = StringVar()
damagedBags = StringVar()
remarks = StringVar()

####################################################################

# Entry Cells

reportType_entry = Entry(root, width=20, borderwidth=3)
crew_entry = Entry(textvariable=crew)
aircraftType_entry = Entry(textvariable=aircraftType)
registration_entry = Entry(textvariable=registration)
route_entry = Entry(textvariable=route)
flight_number_entry = Entry(textvariable=flightNumber)
jClass_entry = Entry(textvariable=jClass)
yClass_entry = Entry(textvariable=yClass)
zoneAA_entry = Entry(textvariable=zoneAA, width=5)
zoneAC_entry = Entry(textvariable=zoneAC, width=5)
zoneAI_entry = Entry(textvariable=zoneAI, width=5)
zoneBA_entry = Entry(textvariable=zoneBA, width=5)
zoneBC_entry = Entry(textvariable=zoneBC, width=5)
zoneBI_entry = Entry(textvariable=zoneBI, width=5)
zoneCA_entry = Entry(textvariable=zoneCA, width=5)
zoneCC_entry = Entry(textvariable=zoneCC, width=5)
zoneCI_entry = Entry(textvariable=zoneCI, width=5)
lirEdno_entry = Entry(textvariable=lirEdno)

container1_entry = Entry(textvariable=container)
position1_entry = Entry(textvariable=position)
number_of_xq1_entry = Entry(textvariable=number_of_xq)
type_xq1_entry = Entry(textvariable=type_xq)
container2_entry = Entry(textvariable=container2)
position2_entry = Entry(textvariable=position2)
number_of_xq2_entry = Entry(textvariable=number_of_xq2)
type_xq2_entry = Entry(textvariable=type_xq2)
container3_entry = Entry(textvariable=container3)
position3_entry = Entry(textvariable=position3)
number_of_xq3_entry = Entry(textvariable=number_of_xq3)
type_xq3_entry = Entry(textvariable=type_xq3)
container4_entry = Entry(textvariable=container4)
position4_entry = Entry(textvariable=position4)
number_of_xq4_entry = Entry(textvariable=number_of_xq4)
type_xq4_entry = Entry(textvariable=type_xq4)
container5_entry = Entry(textvariable=container5)
position5_entry = Entry(textvariable=position5)
number_of_xq5_entry = Entry(textvariable=number_of_xq5)
type_xq5_entry = Entry(textvariable=type_xq5)
container6_entry = Entry(textvariable=container6)
position6_entry = Entry(textvariable=position6)
number_of_xq6_entry = Entry(textvariable=number_of_xq6)
type_xq6_entry = Entry(textvariable=type_xq6)
container7_entry = Entry(textvariable=container7)
position7_entry = Entry(textvariable=position7)
number_of_xq7_entry = Entry(textvariable=number_of_xq7)
type_xq7_entry = Entry(textvariable=type_xq7)
container8_entry = Entry(textvariable=container8)
position8_entry = Entry(textvariable=position8)
number_of_xq8_entry = Entry(textvariable=number_of_xq8)
type_xq8_entry = Entry(textvariable=type_xq8)

stroller_entry = Entry(textvariable=stroller)
wchr_entry = Entry(textvariable=wchr)
localBag_entry = Entry(textvariable=localBag)
transferBag_entry = Entry(textvariable=transferBag)
priorityBag_entry = Entry(textvariable=priorityBag)
totalBulkBag = StringVar()  # here comes the total bulk bags
totalBagsOb = StringVar()  # here comes the total on baord bags
totalBagWeight_entry = Entry(textvariable=totalBagWeight)
captain_entry = Entry(textvariable=captain)
h2o_entry = Entry(textvariable=h2o)
flightPlan_entry = Entry(textvariable=flightPlan)
runway_entry = Entry(textvariable=runway)
runwayCondition_entry = Entry(textvariable=runwayCondition)
fuel_entry = Entry(textvariable=fuel)
damagedBags_entry = Entry(textvariable=damagedBags)
remarks_entry = Entry(textvariable=remarks)
####################################################################

flight_number_entry.grid(row=2, column=3)
route_entry.grid(row=3, column=3)
registration_entry.grid(row=4, column=3)
aircraftType_entry.grid(row=5, column=3)
crew_entry.grid(row=6, column=3)

jClass_entry.grid(row=8, column=1)
yClass_entry.grid(row=8, column=3)
zoneAA_entry.grid(row=10, column=1)
zoneAC_entry.grid(row=10, column=2)
zoneAI_entry.grid(row=10, column=3)
zoneBA_entry.grid(row=11, column=1)
zoneBC_entry.grid(row=11, column=2)
zoneBI_entry.grid(row=11, column=3)
zoneCA_entry.grid(row=12, column=1)
zoneCC_entry.grid(row=12, column=2)
zoneCI_entry.grid(row=12, column=3)

lirEdno_entry.grid(row=15, column=1)
total_xq_in_ake = StringVar()  # here comes the total bags in AKE formula

container1_entry.grid(row=19, column=0)
position1_entry.grid(row=19, column=1)
number_of_xq1_entry.grid(row=19, column=2)  # 1st AKE     # add plus button to create more fields for extra AKEs
type_xq1_entry.grid(row=19, column=3)

container2_entry.grid(row=20, column=0)
position2_entry.grid(row=20, column=1)
number_of_xq2_entry.grid(row=20, column=2)  # 2nd AKE
type_xq2_entry.grid(row=20, column=3)

container3_entry.grid(row=21, column=0)
position3_entry.grid(row=21, column=1)
number_of_xq3_entry.grid(row=21, column=2)  # 3rd AKE
type_xq3_entry.grid(row=21, column=3)

container4_entry.grid(row=22, column=0)
position4_entry.grid(row=22, column=1)
number_of_xq4_entry.grid(row=22, column=2)  # 4th AKE
type_xq4_entry.grid(row=22, column=3)

container5_entry.grid(row=23, column=0)
position5_entry.grid(row=23, column=1)
number_of_xq5_entry.grid(row=23, column=2)  # 5th AKE
type_xq5_entry.grid(row=23, column=3)

container6_entry.grid(row=24, column=0)
position6_entry.grid(row=24, column=1)
number_of_xq6_entry.grid(row=24, column=2)  # 6th AKE
type_xq6_entry.grid(row=24, column=3)

container7_entry.grid(row=25, column=0)
position7_entry.grid(row=25, column=1)
number_of_xq7_entry.grid(row=25, column=2)  # 7th AKE
type_xq7_entry.grid(row=25, column=3)

container8_entry.grid(row=26, column=0)
position8_entry.grid(row=26, column=1)  # 8th AKE
number_of_xq8_entry.grid(row=26, column=2)
type_xq8_entry.grid(row=26, column=3)

verticalSpace1.grid(row=27, column=0)

stroller_entry.grid(row=3, column=7)
wchr_entry.grid(row=4, column=7)
localBag_entry.grid(row=5, column=7)
transferBag_entry.grid(row=6, column=7)
priorityBag_entry.grid(row=7, column=7)
totalBulkBag = StringVar()  # here comes the total bulk bags
totalBagsOb = StringVar()  # here comes the total on baord bags
totalBagWeight_entry.grid(row=10, column=7)
captain_entry.grid(row=12, column=7)
h2o_entry.grid(row=13, column=7)
flightPlan_entry.grid(row=14, column=7)
runway_entry.grid(row=15, column=7)
runwayCondition_entry.grid(row=16, column=7)
fuel_entry.grid(row=17, column=7)
damagedBags_entry.grid(row=18, column=7)
remarks_entry.grid(row=19, column=7)

sendButton.grid(row=28, column=1)
saveButton.grid(row=28, column=3)
exitButton.grid(row=28, column=7)

root.mainloop()
