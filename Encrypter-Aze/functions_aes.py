import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import hashlib,ctypes,base64,os
from functions import acari_yoxla
from Cryptodome.Cipher import AES
import easygui
from Cryptodome.Random import get_random_bytes
try:
    __key__ = hashlib.sha256(bytes(acari_yoxla()[:32], encoding='utf-8')).digest()

    def encrypt_text(raw):
        BS = AES.block_size
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

        raw = base64.b64encode(pad(raw).encode('utf8'))
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key= __key__, mode= AES.MODE_CFB,iv= iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt_text(enc):
        
        enc  = enc[2:len(enc)]
        unpad = lambda s: s[:-ord(s[-1:])]
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(__key__, AES.MODE_CFB, iv)
        return unpad(base64.b64decode(cipher.decrypt(enc[AES.block_size:])).decode('utf8'))


    def encrypt(file_path, key):
        try:
            with open(file_path, 'rb') as file:
                plaintext = file.read()

            iv = os.urandom(16)


            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            encryptor = cipher.encryptor()


            ciphertext = encryptor.update(plaintext) + encryptor.finalize()
            ciphertext = iv + ciphertext
            with open(file_path, 'wb') as file:
                file.write(ciphertext)
        
        except PermissionError as pe:
                ctypes.windll.user32.MessageBoxW(None, pe, 'Bu qovluğa icazəniz yoxdur', 0x10 | 0x100, 500, 300)

    def decrypt(file_path, key):
        with open(file_path, 'rb') as file:
            ciphertext = file.read()

        iv = ciphertext[:16]
        ciphertext = ciphertext[16:]

        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        with open(file_path, 'wb') as file:
            file.write(plaintext)




    ###########################    Lock - Unlock Funksiyalari   ###########################
    def lock(qovlug_yolu, key):
        for root, dirs, files in os.walk(qovlug_yolu):
            for file in files:
                fayl_yolu = os.path.join(root, file)
                encrypt(fayl_yolu, key)

    def unlock(qovlug_yolu, key):
        for root, dirs, files in os.walk(qovlug_yolu):
            for file in files:
                fayl_yolu = os.path.join(root, file)
                decrypt(fayl_yolu, key)
    #######################################################################################
    def acar_yarat_gen(password=b'gcosx.js'):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32,
            backend=default_backend()
        )
        key = kdf.derive(password)
        return key

except PermissionError as pe:
    ctypes.windll.user32.MessageBoxW(None, pe, 'Bu qovluğa icazəniz yoxdur', 0x10 | 0x100, 500, 300)

except FileNotFoundError as fnt:
    ctypes.windll.user32.MessageBoxW(None, fnt, 'Fayl tapılmadı!', 0x10 | 0x100, 500, 300)