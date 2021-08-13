from datetime import datetime # datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S


persondict = {
    "fname":"",
    "lname":"",
    "age":0,
    "body_temp":"",
    "location":"",
    "risk":False,
    "covid":False,
}

def get_personinfo(persondict):
    persondict.update({"dateime":dt_string})
    fname = input("Enter your first name: ")
    persondict.update({"fname":fname})
    lname = input("Enter your last name: ")
    persondict.update({"lname":lname})
    age = input("Enter your age: ")
    persondict.update({"age":age})
    boddy_temp = float(input("Enter your temperature: "))
    persondict.update({"body_temp":boddy_temp})
    print("location")
    print ("1. Bangkok") 
    print ("2. Kanchanaburi") 
    print ("3. Chanthaburi") 
    print ("4. Chachoengsao") 
    print ("5. Chumphon") 
    print ("6. Chonburi") 
    print ("7. Trat") 
    print ("8. Tak") 
    print ("9. Nakhon Nayok") 
    print ("10. Nakhon Pathom") 
    print ("11. Nonthaburi") 
    print ("12. Pathum Thani") 
    print ("13. Prachuap Khiri Khan") 
    print ("14. Prachinburi") 
    print ("15. Ayutthaya") 
    print ("16. Phetchaburi") 
    print ("17. Ratchaburi") 
    print ("18. Ranong") 
    print ("19. Rayong") 
    print ("20. Lopburi") 
    print ("21. Singburi") 
    print ("22. Samut Prakan") 
    print ("23. Samut Songkhram") 
    print ("24. Samut Sakhon") 
    print ("25. Suphanburi") 
    print ("27. Saraburi") 
    print ("28. Ang Thong") 
    print ("0. Others") 
    location = int(input("Enter location number: "))
    persondict.update({"location":location})



def covid_evaluation(persondict):
    if persondict.get("location") !=0:
        persondict.update({"risk":True})
        if persondict.get("body_temp") >37.5:
            persondict.update({"covid":True})
        else:
            persondict.update({"covid":False})
    else:
        persondict.update({"risk":False})


    





