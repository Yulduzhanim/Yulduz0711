mobile_num = "+998970370796"
card_num = "1111"
card_balance = int(10000000)
atm_balance = int(100000000)


def service_1():
    service_type_uz = int(input("""
        1. SMS ulash
        2. SMS o'chirish
        3. Ortga qaytish
    """))

    if service_type_uz == 1:
        a = input("Telefon raqam kiriting:")
        if a == mobile_num:
            print("Amaliyot bajarildi")

    elif service_type_uz == 2:
        print("Kartadagi amaliyot muvaffaqiyatli bajarildi")

    elif service_type_uz == 3:
        main()

    else:
        print("Bunday xizmat turi mavjud emas")
    service_1()


def service_2():
    b = input("Karta raqamini kiriting:")
    if b == card_num:
        print("balansingizda", card_balance, "so'm bor")

    services_uz()


def service_3():
    global card_balance
    global atm_balance
    c = int(input("Kerakli summani kiriting:"))
    if card_balance < c:
        print("Kartangizda mablag' yetarli emas")
    else:
        card_balance = card_balance - (c * 0.01 + c)
        atm_balance = atm_balance - c
        print("Naqd pullaringizni oling")
        print("hisobingizda ", card_balance, " qoldi")
        print("atm da ", atm_balance, " qoldi")

    main()


def service_4():
    d = int(input("Mavjud karta raqamini kiriting:"))
    if d == card_num:
        new_data = input("Yangi kodni kiriting:")
        print("Amaliyot muvaffaqiyatli bajarildi")

    else:
        print("Bunday xizmat turi mavjud emas")
        service_4()
    main()


def menu_uzbek():
    print("Uzbek menu")
    n = 3
    while n > 0:
        password = int(input("karta codini kiriting: "))
        if thecheck_password(password) == True:
            return services_uz()
        else:
            print("Xato kod kiritildi")
            n -= 1
    print("Kartangiz bloklandi")
    return main()


def thecheck_password(password):
    card_password = 1111
    if card_password == password:
        return True
    else:
        return False


def main():
    til = int(input("""
        Tilni tanlang:
        1. Uzbek
        2. Rus
        3. English
        ==>> """))
    if til == 1:
        menu_uzbek()
        # elif til == 2:
    # menu_rus()

    # elif til == 3:
    # menu_english()


def services_uz():
    service = int(input("""Xizmat turini tanglang: 
                    1. SMS xabarnomani ulash
                    2. Karta balansini ko'rish
                    3. Naqd pul olish
                    4. Pin kodni o'zgartirish
                """))
    if service == 1:
        service_1()

    elif service == 2:
        service_2()

    elif service == 3:
        service_3()

    elif service == 4:
        service_4()

    else:
        print("Bunday xizmat turi mavjud emas")
        main()


if __name__ == "__main__":
    main()
