from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key, Listener as KeyboardListener
import time

start = Key.enter
stop = Key.esc
control_mouse = Key.tab

mouse_controller = Controller()

def on_move(x, y):
    print('Pointer moved to ({}, {})'.format(x, y))

def on_click(x, y, button, pressed):
    print('{} at ({}, {})'.format('Pressed' if pressed else 'Released', x, y))

def on_scroll(x, y, dx, dy):
    print('Scrolled {} at ({}, {})'.format('down' if dy < 0 else 'up', x, y))

def record_mouse():
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

def controll_mouse():
    print('The current pointer position is {}'.format(mouse_controller.position))
    mouse_controller.position (500, 500)
    print('Now we have moved it to {}'.format(mouse_controller.position))
    mouse_controller.move(10, 10)
    #mouse_controller.press(Button.right)
    #mouse_controller.release(Button.left)
    #mouse_controller.click(Button.right, 2)
    #mouse_controller.scroll(0, 2)


def welcome():
    print("-----------------------------Mouse controller and monitoring by Iamtherootx-----------------------------")

def on_press(key):
    if key == start:
        record_mouse()
        print("Record position of your mouse")
    elif key == control_mouse:
        controll_mouse()
        print("Control the mouse")
    elif key == stop:
        print("Stopping the program")
        return False  
    

def main():
    welcome()
    with KeyboardListener(on_press=on_press) as keyboard_listener:
        keyboard_listener.join()
        

if __name__ == "__main__":
    main()
