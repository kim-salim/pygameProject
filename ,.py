def mainmenu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(mainmenu_background, (0, 0))
        Button(mainmenu_start, 405, 250, 150, 80, mainmenu_start_click, 380, 235, game)
        Button(mainmenu_explain, 405, 350, 150, 80, mainmenu_explain_click, 380, 335, explain)
        Button(mainmenu_finish, 405, 450, 150, 80, mainmenu_finish_click, 380, 435, finishgame)

        pygame.display.update()
        clock.tick(15)