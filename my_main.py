from my_game import My_game

game = My_game()

game.start()
while game.running:
    game.run()
game.quit()