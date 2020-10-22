class Siswa(object):
	"""docstring for Siswa"""
	def __init__(self, nama, nim):
		self.nama = nama
		self.nim = nim

	def get_nama(self):
		return self.nama

	def get_nim(self):
		return self.nim

class Atribut(Siswa):
	"""docstring for Atribut"""
	def __init__(self, alamat, umur):
		self.alamat = alamat
		self.umur = umur

	def alamat(self):
		return self.alamat

	def umur(self):
		return self.umur

orang = Atribut("Bandung", "20")
print(orang.alamat)

orang.nama = "Ibad"
print(orang.get_nama())		
		