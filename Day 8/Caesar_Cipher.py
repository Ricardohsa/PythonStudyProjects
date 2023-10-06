import arts
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


list = []
cipher_text = ""
total_aplhabet_words = 25
go_again =""
direction = ""
text = ""
shift = ""


print(arts.logo)


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 



#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.


def ceaser(text, shift, direction):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
  
    
    cipher_text = ""
    
    if shift > 25:
      shift = 1
    
    for i in text:
        position_on_alphabet = alphabet.index(i)
        
        if direction == "decode":
            new_position = position_on_alphabet - shift  
            
            if new_position > 25:
                new_position = 0            
                new_position += (shift - 1)
                new_letter = alphabet[new_position] 
                cipher_text += new_letter    
            else:
                new_letter = alphabet[new_position]
                cipher_text += new_letter    
        elif direction == "encode":
            new_position = position_on_alphabet + shift 
            
            if new_position > 25:           
               new_position = 0            
               new_position += (shift - 1)
               new_letter = alphabet[new_position] 
               cipher_text += new_letter    
            else:
               new_letter = alphabet[new_position]
               cipher_text += new_letter    
               
    print(cipher_text)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    
    if go_again == "yes":
      ceaser(text, shift, direction)

ceaser(text, shift, direction)



# def encrypt(text, shift):
#     cipher_text = ""
#     for i in text:
#         position_in_alphabet = alphabet.index(i)
#         new_position = position_in_alphabet + shift        
        
#         if new_position > 25:           
#            new_position = 0            
#            new_position += (shift - 1)
#            new_letter = alphabet[new_position] 
#            cipher_text += new_letter    
#         else:
#            new_letter = alphabet[new_position]
#            cipher_text += new_letter    
#     print(f" The encoded test is {cipher_text}")


# def decrypt(text, shift):
#     cipher_text = ""
#     for i in text:
#         position_on_alphabet = alphabet.index(i)
#         new_position = position_on_alphabet - shift        
       
#         if new_position > 25:           
#            new_position = 0            
#            new_position += (shift - 1)
#            new_letter = alphabet[new_position] 
#            cipher_text += new_letter    
#         else:
#            new_letter = alphabet[new_position]
#            cipher_text += new_letter    
           
#     print(f" The decoded test is {cipher_text}")


# def ceaser(text, shift, direction):
#     cipher_text = ""
    
#     if direction == "decode":
#         for i in text:
#             position_on_alphabet = alphabet.index(i)
#             new_position = position_on_alphabet - shift        
        
#             if new_position > 25:           
#                 new_position = 0            
#                 new_position += (shift - 1)
#                 new_letter = alphabet[new_position] 
#                 cipher_text += new_letter    
#             else:
#                 new_letter = alphabet[new_position]
#                 cipher_text += new_letter    
#         print(f" The {direction} test is {cipher_text}")
        
#     elif direction == "encode":
#         for i in text:
#             position_in_alphabet = alphabet.index(i)
#             new_position = position_in_alphabet + shift        
        
#             if new_position > 25:           
#                new_position = 0            
#                new_position += (shift - 1)
#                new_letter = alphabet[new_position] 
#                cipher_text += new_letter    
#             else:
#                new_letter = alphabet[new_position]
#                cipher_text += new_letter    
    
#         print(f" The {direction} test is {cipher_text}")