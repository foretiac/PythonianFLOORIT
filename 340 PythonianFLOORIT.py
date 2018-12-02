#Anthony Foretich
#ISAT 340
#PYTHONIAN PROGRAM

#This program presents the user with a dilemma, where they have started
#to FLOOR IT from 0 out of a parking lot, 4 seconds go by without alert.
#Then you get an alert that there is an obstacle 40 feet ahead!
#BUT you can only slow 8 ft per second
#The program tells you the speed of you accelerating for the first four seconds
#and then your speed per second as you try to accelerate to zero before hitting the obstacle
#The program then tells you if you hit the obstacle or not. 

#Start a class that contains the functions accelerate and brake.
#It also contains the value of speed as it gets iterated 
class Accelbrake:
#Initialize the speed variable, which will be influenced by the acceleration valariable. 
    def __init__(self, acceleration, speed):
        self.__speed = 0
    
#The acceleration function. It will be iterated 5 times in the main function. 
    def accelerate(self, acceleration):
#The speed is determined by the acceleration which is determined from user input of zerotosixtytime. 
        self.__speed += acceleration
        return self.__speed
#The brake function. It will be iterated 5 times or until the speed reaches 0.         
    def brake(self):
        self.__speed -= 4
        return self.__speed
    
# The main function contains the initial informaiton for the user as well as input and calls the class functions. 
def main():
    print(' You start to FLOOR IT from 0 out of a parking lot, 4 seconds go by without alert. ')
    print(' ALERT! there is an obstacle 40 feet ahead! ')
    print( 'You start to break, but you can only slow 8 ft per second! ')
#The main also contains the zerotosixtytime input from the user. 
    zerotosixtytime = float(input('What is the 0 to 60 (mph) time of your car in seconds? '))
#acceleratoin variable is the zerotosiztytime variable, which gets defined in the lambda expression below. 
    acceleration = zerotosixtytime
#The speed must be initialized
    speed = 0
#The crash class is called in the main, which contains the arguments acceleration and speed 
    crash = Accelbrake(acceleration, speed)
#The user is promted about the breakdown of speed
    print('-Per second, the breakdown of your speed before reaching the obstacle is: ')
#A for loop is used to iterate the accelation function four times, representative of the four seconds of accleration. 
    for i in range(4):
        print(' while accelerating, your speed is: ', crash.accelerate(acceleration))
#A for loop is used to iterate the brake function five times, which at 8 ft/sec slowing is 40 feet total. 
    for i in range(5):
        while crash.brake() > 0:
            print(' while breaking, your speed is', crash.brake())
#The user will be prompted whether of not they hit the obstacle by if operators calling the brake function. 
    if crash.brake() > 0:
        print (' you hit the obstacle going' , crash.brake(), 'miles per hour')
    if crash.brake() <= 0:
        print (' luckily, you avoided the obstacle') 

# A lambda expression is used to definte the acceleration variable from zerotosixtytime in the main. 
lambda zerotosixtytime: 60/zerotosixtytime

#The main function must be called.     
main ()
