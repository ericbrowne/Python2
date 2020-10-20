#Eric Browne Student ID: 873517924
#Python 2 Software Development
#Project 6: Auto mpg data



class AutoMPG:
	"""This will represent the make model and year from the data."""

	def __init__(self,make,model,year,mpg):
		self.make = make
		self.model = model
		self.year = year
		self.mpg = mpg


	def __repr__(self):
		"""built-in function used to compute the 'official' string reputation of an object"""
		return "AutoMPG("+repr(self.make) + ","+repr(self.model) + ","+ repr(self.year) +	 "," + repr(self.mpg)+")"

	def __str__(self):
		return repr(self)

	def __eq__(self,other):
		return (type(self)==type(other)
			and self.make == other.make
			and self.model == other.model
			and self.year == other.year
			and self.mpg == other.mpg)


	def __lt__(self,other):
		if (type(self) != type(other)):
			raise ValueError("Must compare AutoMPG to AutoMPG")

		if (self.make != other.make):
			return self.make < other.make
		if (self.model != other.model):
			return self.model < other.model
		if (self.year != other.year):
			return self.year < other.year
		if (self.mpg != other.mpg):
			return self.mpg < other.mpg

		return False

	def __hash__(self):
		return hash(self.make) ^ (hash(self.model) <<5) ^ (hash(self.year) >>7) ^(hash(self.mpg)<<3)

class AutoMPGData:
	""" description of the class"""



	def __iter__(self):
		return iter(self.data)
	def __init__(self):
		self.data = []

	def _load_data(self):
		file = open("auto-mpg.clean.txt","r")

		for line in file:
			if len(line) == 0:
				break
			x = line.split()

			try:
				year = int(float(x[6]))
				mpg = float(x[0])
				name = " ".join(x[8:]).replace("\"","")

				nameSplit = name.split()
				make = nameSplit[0]
				model = " ".join(nameSplit[1:])

				record = AutoMPG(make,model,year,mpg)
				self.data.append(record)
			except:
				pass

	def _clean_data(self):
		file = open("auto-mpg.data.txt","r")
		outfile = open("auto-mpg.clean.txt","w+")

		for line in file:
			line = line.expandtabs(4)
			outfile.write(line)

def main():
	dataset = AutoMPGData()
	dataset._clean_data()
	dataset._load_data()

	for x in dataset:
		print(x)

if __name__ == '__main__':
    main()
