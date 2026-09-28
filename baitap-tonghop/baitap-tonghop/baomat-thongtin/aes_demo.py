import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

KEY = b'1234567890123456'

def aes_encrypt(plain_text):
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    padded_data = pad(plain_text.encode('utf-8'), AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_data)
    return iv.hex(), encrypted_bytes.hex()

def aes_decrypt(iv_hex, cipher_hex):
    iv = bytes.fromhex(iv_hex)
    cipher_bytes = bytes.fromhex(cipher_hex)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(cipher_bytes)
    return unpad(decrypted_padded, AES.block_size).decode('utf-8')

if __name__ == "__main__":
    message = "Hệ thống An toàn Thông tin - Domain: nghvtuan.id.vn - Sinh viên: Nguyễn Văn Tuấn"
    
    print("==================================================")
    print("[-] Thông điệp ban đầu:")
    print(message)
    print("==================================================")
    
    iv_hex, cipher_hex = aes_encrypt(message)
    print("[+] IV (Vector khởi tạo Hex):", iv_hex)
    print("[+] Bản mã Ciphertext (Hex) :", cipher_hex)
    print("==================================================")
    
    decrypted_msg = aes_decrypt(iv_hex, cipher_hex)
    print("[+] Bản rõ thu được sau giải mã:")
    print(decrypted_msg)
    print("==================================================")
