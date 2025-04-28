from des import des_encrypt, des_decrypt, text_to_binary, binary_to_text

def pad_key(key):
    if len(key) < 8:
        return key + '0' * (8 - len(key))
    return key[:8]

def main():
    print("DES (Data Encryption Standard) Chiffrement/Déchiffrement")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Chiffrer un message")
        print("2. Déchiffrer un message")
        print("3. Quitter")
        
        choice = input("\nEntrez votre choix (1-3) : ")
        
        if choice == '1':
            
            plaintext = input("\nEntrez le texte à chiffrer : ")
            key = input("Entrez la clé de chiffrement (sera complétée/tronquée à 8 caractères) : ")
            key = pad_key(key)
            
            try:
                
                encrypted = des_encrypt(plaintext, key)
                print("\nRésultat binaire chiffré :")
                print(encrypted)
                
            except Exception as e:
                print(f"\nErreur lors du chiffrement : {str(e)}")
        
        elif choice == '2':
            binary = input("\nEntrez la chaîne binaire à déchiffrer : ")
            key = input("Entrez la clé de déchiffrement (sera complétée/tronquée à 8 caractères) : ")
            key = pad_key(key)
            
            try:     
                decrypted = des_decrypt(binary, key)
                print("\nTexte déchiffré :")
                print(decrypted)
                
            except Exception as e:
                print(f"\nErreur lors du déchiffrement : {str(e)}")
        
        elif choice == '3':
            print("\nAu revoir !")
            break
        
        else:
            print("\nChoix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main() 