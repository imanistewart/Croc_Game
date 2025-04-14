import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lego Click Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
START_MENU_BG = (225, 239, 255)  # Light blue for start menu

# Fonts
font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 40)

# Base path for assets
ASSETS_PATH = "assets/"

# Load sounds
ding_sound = pygame.mixer.Sound(os.path.join(ASSETS_PATH, "ding.wav"))

# Load final images per step
final_images = [pygame.image.load(os.path.join(ASSETS_PATH, "final_image.png")).convert_alpha()] + \
               [pygame.image.load(os.path.join(ASSETS_PATH, f"final_image_{i}.png")).convert_alpha() for i in range(2, 22)]
final_assembled = pygame.image.load(os.path.join(ASSETS_PATH, "assembled_head_body_tail.png")).convert_alpha()
midpoint_body = pygame.image.load(os.path.join(ASSETS_PATH, "top_down_body.png")).convert_alpha()
midpoint_head_body = pygame.image.load(os.path.join(ASSETS_PATH, "assembled_head_body.png")).convert_alpha()

# Step pieces
steps = [
    [   # Step 1
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "yellowplate_2x3.png")).convert_alpha(), "pos": (100, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x6.png")).convert_alpha(), "pos": (300, 100), "clicks_required": 2, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x1.png")).convert_alpha(), "pos": (500, 100), "clicks_required": 2, "clicks": 0}
    ],
    [   # Step 2
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x4_modified.png")).convert_alpha(), "pos": (300, 100), "clicks_required": 2, "clicks": 0}
    ],
    [   # Step 3
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_2x4.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenbrick_1x1_stud.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 1, "clicks": 0}
    ],
    [   # Step 4
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "yellowplate_2x4.png")).convert_alpha(), "pos": (300, 100), "clicks_required": 1, "clicks": 0}
    ],
    [   # Step 5
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_2x2_winged.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "whitejagged.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 2, "clicks": 0}
    ],
    [   # Step 6
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x2.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greentile_1x2.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 1, "clicks": 0}
    ],
    [   # Step 7
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x4_modified.png")).convert_alpha(), "pos": (300, 100), "clicks_required": 2, "clicks": 0}
    ],
    [   # Step 8
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenslope_1x2.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 2, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_2x2.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 1, "clicks": 0}
    ],
    [   # Step 9
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x4.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 2, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x2_horizontalclip.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 1, "clicks": 0}
    ],
    [   # Step 10
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenlshapeplate.png")).convert_alpha(), "pos": (300, 100), "clicks_required": 2, "clicks": 0}
    ],
    [   # Step 11
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_2x2.png")).convert_alpha(), "pos": (300, 100), "clicks_required": 2, "clicks": 0}
    ],
    [   # Step 12
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x2_modified.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 4, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenslope_1x1.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 8, "clicks": 0}
    ],
    [   # Step 13
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "whiteplate_2x3.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "whiteplate_1x2_modified.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 2, "clicks": 0}
    ],
    [   # Step 14
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_2x4.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenslope_1x1.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 2, "clicks": 0}
    ],
    [   # Step 15
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenbrick_1x1_stud.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 2, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "whiteround_1x1.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 2, "clicks": 0}
    ],
    [   # Step 16
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenslope_wide.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "redplate_1x2.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 1, "clicks": 0}
    ],
    [   # Step 17
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_2x3.png")).convert_alpha(), "pos": (100, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x2.png")).convert_alpha(), "pos": (300, 100), "clicks_required": 2, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_2x1_stud.png")).convert_alpha(), "pos": (500, 100), "clicks_required": 1, "clicks": 0}
    ],
    [   # Step 18
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_2x3.png")).convert_alpha(), "pos": (100, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_2x1_stud.png")).convert_alpha(), "pos": (300, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x2.png")).convert_alpha(), "pos": (500, 100), "clicks_required": 1, "clicks": 0}
    ],
    [   # Step 19
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_2x3.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 1, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x3.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 1, "clicks": 0}
    ],
    [   # Step 20
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x3.png")).convert_alpha(), "pos": (300, 100), "clicks_required": 1, "clicks": 0}
    ],
    [   # Step 21
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenslope_1x1.png")).convert_alpha(), "pos": (200, 100), "clicks_required": 2, "clicks": 0},
        {"image": pygame.image.load(os.path.join(ASSETS_PATH, "greenplate_1x1.png")).convert_alpha(), "pos": (400, 100), "clicks_required": 1, "clicks": 0}
    ]
]

