lst = [1,2,3,4,5,6,7,8,9,10]

for i in lst:
	print(i)

son	= 10

if son > 10:
	print("deeeng")


def Salom(ism):
	print("Salom", ism)


Salom(input())


def ddd():
	d = 4
	if d % 2 == 0:
		print("EVEN Number")
ddd()

class Dict:
	def yangi_soz(self):
		pass
	def sozlarni_korish(self):
		pass
	def izlash(self):
		pass
	def chiqish(self):
		pass


	def menu(self):
		print("""
		Lug'at
		Yangi so'z yozish uchun 1 ni bosing
		So'zlarni ko'rish uchun 2 ni bosing
		So'zni izlash uchun 3 ni bosing
		Chiqish uchun 4 ni bosing
		""")
		intooot = input()
		while intooot not in ["1", "2", "3", "4"]:
			intooot = input()

		if intooot == '1':
			self.yangi_soz()

		elif intooot == '2':
			self.sozlarni_korish()

		elif intooot == '3':
			self.izlash()

		else:
			self.chiqish()

