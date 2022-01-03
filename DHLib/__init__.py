class DH_Encrypt:
    """ Diffie Hellman library """

    def __init__(self):
        print("Init:", self.__doc__)

    def do(self, g: int, a: int, p: int) -> int:
        c = 0
        f = 1
        a = bin(a)
        a = a[2:len(a)]
        g = g % p
        for i in range(0, len(a)):
            c *= 2
            f = (f * f) % p
            if a[i] == '1':
                c += 1
                f = (f * g) % p
        return f


class DHP_Password_Gen:
    password = ""
    int_password = 0

    def __init__(self, password):
        self.password = password
        self.int_password = self.intify_password(self.password)

    def intify_password(self, passw):
        pass_summ = 0
        for x in range(len(passw)):
            pass_summ += (int(ord(passw[x])) * (2 ** (256 * 8)))
        return pass_summ

    def response(self):
        return {"password": self.password, "int": self.int_password, "hex": hex(self.int_password)}


class DHP_Password_Verify:
    password = ""
    response = {}

    def __init__(self, response: dict):
        self.password = response["password"]
        self.response = response

    def intify_password(self, passw):
        pass_summ = 0
        for x in range(len(passw)):
            pass_summ += (int(ord(passw[x])) * (2 ** (256 * 8)))
        return pass_summ

    def check(self):
        valid = True

        if self.response["int"] != self.intify_password(self.password):
            valid = False
        if hex(self.response['int']) != self.response['hex']:
            valid = False

        return valid
