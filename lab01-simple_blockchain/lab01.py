import hashlib

class Lab01:
        
    def caesar_encrypt(self, text, key):
        encrypted_text = ""
        for i in range(len(text)):
            char = text[i]
            if char.isalpha():
                if char.isupper():
                    encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
                else:
                    encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
            elif char.isdigit():
                encrypted_text += str((int(char) + key) % 10)
            else:
                encrypted_text += char
        return encrypted_text


    def sha256_hash(self, text):
        # Convert the text to bytes
        text_bytes = text.encode('utf-8')
        
        # Create a new SHA-256 hash object
        hash_obj = hashlib.sha256()
        
        # Update the hash object with the text bytes
        hash_obj.update(text_bytes)
        
        # Get the hexadecimal digest of the hash
        hex_digest = hash_obj.hexdigest()
        
        return hex_digest