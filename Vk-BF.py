import os


os.system('clear')


def get_proxy():
	import os
	os.system("python3 parser.py") # надо встроить 
	

	


banner = '''
8b           d8  88                 88888888ba   88888888888  
`8b         d8'  88                 88      "8b  88           
 `8b       d8'   88                 88      ,8P  88           
  `8b     d8'    88   ,d8           88aaaaaa8P'  88aaaaa      
   `8b   d8'     88 ,a8"  aaaaaaaa  88""""""8b,  88"""""      
    `8b d8'      8888[    """"""""  88      `8b  88           
     `888'       88`"Yba,           88      a8P  88           
      `8'        88   `Y8a          88888888P"   88           
                                                              
                                                              '''
print(banner)

text = '''
     
      [1]-VkBruteForceV1
      [2]-VkBruteForceV2
      [3]-passgen   #Добавить в 1 и 2
     
      '''
print(text)

v = int(input("Выберите номер:"))
def Vkpassgen():
	import os
	os.system("python3 passgen.py")

def Vkpassgen2():
  print("пусто")

def VkBruteForceV1():
	import os
	os.system("python3 vk.py")

def VkBruteForceV2():
	import os
	os.system('python vk2.py')

if v ==3:
	Vkpassgen()
elif v ==1:
  VkBruteForceV1()
elif v ==2:
  VkBruteForceV2()
