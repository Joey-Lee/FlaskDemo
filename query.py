import leancloud
from leancloud import Object
leancloud.init('6u08iptfcuy9e3v7dsjyqx8ox0ey65snytd5y6ozysjq4f8h', master_key='vxraujc4mwur67lyl2yaudkols28q52q82t3zjjp14ruks4k')

class Detail(Object):
	"""docstring for """
	"""
	@property
	def id(self):
	    return self.get('id')
	"""

	@property
	def zi(self):
	    return self.get('zi')

	@property
	def wubi(self):
	    return self.get('wubi')

	@property
	def bushou(self):
	    return self.get('bushou')

	@property
	def bihua(self):
	    return self.get('bihua')

	@property
	def pinyin(self):
	    return self.get('pinyin')

	@property
	def jiben(self):
	    return self.get('jiben')

	@property
	def xiangxi(self):
	    return self.get('xiangxi')

	@property
	def py(self):
	    return self.get('py')

	@property
	def ucode(self):
	    return self.get('ucode')
	
	
	"""
	@id.setter
	def id(self, value):
		return self.set('id', value)
	"""

	@zi.setter
	def zi(self, value):
		return self.set('zi', value)

	@wubi.setter
	def wubi(self, value):
		return self.set('wubi', value)

	@bushou.setter
	def bushou(self, value):
		return self.set('bushou', value)

	@bihua.setter
	def bihua(self, value):
		return self.set('bihua', value)

	@pinyin.setter
	def pinyin(self, value):
		return self.set('pinyin', value)

	@jiben.setter
	def jiben(self, value):
		return self.set('jiben', value)

	@xiangxi.setter
	def xiangxi(self, value):
		return self.set('xiangxi', value)

	@py.setter
	def py(self, value):
		return self.set('py', value)

	@ucode.setter
	def ucode(self, value):
		return self.set('ucode', value)

from leancloud import Query
query = Query(Detail)
detail = query.get('55cf129100b042cb01b8a4cc')
print detail.get('xiangxi')