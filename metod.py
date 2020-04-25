class huhaha:
    def mulai(self,user):
        print(f"Selamat Datang {user}")
    def selesai(self, waktu):
        print("Loading")
        while waktu > 0:
                print(waktu)
                waktu -= 1
    def ulang1 (self,pin1):
        vpin= pin1 + "1"
        knt=0
        while vpin != pin1:
            if knt > 0:
               print("Password salah")
            knt=1
            print("Masukkan password")
            vpin = input()
        print("Login berhasil")
    def ulang2 (self,pin2):
        vpin=pin2 + "1"
        knt=0
        while vpin != pin2:
            if knt > 0:
               print("Password salah")
            knt=1
            print("Masukkan password")
            vpin = input()
        print("Login berhasil")
    def buatpassword (self):
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


