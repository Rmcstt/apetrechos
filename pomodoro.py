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
    play_sound("assets/8d82b5_MK_vs_DCU_Round_One_Sound_Effect.mp3")
    for cycle in range(1, cycles + 1):  # +1 to include the last cycle
        for remaining_minutes in range(work_time, -1, -1):
            for remaining_seconds in range(59, -1, -1):
                clear_screen()
                print("Pomodoro Timer\n")
                print(f"Round: {cycle}/{cycles}")
                print(f"Work Timer: " + format_time(remaining_minutes, remaining_seconds))
                time.sleep(1)

        play_sound("assets/8d82b5_MK_vs_DCU_Finish_Him_Sound_Effect.mp3")

        for remaining_minutes in range(break_time, -1, -1):
            for remaining_seconds in range(59, -1, -1):
                clear_screen()
                print("Pomodoro Timer\n")
                print(f"Round: {cycle}/{cycles}")
                print("Break Timer: " + format_time(remaining_minutes, remaining_seconds))
                time.sleep(1)
        if cycle  == 1:
            play_sound("assets/8d82b5_MK_vs_DCU_Round_Two_Sound_Effect.mp3")
        elif cycle == 2:
            play_sound("assets/8d82b5_Mortal_Kombat_3_Round_Three_Sound_Effect.mp3")
        else:
            play_sound("assets/8d82b5_MK_vs_DCU_Final_Round_Sound_Effect.mp3")


if __name__ == "__main__":
    work_minutes = int(sys.argv[1])
    break_minutes = int(sys.argv[2])
    pomodoro_cycles = 4

    pomodoro_timer(work_minutes, break_minutes, pomodoro_cycles)
