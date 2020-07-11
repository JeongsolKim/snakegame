import pygame
from snake import Snake
from mytoken import MyTokens

# Initialize
pygame.init()
pygame.font.init()

# Display
size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake Game')

# Frame
clock = pygame.time.Clock()
Frame = 30 # 30 frames per second

# game parameters / create token and snake
init_length = 5
width = 10
end = False
done = False
token_num = 5
tokens = MyTokens(size[0], size[1], width, token_num)
snake = Snake((size[0]/2), (size[1]/2), 1, 'N', init_length, width)

# Font create
score_font = pygame.font.SysFont('Comic Sans MS', 20)
score_surface = score_font.render('Score: {}'.format(snake.score), False, (255,255,255))
end_font = pygame.font.SysFont('Comic Sans MS', 50)
end_surface = end_font.render('GAME OVER', False, (255,255,255))
ask_font = pygame.font.SysFont('Comic Sans MS', 20)
ask_surface = ask_font.render('Restart (r) or Quit (esc)', False, (255,255,255))

# Entire game window
while not end:
    # One game
    while not done:
        clock.tick(Frame)
        # Get inputs from user.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                # buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]

                if event.key == pygame.K_ESCAPE:
                    done = True
                elif pressed[pygame.K_UP]:
                    snake.entire_move('N')
                elif pressed[pygame.K_DOWN]:
                    snake.entire_move('S')
                elif pressed[pygame.K_LEFT]:
                    snake.entire_move('W')
                elif pressed[pygame.K_RIGHT]:
                    snake.entire_move('E')

            elif event.type == pygame.QUIT:
                done = True

        # refresh the screen
        screen.fill((0,0,0))

        # snake auto move
        snake.entire_move(snake.parts[0].orientation)

        # draw the snake
        for part in snake.parts:
            pygame.draw.rect(screen, part.color, [part.posi_x, part.posi_y, part.width, part.width], 2)

        # draw the tokens
        for token in tokens.token_posi:
            pygame.draw.rect(screen, (0,255,0),[token[0], token[1], snake.parts[0].width, snake.parts[0].width])

        screen.blit(score_surface, (5/400*size[0], 5/300*size[1]))
        pygame.display.update()

        # Crash to the wall
        if snake.parts[0].posi_x<0 or snake.parts[0].posi_x>size[0]\
            or snake.parts[0].posi_y<0 or snake.parts[0].posi_y>size[1]:
            done = True
        # Crash to itself
        if snake.is_self_crash():
            done = True

        # Eat any token?
        if [snake.parts[0].posi_x, snake.parts[0].posi_y] in tokens.token_posi:
            # Snake update
            snake.add_parts()
            # Token update
            tokens.token_posi.remove([snake.parts[0].posi_x, snake.parts[0].posi_y])
            tokens.add_new_token()
            # Score text update
            score_surface = score_font.render('Score: {}'.format(snake.score), False, (255, 255, 255))

    # Game Over. Restart or Quit?
    screen.blit(end_surface, (size[0]//3, size[1]//3))
    screen.blit(ask_surface, (size[0]//2.7, size[1]//1.8))
    pygame.display.update()
    for event in pygame.event.get():
        if event.key == pygame.K_ESCAPE:
            end = True
        elif event.key == pygame.K_r:
            done = False
            snake = Snake((size[0] / 2), (size[1] / 2), 1, 'N', init_length, width)
            tokens = MyTokens(size[0], size[1], width, token_num)
            score_surface = score_font.render('Score: {}'.format(snake.score), False, (255, 255, 255))

pygame.quit()

