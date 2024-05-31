class Student:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def print_data(self):
        return f"nama :{self.nama}\n nim :{self.nim}\n nilai :{self.nilai}"


saya = Student("Hakim", "064002300027", 100)
teman1 = Student("Malik", "09287654821", 90)
teman2 = Student("Cemen", "13147924190", 88)
teman3 = Student("Acong", "237282723985", 78)

print("---Data Pribadi---")
print(saya.print_data())
print("=> Data Teman ke 1")
print(teman1.print_data())
print("=> Data Teman ke 2")
print(teman2.print_data())
print("=> Data Teman ke 3")
print(teman3.print_data())