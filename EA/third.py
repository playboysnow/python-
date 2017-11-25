# -*- coding: utf-8 -*-
import hashlib,requests,json
import time,unittest
from common import config

class third(unittest.TestCase):
	def setUp(self):
		self.url='%s%s' % (config().API_url,config().API_endpoint[1])
		self.data={
			'game_id':'8881',
			'device_id':'85966964ba32e5108d1044b6bdfd26596cecb658',
			'third_id':'1502365533',
			'third_type':'fb',
			'birthday':int(time.time()*1000),
			'sex':'male',
			'email':'123@123.com',
			'avatar':'http://www.baidu.com',
			'username':'test',
			
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
		self.data['encrypt']=config().md5(str(self.data['third_id']),str(self.key),str(self.data['t2']))
		res=requests.post(self.url,data=self.data,verify=False)
		print (res.text)
		#print (self.data)
		code = json.loads(res.text)['code']
		self.assertEqual(str(code), '0')
	def test_third_id_empty_error(self):
		third_id=['',]
		for i in range(0,len(third_id)):
			self.data['third_id']=third_id[i]
			self.data['encrypt']=config().md5(str(self.data['third_id']),str(self.key),str(self.data['t2']))
			res=requests.post(self.url,data=self.data,verify=False)
			print (res.text)
			print (self.data)
			code = json.loads(res.text)['code']
			self.assertEqual(str(code), '10000')# third_id校验是否为空  非空不校验
	def test_third_type(self):
		third_type=['au','google','gamecenter']
		for i in range(0,len(third_type)):
			self.data['third_type']=third_type[i]
			self.data['encrypt']=config().md5(str(self.data['third_id']),str(self.key),str(self.data['t2']))
			res=requests.post(self.url,data=self.data,verify=False)
			print (res.text)
			print (self.data)
			code = json.loads(res.text)['code']
			self.assertEqual(str(code), '0')	#未校验 third_type      third_id及third_type都是第三方返回的   因此只校验是否为空   此两处没问题
			
if __name__=='__main__':
	case = unittest.TestLoader().loadTestsFromTestCase(third)
	unittest.TextTestRunner(verbosity=2).run(case)