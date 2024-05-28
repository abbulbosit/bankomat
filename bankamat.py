from datetime import datetime

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Lenguage Uzbek>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

user_info = {
    "first_name": "John", "last_name": "Smith",
    "card_password": 2009, "card_balance": 2000000,
    "card_number":"8600963096308520",
    "phone_number": "", "status": False}
data_atm = {"balance": 5000000}

def uzbek_balance_display():
    a = input(f"""
    Sizning balansingiz {user_info["card_balance"]} so'm
    Boshqa xizmatdan foydalanishni istaysizmi?
        1. Ha
        2. Yo'q
            >>> """)

    if a == "1":
        return uzbek_services()

    elif a == "2":
        return main()

    else:
        print("Error")
        return uzbek_balance_display()

def uzbek_balance_check():
    print("Bizni tanlaganiz uchun tashakkur")
    check = f"""
                CHECK
        Balance: {user_info["card_balance"]}
        Card: {12 * "*" + user_info["card_number"][-4::]}
        Time: {datetime.now()}
    """
    print(check)
    return main()

def uzbek_service_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    services = input("""
        1. Ekranda ko'rish
        2. Chekda ko'rish
            >>> """)
    if services == "1":
        return uzbek_balance_display()

    elif services == "2":
        return uzbek_balance_check()

def check_balance(money):
    m = money * 1.01
    if user_info["card_balance"] > m and data_atm["balance"] >= money:
        tasdiq = input(f"""
                        Kartadan yechiladigan summa {m}
                            1. Davom etish
                            2. Bekor qilish
                                >>> """)
        if tasdiq == "1":
            user_info["card_balance"] -= m
            data_atm["balance"] -= money
            print("Amaliyot muvaffaqiyatli yakunlandi")
            return uzbek_services()

        elif tasdiq == "2":
            print("Xizmat bekor qilindi")
            return uzbek_services()

        else:
            print("Error")
            return uzbek_service_money()

    else:
        print("Xatolik!!!")
        return main()


def uzbek_service_money():
    money = input("""
        Summani tanlang:
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. Boshqa summa
            0. Orqaga
                >>> """)

    if money == "1":
        return check_balance(50000)

    elif money == "2":
        return check_balance(100000)

    elif money == "3":
        return check_balance(300000)

    elif money == "4":
        return check_balance(400000)

    elif money == "6":
        money = input("""Summani kiriting: """)
        return check_balance(int(money))

    elif money == "0":
        return uzbek_services()

    else:
        print("Error")
        return uzbek_service_money

def uz_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
            Telefon raqamingizni kiriting: 
                +998 _ >>> """)
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Successful")
            return uzbek_services()
        else:
            print('Xatolik')
            return uz_sms_on()
    else:
        print("Bu raqamga allaqachon sms xabarnoma ulangan")
        return uzbek_services()

def uz_sms_off():
    if user_info["status"] == True:
        print("Successfull")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return uzbek_services()

    else:
        print("Bu raqamga allaqachon sms xabarnoma ulanmagan")
        return uzbek_services()

def uzbek_service_sms():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        Phone Number {user_info["phone_number"]}
        """)
    service = input("""
        1. SMS Xabarnomani ulash
        2. SMS Xabarnomani o'chirish
            >>> """)
    if service == "1":
        return uz_sms_on()

    elif service == "2":
        return uz_sms_off()


def uzbek_service_add_money():
    print("ADD")
    money = input("Summani kiriting: ")
    if money.isalnum():
        user_info["card_balance"] += int(money)
        data_atm["balance"] += int(money)
        print("Successfull")
        return uzbek_services()
    else:
        print("Error")
        return uzbek_service_money()

def chage_the_pin():
    pin1 = input("hozirgi pin kodni kiriting: ")
    if pin1 == user_info["card_password"]:
        pin2 = input("o'zgartirishni xoxlagan pin kodni kiriting: ")
        user_info["card_balance"] = int(pin2)
def uzbek_services():
    print("Service Page")
    services = input("""
        Xizmat turini tanglang:
            1. Balanceni ko'rish
            2. Naqt pul yechish
            3. SMS Xabarnoma
            4. Kartani to'ldirish
            5. pin kodeni o'zgartirish
            0. Back
                >>> """)

    if services == "1":
        return uzbek_service_balance()

    elif services == "2":
        return uzbek_service_money()

    elif services == "3":
        return uzbek_service_sms()

    elif services == "4":
        return uzbek_service_add_money()

    elif services == "5":
        return chage_the_pin()

    elif services == "0":
        print("Bizni tanlaganiz uchun tashakkur!")
        return main()

    else:
        print("Bunday xizmat turi mavjud emas")
        return uzbek_services()


