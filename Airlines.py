import mysql.connector as mysql
import random
import string

def main_page():    
    print("\n\nAvailable Facilities on the interface : ")
    print("1. Book Flights\n2. Ticket Status\n3. Plan B(Cancellation)\n4. Check-in\n5. Exit")
    try :
        choice=int(input("Your Choice (in digit) : "))
    except :
        print("Wrong Input")
        main_page()
    if choice==1 :
        print("\n\t\t FLIGHT BOOKING")
        booking() 
    elif choice==2 :
        print("\n\t\t TICKET STATUS")
        t_status()
    elif choice==3 :
        print("\n\t\tPLAN B (CANCELLATION)")
        plan_b()
    elif choice==4 :
        print("\n\t\tWELCOM TO WEB CHECK-IN")
        web_c_i()
    elif choice==5 :
        print("\n\t\tTHANK YOU FOR VISITING US!")
        exit()
    else :
        print("Wrong Choice!")
        main_page()
        
def booking():
    places_list=[]
    dept_dates=[]
    names=[]
    ages=[]
    NAMES="("
    AGE="("
    PLACES=""
    DEPT_DATES=""
    print("Types of Trips : \n1. One Way\n2. Round Trip\n3. Multi-City")
    try :
        trip_type=int(input("Your type of trip (from the above in digit) : "))
    except :
        print("Invalid Input")
        booking()
    if trip_type==1:
        t_t="One Way"
        dep_date=input("Departure Date (YYYY-MM-DD) : ")
        re_date="NIL"
        PLACES="NIL"
        DEPT_DATES="NIL"
    elif trip_type==2 :
        t_t="Round Trip"
        dep_date=input("Departure Date (YYYY-MM-DD) : ")
        re_date=input("Return Date (YYYY-MM-DD) : ")
        PLACES="NIL"
        DEPT_DATES="NIL"
    elif trip_type==3 :
        t_t="Multi-City"
        print("Ranquem Airlines can currently connect not more than 2 extra cities\nWill be available with multiple in future!")
        dep_date=input("Initial Departure Date (YYYY-MM-DD) : ")
        PLACES="("
        DEPT_DATES="("
        for i in range(0,2) :
            place=input("City Name : ")
            places_list.append(place)
            dept_date=input("Departure Date (YYYY-MM-DD) : ")
            dept_dates.append(dept_date)
        for m in places_list :
            PLACES=PLACES+m+","
            PLACES=PLACES+")"
        for n in dept_dates :
            DEPT_DATES=DEPT_DATES+n+","
            DEPT_DATES=DEPT_DATES+")"
        re_choice=input("Is this a round trip multi-city trip? Press 'Y' for Yes : ")
        if re_choice=='y' or re_choice=='Y':
            re_date=input("Return Date (YYYY-MM-DD) : ")
        else :
            re_date="NIL"
    else :
        print("Choice out of bounds")
        booking()
    d_from=input("From : ")
    ar_to=input("To : ")
    num_pass=int(input("Number of Passenger(s) : "))
    for j in range(num_pass) :
        full_name=input("Enter your full name : ")
        names.append(full_name)
        age=int(input("Enter your age : "))
        ages.append(age)
    phno=int(input("Phone Number(10 Digits) : "))
    pnr=PNR()
    for k in names :
        NAMES=NAMES+k+","
    NAMES=NAMES+")"
    for l in ages :
        AGE=AGE+str(l)+","
    AGE=AGE+")"
    final_choice=input("Do you want to confirm your booking (Y/N) : ")
    if final_choice=='y' or final_choice=='Y' :
        status="Confirmed"
        query1="insert into bookings values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        record=(t_t,d_from,ar_to,dep_date,re_date,PLACES,DEPT_DATES,NAMES,AGE,phno,pnr,status)
        connection1(query1,record)
        display_booking(t_t,d_from,ar_to,dep_date,re_date,PLACES,DEPT_DATES,NAMES,AGE,phno,pnr,status)
        continuation=input("Do you want to continue with different facilities?\nPress 'Y' : ")
        if continuation=='y' or continuation=="Y":
            print("Redirecting To Main Page.....")
            main_page()
        else :
            exit()
    else :
        print("Booking Cancelled!")
        print("Redirecting To Main Page.......")
        main_page()
        
