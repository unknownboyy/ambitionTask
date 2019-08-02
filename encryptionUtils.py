import re

"""
 * Encryption Algorithm ~Ankit Agrawal ( 161500085 )
 * Step 0: If key contains chars, call convertToNumericKey() to convert key into numerical key
 * Step 1: Take ascii value of each char
 * Step 2: Convert it to binary
 * Step 3: Shift it according to the value of key at that index ( in case key have smaller length it starts from beginning )
 * Step 4: Append above 8-bit string ( if length is not 8, then append 0`s ) to a binary string
 * Step 5: Reverse the binary string
 * Step 6: Divide the binary string into segments of six
 * Step 7: Convert each segment into its decimal equivalent number and take char value of it
 * Step 8: Shift char to 32 places right and append it to encoded string
 * Step 9: Return the encoded string
"""


def dec2bin(dec):
    return bin(dec)[2:]


def convertToNumericKey(key):
    numeric_key = ""
    for i in range(len(key)):
        numeric_key += str(ord(key[i]))
    numeric_key = numeric_key.replace("9","7")
    return numeric_key


def encrypt(data,key):
    if re.match(r"\w+",key):
        key = convertToNumericKey(key)
    

    binary_string = ""
    k = 0
    shifts = None
    num = None
    code = None

    for i in range(len(data)):

        code = ord(data[i])

        shifts = int(key[k])

        k = (k+1)%(len(key))

        num = '0'*int( 8-len(dec2bin(code)) ) + dec2bin( code )  # We Got Number in Binary of Length 8

        binary_string += num[8-shifts:8]+num[0:8-shifts]  # Added to Binary String after shifting
    

    binary_string = binary_string[::-1]  # Reversed Binary String
    # print(binary_string,"encoded binary string")


    # Made Binary String Length divisible by 6 because we will divide it into parts of 6 that will cause an unclear value of last 6-bit segment that will not be of length 6
    if len(binary_string) % 6 != 0:
        binary_string = binary_string + "0"*int(6-len(binary_string)%6)
    

    # print(binary_string)

    encrypted_string = ""

    # AGain getting char from ascii value
    for i in range(0,len(binary_string),6):
        code = int( binary_string[ i: i+ 6 ] , 2 )

        # Again shifting code to 32 places right ( so that it have more readable chars )
        encrypted_string += chr( code + 32 )
    
    return encrypted_string




def decrypt(encrypted_string,key):
    if re.match(r"\w+",key):
        key = convertToNumericKey(key)


    binary_string = ""
    code = None
    num_string = None
    k=0
    shifts = None

    #  Making Binary String from chars
    for i in range(len(encrypted_string)):
        # Shfiting chars back to 32 places left
        code = ord(encrypted_string[i]) - 32
        binary_string += '0'*int(6-len(dec2bin(code))) + dec2bin(code)
    

    # Making its length divisible by 8
    binary_string = binary_string[0:len(binary_string)-len(binary_string)%8]

    # print(binary_string,"ready to decode")

    # Reversing It
    binary_string = binary_string[::-1]

    decoded_string = ""
    for i in range(0,len(binary_string),8):
        # Taking 8-bit segment
        num_string = binary_string[i:i+8]

        shifts = int(key[k])
        k = (k+1)%(len(key))
        # Shifting back 8-bit segment from key
        num_string = num_string[shifts: 8] + num_string[0:shifts]
        # getting integer value
        code = int( num_string , 2 )
        # append char to decoded string from ascii value
        decoded_string += chr( code )
    

    return decoded_string



# Sample Run


"""
string = "hello boss !! This is unknownboy"
key = "vgsdsdgbvsbs64164"
coded_message = encrypt(string,key)
decoded_message = decrypt(coded_message,key)
print( "Encoded message =", coded_message)
print( "Decoded message =", decoded_message)
"""