from pynput.keyboard import Key, Listener
import threading


def listner():
    def on_press(key):
        print('{0} pressed'.format(
            key))
        return True

    def on_release(key):
        print('{0} release'.format(
            key))
        if key == Key.esc:
            # Stop listener
            return False

    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
# Collect events until released


if __name__ == "__main__":
    pass
