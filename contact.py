contacts={
    "nived":"9947810550",
    "arun":"9078674512",
    "anjana":"9889755766",
    "devika":"7698884435"
}
while True:
 print("Menu:\n 1.Add contact\n 2.View Contact\n 3.Update Contact\n 4.Delete Contact\n 5.Exit\n")
 choice=input("enter your choice: ")
 if choice=="1":
  name=input("enter your name: ")
  if name in contacts:
   print("contact already exist")
  else:
   phone=input("enter your number:")
   contacts[name]=[phone]
  print("contactsaved sucessfully")  
 elif choice == "2":
             if not  contacts:
                 print("no result found:")
             else:
                 print("saved contacts:")
                 for name, phone in contacts.items():
                     print(name,":",phone)
 elif choice=="3":
     name=input("enter contact name to update :")
     if name in contacts:
         number=int(input("enetr the new number:"))
         contacts[name].append(number)
         print("contact updated sucessfully")
     else:
         print("no result found")    
 elif choice=="4":
     name=input("enter the name:")
     if name in contacts:
         del contacts[name]
         print("contact deleted sucessfully")
     else:
         print("no result found")            
 elif choice=="5":
     print("exiting contact book:")
     break
 else:
  print('invalid user_input,please try again:')
            
     
























# ----------------------------
# contacts = {
#     "Radhika":"9747085042",
#     "Sahala":"9207165232",
#     "Nabeel":"9567839598",
#     "Alfidha":"9686569686"
#  }
# while True:
#       print(" contact book ")
#       print(" 1. add contacts ")
#       print(" 2. view contacts ")
#       print(" 3. update contact ")
#       print(" 4. delete contact ")
#       print(" 5. exit")

#       user_input = input("enter your input:")

#       if user_input =="1":
#         name = input("enter contact name:")
#         if name in contacts:
#             print("contact already exist:")
#         else:
#             phone = input("enter the phone number:")
#             contacts[name] = phone
#             print("contact added sucessfully:")
#       elif user_input == "2":
#             if not  contacts:
#                 print("no result found:")
#             else:
#                 print("saved contacts:")
#                 for name, phone in contacts.items():
#                     print(name,":",phone)
#       elif user_input == "3":
#             name= input("enter contact name to update:")
#             if name in contacts:
#                 phone = input("enter new phone number:")
#                 contacts[name] = phone 
#                 print("contact updated sucessfully:")
#             else:
#                 print("no result found:")
#       elif user_input=="4":
#             name = input("enter the contact name to be deleted:")
#             if name in contacts:
#                 del contacts[name]
#                 print("contact deleted sucessfully:")
#             else:
#                 print(" no result found:")
#       elif user_input =="5":
    #         print("exiting contact book:")
    #         break
    #   else:
    #         print('invalid user_input,please try again:')
