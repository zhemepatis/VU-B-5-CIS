import math

# Function to encrypt a letter
def encrypt(letter, k1, k2):
    return (k1 * letter + k2) % 32

# Function to decrypt a letter
def decrypt(cipher_letter, k1_inv, k2):
    return (k1_inv * (cipher_letter - k2)) % 32

# Given cipher text
text = "SŠEIĮURERMALŲĮBERZMČSŠEIŲALŪCĘOSYŪOŲPĘBDŽBŠCAŪIGĮILŲMICSFĮBĮČGAIBSAĮBĮŪIAŽDBSAĮPŲALŪCNBDĮASREĖAIBILŲŽRĖAFAEŪACĮŲŽIŪACĮŲĮŲEYŪŲŽIĮŲEYŪŲŲŠCAIBŽEAOBŠCABŠPIGŽEARJBEF"
# Lithuanian alphabet with 32 letters
abc = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"

# Try different values of k1 and k2
for k1 in range(1, 16):
    # Check if k1 is coprime with 32
    if math.gcd(k1, 32) != 1:
        continue
    
    # Calculate the modular inverse of k1 mod 32
    k1_inv = pow(k1, -1, 32)
    
    for k2 in range(32):
        # Try to decrypt the ciphertext
        result = ""
        for letter in text:
            idx = abc.index(letter)
            decrypted_idx = decrypt(idx, k1_inv, k2)
            result += abc[decrypted_idx]
        
        # Check if the result starts with "B"
        # if result[0] == "B":
        print(f"Possible key: k1={k1}, k2={k2}")
        print(f"Decrypted text: {result}")

    


