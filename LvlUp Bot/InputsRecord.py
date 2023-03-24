import threading
import mouse
import keyboard

from mouse import ButtonEvent
from mouse import MoveEvent
from mouse import WheelEvent

from keyboard import KeyboardEvent
from Movement import *
import time

import json
import sys


def record(file='record.txt'):
    f = open(file, 'w+')
    mouse_events = []
    keyboard_events = []
    keyboard.start_recording()
    starttime = time.time()
    mouse.hook(mouse_events.append)
    keyboard.wait('esc')
    keyboard_events = keyboard.stop_recording()
    mouse.unhook(mouse_events.append)
    # first line = start of recording
    # mouse events = second line
    # keyboard events = every remaining line = 1 event
    print(starttime, file=f)
    print(mouse_events, file=f)
    for kevent in range(0, len(keyboard_events)):
        print(keyboard_events[kevent].to_json(), file=f)
    f.close()


def play(file, speed=0.5):
    f = open(file, 'r')
    # per definition the first line is mouse events and the rest is keyboard events
    lines = f.readlines()
    f.close()
    # mouse_events = eval(lines[1])
    keyboard_events = []
    for index in range(2, len(lines)):
        keyboard_events.append(
            keyboard.KeyboardEvent(**json.loads(lines[index])))

    starttime = float(lines[0])
    keyboard_time_interval = keyboard_events[0].time - starttime
    keyboard_time_interval /= speed
    # mouse_time_interval = mouse_events[0].time - starttime
    # mouse_time_interval /= speed
    print(keyboard_time_interval)
    # print(mouse_time_interval)
    # Keyboard threadings:
    k_thread = threading.Thread(target=lambda: time.sleep(
        keyboard_time_interval) == keyboard.play(keyboard_events, speed_factor=speed))
    # Mouse threadings:
    # m_thread = threading.Thread(target = lambda : time.sleep(mouse_time_interval) == mouse.play(mouse_events, speed_factor=speed))
    # start threads
    # m_thread.start()
    k_thread.start()
    # waiting for both threadings to be completed
    k_thread.join()
    # m_thread.join()


if __name__ == '__main__':
    focus_window("PROClient")
    # record()
    play("record.txt")
