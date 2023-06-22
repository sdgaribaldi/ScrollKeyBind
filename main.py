from time import sleep
from pynput import keyboard
from pynput.mouse import Controller

# Bind mouse
mouse = Controller()

# Make a function to detect which keys are pressed
def on_press(key):
    # On key arrow-up
    if key == keyboard.Key.up:
        # Scroll up 3 units
        mouse.scroll(0, 3)
        #print('Scrolling up')
    elif key == keyboard.Key.down:
        # Scroll down 3 units
        mouse.scroll(0, -3)
        #print('Scrolling down')
    elif key == keyboard.Key.esc:
        # Exit program
        print('Closing in 3 seconds')
        sleep(1)
        print('Closing in 2 seconds')
        sleep(1)
        print('Closing in 1 seconds')
        sleep(1)
        quit()

# Listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()