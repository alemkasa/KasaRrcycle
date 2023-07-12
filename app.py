import hashlib
import geolocation
import re
import barcode
from PIL import Image

# אבטחת מידע של המשתמש
def encrypt_data(data):
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    return hashed_data

# קליטה של שם ושם משפחה
def get_full_name():
    first_name = input("הזן שם פרטי: ")
    last_name = input("הזן שם משפחה: ")
    return first_name, last_name

# קליטה של מקום מגורים + שיתוף מיקום
def get_location():
    location = input("הזן מקום מגורים: ")
    share_location = input("האם תרצה לשתף את מיקומך? (כן/לא): ")
    return location, share_location

# הכנסה של מספר נייד (כאן ניתן להכניס רק מספרים) כולל קידומת ארצית
def get_phone_number():
    phone_number = input("הזן מספר טלפון: ")
    # בדיקת תקינות מספר הטלפון
    if re.match(r'^\d{10}$', phone_number):
        return phone_number
    else:
        print("מספר טלפון לא תקין!")
        return None

# יכולת לצלם ברקוד של מוצר בהתאם לחוק הפיקדון
def capture_barcode():
    # קידוד המוצר בברקוד
    product_code = barcode.generate_product_code()
    # צילום הברקוד
    barcode_image = barcode.capture_barcode()
    return product_code, barcode_image

# שמירה של הצילום
def save_image(image):
    image.save("captured_image.jpg")

# סיווג של הצילום לפי חוק הפיקדון
def classify_image(image):
    classification = barcode.classify_image(image)
    return classification

# שכלול הנתונים והצגה של סך הכל בצורה נוחה ומובנת
def display_summary(data):
    print("סיכום נתונים:")
    for key, value in data.items():
        print(f"{key}: {value}")

# יצירת קוד קופון אישי (QR) לאחר סיום פעולת הצילום
def generate_personal_coupon():
    user_id = input("הזן מזהה משתמש: ")
    coupon_code = barcode.generate_coupon_code(user_id)
    qr_code = barcode.generate_qr_code(coupon_code)
    return qr_code

# דוגמה לשימוש של הפונקציות:
user_data = {}

# אבטחת מידע של המשתמש
password = input("הזן סיסמה: ")
encrypted_password = encrypt_data(password)
user_data['password'] = encrypted_password

# קליטה של שם ושם משפחה
first_name, last_name = get_full_name()
user_data['first_name'] = first_name
user_data['last_name'] = last_name

# קליטה של מקום מגורים + שיתוף מיקום
location, share_location = get_location()
user_data['location'] = location
user_data['share_location'] = share_location

# הכנסה של מספר נייד (כאן ניתן להכניס רק מספרים) כולל קידומת ארצית
phone_number = get_phone_number()
if phone_number:
    user_data['phone_number'] = phone_number

# יכולת לצלם ברקוד של מוצר בהתאם לחוק הפיקדון
product_code, barcode_image = capture_barcode()
user_data['product_code'] = product_code

# שמירה של הצילום
save_image(barcode_image)

# סיווג של הצילום לפי חוק הפיקדון
classification = classify_image(barcode_image)
user_data['classification'] = classification

# שכלול הנתונים והצגה של סך הכל בצורה נוחה ומובנת
display_summary(user_data)

# יצירת קוד קופון אישי (QR) לאחר סיום פעולת הצילום
personal_coupon = generate_personal_coupon()
print("קוד קופון אישי (QR):", personal_coupon)
import xlwt
import os

# יציאת הנתונים לאקסל
def export_to_excel(data):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Data')
    row = 0
    for key, value in data.items():
        sheet.write(row, 0, key)
        sheet.write(row, 1, value)
        row += 1
    workbook.save('data.xls')
    print("הנתונים יוצאים לאקסל בהצלחה!")

# תמונת מצב
def show_status_image():
    image_path = 'status_image.jpg'
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image.show()
    else:
        print("תמונת המצב לא נמצאה.")

# עדכון נתונים וסטטיסטיקות
def update_data_statistics(data):
    # עדכון הנתונים והסטטיסטיקות
    print("עדכון הנתונים והסטטיסטיקות...")
    # לשים כאן את הלוגיקה המתאימה לעדכון הנתונים והסטטיסטיקות
    print("הנתונים והסטטיסטיקות עודכנו בהצלחה.")

# משחק צורות בקבוקים
def play_bottle_shapes_game():
    print("משחק צורות בקבוקים!")
    # לשים כאן את הלוגיקה של המשחק
    print("סיום משחק צורות בקבוקים.")

# תפריט האפליקציה
def show_menu():
    while True:
        print("\nברוך הבא לאפליקציה!")
        print("1. אבטחת מידע של המשתמש")
        print("2. קליטת שם ושם משפחה")
        print("3. קליטת מקום מגורים ושיתוף מיקום")
        print("4. הכנסת מספר נייד")
        print("5. יציאת הנתונים לאקסל")
        print("6. תמונת מצב")
        print("7. עדכון נתונים וסטטיסטיקות")
        print("8. משחק צורות בקבוקים")
        print("9. יציאה")

        choice = input("בחר את הפעולה שברצונך לבצע: ")

        if choice == "1":
            # אבטחת מידע של המשתמש
            password = input("הזן סיסמה: ")
            encrypted_password = encrypt_data(password)
            user_data['password'] = encrypted_password
        elif choice == "2":
            # קליטת שם ושם משפחה
            first_name, last_name = get_full_name()
            user_data['first_name'] = first_name
            user_data['last_name'] = last_name
        elif choice == "3":
            # קליטת מקום מגורים ושיתוף מיקום
            location, share_location = get_location()
            user_data['location'] = location
            user_data['share_location'] = share_location
        elif choice == "4":
            # הכנסת מספר נייד
            phone_number = get_phone_number()
            if phone_number:
                user_data['phone_number'] = phone_number
        elif choice == "5":
            # יציאת הנתונים לאקסל
            export_to_excel(user_data)
        elif choice == "6":
            # תמונת מצב
            show_status_image()
        elif choice == "7":
            # עדכון נתונים וסטטיסטיקות
            update_data_statistics(user_data)
        elif choice == "8":
            # משחק צורות בקבוקים
            play_bottle_shapes_game()
        elif choice == "9":
            # יציאה מהתוכנה
            print("יציאה מהאפליקציה.")
            break
        else:
            print("בחירה לא תקינה. נסה שוב.")

# הוספת התפריט לתוכנית הראשית
show_menu()
