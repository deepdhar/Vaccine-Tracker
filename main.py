import requests
from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title ("Vaccine Stats")
window.configure(background="white")
window.geometry("650x400")

photo = PhotoImage(file = 'corona.png')
window.iconphoto(False, photo)

scrText = scrolledtext.ScrolledText(window, wrap=WORD, font=("Calibri", 14))
scrText.pack(fill="both")

def find_vaccine(pin, date):
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + pin + "&date=" + date
    r = requests.get(url = URL,)
    if r.status_code==200:
        count = 1
        response = r.json()['centers']
        flag = 0
        for each in response:
            for session in each['sessions']:
                if session['available_capacity_dose1']:
                    scrText.insert('insert', str(count) + ". ")
                    scrText.insert('insert', each['name'] + "\n")
                    scrText.insert('insert', "Date: " + session['date'] + "\n")
                    scrText.insert('insert', "Available Dose 1: " + str(session['available_capacity_dose1']) + "\n")
                    scrText.insert('insert', "Minimmum age limit: " + str(session['min_age_limit']) + "\n")
                    scrText.insert('insert', "Vaccine name: " + session['vaccine'] + "\n\n")
                    count += 1
                    flag = 1
        if flag != 1:
            scrText.insert('insert', "No vaccines found!")
    else:
        scrText.insert('insert', "Response error, try again!")
            
    
pincode = input("Enter your PIN Code: ")
date = input("Enter date (DD-MM-YYYY): ")
find_vaccine(pincode, date)

scrText.focus()
window.mainloop()