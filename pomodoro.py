import time
import os
import pygame
import sys


# this program need a mp3 file attached in assets folder

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(minutes, seconds):
    return "{:02d}:{:02d}".format(minutes, seconds)

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def pomodoro_timer(work_time, break_time, cycles):
    sound_file = "assets/digital-alarm-3-151917.mp3"  # Replace with the actual path to your sound file
    
    for _ in range(cycles):
        for remaining_minutes in range(work_time, -1, -1):
            for remaining_seconds in range(59, -1, -1):
                clear_screen()
                print("Pomodoro Timer\n")
                print("Work Timer: " + format_time(remaining_minutes, remaining_seconds))
                time.sleep(1)
        
        play_sound(sound_file)
        
        for remaining_minutes in range(break_time, -1, -1):
            for remaining_seconds in range(59, -1, -1):
                clear_screen()
                print("Pomodoro Timer\n")
                print("Break Timer: " + format_time(remaining_minutes, remaining_seconds))
                time.sleep(1)
        
        play_sound(sound_file)

if __name__ == "__main__":
    work_minutes = int(sys.argv[1])
    break_minutes = int(sys.argv[2])
    pomodoro_cycles = int(sys.argv[3])

    pomodoro_timer(work_minutes, break_minutes, pomodoro_cycles)