# Game state
current_step = 0
pieces = steps[current_step]
current_final = final_images[current_step]
previous_final = None

# Fade/step state
fading = False
fade_alpha = 0
final_displayed = False
waiting_for_click = False
step_completed = False

# Menu & screen states
show_start_menu = True
show_midpoint_1 = False
show_midpoint_2 = False
show_final_image = False

# Clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Fill screen based on current state
    if show_start_menu:
        screen.fill(START_MENU_BG)  # Use custom start menu color
    else:
        screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if show_start_menu:
                show_start_menu = False

            elif show_midpoint_1:
                show_midpoint_1 = False
                current_step = 12  # Step 13
                pieces = steps[current_step]
                current_final = final_images[current_step]
                previous_final = None  # No previous image on step 13
                final_displayed = False
                fading = False
                step_completed = False
                waiting_for_click = False

            elif show_midpoint_2:
                show_midpoint_2 = False
                current_step = 16  # Step 17
                pieces = steps[current_step]
                current_final = final_images[current_step]
                previous_final = None  # No previous image on step 17
                final_displayed = False
                fading = False
                step_completed = False
                waiting_for_click = False

            elif show_final_image:
                show_final_image = False
                running = False  # End game

            elif final_displayed and waiting_for_click:
                waiting_for_click = False
                step_completed = False
                current_step += 1

                # Handle special cases after step 12, 16, and 21
                if current_step == 12:
                    show_midpoint_1 = True
                elif current_step == 16:
                    show_midpoint_2 = True
                elif current_step >= len(steps):
                    show_final_image = True
                else:
                    pieces = steps[current_step]
                    current_final = final_images[current_step]
                    final_displayed = False
                    fading = False
            elif not fading and not final_displayed:
                mouse_pos = pygame.mouse.get_pos()
                for piece in pieces:
                    if piece["clicks"] < piece["clicks_required"]:
                        rect = piece["image"].get_rect(topleft=piece["pos"])
                        if rect.collidepoint(mouse_pos):
                            piece["clicks"] += 1
                            ding_sound.play()

    # ========== Screens ==========
    if show_start_menu:
        # Title
        title = big_font.render("Crocodile Lego Builder", True, BLACK)
        screen.blit(title, ((WIDTH - title.get_width()) // 2, 50))

        # Final assembled image
        assembled_scaled = pygame.transform.scale(final_assembled, (final_assembled.get_width() // 2, final_assembled.get_height() // 2))
        assembled_pos = ((WIDTH - assembled_scaled.get_width()) // 2, (HEIGHT - assembled_scaled.get_height()) // 2 - 50)
        screen.blit(assembled_scaled, assembled_pos)

        # Start message
        start_msg = font.render("Click anywhere to start.", True, BLACK)
        screen.blit(start_msg, ((WIDTH - start_msg.get_width()) // 2, HEIGHT // 2 + 100))

        # Credits
        credit1 = font.render("Model and instructions by Alex Evstyugov", True, BLACK)
        credit2 = font.render("Python game built by Imani Stewart", True, BLACK)
        screen.blit(credit1, ((WIDTH - credit1.get_width()) // 2, HEIGHT - 60))
        screen.blit(credit2, ((WIDTH - credit2.get_width()) // 2, HEIGHT - 30))

    elif show_midpoint_1:
        # Show top_down_body.png after step 12 (body completed) at full size
        midpoint_pos = ((WIDTH - midpoint_body.get_width()) // 2, (HEIGHT - midpoint_body.get_height()) // 2)
        screen.blit(midpoint_body, midpoint_pos)
        msg = big_font.render("Body Complete!", True, BLACK)
        click_continue = font.render("Click to start building the head.", True, BLACK)
        screen.blit(msg, ((WIDTH - msg.get_width()) // 2, 30))
        screen.blit(click_continue, ((WIDTH - click_continue.get_width()) // 2, HEIGHT - 50))

    elif show_midpoint_2:
        # Show assembled_head_body.png after step 16 (head and body connected) at full size
        midpoint_pos = ((WIDTH - midpoint_head_body.get_width()) // 2, (HEIGHT - midpoint_head_body.get_height()) // 2)
        screen.blit(midpoint_head_body, midpoint_pos)
        msg = big_font.render("Head and Body Connected!", True, BLACK)
        click_continue = font.render("Click to start building the tail.", True, BLACK)
        screen.blit(msg, ((WIDTH - msg.get_width()) // 2, 30))
        screen.blit(click_continue, ((WIDTH - click_continue.get_width()) // 2, HEIGHT - 50))

    elif show_final_image:
        # Show assembled_head_body_tail.png after step 21 at full size
        final_pos = ((WIDTH - final_assembled.get_width()) // 2, (HEIGHT - final_assembled.get_height()) // 2)
        screen.blit(final_assembled, final_pos)
        congrats = big_font.render("You finished building the crocodile!", True, BLACK)
        screen.blit(congrats, ((WIDTH - congrats.get_width()) // 2, 30))
        exit_text = font.render("Click to exit.", True, BLACK)
        screen.blit(exit_text, ((WIDTH - exit_text.get_width()) // 2, HEIGHT - 50))

    else:
        # Step label
        step_text = big_font.render(f"Step {current_step + 1}", True, BLACK)
        screen.blit(step_text, (20, 20))

        # Draw pieces and click counters
        for piece in pieces:
            screen.blit(piece["image"], piece["pos"])
            remaining = piece["clicks_required"] - piece["clicks"]
            if remaining > 0:
                count_text = font.render(f"x{remaining}", True, BLACK)
                x = piece["pos"][0] + piece["image"].get_width() // 2 - count_text.get_width() // 2
                y = piece["pos"][1] + piece["image"].get_height() + 5
                screen.blit(count_text, (x, y))

        # Draw previous final image (except for steps 13 and 17)
        if previous_final is not None and not fading and not final_displayed:
            fw, fh = int(previous_final.get_width() * 0.8), int(previous_final.get_height() * 0.8)
            prev_scaled = pygame.transform.scale(previous_final, (fw, fh))
            screen.blit(prev_scaled, ((WIDTH - fw) // 2, (HEIGHT - fh) // 2))

        # Fade current final image
        if fading:
            fw, fh = int(current_final.get_width() * 0.8), int(current_final.get_height() * 0.8)
            final_scaled = pygame.transform.scale(current_final, (fw, fh))
            faded_image = final_scaled.copy()
            faded_image.set_alpha(fade_alpha)
            screen.blit(faded_image, ((WIDTH - fw) // 2, (HEIGHT - fh) // 2))

            fade_alpha += 5
            if fade_alpha >= 255:
                fade_alpha = 255
                fading = False
                final_displayed = True
                waiting_for_click = True

        # Display final image (after fade)
        if final_displayed:
            fw, fh = int(current_final.get_width() * 0.8), int(current_final.get_height() * 0.8)
            final_scaled = pygame.transform.scale(current_final, (fw, fh))
            screen.blit(final_scaled, ((WIDTH - fw) // 2, (HEIGHT - fh) // 2))

        # Trigger fade
        if not fading and not final_displayed and not step_completed:
            if all(p["clicks"] == p["clicks_required"] for p in pieces):
                fading = True
                fade_alpha = 0
                step_completed = True
                previous_final = current_final

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
