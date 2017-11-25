# -*- coding: utf-8 -*-
import hashlib,requests,json
import time,unittest
from common import config

class gethelpconfig(unittest.TestCase):
	def setUp(self):
		self.url='%s%s' % (config().API_url,config().API_endpoint[7])
		self.data={
			'game_id':'80',
			't':'',
			'encrypt':'',
			'sdk_version':'4.2.0',
		}
		self.key_time=config().get_key_time(config().get_config_url)
		self.data['t']=int(time.time()*1000)
		self.data['t2']=int(time.time()*1000)-self.key_time['c_time']
		self.key=self.key_time['key']
		#self.data['encrypt']=config().md5(str(self.data['game_id']),str(self.data['t']),str(self.key),str(self.data['t2']))
	def tearDown(self):
		self.data={}
	
	def test_normal(self):
		self.data['encrypt']=config().md5(str(self.data['game_id']),str(self.data['t']),str(self.key),str(self.data['t2']))
		res=requests.post(self.url,data=self.data,verify=False)
		print (res.text)
		#print (self.data)
		code = json.loads(res.text)['code']
		self.assertEqual(str(code), '0')
	def test_gameid_error(self):
		self.data['game_id']='100000'
		self.data['encrypt']=config().md5(str(self.data['game_id']),str(self.data['t']),str(self.key),str(self.data['t2']))
		res=requests.post(self.url,data=self.data,verify=False)
		print (res.text)
		print (self.data)
		code = json.loads(res.text)['code']
		self.assertEqual(str(code),'0')   #未校验gameID
	def test_gameid_empty(self):
		self.data['game_id']=''
		self.data['encrypt']=config().md5(str(self.data['game_id']),str(self.data['t']),str(self.key),str(self.data['t2']))
		res=requests.post(self.url,data=self.data,verify=False)
		print (res.text)
		print (self.data)
		code = json.loads(res.text)['code']
		self.assertEqual(str(code),'3000')   #未校验gameID
	def test_t2_empty(self):
		self.data['t2']=''
		self.data['encrypt']=config().md5(str(self.data['game_id']),str(self.data['t']),str(self.key),str(self.data['t2']))
		res=requests.post(self.url,data=self.data,verify=False)
		print (res.text)
		print (self.data)
		code = json.loads(res.text)['code']
		self.assertEqual(str(code),'0')   #t2未校验
	def test_empty_encrypt(self):
		self.data['encrypt']=''
		res=requests.post(self.url,data=self.data,verify=False)
		print (res.text)
		print (self.data)
		code = json.loads(res.text)['code']
		self.assertEqual(str(code),'30002') #签名校验
	
if __name__=='__main__':
	case = unittest.TestLoader().loadTestsFromTestCase(gethelpconfig)
	unittest.TextTestRunner(verbosity=2).run(case)
