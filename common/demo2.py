from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import base64

# 私钥
private_key = '''-----BEGIN RSA PRIVATE KEY-----
5353dfggd
-----END RSA PRIVATE KEY-----
'''

# 公钥
public_key = b"""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDK81LDulITfvkZ5yqUhKzT5hMjxAPnsJWmFs9k02s9Vpi0qsvvv/c/7B3FBS3CtfyeAjf52kY6cIpK6941FvTKP1cPEr6LnexIMtuTt++HUdD9Qzt0uZY2Jc12/f7ZnMiF+HYTqDQYGYeS/Zo2IYjb5+vhdNaUIDGrSHIfQDmR9wIDAQAB
-----END PUBLIC KEY-----"""
key = '44x5b80r5ikacytg'
iv = 'gzsek651g5g68bta'


def test(key, iv):
    """校验RSA加密 使用公钥进行加密"""
    message = key + ":" + str(iv)
    cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(public_key))
    return base64.b64encode(cipher.encrypt(message.encode())).decode()
