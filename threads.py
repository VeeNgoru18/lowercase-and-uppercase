
from time import sleep 
from threading import * #from package thread
class capitalLetters(Threads):
    def countUpperCase(string):
        upper = 0
 for i in range(len(string)):
     if (ord(string[i]) >= 65 and ord(string[i]) <= 90):
         upper +=1

        print  ('Uppercase characters = %s' %upper)

        sleep(1)   
    class smallLetters(Thread):
    def countLowerCase(string):
        lower = 0
        for i in range(len(string)):
            if(ord(string[i]) >= 97 and ord(string[i]) <=122)
            lower += 1

            print ('Lowercase characters = %s' %lower)
            sleep(1)


 t1 = upper()
 t2 = lower()  
 
 t1.start()
 sleep(0.5)
 t2.start()


t1.join()
t2.join()

#driver code
string = 'I love Python programmiNG'




