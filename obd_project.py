import csv
import re 
import sys
sys.stdout.reconfigure(encoding='utf-8') 


def load_codes(filename):
    codes = {}
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            code, description = row
            codes[code] = description
    return codes


def find_repair(code, codes):
    if code in codes:
        return codes[code]
    else:
        return "This code is not in the database"


def is_valid_code(code):
    pattern = r"^[PBCU]\d{4}$"
    return bool(re.match(pattern, code))

def get_category(code):
    categories = {
        "P": "🔧 Powertrain (Motor a převodovka)",
        "B": "🚗 Body (Karoserie a komfortní systémy)",
        "C": "🛞 Chassis (Podvozek, ABS, stabilizace)",
        "U": "⚡Network (Komunikační chyby mezi moduly)"
    }
    return categories.get(code[0], "Unknown category")

def main():
    print(" 🛠️  Welcome in diagnostic OBD-II! 🛠️ ")
    codes = load_codes("obd_trouble_code.csv")

    while True:
        print("\n📌 Choose an option: ")
        print("1️⃣ Enter a trouble code")
        print("2️⃣ Show codes by category")
        print("3️⃣ Exit ")
        choice = input("➡️ Enter your choice: ")

        if choice == "1":
            code = input("🔍 Enter code: ").upper()
            if not is_valid_code(code):
                print("❌ Invalid OBD-II code! Please enter a valid format (e.g., P0300, C1234).")
                continue
            category = get_category(code)
            repair = find_repair(code, codes)
            print(f"📂 Category: {category}")
            print(f"⚙️ Problem with: {repair}")

        elif choice == "2":
            print("\n🗂️ Available categories:")
            print("🔧 P - Powertrain (Motor and Transmission)")
            print("🚗 B - Body (Body and Comfort Systems)")
            print("🛞 C - Chassis (Brakes, Suspension, Stability)")
            print("⚡U - Network (Communication between modules)")
            category_choice = input("Enter category (P, B, C, U): ").upper()

            if category_choice in "PBCU":
                print(f"\n🔽 Listing codes in category {category_choice}:")
                for code, desc in codes.items():
                    if code.startswith(category_choice):
                        print(f"🔹{code}: {desc}")
            else:
                print("❌ Invalid category!")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please select a valid option")


if __name__ == "__main__":
    main()
