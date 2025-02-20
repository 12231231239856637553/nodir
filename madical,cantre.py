import json
from abc import ABC, abstractmethod

class PatientQueue:
    def __init__(self):
        self.queue = []
        self.ticket_number = 0

    def get_ticket(self):
        self.ticket_number += 1
        self.queue.append(self.ticket_number)
        return self.ticket_number

    def next_patient(self):
        if self.queue:
            return self.queue.pop(0)
        return None

class Doctor(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def diagnose(self, patient_name, complaint):
        pass

class Travmatolog(Doctor):
    def diagnose(self, patient_name, complaint):
        return f"{patient_name}, sizning shikoyatingiz: '{complaint}'. Sizda suyak sinishi bor. Gips qo'yildi.", "Og'riq qoldiruvchi dorilar"

class Psixolog(Doctor):
    def diagnose(self, patient_name, complaint):
        return f"{patient_name}, sizning shikoyatingiz: '{complaint}'. Siz depressiyaga moyilsiz. Ruhiy terapiya tavsiya qilinadi.", "Sedativ dorilar"

class Ginekolog(Doctor):
    def diagnose(self, patient_name, complaint):
        return f"{patient_name}, sizning shikoyatingiz: '{complaint}'. Homiladorlik tekshiruvi o'tkazildi.", "Vitamin va foliy kislotasi"

class OilaShifokori(Doctor):
    def diagnose(self, patient_name, complaint):
        return f"{patient_name}, sizning shikoyatingiz: '{complaint}'. Umumiy tibbiy ko‘rikdan o'tdingiz.", "Vitamin komplekslari"

class Stomatolog(Doctor):
    def diagnose(self, patient_name, complaint):
        return f"{patient_name}, sizning shikoyatingiz: '{complaint}'. Tish muolajasi talab etiladi.", "Og'riq qoldiruvchi va antibiotiklar"

class Hirurg(Doctor):
    def diagnose(self, patient_name, complaint):
        print(f"{patient_name}, siz operatsiya xonasiga olib ketildingiz...")
        print("Hamshira operatsiya asboblarini olib kelmoqda...")
        print("Operatsiya boshlandi...")
        print("Afsuski, biz bemorni saqlab qola olmadik.")
        return f"{patient_name}, operatsiya muvaffaqiyatsiz tugadi.", "---"

class MedicalCenter:
    def __init__(self):
        self.queue = PatientQueue()
        self.doctors = [
            Travmatolog("Dr. Rustamov"),
            Psixolog("Dr. G'ulomov"),
            Ginekolog("Dr. Ahmedova"),
            OilaShifokori("Dr. Karimov"),
            Travmatolog("Dr. Usmonov"),
            OilaShifokori("Dr. Shirinova"),
            Stomatolog("Dr. Hasanov"),
            Hirurg("Dr. Akbarov")
        ]
        self.patient_records = []
        self.load_data()

    def visit_doctor(self, patient_name, doctor_index):
        if 0 <= doctor_index < len(self.doctors):
            complaint = input(f"{patient_name}, qanday shikoyatingiz bor? ")
            diagnosis, medication = self.doctors[doctor_index].diagnose(patient_name, complaint)
            self.patient_records.append({"patient": patient_name, "diagnosis": diagnosis, "medication": medication})
            print(diagnosis)
            print(f"Tavsiya etilgan dori-darmonlar: {medication}")
        else:
            print("Xatolik: Notog'ri shifokor tanlandi!")

    def save_data(self):
        with open("patient_records.json", "w") as file:
            json.dump(self.patient_records, file)

    def load_data(self):
        try:
            with open("patient_records.json", "r") as file:
                self.patient_records = json.load(file)
        except FileNotFoundError:
            self.patient_records = []

if __name__ == "__main__":
    center = MedicalCenter()
    vehicle_choice = input("Siz mashinada keldingizmi? (ha/yo'q): ").strip().lower()
    if vehicle_choice == "ha":
        park_choice = input("Parkovkamiz bor, qo'yishni hohlaysizmi? (ha/yo'q): ").strip().lower()
        if park_choice == "ha":
            print("Mashinangiz parkovkaga qo'yildi.")
    
    print("Medical markazimizga xush kelibsiz!")
    
    while True:
        action = input("Tibbiyot markaziga kirish uchun 'kirish', chiqish uchun 'chiqish' deb yozing: ").strip().lower()
        
        if action == "kirish":
            patient_name = input("Ismingizni kiriting: ").strip()
            if not patient_name:
                print("Xatolik: Ism bo'sh bo'lishi mumkin emas!")
                continue

            print("Shifokorni tanlang:")
            for i, doctor in enumerate(center.doctors):
                print(f"{i} - {doctor.__class__.__name__} ({doctor.name})")

            try:
                doctor_index = int(input("Shifokor raqamini kiriting (0-7): "))
                center.visit_doctor(patient_name, doctor_index)
            except ValueError:
                print("Xatolik: Iltimos, 0 dan 7 gacha bo'lgan raqamni kiriting!")

        elif action == "chiqish":
            center.save_data()
            print("Ma'lumotlar saqlandi. Dasturdan chiqilmoqda.")
            break
        
        else:
            print("Noto'g'ri buyruq! 'kirish' yoki 'chiqish' deb yozing.")
