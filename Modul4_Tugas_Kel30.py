import metod
p = metod.huhaha()
print("Buat User 1")
user1 = input()
print("Buat Password 1")
pin1=p.buatpassword()
print("Buat User 2")
user2 = input()
print("Buat Password 2")
pin2=p.buatpassword()

print("Login")
print("1", user1)
print("2", user2)
print("Input Username")
user = input()
if user == user1:
    p.ulang1(pin1)
    
else:
    p.ulang2(pin2)

p.mulai(user)
p.selesai(10)
