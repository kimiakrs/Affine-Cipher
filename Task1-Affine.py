#KimiaSadatKarbasi-SID60393958
#Using random for getting a value
#Using time library for counting brute force process
import random
import time


#GCD calculation for getting a value
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#For decrypted function inverse our a value to a ^ -1
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


#Firs put all of values which has the result of (1, 26) = 1, then  get the random value
def get_valid_a():
    valid_a_values = [i for i in range(1, 26) if gcd(i, 26) == 1]
    return random.choice(valid_a_values)


#E(x) = (a * x + b) mod 26
def affine_encrypt(text, a, b):
    result = ''
    for char in text:
        #I'm trying to encrypt alphabet only
        if char.isalpha():
            #Convert charachter to alphabetic way and apply those to the formula
            base = ord('A') if char.isupper() else ord('a')
            #After putting to the formula change those to the charachter again.
            result += chr(((a * (ord(char) - base) + b) % 26) + base)
        else:
            result += char
    return result

#D(y) = a⁻¹ * (y - b) mod 26
def affine_decrypt(cipher, a, b):
    #the function to inverse the a value
    a_inv = mod_inverse(a, 26)
    result = ''
    for char in cipher:
        if char.isalpha():
            #Convert it to integer for putting in the formula
            base = ord('A') if char.isupper() else ord('a')
            result += chr(((a_inv * ((ord(char) - base - b)) % 26) + base))
        else:
            result += char
    return result

def brute_force_attack(cipher_text, dictionary_path):
    print("Brute-forcing the cipher text...")
    # Read dictionary words once
    with open(dictionary_path, 'r') as dict_file:
        dictionary_words = set(word.lower().strip() for word in dict_file.readlines())

    valid_a_values = [i for i in range(1, 26) if gcd(i, 26) == 1]
    start_time = time.time()
    
    best_match = None
    best_score = 0
    
    for a in valid_a_values:
        for b in range(26):
            try:
                decrypted = affine_decrypt(cipher_text, a, b).lower()
                decrypted_words = decrypted.split()
                #Count how many words appear in the decrypted text are matched with the
                #dictionary word
                score = sum(1 for word in dictionary_words if word in decrypted_words)
                if score > best_score:
                    best_score = score
                    best_match = (a, b, decrypted)
                    print(f"match found: a={a}, b={b}, score={score}")
                    
            except Exception as e:
                continue
    #Require at least 2 matches to get the result
    if best_match and best_score > 1:  
        a, b, decrypted = best_match
        #Time calculating
        elapsed = time.time() - start_time
        print(f"\nThe cipher was unlocked with a = {a}, b = {b}")
        print(f"\nTime taken by the Hacker: {elapsed:.2f} seconds")

        # Save the unlocked text to a defined file
        unlocked_path = "/opt/Affine/Task1/unlocked.txt"
        with open(unlocked_path, "w") as unlocked_file:
            unlocked_file.write(decrypted)
        print(f"Unlocked text saved to {unlocked_path}")
    else:
        print("\nFailed to decrypt the message with the current dictionary.")
    
    print(f"\nTotal time: {time.time() - start_time:.2f} seconds")

# Entry point
if __name__ == "__main__":
    print("This is Task1-Affine.py")
    print("Kimia Sadat Karbasi - Student ID Number ='60393958'")
    # File paths
    plain_path = "/opt/Affine/Task1/plain.txt"
    cipher_path = "/opt/Affine/Task1/cipher.txt"
    decrypted_path = "/opt/Affine/Task1/decrypted.txt"
    dictionary_path = "/opt/Affine/Task1/dictionary.txt"
    unlocked_path = "/opt/Affine/Task1/unlocked.txt"

    # Generate random a value
    a = get_valid_a()
    print(f"Valid 'a' selected randomly: {a}")

    #Ask user for b value
    b = int(input("Enter value for 'b' (0 to 25): "))
    if not (0 <= b < 26):
        raise ValueError

    #Read plain text
    with open(plain_path, "r") as file:
        plain_text = file.read()

    #Encrypt and save the encrypted into the path
    cipher_text = affine_encrypt(plain_text, a, b)
    with open(cipher_path, "w") as file:
        file.write(cipher_text)

    # Decrypt cipher.txt and save into the path
    decrypted_text = affine_decrypt(cipher_text, a, b)
    with open(decrypted_path, "w") as file:
        file.write(decrypted_text)
    print("Encrypted text:", cipher_text)
    print("Decrypted text:", decrypted_text)
    print("\nEncryption and decryption completed successfully.")
    brute_force_attack(cipher_text, dictionary_path)
