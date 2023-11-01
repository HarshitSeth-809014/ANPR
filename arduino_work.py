from pyfirmata import Arduino, SERVO, util, INPUT
from time import sleep

port = 'COM4'
pinServo = 10
board = Arduino(port)

it = util.Iterator(board)
it.start()

def open_barrier(pin, angle):
    board.digital[pin].mode = SERVO


    board.digital[pin].write(angle)
    if (angle==0):
        sleep(5)
    sleep(0.001)


def set_barrier():
    board.digital[2].write(1)
    for i in range(0, 90):
        open_barrier(pinServo, i)
    board.digital[2].write(0)
    

def check_barrier_button():
    prev_state = 0
    button = board.digital[5]
    button.mode = INPUT

    while True:
        board.digital[3].write(1)
        state = button.read()

        if state != prev_state:
            if state == 1:
                board.digital[3].write(0)
                set_barrier()
                break


def check_image_button():
    prev_state = 0
    button = board.digital[6]
    button.mode = INPUT

    while True:
        
        state = button.read()

        if state != prev_state:
            if state == 1:
                return True
