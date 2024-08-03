import phonenumbers
from phonenumbers import timezone,geocoder,carrier,format_number,PhoneNumberFormat
number=input("Enter your number with +__:")
        

phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
f_international= format_number(phone, PhoneNumberFormat.INTERNATIONAL)
f_national= format_number(phone, PhoneNumberFormat.NATIONAL)
f3= format_number(phone, PhoneNumberFormat.E164)
print("Details:",phone)
print("The standard time followed by this Phone Number is:",time)
print("The Sim used by this Mobile Number is:",car)
print("The region of this Mobile Number is:",reg)
print("International Format of Mobile Number:",f_international)
print("National format of the Mobile Number:",f_national)
print("Original Format:",f3)

