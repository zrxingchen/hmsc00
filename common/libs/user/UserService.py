import hashlib,base64


class UserService():
    # 生成密码（结合pwd 和salt）
    @staticmethod
    def generatePwd(pwd,salt):
        m = hashlib.md5()
        str = '%S-%s'%(base64.encodebytes(pwd.encode('utf-8')),salt)
        m.update(str.encode('utf-8'))


        return m.hexdigest()