def uzbek():
    print("<<<<<<<<<<<<<<Uzbek Lenguage>>>>>>>>>>>>>>>>")
    password = input("Pin codeni kiriting: ")
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Error")
        password = int(input("Pin codeni kiriting: "))
        n -= 1

    if user_info["card_password"] == password:
        return uzbek_services()

    print("Sizning Kartangiz bloklandi")
    return main()

def main():
    lenguage = input("""
        Tilni tanglang:
            1. Uzbek
            2. English
            3. Russian
                >>> """)

    if lenguage == "1":
        return uzbek()

    elif lenguage == "2":
        return english()

    elif lenguage == "3":
        return russian()

    else:
        print("Bunday til mavjud emas")
        return main()

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Lenguage English>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def english_balance_display():
        a = input(f"""
        your balans is {user_info["card_balance"]} soum
        Do you want use another service ?
            1. Yes
            2. No
                >>> """)

        if a == "1":
            return english_services()

        elif a == "2":
            return main()

        else:
            print("Error")
            return english_balance_display()()


def  english_balance_check():
        print("thank you for choosing us")
        check = f"""
                    CHECK
            Balance: {user_info["card_balance"]}
            Card: {12 * "*" + user_info["card_number"][-4::]}
            Time: {datetime.now()}
        """
        print(check)
        return main()
def english_services_add_money():
        print("<<<<<<<<<Balance>>>>>>>>")
        services = input("""
            1. wiew on screen
            2. wiew on margin
                >>> """)
        if services == "1":
            return english_balance_display()

        elif services == "2":
            return english_balance_check()

def take_balance(money):
    m = money * 1.01
    if user_info["card_balance"] > m and data_atm["balance"] >= money:
        confirmation = input(f"""
                        Amount debited from the cart {m}
                            1. contination
                            2. canse
                                >>> """)
        if confirmation == "1":
            user_info["card_balance"] -= m
            data_atm["balance"] -= money
            print("operation completed successfully")
            return english_services()

        elif confirmation == "2":
            print("service cancelled")
            return english_services()

        else:
            print("Error")
            return english_services_take_money()

    else:
        print("error!!!")
        return main()

def english_services_take_money():
        money = input("""
            select an amount:
                1. 50.000
                2. 100.000
                3. 200.000
                4. 300.000
                5. 400.000
                6. other amount 
                0. Bakc
                    >>> """)

        if money == "1":
            return take_balance(50000)

        elif money == "2":
            return take_balance(100000)

        elif money == "3":
            return take_balance(300000)

        elif money == "4":
            return take_balance(400000)

        elif money == "6":
            money = input("""enter an amount: """)
            return take_balance(int(money))

        elif money == "0":
            return english_services()

        else:
            print("Error")
            return english_services_take_money

def english_services_sms_notif():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        Phone Number {user_info["phone_number"]}
        """)
    service = input("""
        1. connect SMS Notification
        2. Delete SMS Notification
            >>> """)
    if service == "1":
        return eng_sms_on()

    elif service == "2":
        return eng_sms_off()

def eng_sms_off():
    if user_info["status"] == True:
        print("Successfull")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return english_services()

    else:
        print("Bu raqamga allaqachon sms xabarnoma ulanmagan")
        return english_services()
def eng_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
            enter the phone nomber: 
                +998 _ >>> """)
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Successful")
            return english_services()
        else:
            print('Xatolik')
            return eng_sms_on()
    else:
        print("Bu raqamga allaqachon sms xabarnoma ulangan")
        return english_services()

def english_services_filling_out_the_balans():
        print("ADD")
        money = input("enter the money to be : ")
        if money.isalnum():
            user_info["card_balance"] += int(money)
            data_atm["balance"] += int(money)
            print("Successfull")
            return english_services()
        else:
            print("Error")
            return english_services_take_money()

def english_chage_the_pin():
    pin1 = input("enter your currrent pin: ")
    if pin1 == user_info["card_password"]:
        pin2 = input("enter the pin code you want to change: ")
        user_info["card_balance"] = int(pin2)
def english_services():
    print("Service Page")
    services = input("""
        select the type of service:
            1. wiew the balans 
            2. cash withdrawal
            3. SMS notification
            4. filling out the balans
            0. Back
                >>>  """)
    if services == "1":
        return english_services_add_money()

    elif services =="2":
        return english_services_take_money()

    elif services =="3":
        return english_services_sms_notif()

    elif services =="4":
        return english_services_filling_out_the_balans()

    elif services == "5":
        return english_chage_the_pin()

    else:
        return main()
