class huhaha:
    def __init__(self, user):
        self.user = user
    def mulai(self):
        print(f"Selamat Datang {self. user}")
        options = {
	        1 : 'Senin', #ganti nickname user
	        2 : 'Selasa', #ganti password (koko)
	    }
        x = float(input('Seting data pengguna'))
        print('Hari : %s' % options.setdefault(x, 'Inputan hanya 1 - 7'))

    def selesai(self, waktu):
        print("Loading")
        while waktu > 0:
                print(waktu)
                waktu -= 1
        

