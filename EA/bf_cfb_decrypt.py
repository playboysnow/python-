import blowfish
import base64
s='3LzKx54dh8Q='    # https://apptest.playcomb.com/v4/getConfig?game_id=780&ostype=androidgoogle  获取    base64编码   需先解码
key='huJRE213'
iv='IUaa1WE3'
data=base64.b64decode(s)
cipher=blowfish.Cipher(b'huJRE213')
data_decrypted=b"".join(cipher.decrypt_cfb(data,b'IUaa1we3'))
print (data_decrypted)