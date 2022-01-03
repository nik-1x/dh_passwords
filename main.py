from DHLib import DHP_Password_Gen, DHP_Password_Verify, DH_Encrypt
from random import randint

password = DHP_Password_Gen("password").response()
print(password)  # { password, int, hex }

enc = DH_Encrypt()
one_byte: int = 2 ** (256 * 8)
# one_byte * randint(100000000000, 999999999999)

"""
Can use dependence, on backend generating public and private values script, use something like browser id or ip.
"""

# private, own side, generate on connection
dh_Client_private = password['int']
dh_Server_private = 53152

# public, exchange, server send to client on connections
dh_CS_public1 = 22552
dh_CS_public2 = 51252

# public, exchange, client send public to server and get server public in response
dh_Client_public = enc.do(dh_CS_public1, dh_Client_private, dh_CS_public2)
dh_Server_public = enc.do(dh_CS_public1, dh_Server_private, dh_CS_public2)

# private, own side, use as token to access to web and encrypt data in http (ssl off)
dh_Client_K = enc.do(dh_Server_public, dh_Client_private, dh_CS_public2)
dh_Server_K = enc.do(dh_Client_public, dh_Server_private, dh_CS_public2)

print(dh_Client_K)
print(dh_Server_K)
