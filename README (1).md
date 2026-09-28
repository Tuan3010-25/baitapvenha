# Bài tập về nhà

## Thông tin chung

| Mục | Nội dung |
|---|---|
| **Họ và tên** | Nghiêm Văn Tuấn |
| **Lớp** | K59KMT |
| **MSSV** | K235480106076 |

---

## Repo GitHub

> Điền link repo của bạn vào đây sau khi tạo.

- Link repo: `https://github.com/<username>/<ten-repo>`

---

# Môn 1: An toàn và bảo mật thông tin

## 1. Tìm hiểu thuật toán mã hoá đối xứng DES, AES

**Yêu cầu:**
- Mô tả được thuật toán DES và AES
- Trình bày quy trình mã hoá / giải mã
- Cài đặt AES bằng một ngôn ngữ lập trình bất kỳ

### 1.1. Mô tả thuật toán DES

Thuật toán DES (Data Encryption Standard) là chuẩn mã hóa khối đối xứng do IBM phát triển và được Viện Tiêu chuẩn và Công nghệ Quốc gia Mỹ (NIST) công nhận làm chuẩn 

quốc gia từ năm 1977. DES xử lý dữ liệu theo từng khối cố định có kích thước 64-bit, sử dụng một khóa mã hóa có độ dài ban đầu là 64-bit (trong đó 56-bit được dùng làm 

khóa mã hóa thực tế, 8-bit còn lại dùng làm bit kiểm tra chẵn lẻ parity).

Thuật toán vận hành dựa trên cấu trúc Mạng Feistel (Feistel Network) lặp lại qua 16 vòng biến đổi liên tiếp. Do độ dài khóa thực tế chỉ có 56-bit, không gian khóa của 

DES quá nhỏ ($2^{56}$ khả năng) khiến thuật toán này hiện nay không còn an toàn trước các hình thức tấn công duyệt khóa vét cạn (Brute Force) và đã được thay thế bởi 

AES.

![alt text](1.jpg)

### 1.2. Mô tả thuật toán AES

Thuật toán AES (Advanced Encryption Standard) được NIST lựa chọn vào năm 2001 để thay thế cho DES sau cuộc thi chuẩn hóa mã hóa mở rộng. AES làm việc trên các khối dữ 

liệu cố định có kích thước 128-bit (16 bytes) và hỗ trợ ba độ dài khóa mã hóa linh hoạt gồm: 128-bit, 192-bit và 256-bit.Khác với DES dùng cấu trúc Feistel, AES xây 

dựng trên cấu trúc Mạng hoán vị - thay thế (Substitution-Permutation Network - SPN). Toàn bộ dữ liệu 128-bit đầu vào được biểu diễn dưới dạng ma trận trạng thái (State 

matrix) kích thước $4 \times 4$ bytes. Số lượng vòng biến đổi xử lý phụ thuộc trực tiếp vào độ dài khóa:

Khóa 128-bit: 10 vòng mã hóa ($N = 10$).

Khóa 192-bit: 12 vòng mã hóa ($N = 12$).

Khóa 256-bit: 14 vòng mã hóa ($N = 14$).

![alt text](2.webp)

### 1.3. Quy trình mã hoá / giải mã (DES & AES)

### Quy trình mã hóa và giải mã của DES

1. Hoán vị khởi đầu (Initial Permutation - IP): Khối dữ liệu 64-bit đầu vào được xáo trộn vị trí bit theo bảng hoán vị cố định, sau đó tách làm hai nửa bằng nhau: nửa

 trái $L_0$ (32-bit) và nửa phải $R_0$ (32-bit).

 2. 6 vòng biến đổi Feistel: Tại mỗi vòng $i$ (từ 1 đến 16):

$L_i = R_{i-1}$

$R_i = L_{i-1} \oplus f(R_{i-1}, K_i)$

