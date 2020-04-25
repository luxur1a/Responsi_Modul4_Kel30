import metod
def buatpassword ():
        opin=0
        opin2=1
        knt=0
        while opin != opin2:
            if knt > 0:
               print("Password dan Password Konfirmasi Berbeda")
            knt=1
            print("Masukkan password : ")
            opin = input()
            print("Masukkan password konfirmasi : ")
            opin2 = input()
        return(opin)
        print("Login berhasil")

print("Buat User 1")
user1 = input()
print("Buat Password 1")
pin1=buatpassword()
print("Buat User 2")
user2 = input()
print("Buat Password 2")
pin2=buatpassword()

print("Login")
print(user1)
print(user2)
print("Input Username")
user = input()
p = metod.huhaha(user, pin1, pin2)
if user == user1:
    p.ulang1()
    
else:
    p.ulang2()

p.mulai()
p.selesai(10)
