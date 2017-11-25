# -*- coding: utf-8 -*-
import hashlib, requests, json
import time, unittest
from common import config


class bind(unittest.TestCase):
    def setUp(self):
        self.url = '%s%s' % (config().API_url, config().API_endpoint[4])
        self.data = {
            'game_id': '8881',
            'device_id': '85966964ba32e5108d1044b6bdfd26596cecb658',
            'levela_id': '2100174',
            'levela_type': 'ge',
            'levelb_id':'94100065913',
            'levelb_type':'au',
            'levelb_name':'nicai',
            'levelb_email': '123@321.com',
            'levelb_birthday':'23413241',
            'levelb_avator':'',
            'ostype':'ios',
            'encrypt': '',
            'sdk_version': '4.2.0',
        }
        self.key_time = config().get_key_time(config().get_config_url)
        # self.data['t']=int(time.time()*1000)
        self.data['t2'] = int(time.time() * 1000) - self.key_time['c_time']
        self.key = self.key_time['key']

    # self.data['encrypt']=config().md5(str(self.data['game_id']),str(self.data['t']),str(self.key),str(self.data['t2']))
    def tearDown(self):
        self.data = {}

    def test_normal(self):
        self.data['encrypt'] = config().md5(str(self.data['game_id']), str(self.data['levela_id']),
                                            str(self.data['levela_type']), str(self.data['levelb_id']),
                                            str(self.data['levelb_type']),str(self.key), str(self.data['t2']))
        res = requests.post(self.url, data=self.data, verify=False)
        print(res.text)
        print(self.data)
        code = json.loads(res.text)['code']
        self.assertEqual(str(code), '0')
    '''正常绑定
    {"code":0,"errorInfo":"","message":"操作成功","playerIds":[{"player_id":"8100181","avatar":null,"username":"13112345678"},{"player_id":"5100194","avatar":null,"username":"游戏生涯"}],"user_id":"94100065913","name":"游戏生涯","avatar":null,"type":"au"}
    {'game_id': '8881', 'device_id': '85966964ba32e5108d1044b6bdfd26596cecb658', 'levela_id': '5100194', 'levela_type': 'ge', 'levelb_id': '94100065913', 'levelb_type': 'au', 'levelb_name': 'nicai', 'levelb_email': '123@321.com', 'levelb_birthday': '23413241', 'levelb_avator': '', 'ostype': 'android', 'encrypt': '7ebedfca16eeb00337478c7e32c19b21', 'sdk_version': '4.2.0', 't2': 1505704710708}
    '''
    '''重复绑定
    {"responseType":"typeHaveBinded","code":10000,"errorInfo":"typeHaveBinded","message":"你已经绑定过此类型账号了"}
    {'game_id': '8881', 'device_id': '85966964ba32e5108d1044b6bdfd26596cecb658', 'levela_id': '2100174', 'levela_type': 'ge', 'levelb_id': '94100065913', 'levelb_type': 'au', 'levelb_name': 'nicai', 'levelb_email': '123@321.com', 'levelb_birthday': '23413241', 'levelb_avator': '', 'ostype': 'android', 'encrypt': '1a424f3a9272233ed8c82dc7610db67b', 'sdk_version': '4.2.0', 't2': 1505712435432}
    '''
    def test_normal_fb_gl(self):
        parm=[{
                'id':'1502361513',
                'type':'gamecenter',
            },{
                'id':'1502365533',
                'type':'fb',
            },{
                'id':'1502365513',
                'type':'google',
            }
            ]
        for i in range(0,len(parm)):
            self.data['levela_id']=parm[i]['id']
            self.data['levela_type']=parm[i]['type']
            self.data['encrypt'] = config().md5(str(self.data['game_id']), str(self.data['levela_id']),
                                            str(self.data['levela_type']), str(self.data['levelb_id']),
                                            str(self.data['levelb_type']),str(self.key), str(self.data['t2']))
            res = requests.post(self.url, data=self.data, verify=False)
            print(res.text)
            print(self.data)
            code = json.loads(res.text)['code']
            self.assertEqual(str(code), '0')
        '''绑定三方成功
        {"code":0,"errorInfo":"success_bind_gamecenter_au","message":"au绑定gamecenter成功","playerIds":[{"player_id":"8100181","avatar":null,"username":"13112345678"},{"player_id":"5100194","avatar":null,"username":"游戏生涯"},{"player_id":"4100223","avatar":"http://www.baidu.com","username":"test"},{"player_id":"1100258","avatar":"http://www.baidu.com","username":"test"},{"player_id":"3100283","avatar":"http://www.baidu.com","username":"test"}],"user_id":"94100065913","type":"au","name":"13112345678","avatar":null}
        {'game_id': '8881', 'device_id': '85966964ba32e5108d1044b6bdfd26596cecb658', 'levela_id': '1502361513', 'levela_type': 'gamecenter', 'levelb_id': '94100065913', 'levelb_type': 'au', 'levelb_name': 'nicai', 'levelb_email': '123@321.com', 'levelb_birthday': '23413241', 'levelb_avator': '', 'ostype': 'ios', 'encrypt': '3eace7ea09924b8143f3dc60eb7fe691', 'sdk_version': '4.2.0', 't2': 1505718769650}
        {"code":0,"errorInfo":"success_bind_fb_au","message":"au绑定fb成功","playerIds":[{"player_id":"8100181","avatar":null,"username":"13112345678"},{"player_id":"5100194","avatar":null,"username":"游戏生涯"},{"player_id":"3100283","avatar":"http://www.baidu.com","username":"test"}],"user_id":"94100065913","type":"au","name":"13112345678","avatar":null}
        {'game_id': '8881', 'device_id': '85966964ba32e5108d1044b6bdfd26596cecb658', 'levela_id': '1502365533', 'levela_type': 'fb', 'levelb_id': '94100065913', 'levelb_type': 'au', 'levelb_name': 'nicai', 'levelb_email': '123@321.com', 'levelb_birthday': '23413241', 'levelb_avator': '', 'ostype': 'android', 'encrypt': 'c782364eab9a0baef4f7bce5e9d59242', 'sdk_version': '4.2.0', 't2': 1505718227982}
        {"code":0,"errorInfo":"success_bind_google_au","message":"au绑定google成功","playerIds":[{"player_id":"8100181","avatar":null,"username":"13112345678"},{"player_id":"5100194","avatar":null,"username":"游戏生涯"},{"player_id":"1100258","avatar":"http://www.baidu.com","username":"test"},{"player_id":"3100283","avatar":"http://www.baidu.com","username":"test"}],"user_id":"94100065913","type":"au","name":"13112345678","avatar":null}
        {'game_id': '8881', 'device_id': '85966964ba32e5108d1044b6bdfd26596cecb658', 'levela_id': '1502365513', 'levela_type': 'google', 'levelb_id': '94100065913', 'levelb_type': 'au', 'levelb_name': 'nicai', 'levelb_email': '123@321.com', 'levelb_birthday': '23413241', 'levelb_avator': '', 'ostype': 'android', 'encrypt': '5f4139c8520d5671a72a3732de898ccc', 'sdk_version': '4.2.0', 't2': 1505718227982}
        '''
if __name__ == '__main__':
    case = unittest.TestLoader().loadTestsFromTestCase(bind)
    unittest.TextTestRunner(verbosity=2).run(case)