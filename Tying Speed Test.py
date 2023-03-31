from time import *
import random as r
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error
def speed_time(time1,time2,userinput):
    time_delay = time2 - time1
    time_r = round(time_delay,2)
    speed = len(userinput) / time_r
    return round(speed)

test = ['The dog or domestic dog is a domesticated descendant of the wolf', 'Cats, also called domestic cats are small, carnivorous mammals, of the family Felidae','A computer mouse is an input device that is used with a computer']
test1 = r.choice(test)
print(" ******Typing Speed Test******")
print(test1)
print("\n\n")
time1 = time()
testinput = input(" Enter : ")
time2 = time()

print(" Speed : ", speed_time(time1,time2,testinput)," words/sec")
print(" Error : ", mistake(test1,testinput))