def PNR() :
    b=""
    for i in range(0,6):
        r=random.choice(string.ascii_letters).upper()
        b=b+r
    return b

def display_booking(t_t,d_from,ar_to,dep_date,re_date,PLACES,DEPT_DATES,NAMES,AGE,phno,pnr,status):
    print("BOOKING DETAILS : ")
    if t_t=="One Way" :
        print("From\tTo\tTrip Type\tDeparture Date\tName(s)\tAge")
        print(d_from,"\t",ar_to,"\t",t_t,"\t",dep_date,"\t\t",NAMES,"\t\t",AGE)
        print("PNR : ",pnr)
        print("Phone Number : ",phno)
        print("Status : Confirmed")
    elif t_t=="Round Trip" :
        print("From\tTo\tTrip Type\tDeparture Date\tReturn Date\tName(s)\tAge")
        print(d_from,"\t",ar_to,"\t",t_t,"\t",dep_date,"\t",re_date,"\t",NAMES,"\t",AGE)
        print("PNR : ",pnr)
        print("Phone Number : ",phno)
        print("Status : Confirmed")
    if t_t=="Multi-City" :
        print("From\tTo\tTrip Type\tInitial Departure Date\tOther Cities\tDeparture Dates\tName(s)\tAge")
        print(d_from,"\t",ar_to,"\t",t_t,"\t",dep_date,"\t",PLACES,"\t",DEPT_DATES,"\t\t",NAMES,"\t\t",AGE)
        print("PNR : ",pnr)
        print("Phone Number : ",phno)
        print("Status : Confirmed")
        
def t_status():
    pnr_check=input("PNR : ")
    query="select Status from bookings where PNR=%s"
    rec=[pnr_check]
    connection2(query,rec)

def plan_b():
    pnr_check=input("PNR : ")
    print("You will be refunded 25% of the cost of ticket")
    choice=input("Are you sure you want to cancel your flight ticket?\nPress 'Y' to continue : ")
    if choice=='Y' or choice=='y':
        query2="delete from bookings where PNR=%s"
        rec=[pnr_check]
        connection1(query2,rec)
        print("\nYour ticket has been successfully cancelled\nYou will be refunded shortly\nThank You.")
    else :
        print("The ticket wasn't cancelled")
    print("\n\nRegards,\nRanquem Airlines")
    

def web_c_i():
    pnr_check=input("PNR : ")
    c_i_choice=input("Do you want to check-in now?\nPress 'Y' for checking in right now : ")
    if c_i_choice=='Y' or c_i_choice=='y' : 
        query2="update bookings set Status=\"Checked-In\" where PNR=%s"
        rec=[pnr_check]
        connection1(query2,rec)
        print("\nYou have successfully checked-in\nHave a Safe Journey\n\nRegards,\nRanquem Airlines")
    else :
        print("You haven't checked in\Thank You.")

def connection1(Q,R):
    conn=mysql.connect(host="localhost",user="root",password="h@cker_101",database="IndiGoAirlines")
    cursor=conn.cursor()
    cursor.execute(Q,R)
    conn.commit()
    conn.close()
    
def connection2(Q,R):
    conn=mysql.connect(host="localhost",user="root",password="h@cker_101",database="IndiGoAirlines")
    cursor=conn.cursor()
    cursor.execute(Q,R)
    for x in cursor :
        print(x)
    conn.commit()
    conn.close()
print("\t\tWELCOME TO RANQUEM AIRLINES")
print("\t\t\tTravel Anywhere Anytime!")
main_page()
