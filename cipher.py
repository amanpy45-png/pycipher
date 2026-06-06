import random
import string                 
chars= " " + string.punctuation + string.digits +string.ascii_letters                      
chars=list(chars)              
shuffled_key = chars.copy()               
# print(f"chars:{chars}")                
random.shuffle(shuffled_key) 

encrypt_dict = {chars[i]: shuffled_key[i] for i in range(len(chars))}

decrypt_dict = {shuffled_key[i]: chars[i] for i in range(len(chars))}               

# encoder
def encrypt(plain_text, lookup_table):
    encrypted_msg = ""

    for letter in plain_text:
        # If letter isn't in the dict -> it just returns the letter itself
        encrypted_msg += lookup_table.get(letter, letter) 

    return encrypted_msg



# decoder
def decrypt(cipher_text, lookup_table):

    decrypted_msg = ""

    for letter in cipher_text:
        # Safely falls back to the original letter if unknown
        decrypted_msg += lookup_table.get(letter, letter) 

    return decrypted_msg    


org_msg = input("Enter a msg to encrypt : ")

secret_msg = encrypt(org_msg, encrypt_dict)

secret_decrypt_msg = decrypt(secret_msg, decrypt_dict)



print(f"original_msg  : {org_msg}")

print(f"encrypted_msg : {secret_msg}")

print(f"decrypted_msg : {secret_decrypt_msg}")   

