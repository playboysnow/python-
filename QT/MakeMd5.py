import hashlib

class Md5():
    def md5(self,*args):
        data=""
        for arg in args:
            data=data+arg

        hash_md5=hashlib.md5(data)
        return hash_md5.hexdigest()
    def Mkmd5(self,data):
        pass
