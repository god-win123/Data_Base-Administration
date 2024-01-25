import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="S-technologies"
)


mycursor = mydb.cursor()
balance = 0
#var = 0
fee_num = 0
new_third = 0
print('---------------------------------S-technologies------------------------------------------------')
while True:
    print('1.ADMISSION\n''2.COURSES_AVAILABLE\n''3.CHOSEN_COURSES\n''4.fees_payment\n''5.ENQURIY\n''6.PLACEMENT\n''7.EXIT')
    
    try:
        choice = int(input('Enter a choice : '))
    except:
        print('😑val vazha vacha mathyarnu enn thonnu ipo enik😑')
    else:
        
        if choice > 7:
            print("😊 Bro this choice doesn't exist 😊")

        else:

            if choice == 1:
                print('------------------ADMISSION------------------------------')
                while True:
                    print('1.New_Addmission\n''2.Edit_Admission\n''3.Delete\n''4.View\n''5.Back')
                    try:

                        option = int(input('choose the below option : '))
                    except:
                        print('🥴 Enthonde thodakthile kili poyaa 🥴')
                    else:
                        if option == 1:
                            print('---------------------New_Addmission------------------------------')
                            name = input('Enter the name : ')
                            while True:
                                try:
                                    ph = int(input('Enter the number: '))
                                except:
                                    print(' 😒 Number adiyada porke  😒 ')
                                    
                                else:
                                    addr = input("Enter the address : ")
                                    mail = input("Enter your mail_id : ")
                                    dist = input("Enter your district : ")
                                    gaur_d = input("Enter your gaurdian_name : ")
                                    
                                    try:
                                        g_ph  = int(input("Enter the phone_number : ")) 
                                    except:
                                        print(' 😤Ninode ethra thavana paryanam mowne number adikan 😤')
                                    else:
                                        mycursor.execute("SELECT * FROM course_available")
                                        myresult = mycursor.fetchall()
                                        for x in myresult:
                                            print()
                                            print(" ",x[0]," ",x[1]," ",x[2]," ",x[3])
                                            print()
                                            print()
                                        try:
                                            cours_no = int(input("Enter the id : "))
                                        except:
                                            print(' 😬Aha kolamalo id adikan paranjapol vere enthengilum adikano  😬\n Entha salsa ')
                                        else:
                                            
                                            sql = "SELECT COUNT(*) FROM course_available WHERE id = %s"
                                            val = (cours_no,)
                                            mycursor.execute(sql,val)
                                            myresult = mycursor.fetchall()
                                            # for x in myresult:
                                            # sql = "SELECT name from course_available WHERE id = %s"
                                            # val = (cours_no,)
                                            # mycursor.execute(sql,val)
                                            # myresult = mycursor.fetchall()
                                            # for a in myresult:
                                            #     stu_n = str(a)
                                            sql = "SELECT course_name from course_available WHERE id = %s"
                                            val = (cours_no,)
                                            mycursor.execute(sql,val)
                                            myresult = mycursor.fetchall()
                                            for b in myresult:
                                                course_na = str(b[0])
                                            sql = "SELECT fees from course_available WHERE id = %s"
                                            val = (cours_no,)
                                            mycursor.execute(sql,val)
                                            myresult = mycursor.fetchall()
                                            for c in myresult:
                                                fee_cour = str(c[0])
                                                var = int(fee_cour)

                                            sql = "SELECT duration from course_available WHERE id = %s"
                                            val = (cours_no,)
                                            mycursor.execute(sql,val)
                                            myresult = mycursor.fetchall()
                                            for d in myresult:
                                                dura_cour = str(d[0])
                                            
                                            
                                            
                                            # Insert into addmission

                                            sql = "INSERT INTO addmission (name,ph_no,address,mail,gaurdian_name,gaurdian_pho_no,chosen_courses,district) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                                            val = (name,ph,addr,mail,gaur_d,g_ph,course_na,dist)
                                            mycursor.execute(sql, val)
                                            mydb.commit()

                                            # Insert into chosen_courses
                                            sql = "INSERT INTO chosen_courses (name,course_name,fees,Duration) VALUES (%s,%s,%s,%s)"
                                            val = (name,course_na,fee_cour,dura_cour,)
                                            mycursor.execute(sql,val)
                                            mydb.commit()
                                            #Insert into fees
                                            sql = "INSERT INTO fees_payment (name,fees) VALUES (%s,%s)"
                                            val = (name,fee_cour)
                                            mycursor.execute(sql,val)
                                            mydb.commit()

                                            #Insert into placement
                                            sql = "INSERT INTO placement (name,course) VALUES (%s,%s)"
                                            val = (name,course_na)
                                            mycursor.execute(sql,val)
                                            mydb.commit()

                                            # Insert into enquiry
                                            # sql = "INSERT INTO Enquiry (name,ph_no,district) VALUES (%s,%s,%s)"
                                            # val = (name,ph,dist)
                                            # mycursor.execute(sql, val)
                                            # mydb.commit()
                                            break





                        elif option == 2:
                            print('---------------------Edit Admission------------------------------')
                            print('1.Edit_name\n''2.Edit ph_no\n''3.Edit address\n'
                                '4.Edit_mail\n''5.Edit_dist\n''6.Edit_gard\n''7.Edit_gaur_ph\n''8.Edit course')
                            try:
                                choose = int(input('Enter a choice to edit : '))
                            except:
                                print(' 😬Aha kolamalo id adikan paranjapol vere enthengilum adikano 😬\n Entha salsa ')

                            else:
                                if choose == 1:
                                    print("--------------------Edit name-------------------------------")
                                    print()
                                    mycursor.execute("SELECT * FROM addmission")
                                    myresult = mycursor.fetchall()
                                    for x in myresult:
                                        print()
                                        print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6]," ",x[7])
                                        print()
                                        print()
                                    try:
                                        id = int(input('Whose name you want to change tell the id_no: '))
                                    except:
                                        print('😡Edo than entha engne ayi poye😡')
                                    else:
                                        if id > x[0]:
                                            print("😮‍💨 Bro thankal adich id ithil ila  😮‍💨") 
                                        else:
                                            name = input('Enter the new name : ')
                                        # update name in addmission
                                            sql = "UPDATE addmission SET name = %s WHERE id = %s"
                                            val = (name,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                        # update name in chosen_courses
                                            sql = "UPDATE chosen_courses SET name = %s WHERE id = %s"
                                            val = (name,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                        # update name in fees
                                            sql = "UPDATE fees_payment SET name = %s WHERE id = %s"
                                            val = (name,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                        # update name in placement
                                            sql = "UPDATE placement SET name = %s WHERE id = %s"
                                            val = (name,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                        
                                elif choose == 2:
                                    print("-------------------------Edit Phone_number--------------------------------")

                                    mycursor.execute("SELECT * FROM addmission")
                                    myresult = mycursor.fetchall()
                                    for x in myresult:
                                        print()
                                        print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6]," ",x[7])
                                        print()
                                        print()

                                    try:

                                        id = int(input('Whose number you want to change tell the id_no: '))
                                    except:
                                        print('😡Edo than entha engne ayi poye😡')

                                    else:
                                        if id > x[0]:
                                            print("😮‍💨 Bro thankal adich id ithil ila  😮‍💨")
                                        else:
                                            try:
                                                ph_num = int(input('Enter a new number : '))
                                            except:
                                                print('😵‍💫 Thanik number aranjude 😵‍💫')
                                            else:
                                                sql = "UPDATE addmission SET ph_no = %s WHERE id = %s"
                                                val = (ph_num,id,)
                                                mycursor.execute(sql, val)
                                                mydb.commit()
                                elif choose == 3:
                                    print("-------------------------Edit Address--------------------------------")

                                    mycursor.execute("SELECT * FROM addmission")
                                    myresult = mycursor.fetchall()
                                    for x in myresult:
                                        print()
                                        print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6]," ",x[7])
                                        print()
                                        print()

                                    try:
                                        id = int(input('Whose address you want to change tell the id_no: '))
                                    except:
                                        print('😐oh ente deivame😐')
                                    else:
                                        if id > x[0]:
                                            print(" 🤪 Mowne dinesha No id found   🤪")
                                        else:
                                            new_add = input('Enter the new address : ')
                                            sql = "UPDATE addmission SET address = %s WHERE id = %s"
                                            val = (new_add,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                elif choose == 4:
                                    print("-----------------------Edit email----------------------")

                                    mycursor.execute("SELECT * FROM addmission")
                                    myresult = mycursor.fetchall()
                                    for x in myresult:
                                        print()
                                        print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6]," ",x[7])
                                        print()
                                        print()
                                    try:
                                        id = int(input('Whose email you want to change tell the id_no: '))
                                    except:
                                        print('😐oh ente deivame😐')
                                    else:
                                        if id > x[0]:
                                            print(" 🤪 Mowne dinesha No id found   🤪")
                                        else:
                                            new_email = input('Enter the new email : ')
                                            sql = "UPDATE addmission SET mail = %s WHERE id = %s"
                                            val = (new_email,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                elif choose == 5:
                                    print("----------------------------Edit district-------------------------")

                                    mycursor.execute("SELECT * FROM addmission")
                                    myresult = mycursor.fetchall()
                                    for x in myresult:
                                        print()
                                        print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6]," ",x[7])
                                        print()
                                        print()
                                    try:
                                        id = int(input('Whose district you want to change tell the id_no: '))
                                    except:
                                        print('😑val vazha vacha mathyarnu enn thonnu ipo enik😑')
                                    else:
                                        if id > x[0]:
                                            print(" 🤪 Mowne dinesha No id found   🤪")
                                        else:
                                            new_dist = input('Enter the new district name : ')
                                            sql = "UPDATE addmission SET district = %s WHERE id = %s"
                                            val = (new_dist,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                elif choose == 6:
                                    print("-------------------------Edit gardian name--------------------")

                                    mycursor.execute("SELECT * FROM addmission")
                                    myresult = mycursor.fetchall()
                                    for x in myresult:
                                        print()
                                        print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6]," ",x[7])
                                        print()
                                        print()

                                    try:
                                        id = int(input('Whose gaurdian you want to change tell the id_no: '))
                                    except:
                                        print('😡Edo than entha engne ayi poye😡')

                                    else:
                                        if id > x[0]:
                                            print(" 🤪 Mowne dinesha No id found  🤪")
                                        else:
                                            new_gaurd = input('Enter the new gaurd_name : ')
                                            sql = "UPDATE addmission SET gaurdian = %s WHERE id = %s"
                                            val = (new_gaurd,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                elif choose == 7:
                                    
                                    mycursor.execute("SELECT * FROM addmission")
                                    myresult = mycursor.fetchall()
                                    for x in myresult:
                                        print()
                                        print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6]," ",x[7])
                                        print()
                                        print()

                                    print("-----------------------Edit gardian phone number-----------------------------")
                                    print()
                                    try:
                                        id = int(input('Whose gaurdian_number you want to change tell the id_no: '))
                                    except:
                                        print(' 😩sathyam para ede nii pottan thane!!!\natho abhineyikokeyano 😩')
                                    else:
                                        if id > x[0]:
                                            print("☠️ No id found ☠️")
                                        else:
                                            try:
                                                gh_num = int(input('Enter a new_gh number : '))
                                            except:
                                                print('😷Ath sheri ennit😷')
                                            else:
                                                sql = "UPDATE addmission SET g_ph = %s WHERE id = %s"
                                                val = (gh_num,id,)
                                                mycursor.execute(sql, val)
                                                mydb.commit()
                                elif choose == 8:
                                    print("-----------------------------Edit course-----------------------------")
                                    print()

                                    mycursor.execute("SELECT * FROM addmission")
                                    myresult = mycursor.fetchall()
                                    for x in myresult:
                                        print()
                                        print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6]," ",x[7])
                                        print()
                                        print()

                                    try:
                                        id = int(input('Whose course you want to change tell the id_no: '))
                                    except:
                                        print(' 👽 oho kolamalo mowne  👽')
                                    else:
                                        if id > x[0]:
                                            print("☠️ No id found ☠️")
                                        else:
                                            new_course_book = input("Enter the new course : ")
                                            sql = "UPDATE addmission SET chosen_courses = %s WHERE id = %s"
                                            val = (new_course_book,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()

                                            sql = "UPDATE chosen_courses SET course_name = %s WHERE id = %s"
                                            val = (new_course_book,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()

                                            sql = "UPDATE placement SET course = %s WHERE id = %s"
                                            val = (new_course_book,id,)
                                            mycursor.execute(sql, val)
                                            mydb.commit()




                        elif option == 3:
                            print('---------------------Delete Admission------------------------------')
                            mycursor.execute("SELECT * FROM addmission")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                print(x)
                            try:
                                id = int(input('Enter the id to delete : '))
                            except:
                                print(' 😫oh ene ang koll😫')
                            else:
                                if id > x[0]:
                                    print("😮‍💨 Bro thankal adich id ithil ila  😮‍💨")
                                else:
                                    
                            # deleting the data which is connected with any table
                            
                                    sql = "DELETE FROM addmission WHERE id = %s"
                                    val = (id,)
                                    mycursor.execute(sql,val)
                                    mydb.commit()

                                    sql = "DELETE FROM chosen_courses WHERE id = %s"
                                    val = (id,)
                                    mycursor.execute(sql,val)
                                    mydb.commit()

                                    sql = "DELETE FROM fees_payment WHERE id = %s"
                                    val = (id,)
                                    mycursor.execute(sql,val)
                                    mydb.commit()

                                    sql = "DELETE FROM placement WHERE id = %s"
                                    val = (id,)
                                    mycursor.execute(sql,val)
                                    mydb.commit()


                        elif option == 4:
                            print('--------------------------View Addmission-------------------------------')
                            mycursor.execute("SELECT * FROM addmission")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                print()
                                print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6]," ",x[7]," ",x[8])
                                print()
                        elif option == 5:
                            print('----------------------To go back----------------------------------------')
                            break
            elif choice == 2:
                print('--------------------------------Courses_Available-----------------------------------------')
                while True:
                    print('1.New_course\n''2.Edit_course\n''3.Delete_course\n''4.View_course\n''5.Back')
                    try:
                        option2 = int(input('choose the below option : '))
                    except:
                        print('Invalid Input')
                    else:
                        if option2 == 1:
                            print('---------------------New_Courses------------------------------')
                            course = input('Enter a new_course : ')
                            try:
                                cour_fee = int(input('Enter the course_fee: '))
                            except:
                                print('🤨Entha ninka ninte swantham course fees aranjude🤨')
                            else:
                                dur_time = input('Enter a time_duration : ')
                                sql = "INSERT INTO course_available (course_name,fees,Duration) VALUES (%s,%s,%s)"
                                val = (course,cour_fee,dur_time)
                                mycursor.execute(sql, val)
                                mydb.commit()
                        elif option2 == 2:
                            print('-----------------------Edit_courses--------------------------------')
                            while True:
                                print('1.Edit_course_Name\n''2.Edit fees\n''3.Edit time_duration\n''4.Back')
                                try:
                                    cho_edit = int(input('Enter a option to edit : '))
                                except:
                                    print(' 👽 oho kolamalo mowne  👽')
                                else:
                                    if cho_edit == 1:
                                        print('---------------------------------Edit_course_name------------------------------')
                                        mycursor.execute("SELECT * FROM course_available")
                                        myresult = mycursor.fetchall()
                                        for x in myresult:
                                            print()
                                            print(" ",x[0]," ",x[1]," ",x[2]," ",x[3])
                                            print()
                                        try:
                                            ask = int(input('Enter the id to find the course name : '))
                                        except:
                                            print('😡Edo than entha engne ayi poye😡')
                                        else:
                                            if ask > x[0]:
                                                print("😮‍💨 Bro thankal adich id ithil ila  😮‍💨")
                                            else:
                                                new_course = input('Enter the new course : ')
                                                sql = "UPDATE course_available SET course_name = %s WHERE id = %s"
                                                val = (new_course,ask,)
                                                mycursor.execute(sql, val)
                                                mydb.commit()
                                    elif cho_edit == 2:
                                        print('-----------------------------Edit_fees-----------------------------')
                                        mycursor.execute("SELECT * FROM course_available")
                                        myresult = mycursor.fetchall()
                                        for x in myresult:
                                            print()
                                            print(" ",x[0]," ",x[1]," ",x[2]," ",x[3])
                                            print()
                                        try:
                                            ask_1 = int(input('Enter the id to find the course_fees : '))
                                        except:
                                            print('Invalid Input')
                                        else:
                                            if ask_1 > x[0]:
                                                print("😮‍💨 Bro thankal adich id ithil ila  😮‍💨")
                                            else:
                                                try:
                                                    fee_num = int(input('Enter a new fees : '))
                                                    number = fee_num 
                                                except:
                                                    print('🙄 Bro oru fees adakan a paranjath ok!!! 🙄')
                                                else:
                                                    sql = "UPDATE course_available SET fees = %s WHERE id = %s"
                                                    val = (fee_num,ask_1)
                                                    mycursor.execute(sql, val,)
                                                    mydb.commit()

                                    elif cho_edit == 3:
                                        print('------------------------------------Edit_duration--------------------------------------')
                                        mycursor.execute("SELECT * FROM course_available")
                                        myresult = mycursor.fetchall()
                                        for x in myresult:
                                            print()
                                            print(" ",x[0]," ",x[1]," ",x[2]," ",x[3])
                                            print()
                                        try:
                                            ask_2 = int(input('Enter the id to find the duration : '))
                                        except:
                                            print('💀Ath kolamalo makel ini vere enthelum undo ee thalyil💀')
                                        else:
                                            if ask_2 > x[0]:
                                                print(" 🤪 Mowne dinesha No id found   🤪")
                                            else:
                                                new_duration = input('Enter a new_duration : ')
                                                sql = "UPDATE course_available SET Duration = %s WHERE id = %s"
                                                val = (new_duration,ask_2,)
                                                mycursor.execute(sql, val,)
                                                mydb.commit()
                                    elif cho_edit == 4:
                                        break
                
                        elif option2 == 3:
                            print('---------------------Delete Course------------------------------')
                            mycursor.execute("SELECT * FROM course_available")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                print()
                                print(" ",x[0]," ",x[1]," ",x[2]," ",x[3])
                                print()
                            try:
                                ask_3 = int(input('Enter the id to delete : '))
                            except:
                                print('🤖Ni po mowne dinesha🤖')
                            else:
                                if ask_3 > x[0]:
                                    print(" 🤪 Mowne dinesha No id found   🤪")
                                else:
                                    sql = "DELETE FROM course_available WHERE id = %s"
                                    val = (ask_3,)
                                    mycursor.execute(sql,val)
                                    mydb.commit()       
                        elif option2 == 4:
                            print('--------------------------View Corses-------------------------------')
                            mycursor.execute("SELECT * FROM course_available ")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                print()
                                print(" ",x[0]," ",x[1]," ",x[2]," ",x[3])
                                print()
                        elif option2 == 5:
                            print('----------------------To go back----------------------------------------')
                            break     
            elif choice == 3:
                print('------------------------------------chosen_courses---------------------------------')
                while True:

                    mycursor.execute("SELECT * FROM chosen_courses")
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print()
                        print(" ",x[0]," ",x[1]," ",x[2]," ",x[3])
                        print()
                    print("1.Back")
                    try:
                        back = int(input("Do you want to go back\nif yes then type:1\n"))
                    except:
                        print('😫oh ene ang koll😫')
                    else:
                        if back == 1:
                            break



            elif choice == 4:
                print('-------------------------------Fees--------------------------------------------')
                mycursor.execute("SELECT * FROM fees_payment")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print()
                    print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6])
                    print()
                try:
                    num = int(input('Enter the id to pay the fees : '))
                except:
                    print('🤖Ni po mowne dinesha🤖')
                else:
                    if num > x[0]:
                        print("😓Data not found😓")
                    else:
                        sql = "SELECT fees from fees_payment WHERE id = %s"
                        val = (num,)
                        mycursor.execute(sql,val)
                        myresult = mycursor.fetchall()
                        for o in myresult:
                            str_first_amnt = str(o[0])
                            int_first_amnt = int(str_first_amnt)

                        sql = "SELECT balance from fees_payment WHERE id = %s"
                        val = (num,)
                        mycursor.execute(sql,val)
                        myresult = mycursor.fetchall()
                        for l in myresult:
                            str_bal_amnt = str([0])
                            int_bal_amnt = int(str_first_amnt)
                        

                        
                        sql = "SELECT first_installment from fees_payment WHERE id = %s"
                        val = (num,)
                        mycursor.execute(sql,val)
                        myresult = mycursor.fetchall()
                        for z in myresult:
                            amnt_str = str(z[0])
                            amnt = int(amnt_str)
                        if amnt < 1:
                            while True:
                                try:
                                    first_insta = int(input("Enter the amount you want to pay : "))
                                except:
                                    print('💀Ath kolamalo makel ini vere enthelum undo ee thalyil💀')

                                else:
                                    print(int_first_amnt)
                                    if first_insta == int_first_amnt:
                                        sum = first_insta -int_first_amnt
                                        fee_status = "Completed"
                                        sql = "UPDATE fees_payment SET first_installment = %s WHERE id = %s"
                                        val = (first_insta,num,)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        sql = "UPDATE fees_payment SET second_installment = %s WHERE id = %s"
                                        val = (sum,num,)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        sql = "UPDATE fees_payment SET third_installment = %s WHERE id = %s"
                                        val = (sum,num,)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        sql = "UPDATE fees_payment SET balance = %s WHERE id = %s"
                                        val = (sum,num,)
                                        mycursor.execute(sql,val)
                                        mydb.commit()

                                        sql = "UPDATE fees_payment SET status = %s WHERE id = %s"
                                        val = (fee_status,num,)
                                        mycursor.execute(sql,val)
                                        mydb.commit()

                                        break
                                    else:
                                        sql = "UPDATE fees_payment SET first_installment = %s WHERE id = %s"
                                        val = (first_insta,num,)
                                        mycursor.execute(sql,val)
                                        mydb.commit()

                                        full_ball = int_first_amnt - first_insta
                                        fee_status1 = "Not Completed"
                                        sql = "UPDATE fees_payment SET balance = %s WHERE id = %s"
                                        val = (full_ball,num,)
                                        mycursor.execute(sql,val)
                                        mydb.commit()

                                        sql = "UPDATE fees_payment SET status = %s WHERE id = %s"
                                        val = (fee_status1,num,)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        
                                        break
                        elif amnt > 1:
                                
                            sql = "SELECT second_installment from fees_payment WHERE id = %s"
                            val = (num,)
                            mycursor.execute(sql,val)
                            myresult = mycursor.fetchall()
                            for w in myresult:
                                second_str = str(w[0])
                                second_amnt = int(second_str)
                                if second_amnt < 1:
                                    while True:
                                        try:
                                            second_insta = int(input("Enter the second_installment you want to pay : "))
                                        except:
                                            print('🤕Kurach bodhi edekate🤕')
                                        else:
                                            sql = "UPDATE fees_payment SET second_installment = %s WHERE id = %s"
                                            val = (second_insta,num,)
                                            mycursor.execute(sql,val)
                                            mydb.commit()
                                            new_bal = int_first_amnt - second_insta
                                            org_bal = new_bal - amnt
                                            fee_status = "Completed"
                                            if org_bal == 0:
                                                # sql = "UPDATE fees_payment SET second_installment = %s WHERE id = %s"
                                                # val = (second_insta,num,)
                                                # mycursor.execute(sql,val)
                                                # mydb.commit()
                                                sql = "UPDATE fees_payment SET third_installment = %s WHERE id = %s"
                                                val = (org_bal,num,)
                                                mycursor.execute(sql,val)
                                                mydb.commit()
                                                sql = "UPDATE fees_payment SET balance = %s WHERE id = %s"
                                                val = (org_bal,num,)
                                                mycursor.execute(sql,val)
                                                mydb.commit()

                                                sql = "UPDATE fees_payment SET status = %s WHERE id = %s"
                                                val = (fee_status,num,)
                                                mycursor.execute(sql,val)
                                                mydb.commit()
                                    
                                            elif org_bal != 0:
                                                fee_status1 = " Not Completed"
                                                sql = "UPDATE fees_payment SET balance = %s WHERE id = %s"
                                                val = (org_bal,num,)
                                                mycursor.execute(sql,val)
                                                mydb.commit()

                                                sql = "UPDATE fees_payment SET status = %s WHERE id = %s"
                                                val = (fee_status1,num,)
                                                mycursor.execute(sql,val)
                                                mydb.commit()
                                                break
                                            break
                                elif second_amnt > 1:
                                        sql = "SELECT third_installment from fees_payment WHERE id = %s"
                                        val = (num,)
                                        mycursor.execute(sql,val)
                                        myresult = mycursor.fetchall()
                                        for q in myresult:
                                            third_str = str(q[0])
                                            third_amnt = int(third_str)
                                        sql = "SELECT balance from fees_payment WHERE id = %s"
                                        val = (num,)
                                        mycursor.execute(sql,val)
                                        myresult = mycursor.fetchall()
                                        for y in myresult:
                                            bal_str = str(y[0])
                                            bal_amnt = int(third_str)
                                    
                                            if third_amnt < 1:
                                                try:
                                                    third_insta = int(input("Enter the third_installment you want to pay : "))
                                                    new_third += third_insta
                                                except:
                                                    print(' 👽 oho kolamalo mowne  👽')
                                                else:
                                                    sql = "UPDATE fees_payment SET third_installment = %s WHERE id = %s"
                                                    val = (third_insta,num,)
                                                    mycursor.execute(sql,val)
                                                    mydb.commit()
                                                    bal =  bal_amnt - third_insta
                                    
                                                    # sql = "UPDATE fees_payment SET third_installment = %s WHERE id = %s"
                                                    # val = (third_insta,num,)
                                                    # mycursor.execute(sql,val)
                                                    # mydb.commit()
                                                    if amnt + second_amnt + third_insta == int_first_amnt:
                                                        real_bal = int_first_amnt - int_first_amnt
                                                        fee_status = "Completed"
                                                        sql = "UPDATE fees_payment SET balance = %s WHERE id = %s"
                                                        val = (real_bal,num,)
                                                        mycursor.execute(sql,val)
                                                        mydb.commit()

                                                        sql = "UPDATE fees_payment SET status = %s WHERE id = %s"
                                                        val = (fee_status,num,)
                                                        mycursor.execute(sql,val)
                                                        mydb.commit()
                                                    else:
                                                        full_amnt = amnt + second_amnt + third_insta
                                                        new_full = int_first_amnt - full_amnt
                                                        fee_status1 = "Not completed"
                                                        sql = "UPDATE fees_payment SET balance = %s WHERE id = %s"
                                                        val = (new_full,num,)
                                                        mycursor.execute(sql,val)
                                                        mydb.commit()

                                                        sql = "UPDATE fees_payment SET status = %s WHERE id = %s"
                                                        val = (fee_status1,num,)
                                                        mycursor.execute(sql,val)
                                                        mydb.commit()



                                            else:
                                                if bal_amnt >= 1:
                                                    print(bal_amnt)
                                                    try:
                                                        third_installment = int(input("Enter the third_installment you want to pay : "))
                                                        new_third+=third_installment
                                                    except:
                                                        print(' 👽 oho kolamalo mowne  👽')
                                                    else:
                                                        sql = "UPDATE fees_payment SET third_installment = %s WHERE id = %s"
                                                        val = (new_third,num,)
                                                        mycursor.execute(sql,val)
                                                        mydb.commit()

                                                        bal = bal_amnt - third_installment
                                                    
                                                        

                                                        sql = "UPDATE fees_payment SET balance = %s WHERE id = %s"
                                                        val = (bal,num,)
                                                        mycursor.execute(sql,val)
                                                        mydb.commit()

                                                        if amnt + second_amnt + new_third == int_first_amnt:
                                                            real_bal = int_first_amnt - int_first_amnt
                                                            fee_status = "Completed"
                                                            sql = "UPDATE fees_payment SET balance = %s WHERE id = %s"
                                                            val = (real_bal,num,)
                                                            mycursor.execute(sql,val)
                                                            mydb.commit()
                                                            sql = "UPDATE fees_payment SET status = %s WHERE id = %s"
                                                            val = (fee_status,num,)
                                                            mycursor.execute(sql,val)
                                                            mydb.commit()
                                                        else:
                                                            full_amnt = amnt + second_amnt + new_third
                                                            new_full = int_first_amnt - full_amnt
                                                            fee_status1 = "Not Completed"
                                            
                                                            sql = "UPDATE fees_payment SET balance = %s WHERE id = %s"
                                                            val = (new_full,num,)
                                                            mycursor.execute(sql,val)
                                                            mydb.commit()

                                                            sql = "UPDATE fees_payment SET status = %s WHERE id = %s"
                                                            val = (fee_status1,num,)
                                                            mycursor.execute(sql,val)
                                                            mydb.commit()
                                            
                                            

            elif choice == 5:
                print('--------------------------------Enquiry-------------------------------')
                while True:
                    print('1.ADD Enquiry\n''2.View_Enquiry\n''3.Status_Update\n''4.Edit\n''5.Delete\n''6.Back')
                    try:
                        enq_op = int(input('Enter a choice : '))
                    except:
                        print('💀Ath kolamalo makel ini vere enthelum undo ee thalyil💀')

                    else:
                        if enq_op == 1:
                            print()
                            print('----------------------ADD Enquiry---------------------------------')
                            print()
                            enq_name = input('Enter the name : ')
                            try:
                                enq_ph = int(input('Enter the number: '))
                            except:
                                print(' 😒 Number adiyada porke  😒 ')
                            else:
                                enq_dist = input("Enter your district : ")
                                try:
                                    age = int(input("Enter the age  : "))
                                except:
                                    print(' 😒 Number adiyada porke  😒 ')
                                else:
                                    print('please Select any courses!!!')
                                    print()
                                    mycursor.execute("SELECT * FROM course_available")
                                    myresult = mycursor.fetchall()
                                    for x in myresult:
                                        print()
                                        print(" ",x[0]," ",x[1]," ",x[2]," ",x[3])
                                        print()
                                        print()
                                        print("!!!!Select any one course id!!!!")
                                        print()
                                    try:
                                        cours_id = int(input("Enter the id : "))
                                    except:
                                        print(' 😒 Number adiyada porke  😒 ')
                                    else:
                                        if cours_id > x[0]:
                                            print(" 🤪 Mowne dinesha No id found   🤪")
                                        else:
                                        # Insert into enquiry
                                            sql = "SELECT course_name from course_available WHERE id = %s"
                                            val = (cours_id,)
                                            mycursor.execute(sql,val)
                                            myresult = mycursor.fetchall()
                                            for l in myresult:
                                                course_name = str(l[0])
                                            print("1.Intrested\n""2.Waiting\n""3.Not_Intrested")
                                            print()
                                            status = int(input("What is your status : "))
                                            print()
                                            if status == 1:
                                                sta_tus = "Intrested"
                                            elif status == 2:
                                                sta_tus = "Waiting"
                                            elif status == 3:
                                                sta_tus = "Intrested"
                                            sql = "INSERT INTO Enquiry (name,ph_no,age,place,courses_intrested,status) VALUES (%s,%s,%s,%s,%s,%s)"
                                            val = (enq_name,enq_ph,age,enq_dist,course_name,sta_tus)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                        elif enq_op == 2:
                            print('--------------------------View Enquiry---------------------------------')
                            mycursor.execute("SELECT * FROM enquiry")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                print()
                                print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6])
                                print()
                                print()
                        elif enq_op == 3:
                            print("------------------------------Status update----------------------------------")
                            mycursor.execute("SELECT * FROM enquiry")
                            myresult = mycursor.fetchall()
                            for y in myresult:
                                print()
                                print(" ",y[0]," ",y[1]," ")
                                print()
                            try:
                                choice_enq = int(input("Enter the id : "))
                            except:
                                print(' 👽 oho kolamalo mowne  👽')
                            else:
                                if choice_enq > y[0]:
                                    print("👺Id not found!!!👺")
                                else:
                                    print("1.Intrested\n""2.Waiting\n""3.Not_Intrested")
                                    print()
                                    try:
                                        status_update = int(input("What is your status : "))
                                    except:
                                        print(' 👽 oho kolamalo mowne  👽')
                                    else:
                                        print()
                                        if status_update == 1:
                                            sta_tus_up = "Intrested"
                                        elif status_update == 2:
                                            sta_tus_up = "Waiting"
                                        elif status_update == 3:
                                            sta_tus_up = "Not Intrested"
                                        sql = "UPDATE enquiry SET status = %s WHERE id = %s"
                                        val = (sta_tus_up,choice_enq)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                        elif enq_op == 4:
                            print("----------------------------Edit Enquiry-------------------------------")
                            while True:

                                print('1.Edit_name\n''2.Edit ph_no\n''3.Edit age\n'
                                    '4.Edit courses_intrested\n''5.Edit place\n''6.Back')
                                try:
                                    Edit_enq = int(input('Enter a choice to edit : '))
                                except:
                                    print(' 😫oh ene ang koll😫')
                                else:
                                    if Edit_enq == 1:

                                        print('--------------------------Edit name-------------------------')
                                        mycursor.execute("SELECT * FROM enquiry")
                                        myresult = mycursor.fetchall()
                                        for x in myresult:
                                            print()
                                            print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6])
                                            print()

                                        try:
                                            enq_id = int(input('Whose name you want to change tell the id_no: '))
                                        except:
                                            print(' 👽 oho kolamalo mowne  👽')
                                        else:
                                            if enq_id > x[0]:
                                                print(" 🤪 Mowne dinesha No id found   🤪")
                                            else:
                                                name = input('Enter the new name : ')
                                                sql = "UPDATE enquiry SET name = %s WHERE id = %s"
                                                val = (name,enq_id,)
                                                mycursor.execute(sql, val)
                                                mydb.commit()

                                    elif Edit_enq == 2:
                                            print("-----------------------Edit number--------------------------")

                                            mycursor.execute("SELECT * FROM enquiry")
                                            myresult = mycursor.fetchall()
                                            for x in myresult:
                                                print()
                                                print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6])
                                                print()

                                            try:

                                                enq_id_2 = int(input('Whose number you want to change tell the id_no: '))
                                            except:
                                                print(' 😫oh ene ang koll😫')
                                            else:
                                                if enq_id_2 > x[0]:
                                                    print(" 🤪 Mowne dinesha No id found   🤪")
                                                else:
                                                    try:
                                                        ph_num = int(input('Enter a new number : '))
                                                    except:
                                                        print('😑val vazha vacha mathyarnu enn thonnu ipo enik😑')
                                                    else:
                                                        sql = "UPDATE enquiry SET ph_no = %s WHERE id = %s"
                                                        val = (ph_num,enq_id_2,)
                                                        mycursor.execute(sql, val)
                                                        mydb.commit()

                                    elif Edit_enq == 3:

                                        print("------------------------------Edit Age---------------------------")

                                        mycursor.execute("SELECT * FROM enquiry")
                                        myresult = mycursor.fetchall()
                                        for x in myresult:
                                            print()
                                            print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6])
                                            print()

                                        try:
                                            enq_id_3 = int(input("Whose age you want to change give id no: "))
                                        except:
                                            print('🤖Ni po mowne dinesha🤖')
                                        else:
                                            if enq_id_3 > x[0]:
                                                print(" 🤪 Mowne dinesha No id found  🤪")
                                            else:
                                                try:
                                                    new_enq_age = int(input("Enter a new age : "))
                                                except:
                                                    print('🤖Ni po mowne dinesha🤖')
                                                else:
                                                    sql = "UPDATE enquiry SET age = %s WHERE id = %s"
                                                    val = (new_enq_age,enq_id_3,)
                                                    mycursor.execute(sql, val)
                                                    mydb.commit()

                                    elif Edit_enq == 4:
                                        mycursor.execute("SELECT * FROM enquiry")
                                        myresult = mycursor.fetchall()
                                        for x in myresult:
                                            print()
                                            print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6])
                                            print()
                                        try:
                                            enq_id_4 = int(input("Whose course you want to change give id no :"))
                                        except:
                                            print('😑val vazha vacha mathyarnu enn thonnu ipo enik😑')
                                        else:
                                            if enq_id_4 > x[0]:
                                                print(" 🤪 Mowne dinesha No id found 🤪")
                                            else:
                                                mycursor.execute("SELECT * FROM course_available")
                                                myresult = mycursor.fetchall()
                                                for x in myresult:
                                                    print()
                                                    print(" ",x[0]," ",x[1]," ",x[2]," ",x[3])
                                                    print()
                                                    print()
                                                try:
                                                    new_cours_id = int(input("Enter the id : "))
                                                except:
                                                    print('😑val vazha vacha mathyarnu enn thonnu ipo enik😑')
                                                else:
                                                    sql = "SELECT course_name from course_available WHERE id = %s"
                                                    val = (new_cours_id,)
                                                    mycursor.execute(sql,val)
                                                    myresult = mycursor.fetchall()
                                                    for m in myresult:
                                                        enq_course_name = str(m[0])
                                                    sql = "UPDATE enquiry SET courses_intrested = %s WHERE id = %s"
                                                    val = (enq_course_name,enq_id_4,)
                                                    mycursor.execute(sql, val)
                                                    mydb.commit()
                                                    break
                                    elif Edit_enq == 5:

                                        print("-----------------------------Edit place---------------------------")

                                        mycursor.execute("SELECT * FROM enquiry")
                                        myresult = mycursor.fetchall()
                                        for x in myresult:
                                            print()
                                            print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6])
                                            print()

                                        try:
                                            enq_id_5 = int(input('Whose place you want to change tell the id_no: '))
                                        except:
                                            print('😑val vazha vacha mathyarnu enn thonnu ipo enik😑')
                                        else:
                                            if enq_id_5 > x[0]:
                                                print(" 🤪 Mowne dinesha No id found   🤪")
                                            else:
                                                new_place = input('Enter the new address : ')
                                                sql = "UPDATE enquiry SET place = %s WHERE id = %s"
                                                val = (new_place,enq_id_5,)
                                                mycursor.execute(sql, val)
                                                mydb.commit()
                                    elif Edit_enq == 6:
                                        break
                        elif enq_op == 5:

                            print("--------------------------------Delete enquiry--------------------------------")

                            mycursor.execute("SELECT * FROM enquiry")
                            myresult = mycursor.fetchall()
                            for x in myresult:
                                print()
                                print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ",x[5]," ",x[6])   

                            try:
                                enq_del = int(input('Enter the id to delete : '))
                            except:
                                print(' 😬Aha kolamalo id adikan paranjapol vere enthengilum adikano 😬\n Entha salsa ')

                            else:
                                if id > x[0]:
                                    print(" 🤪 Mowne dinesha No id found   🤪")
                                else:
                                    sql = "DELETE FROM enquiry WHERE id = %s"
                                    val = (enq_del,)
                                    mycursor.execute(sql,val)
                                    mydb.commit()

                        elif enq_op == 6:
                            print("-------------------------Exit-------------------------------")
                            break

            elif choice == 6:
                print("--------------------------Placement------------------------------------")
                print()
                mycursor.execute("SELECT * FROM placement")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print()
                    print(" ",x[0]," ",x[1]," ",x[2]," ",x[3]," ",x[4]," ")
                try:
                    st_id = int(input("Enter the id no: "))
                except:
                    print("☠️ id adika bro ☠️")
                else:
                    if st_id > x[0]:
                        print("☠️ No id found ☠️")
                    else:
                        try:    
                            st_interview = int(input("Enter the total inteviews that you have attended : "))
                        except:
                            print("☠️ Enthonde ethra interviwe attend cheyithath kudi arythile ☠️")
                        else:
                            print()
                            print()
                            sql = "UPDATE placement SET interviews = %s WHERE id = %s"
                            val = (st_interview,st_id)
                            mycursor.execute(sql,val)
                            mydb.commit()

                            if st_interview >= 1:
                                company = "Placed"
                                sql = "UPDATE placement SET status = %s WHERE id = %s"
                                val = (company,st_id)
                                mycursor.execute(sql,val)
                                mydb.commit()
                            else:
                                st_interview < 1
                                company = "Not Placed"
                                sql = "UPDATE placement SET status = %s WHERE id = %s"
                                val = (company,st_id)
                                mycursor.execute(sql,val)
                                mydb.commit()
            elif choice == 7:
                try:
                    ask5 = int(input("Do you want to exit from the program\ntype 1 for yes and 2 for no\n"))
                except:
                    print(' 👽 oho kolamalo mowne  👽')
                else:
                    if ask5 == 1:
                        print("😎 Enna sheri Bro\nIni run cheyumbol veram 😎")
                        exit()
                    else:
                        continue

                        



                                
                    



            



                    












                                
                            
                            


                        

                        

                            