Hàm phi tuyến $f$ mở rộng $R_{i-1}$ từ 32-bit lên 48-bit, XOR với khóa vòng 48-bit $K_i$,

 đưa qua các hộp thay thế phi tuyến (S-Boxes) đưa về 32-bit rồi hoán vị.

 3. Hoán vị kết thúc ($IP^{-1}$): Sau vòng thứ 16, ghép $R_{16}$ và $L_{16}$ rồi thực hiện hoán vị nghịch đảo $IP^{-1}$ để thu được bản mã.

 4. Giải mã: Thực hiện quy trình đảo ngược hoàn toàn bằng cách áp dụng chuỗi khóa vòng theo thứ tự ngược lại từ $K_{16}$ đến $K_1$.

 ### Quy trình mã hóa và giải mã của AES

 1. Vòng khởi tạo (Initial Round): Thực hiện bước AddRoundKey bằng cách XOR ma trận trạng thái đầu vào với khóa gốc $K_0$.

 2. Các vòng lặp chính (Vòng 1 đến $N-1$): Mỗi vòng lặp gồm 4 thao tác nối tiếp:

 SubBytes: Thay thế phi tuyến từng byte trong ma trận trạng thái qua bảng S-Box.

 ShiftRows: Dịch chuyển vòng các hàng của ma trận trạng thái về phía bên trái 
 
 (hàng 0 không dịch, hàng 1 dịch 1 byte, hàng 2 dịch 2 bytes, hàng 3 dịch 3 bytes).

 MixColumns: Trộn các phần tử trong từng cột thông qua phép nhân ma trận trên trường hữu hạn $GF(2^8)$.

 AddRoundKey: XOR ma trận trạng thái với khóa vòng $K_i$ sinh ra từ lịch trình khóa.

 Vòng cuối cùng (Vòng $N$): Thực hiện tương tự vòng chính nhưng bỏ qua bước MixColumns (chỉ gồm SubBytes, ShiftRows, và AddRoundKey).

 Giải mã: Thực hiện các phép biến đổi nghịch đảo gồm InvShiftRows, InvSubBytes, AddRoundKey và InvMixColumns với chuỗi khóa vòng áp dụng từ $K_N$ về $K_0$.

### 1.4. Cài đặt AES (code demo)

- Ngôn ngữ sử dụng: Python 3
- Đường dẫn source code: src/aes/aes_demo.py

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

 Khóa bí mật AES 128-bit (16 bytes)
KEY = b'1234567890123456'

def aes_encrypt(plain_text: str):
    # Sinh ngẫu nhiên Vector khởi tạo IV (16 bytes)
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    padded_data = pad(plain_text.encode('utf-8'), AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_data)
    return iv.hex(), encrypted_bytes.hex()

def aes_decrypt(iv_hex: str, cipher_hex: str):
    iv = bytes.fromhex(iv_hex)
    cipher_bytes = bytes.fromhex(cipher_hex)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(cipher_bytes)
    return unpad(decrypted_padded, AES.block_size).decode('utf-8')

if __name__ == "__main__":
    message = "An toan va bao mat thong tin - Sinh vien: Nghiem Van Tuan - Lop: K59KMT"
    
    print("[-] Thong diep ban dau:", message)
    iv_hex, cipher_hex = aes_encrypt(message)
    print("[+] IV (Vector khoi tao Hex):", iv_hex)
    print("[+] Ban ma Ciphertext (Hex):", cipher_hex)
    
    decrypted_msg = aes_decrypt(iv_hex, cipher_hex)
    print("[+] Ban ro thu duoc sau giai ma:", decrypted_msg)

---

## 2. Tìm hiểu thuật toán mã hoá bất đối xứng RSA

**Yêu cầu:**
- Nguyên lý sinh cặp khoá bí mật (private key) và khoá công khai (public key)

![alt text](3.png)

---

## 3. Các mô hình áp dụng RSA & so sánh với AES

**Yêu cầu:**
- Trình bày các mô hình áp dụng RSA: xác thực người gửi, xác thực người nhận, xác thực cả hai
- So sánh thời gian mã hoá / giải mã giữa RSA và AES
- Đề xuất cách dùng kết hợp RSA và AES

![alt text](4.png)

---

# Môn 2: Lập trình web

## Bài tập 1

### 1. Giả lập Linux OS

- Công cụ sử dụng:  VMware 

![alt text](5.png)

### 2. Cài đặt Docker Compose

![alt text](6.png)


### 3. Cài các dịch vụ trên Docker Compose

Các dịch vụ cần cài: `nginx`, `nodered`, `mariadb`, `phpmyadmin`, `cloudflared` (cần domain riêng)

- File cấu hình: `docker-compose.yml`

![alt text](7.png)

### 4. Cấu hình Nginx chạy 2 website với 2 domain khác nhau

- Domain 1: nghvtuan.id.vn
- Domain 2: nghvtuan.id.vn/api/tacke
- File cấu hình nginx: `nginx/conf.d/`

![alt text](8.png)

---

## Bài tập 2

### 1. Tạo API đơn giản bằng Node-RED

- Sử dụng node `http in` + `http response` để tạo API

![alt text](9.png)

### 2. Cấu hình Nginx để web gọi được API Node-RED (qua JS)

Ví dụ API trả về JSON:

msg.payload = {
    "ok": 1,
    "msg": "Thành công từ hệ thống nghvtuan.id.vn",
    "dssv": [
        {"name": "nghvtuan", "money": 999},
        {"name": "Nguyễn Văn Tuấn", "money": 888}
    ]
};
return msg;

### 3. Code JS gọi API trong trang HTML

- File: `index.html`

![alt text](10.png)

---

