# def encrypt(text_p, shift_p):
#     cipher_text = ""
#     for char in text_p :
#         position_of_char = 0
#         i=0
#         while char != alphabets[i] :
#             position_of_char = i
#             i+=1

#         cipher_text += alphabets[position_of_char + shift_p +1]
#     print(f"Encrypted message is : {cipher_text}")  


# def decrypt(text_p, shift_p):
#     plain_text = ""
#     for char in text_p :
#         position_of_char = 0
#         i=0
#         while char != alphabets[i] :
#             position_of_char = i
#             i+=1

#         plain_text += alphabets[position_of_char - shift_p + 1]
#     print(f"decoded message is : {plain_text}")  

def caeser(direction_c, text_c, shift_c):
    end_text = ""
    shift_c = shift_c % 25
    for char in text_c :
        if char not in alphabets :
            end_text += char
        else:
            position = alphabets.index(char)
            if direction == "decode":
                shift_c *= -1
            new_position = position + shift_c
            end_text += alphabets[new_position]
    print(f"The {direction_c}d text is : {end_text}")




alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt and type 'decode' to decrypt : \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))
caeser(direction, text, shift)