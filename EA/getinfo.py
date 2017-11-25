# -*- coding: utf-8 -*-
import hashlib,requests,json
import time,unittest
from common import config

class get_info(unittest.TestCase):
	def setUp(self):
		self.url='%s%s' % (config().API_url,config().API_endpoint[3])
		self.data={
			'login_id':'94100065913',
			'player_id':'6125826',
			'game_id':'80',
			'login_type':'au',
			
			'encrypt':'',
			'sdk_version':'4.2.0',
		}
		self.key_time=config().get_key_time(config().get_config_url)
		#self.data['t']=int(time.time()*1000)
		self.data['t2']=int(time.time()*1000)-self.key_time['c_time']
		self.key=self.key_time['key']
		#self.data['encrypt']=config().md5(str(self.data['game_id']),str(self.data['t']),str(self.key),str(self.data['t2']))
	def tearDown(self):
		self.data={}
	
	def test_normal(self):
		self.data['encrypt']=config().md5(str(self.data['login_id']),str(self.key),str(self.data['t2']))
		res=requests.post(self.url,data=self.data,verify=False)
		print (res.text)
		print (self.data)
		code = json.loads(res.text)['code']
		self.assertEqual(str(code), '0')
	def test_loginid(self):
		login_id=['12345',]
		for i in range(0,len(login_id)):
			self.data['login_id']=login_id[i]
			self.data['encrypt']=config().md5(str(self.data['login_id']),str(self.key),str(self.data['t2']))
			res=requests.post(self.url,data=self.data,verify=False)
			print (res.text)
			print (self.data)
			code = json.loads(res.text)['code']
			self.assertEqual(str(code), '0')    #  
	def test_logintype(self):
		login_type=['','google','gamecenter']
		for i in range(0,len(login_type)):
			self.data['login_type']=login_type[i]
			self.data['encrypt']=config().md5(str(self.data['login_id']),str(self.key),str(self.data['t2']))
			res=requests.post(self.url,data=self.data,verify=False)
			print (res.text)
			print (self.data)
			code = json.loads(res.text)['code']
			self.assertEqual(str(code), '10000')  #类型不存在id  会报错 用户不存在
			
if __name__=='__main__':
	case = unittest.TestLoader().loadTestsFromTestCase(get_info)
	unittest.TextTestRunner(verbosity=2).run(case)	