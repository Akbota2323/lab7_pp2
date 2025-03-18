import pygame
import os


pygame.mixer.init()
pygame.font.init()


music_folder = 'C:/Users/abylk/Desktop'


music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
current_track_index = 0

def load_track(index):
    track_path = os.path.join(music_folder, music_files[index])
    pygame.mixer.music.load(track_path)
    pygame.mixer.music.play()

def play_music():
    if not pygame.mixer.music.get_busy():
        load_track(current_track_index)

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    load_track(current_track_index)

def prev_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    load_track(current_track_index)

# Основной цикл
def main():
    global current_track_index
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Music player')
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    play_music()
                elif event.key == pygame.K_s:
                    stop_music()
                elif event.key == pygame.K_n:
                    next_track()
                elif event.key == pygame.K_b:
                    prev_track()

        screen.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