def english():
    print("<<<<<<<<<<<<<<english Lenguage>>>>>>>>>>>>>>>>")
    password = int(input("enter password: "))
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Error")
        password = input("enter password: ")
        n -= 1

    if user_info["card_password"] == password:
        return english_services()

    print("your card is locked")
    return main()

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<lengueg russian>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def rus_service_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    services = input("""
        1. uvidit v ekrane
        2. uvidit v cheke
            >>> """)
    if services == "1":
        return rus_balance_display()

    elif services == "2":
        return rus_balance_check()
def rus_balance_check():
    print("spasiba za to shto vibrili nas")
    check = f"""
                CHECK
        Balance: {user_info["card_balance"]}
        Card: {12 * "*" + user_info["card_number"][-4::]}
        Time: {datetime.now()}
    """
    print(check)
    return main()
def rus_balance_display():
    a = input(f"""
    vash balans {user_info["card_balance"]} so'm
    xatite ispolzavat drugiye vazmojnistey?
        1. da
        2. net
            >>> """)

    if a == "1":
        return russian()

    elif a == "2":
        return main()

    else:
        print("Error")
        return rus_balance_display()

def rus_check_balance(money):
    m = money * 1.01
    if user_info["card_balance"] > m and data_atm["balance"] >= money:
        tasdiq = input(f"""
                        summa abnalichvayemiy iz karti {m}
                            1. saoglasitsa
                            2. atmenit
                                >> """)
        if tasdiq == "1":
            user_info["card_balance"] -= m
            data_atm["balance"] -= money
            print("aperatsiya uspeshna zakonchilsa")
            return main()

        elif tasdiq == "2":
            print("aperatsiya atmenon")
            return main()

        else:
            print("ashipka")
            return rus_service_money()

    else:
        print("ashipka!!!")
        return main()


def rus_service_money():
    money = input("""
        vibirite summu:
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. drugaya summa
            0. nazad
                >>> """)

    if money == "1":
        return check_balance(50000)

    elif money == "2":
        return check_balance(100000)

    elif money == "3":
        return check_balance(300000)

    elif money == "4":
        return check_balance(400000)

    elif money == "6":
        money = input("""vedite summu: """)
        return  rus_check_balance(int(money))

    elif money == "0":
        return russian()

    else:
        print("Error")
        return rus_service_money

def rus_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
            Vedite telefonni nomer: 
                +998 _ >>> """)
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Successful")
            return russian()
        else:
            print('Xatolik')
            return rus_sms_on()
    else:
        print("Bu raqamga allaqachon sms xabarnoma ulangan")
        return russian()

def rus_sms_off():
    if user_info["status"] == True:
        print("zdelana")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return russian()

    else:
        print("na etat nomer uje potkluchon SMS uvedamleniya")
        return russian()
def rus_service_sms():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        telefonni nomer {user_info["phone_number"]}
        """)
    service = input("""
        1. patklyuchit SMS uvedamleniya
        2. atklyuchit SMS uvedamleniya
            >>> """)
    if service == "1":
        return rus_sms_on()

    elif service == "2":
        return rus_sms_off()

def rus_service_add_money():
    print("ADD")
    money = input("vedite summu: ")
    if money.isalnum():
        user_info["card_balance"] += int(money)
        data_atm["balance"] += int(money)
        print("zdelana")
        return russian()
    else:
        print("Error")
        return rus_service_money()

def rus_chage_the_pin():
    pin1 = input("vedite tekushshe pin kod : ")
    if pin1 == user_info["card_password"]:
        pin2 = input("vedite pin kod katoriy vi xateli smenit: ")
        user_info["card_balance"] = int(pin2)
    print("aperatsiya uspeshna zdelan \n spasiba za to shto vi brali nas")
    return main()
def russian():
    print("lenta vazmojnistey")
    services = input("""
        vibirite tip uslugi:
            1. uvidet balans karti
            2. abnalichit nalichkami
            3. SMS uvedamleniye
            4. papalneniye karti
            5. izmenit pin kod
            0. nazad
                >>> """)

    if services == "1":
        return rus_service_balance()

    elif services == "2":
        return rus_service_money()

    elif services == "3":
        return rus_service_sms()

    elif services == "4":
        return rus_service_add_money()

    elif services == "5":
        return rus_chage_the_pin()

    elif services == "0":
        print("spasiba za to shto vibrali nas!")
        return main()

    else:
        print("takoy tip uslugi ne sushestvuet ")
        return russian()

if __name__ == "__main__":
    main()
