# if __name__ == "__main__":
    # print(f"\nCode-------> 1\nDecode-------> 2")
    # ask_num = 0
    # while(True):
    #     ask_num = int(input("Do you want to Code or Decode?"))
    #     if ask_num == 1 or ask_num == 2:
    #         break

    # response = input('Enter your text: ')

import random
def code_less(response):
    return(response[::-1])

def decode_less(response):
    return(response[::-1])

def code_great(response):
    response = response[len(response)-1: len(response)] + response[1: len(response)-1] + response[0:1]
    random_first = chr(random.randint(65,90)) + chr(random.randint(65,90)) + chr(random.randint(65,90))
    random_last = chr(random.randint(65,90)) + chr(random.randint(65,90)) + chr(random.randint(65,90))

    code_txt = random_first + response + random_last
    return(f"Coded Text: {code_txt}")

def decode_great(response):
    response = response[3:len(response)-3]
    response = response[len(response)-1: len(response)] + response[1: len(response)-1] + response[0:1]
    return(f"Decoded Text: {response}")

def verify(ask_num,response): 
    match ask_num:
        case 1:
            if (len(response) <= 3):
                return(code_less(response))
            else:
                return(code_great(response))
        case 2:
            if (len(response) <= 3):
                return(decode_less(response))
            else:
                return(decode_great(response))
        case _ if ask_num == 0:
            print ("No 0")
        case _:
            print("Enter only 1 or 2!!")

    verify(ask_num,response)