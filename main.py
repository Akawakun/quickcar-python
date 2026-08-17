print("===== QuickCar =====")

while True:

    print("\n1. รถเก๋ง - 500 บาท/วัน")
    print("2. รถกระบะ - 700 บาท/วัน")
    print("3. รถตู้ - 1,000 บาท/วัน")

    car = input("เลือกรถ: ")
    days = int(input("จำนวนวันที่เช่า: "))

    if car == "1" or car == "รถเก๋ง":
        car_name = "รถเก๋ง"
        price = 500

    elif car == "2" or car == "รถกระบะ":
        car_name = "รถกระบะ"
        price = 700

    elif car == "3" or car == "รถตู้":
        car_name = "รถตู้"
        price = 1000

    else:
        print("ไม่มีรถประเภทนี้")
        continue

    total = price * days

    print("\n===== ข้อมูลการจอง =====")
    print("รถที่เลือก:", car_name)
    print("จำนวนวัน:", days)
    print("ราคารวม:", total, "บาท")

    print("\nต้องการทำรายการต่อหรือไม่?")
    print("1. ทำรายการใหม่")
    print("2. ออกจากโปรแกรม")

    choice = input("เลือก: ")

    if choice == "2":
        print("\nขอบคุณที่ใช้บริการ QuickCar")
        break
