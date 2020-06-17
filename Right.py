import RPi.GPIO as GPIO
import time
import pygame

pygame.init()
startsound = pygame.mixer.Sound("start you chose right.wav")
startsound.play()



def two_wheels(control_pins_l, control_pins_r, halfstep_seq):

    for i in range(32):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins_l[pin], halfstep_seq[halfstep][pin])

                GPIO.output(control_pins_r[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

            

def one_wheel(control_pins, timer, halfstep_seq):

    for i in range(32):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
    
            time.sleep(float(timer))
    


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    control_pins_l = [11, 7, 5, 3]  # linkerwiel voren
    control_pins_r = [13, 15, 19, 21]  # rechterwiel voren
    
    

    for pin in control_pins_l :
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    for pin in control_pins_r :
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    halfstep_seq = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0 ,0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1]
    ]

   
    halfstep_seq_rv = [
        [1, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0]
    ]
    
                
    GPIO.setup(8, GPIO.IN)  # GPIO 8 -> Left IR out
    GPIO.setup(12, GPIO.IN)  # GPIO 12 -> Middle IR out
    GPIO.setup(10, GPIO.IN)  # GPIO 10-> Right IR out
    
    

    count = 0

    while True :
        if GPIO.input(8) and GPIO.input(10):
            print("Voren")
            two_wheels(control_pins_l,control_pins_r, halfstep_seq)

        elif GPIO.input(8)== 0 and GPIO.input(10) == 0 and count == 0 :
            
            print("Kruispunt")
            
            one_wheel(control_pins_l, 0.001, halfstep_seq)
            one_wheel(control_pins_r, 0.001, halfstep_seq_rv)
            
            one_wheel(control_pins_l, 0.001, halfstep_seq)
            one_wheel(control_pins_r, 0.001, halfstep_seq_rv)
            
            one_wheel(control_pins_l, 0.001, halfstep_seq)
            one_wheel(control_pins_r, 0.001, halfstep_seq_rv)

            two_wheels(control_pins_l,control_pins_r, halfstep_seq)
           
            one_wheel(control_pins_l, 0.001, halfstep_seq)
            one_wheel(control_pins_r, 0.001, halfstep_seq_rv)

            one_wheel(control_pins_l, 0.001, halfstep_seq)
            one_wheel(control_pins_r, 0.001, halfstep_seq_rv)

            one_wheel(control_pins_l, 0.001, halfstep_seq)
            one_wheel(control_pins_r, 0.001, halfstep_seq_rv)
            count += 1
            
            
        elif ((GPIO.input(8)== 0 and GPIO.input(10) == 0) or (GPIO.input(8) == 0 and GPIO.input(12) == 0) or (GPIO.input(10) == 0 and GPIO.input(12) == 0 ))and count == 1:
            print ("Einde")
            print("\n| 00  00  00  00  00  00\n|   00  00  00  00  00\n| 00  00  00  00  00  00\n|   00  00  00  00  00\n| 00  00  00  00  00  00\n|\n|\n|\n|\n|")
            break
                   

        elif GPIO.input(8) == 0 :
            print("links")
            one_wheel(control_pins_r,0.001,halfstep_seq)
            one_wheel(control_pins_r,0.001,halfstep_seq)
            one_wheel(control_pins_l,0.001,halfstep_seq_rv)
            one_wheel(control_pins_l,0.001,halfstep_seq_rv)

            
              

        elif GPIO.input(10) == 0 :
            
            print("rechts")
            one_wheel(control_pins_l,0.001, halfstep_seq)
            one_wheel(control_pins_l,0.001, halfstep_seq)
            one_wheel(control_pins_r,0.001,halfstep_seq_rv)
            one_wheel(control_pins_r,0.001,halfstep_seq_rv)
            

        

        
    GPIO.cleanup()


main()
