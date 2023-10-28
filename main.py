import pygame

def main():
    pygame.init()

    pygame.display.set_caption("Pong")
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    running = True

    # ball
    ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    ball_vel = pygame.Vector2(50, 50)
    # paddle
    paddle_L_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2 - 50)
    paddle_R_pos = pygame.Vector2((screen.get_width() / 4)*3, screen.get_height() / 2 - 50)

    while running:
        #polling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # fill the screen with blue
        screen.fill((0, 0, 255))
        
        # draw items on the screen
        pygame.draw.circle(screen, "red", ball_pos, 20)
        pygame.draw.rect(screen, "white", pygame.Rect(paddle_L_pos.x, paddle_L_pos.y, 20, 100))
        pygame.draw.rect(screen, "white", pygame.Rect(paddle_R_pos.x, paddle_R_pos.y, 20, 100))


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

         # update ball position
        ball_pos += ball_vel * dt

        # check for collision with top and bottom walls
        if ball_pos.y < 20 or ball_pos.y > screen.get_height() - 20:
            ball_vel.y *= -1
        
        # check for collision with paddles
        if (ball_pos.x < paddle_L_pos.x + 20 and ball_pos.x > paddle_L_pos.x -20) and ball_pos.y > paddle_L_pos.y and ball_pos.y < paddle_L_pos.y + 100:
            ball_vel.x *= -1
        if (ball_pos.x < paddle_R_pos.x + 20 and ball_pos.x > paddle_R_pos.x -20) and ball_pos.y > paddle_R_pos.y and ball_pos.y < paddle_R_pos.y + 100:
            ball_vel.x *= -1

        # update paddle position
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_L_pos.y -= 200 * dt
        if keys[pygame.K_s]:
            paddle_L_pos.y += 200 * dt
        if keys[pygame.K_UP]:
            paddle_R_pos.y -= 200 * dt
        if keys[pygame.K_DOWN]:
            paddle_R_pos.y += 200 * dt

    pygame.quit()




# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()