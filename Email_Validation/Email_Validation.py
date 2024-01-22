#                             #Email_ validatio with code + theory

# Email=input("Enter your Email : ")# g@g.in, rkpandey9923@gmail.com
# k,J,d=0,0,0
# if len(Email)>=6: #in we give the email lenth 6 bhi chale ga email aur use jada bhi chale ga
#     #in this we use index function
#     if Email[0].isalpha():
#         #we are give a email  @ or give @ couniting value  in email 
#         if("@"in Email) and (Email.count("@")==1):# inthis(Email.count("@")==1): we give we need a @ one in email
#      # iam giving the dot . postion or we usa string indexing froom last us negative -1-2-3-4
#             if (Email[-4]==".") ^ (Email[-3]=="."):
#                 # I am using forloop or iam itrate the string we chek every thing scape ke barabr to nahi hai
#                 for i in Email:
#                     if i==i.isspace():
#                         k=1
#                     # in thiswe check if uppper case was come than he will be wrong email eg:QWERD
#                     # elif# why iam using the elif if our first i agar pase nahi hai to necha wale ko hint kare wrong email5 ko
#                     elif i.isalpha():# this will be com-->a
#                         if i==i.upper():#--> this will convert the example -->a=A if our "A come in capital then A==A the we do in next line yo can see "
#                             J=1
#                     #know iam check the digit
#                     elif i.isdigit():
#                         continue # UPER JANA CHIYE
#                     # KNOW  IAM CHECK IN MY EMAIL _ , . ,@
#                     elif i=="_"or i=="." or i=="@": # ya valu false nahi lone chiye mail
#                         continue
#                     else:
#                         d=1

#                 if k==1 or J==1 or d==1:
#                     print("Wrong Email 5 ")
#             else:
#                 print("Wrong Email 4")
#         else:
#             print ("Wrong Email 3")
#     else:
#         print("Wrong Email 2")
# else:
#     print("Wrong Email 1 ") #agar 6 se chota hai




                            #Email_ validatio with onlly code 

Email=input("Enter your Email : ")# g@g.in, rkpandey9923@gmail.com
k,J,d=0,0,0
if len(Email)>=6: #1
    if Email[0].isalpha():#2
        if("@"in Email) and (Email.count("@")==1):#3
            if (Email[-4]==".") ^ (Email[-3]=="."):#4
                for i in Email:
                    if i==i.isspace():  #5
                        k=1
                    elif i.isalpha():   #5
                        if i==i.upper():
                            J=1
                    elif i.isdigit():   #5
                        continue 
                    elif i=="_"or i=="." or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or J==1 or d==1:
                    print("Wrong Email 5 ")#5
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4")#4
        else:
            print ("Wrong Email 3")#3
    else:
        print("Wrong Email 2")#2
else:
    print("Wrong Email 1 ") #agar 6 se chota hai #1


#1 condition 1==Enter your Email : Ankit
# Wrong Email 1 


#2 condition 2-->1ankit@gmail.com
# Wrong Email 2

#3 condition 3-->Enter your Email : Ankit@pandey@gmail.com
# Wrong Email 3

#4 condition 4--->Enter your Email : Ankit@gmail.c
# Wrong Email 4

#condtion Space will be not accept 5 --->Enter your Email : Ankit pandey@gmail.com
# Wrong Email 5


#condtion uperCase will be not accept 5 ---> Enter your Email : Ankitpandeygmail@.com
# Wrong Email 5 


#condtion isdigit will be not accept 5-->Enter your Email : ankit#@gmail.com
# Wrong Email 5



#condtion uperCase will be not accept 5---->Enter your Email : an_kit@gmail.com (this will be no throw error because we space by in digit we can us.,_@)



#condtion uperCase will be not accept 5

