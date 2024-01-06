from pynput import keyboard
import threading
import pyautogui, sys
import time

a = False

def on_press(key):
    global a
    print(f'Key pressed: {key}')
    try:
        if key == keyboard.Key.f12:
            sys.exit()

        if key == keyboard.Key.alt_l:
            if a:
                a = False
            else:
                a = True

        if hasattr(key, 'vk'):
            print(key.vk)
            if key.vk == 96:
                pyautogui.click(x=900, y=460, button='right')
                pyautogui.click(x=900, y=460, button='right')

                pyautogui.click(x=900, y=390, button='right')
                pyautogui.click(x=900, y=390, button='right')

                pyautogui.click(x=900, y=320, button='right')
                pyautogui.click(x=900, y=320, button='right')

                pyautogui.click(x=970, y=320, button='right')
                pyautogui.click(x=970, y=320, button='right')

                pyautogui.click(x=1040, y=320, button='right')
                pyautogui.click(x=1040, y=320, button='right')

                pyautogui.click(x=1040, y=390, button='right')
                pyautogui.click(x=1040, y=390, button='right')

                pyautogui.click(x=1040, y=460, button='right')
                pyautogui.click(x=1040, y=460, button='right')

                pyautogui.click(x=970, y=460, button='right')
                pyautogui.click(x=970, y=460, button='right')
    except Exception as e:
        print("ERROR: 0" +str(e))

def listen_for_keys():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    key_listener_thread = threading.Thread(target=listen_for_keys)

    try:
        key_listener_thread.start()
        key_listener_thread.join()
    except KeyboardInterrupt:
        print("Exiting program...")
        key_listener_thread.stop()
