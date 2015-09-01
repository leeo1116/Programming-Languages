__author__ = 'Liang Li'
import datetime
import ntplib                   # https://pypi.python.org/pypi/ntplib/
from time import ctime
from Crypto.Cipher import AES  # https://pypi.python.org/pypi/pycrypto

new_password = input("Input your relieved password: ")
key1 = input("Input AES key1(16*N bytes): ")
attempt_num = 16

while attempt_num > 0 and len(key1) % 16 !=0:
    attempt_num -= 1
    print("Key1 length should be 16*N: ")
    key1 = input("Input AES key1(16*N bytes): ")

key2 = input("Input AES key2(16*N bytes): ")
while attempt_num > 0 and len(key2) % 16 !=0:
    attempt_num -= 1
    print("Key2 length should be 16*N: ")
    key2 = input("Input AES key2(16*N bytes): ")

encrypt_obj = AES.new(key1, AES.MODE_CBC, key2)
cipher_text = encrypt_obj.encrypt(new_password)
decrypt_obj = AES.new(key1, AES.MODE_CBC, key2)
plain_text = decrypt_obj.decrypt(cipher_text)
print(cipher_text)
print(plain_text)



"""
obj = AES.new("This is a key123", AES.MODE_CBC, "This is an IV456")
message = "The answer is no"
cipher_text = obj.encrypt(message)
print(cipher_text)

obj2 = AES.new("This is a key123", AES.MODE_CBC, "This is an IV456")
orginal_message = obj2.decrypt(cipher_text)
print(orginal_message)
"""
