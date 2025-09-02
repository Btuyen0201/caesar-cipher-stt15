def caesar_encrypt(text, k):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + k) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + k) % 26 + 97)
        else:
            result += char  # giữ nguyên ký tự không phải chữ cái
    return result

# Dữ liệu đầu vào
plaintext = "TranThiBichTuyen"
key = 15

# Mã hóa
ciphertext = caesar_encrypt(plaintext, key)

# In kết quả
print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
