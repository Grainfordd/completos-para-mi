class GameStats:

    def __init__(self, settings):

        self.settings = settings
        
        # Empezar el juego con las vidas default
        self.reset_stats()
        
        # Setear el estado del juego
        self.game_active = True 

        self.score = 0


    def reset_stats(self):
        self.lifes_left = self.settings.lifes_limit

    
