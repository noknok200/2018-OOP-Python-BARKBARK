with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()