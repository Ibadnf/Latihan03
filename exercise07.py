class Car(object):

	def __init__(self, max_speed, mileage):
		self.max_speed = max_speed
		self.mileage = mileage


carX = Car(240, 18)
print(f"Kecepatan maksimal mobil adalah: {carX.max_speed}, dengan umur: {carX.mileage}")


class Motor:

	klasifikasi = "honda"

	def __init__(self, nama, pemilik, warna, nopol):
		self.nama = nama
		self.pemilik = pemilik
		self.warna = warna
		self.nopol = nopol

motor1 = Motor("Beat", "Ibad", "Hitam", "D 1123 VCD")
motor2 = Motor("CBR 250", "Luke", "merah", "B 3233 BGH")

print(f"Motor pertama berjenis {motor1.__class__.klasifikasi}")
print(f"Motor kedua juga berjenis {motor2.__class__.klasifikasi}")

print(f"Motor pertama namanya {motor1.nama}, pemiliknya {motor1.pemilik}, punya warna {motor1.warna}, dengan nomor polisi {motor1.nopol}")
print(f"Motor kedua namanya {motor2.nama}, pemiliknya {motor2.pemilik}, punya warna {motor2.warna}, dengan nomor polisi {motor2.nopol}")
		