#coding:utf-8

import sqlite3
import urllib3

import sys
if 'threading' in sys.modules:
    del sys.modules['threading']
import gevent
import gevent.socket
import gevent.monkey
gevent.monkey.patch_all()
#from gevent import monkey
#monkey.patch_all()
import leancloud
leancloud.init('6u08iptfcuy9e3v7dsjyqx8ox0ey65snytd5y6ozysjq4f8h', 'vxraujc4mwur67lyl2yaudkols28q52q82t3zjjp14ruks4k')

from leancloud import Object
urllib3.disable_warnings()

class PinYin(Object):
	"""docstring for PinYin"""
	def __init__(self, arg):
		super(PinYin, self).__init__()
		self.arg = arg

	@property
	def py(self):
	    return self.get('py')

	@property
	def zm(self):
	    return self.get('zm')

	@property
	def hz(self):
	    return self.get('hz')

	@py.setter
	def py(self, value):
		return self.set('py', value)

	@zm.setter
	def zm(self, value):
		return self.set('zm', value)

	@hz.setter
	def hz(self, value):
		return self.set('hz', value)

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

cx = sqlite3.connect('/Users/Jerry/code/Xhzd/xhzd.db')
#cx.text_factory = str
cu = cx.cursor()
cu.execute("select id, zi, wubi, bushou, bihua, pinyin, jiben, xiangxi, py, ucode from detail where id > 11100")  #id > 9 and id <= 50




for i in cu.fetchall():
	 #detail = Detail()
     #detail.set('id', i[0])
     print i[1]
     detail = Detail()
     if i[1]:
     	detail.set('zi', i[1])  #i[1].encode('utf-8')
     if i[2]:
     	detail.set('wubi', i[2])
     if i[3]:
     	detail.set('bushou', i[3])	#.encode('utf-8')
     if i[4]:
     	detail.set('bihua', i[4])
     if i[5]:
     	detail.set('pinyin', i[5])
     if i[6]:
     	detail.set('jiben', i[6])	#.encode('utf-8')
     if i[7]:
     	detail.set('xiangxi', i[7])	#.encode('utf-8')
     if i[8]:
     	detail.set('py', i[8])
     if i[9]:
     	detail.set('ucode', i[9])

     detail.save()

