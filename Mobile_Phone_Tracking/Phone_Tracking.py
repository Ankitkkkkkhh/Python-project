    import phonenumbers
    from phonenumbers import timezone,geocoder,carrier
    number=input("Enter you mobile number +91 : ")
    phone=phonenumbers.parse(number)# parase provide phopne number details 1
    time= timezone.time_zones_for_number(phone) # in this i am importing phone number 1 mese 2 ko import kiya hai
    car=carrier.name_for_number(phone,"en")# esme kaunse companika phone number hai "en" give in english
    reg=geocoder.description_for_number(phone,"en")
    print(phone)
    print(time)
    print(car)
    print(reg)