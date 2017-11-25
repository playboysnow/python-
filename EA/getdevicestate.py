# -*- coding: utf-8 -*-
import hashlib,requests,json
import time,unittest
from common import config

class getdevicestate(unittest.TestCase):
	def setUp(self):
		self.url='%s%s' % (config().API_url,config().API_endpoint[0])
		self.data={
			'game_id':'80',
			'device_id':'85966964ba32e5108d1044b6bdfd26596cecb658',
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
		self.data['encrypt']=config().md5(str(self.data['game_id']),str(self.data['t']),str(self.data['device_id']),str(self.key),str(self.data['t2']))
		res=requests.post(self.url,data=self.data,verify=False)
		print (res.text)
		#print (self.data)
		code = json.loads(res.text)['code']
		self.assertEqual(str(code), '0')
	def test_gameid_empty_error(self):
		g_id=['','0']
		for i in range(0,len(g_id)):
			self.data['game_id']=g_id[i]
			self.data['encrypt']=config().md5(str(self.data['game_id']),str(self.data['t']),str(self.data['device_id']),str(self.key),str(self.data['t2']))
			res=requests.post(self.url,data=self.data,verify=False)
			print (res.text)
			print (self.data)
			code = json.loads(res.text)['code']
			self.assertEqual(str(code), '10000')# 校验问题 报出数据库信息 code10000 应该100
	def test_deviceid_empty_error(self):
		de_id=['','0haisdjoiai']
		for i in range(0,len(de_id)):
			self.data['device_id']=de_id[i]
			self.data['encrypt']=config().md5(str(self.data['game_id']),str(self.data['t']),str(self.data['device_id']),str(self.key),str(self.data['t2']))
			res=requests.post(self.url,data=self.data,verify=False)
			print (res.text)
			print (self.data)
			code = json.loads(res.text)['code']
			self.assertEqual(str(code), '0')#未校验 device_id
	
if __name__=='__main__':
	case = unittest.TestLoader().loadTestsFromTestCase(getdevicestate)
	unittest.TextTestRunner(verbosity=2).run(case)