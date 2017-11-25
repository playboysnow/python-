# -*- coding: utf-8 -*-
import hashlib,requests,json
import blowfish
import base64,time

class config():
	get_config_url='https://apptest.***.com/v4/getConfig?game_id=780&ostype=androidgoogle'
	API_url='https://apptest.***.com/'
	API_endpoint=['v4/device/getDeviceState','v4/users/login/third','v4/users/login/phone','v4/users/get_info',
				'v4/users/bind','v4/users/login/guest','v4/users/player_login','v4/gethelpconfig']
	sdk_ver='4.2'
	
	def md5(self,*args):
		data=""
		for arg in args:
			data=data+arg
		#print (data)
		hash_md5=hashlib.md5(data.encode('utf-8'))
		return hash_md5.hexdigest()  #MD5
	def get_key_time(self,url):
		response=requests.get(self.get_config_url,verify=False)
		encrypted_key=json.loads(response.text)['key']
		#print (encrypted_key)
		key=self.decrypt(encrypted_key)
		times=json.loads(response.text)['times']
		c_time=int(time.time()*1000)-times
		key_time={'key':key,
			'c_time':c_time,	
				}
		return key_time   #返回解码后的key和本地与服务器时间差
	def decrypt(self,key):
		data=base64.b64decode(key)
		cipher=blowfish.Cipher(b"huJRE213")
		data_decrypted=b"".join(cipher.decrypt_cfb(data,b"IUaa1WE3"))
		data_decrypted=str(data_decrypted,encoding="utf-8").strip('\'')
		#print (data_decrypted)
		return (data_decrypted) #解码
	
	
		