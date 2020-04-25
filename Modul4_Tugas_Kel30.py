import metod
print("Buat passsword User 1")
pw1 = input()
print("Buat password User 2")
pw2 = input()
print("Login")
user1 = "User1"
user2 = "User2"
print("(1)", user1)
print("(2)", user2)
print("Input 1 atau 2")
user = int(input())
if user == 1:
    print("Masukkan password ", user1)
    pw = input()
    while pw != pw1:
            print("Password salah")
            print("Masukkan password")
            pw = input()
    print("Login berhasil")
    
else:
    print("Masukkan password ", user2)
    pw = input()
    while pw != pw2:
            print("Password salah")
            print("Masukkan password")
            pw = input()
            print("Login berhasil")
p = metod.huhaha("user")
p.mulai()
p.selesai(10)
