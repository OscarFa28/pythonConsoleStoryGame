class Player:
    # Constructor de la clase Player que se llama al instanciar un nuevo objeto Player.
    def __init__(self, name):
        # Inicialización de los atributos del jugador con valores predeterminados.
        self.playerName = name
        self.difficulty = 0
        self.intelligence = 0
        self.strong = 0
        self.health = 100
        self.social = 0
        self.country = ""
        self.difficultyType = ""
        
    # Método para establecer la dificultad inicial del jugador.
    def set_start_difficulty(self, difficulty):
        self.difficulty = difficulty
    
    # Método para establecer el país inicial del jugador.
    def set_start_country(self, country):
        self.country = country
    
    # Método para establecer el tipo de dificultad del jugador.
    def set_difficultyType(self, difficultyType):
        self.difficultyType = difficultyType

    
