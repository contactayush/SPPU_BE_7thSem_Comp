import random

############################
#from captcha.image import ImageCaptcha
#image = ImageCaptcha(width = 280, height = 90)
##########################

def checkCaptcha(captcha, user_captcha):
    print(captcha)
    print(user_captcha)
    if captcha == user_captcha:
        return True
    return False
 

def generateCaptcha(n):
     
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
    captcha = ""
    while (n):
        k=random.randint(1, 1000) % 62
        captcha += chrs[k]
        n -= 1
    
#######################
    # generate the image of the given text
    #data = image.generate(captcha)  
    # write the image on the given file and save it
    #image.write(captcha, 'CAPTCHA.png')
###############################

    return captcha
 
captcha = generateCaptcha(8)
print(captcha)
 
print("Enter above CAPTCHA:")
usr_captcha = input()
 

if (checkCaptcha(captcha, usr_captcha)):
    print("CAPTCHA Matched")
else:
    print("CAPTCHA Not Matched")