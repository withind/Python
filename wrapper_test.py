#coding=utf-8
def shout(word="yes") :
    return word.capitalize()+" !"
 
print (shout())

del shout
try :
    print (shout())
except NameError:
    print ('Error')
    #输出 : "name 'shout' is not defined"
 
