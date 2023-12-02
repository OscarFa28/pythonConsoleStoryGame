from player import Player  

import random
import time
import sys


# Definición de la clase Actions
class Actions:
    # Constructor de la clase que recibe el nombre del jugador
    def __init__(self, name):
        self.pl = Player(name)  
        self.win_counter = 0
    # Inicializa un objeto Player con el nombre del jugador
    # Métodos para obtener información del jugador
    def return_player_name(self):
        return self.pl.playerName
    
    def return_difficulty(self):
        return self.pl.difficulty
    
    def return_intelligence(self):
        return self.pl.intelligence
    
    def return_strong(self):
        return self.pl.strong
    
    def return_health(self):
        return self.pl.health
    
    def return_social(self):
        return self.pl.social
    
    def return_country(self):
        return self.pl.country
    
    def return_difficulty_type(self):
        return self.pl.difficultyType
    
    
    def set_country(self):
        # Listas de países para diferentes niveles de dificultad
        easy = ["USA", "Germany", "Japan", "Canada", "Australia", "Switzerland", "Sweden"]
        normal = ["Spain", "South Korea", "France", "Italy", "Netherlands", "Belgium"]
        hard = ["Mexico", "Argentina", "Brasil", "Colombia", "El Salvador", "Russia", "India", "China"]
        veryHard = ["Peru", "Honduras", "Guatemala", "Ecuador", "Bolivia", "Vietnam", "Thailand"]
        impossible = ["Uganda", "Afghanistan", "Syria", "Yemen", "Somalia", "North Korea", "South Sudan"]
        
        # Genera un valor de dificultad aleatorio
        difficulty = random.randint(1,100)
        
        # Asigna un país dependiendo del nivel de dificultad
        if difficulty > 5 and difficulty <= 25:
            difficultyType = "Normal"
            country = random.choice(normal)
        elif difficulty > 25 and difficulty <= 65:
            difficultyType = "Hard"
            country = random.choice(hard)
        elif difficulty > 65 and difficulty <= 95:
            difficultyType = "Very Hard"
            country = random.choice(veryHard)
        elif difficulty > 95 and difficulty <= 100:
            difficultyType = "Impossible"
            country = random.choice(impossible)
        else:
            difficultyType ="Easy"
            country = random.choice(easy)
         
        self.pl.set_start_difficulty(difficulty)    
        self.pl.set_start_country(country)
        self.pl.set_difficultyType(difficultyType)

    
    # Método para mostrar el estado actual del jugador
    def show_status(self):
        if self.pl.difficulty > 5 and self.pl.difficulty <= 25:
            difficultyType = "Normal"
            
        elif self.pl.difficulty > 25 and self.pl.difficulty <= 65:
            difficultyType = "Hard"
            
        elif self.pl.difficulty > 65 and self.pl.difficulty <= 95:
            difficultyType = "Very Hard"
            
        elif self.pl.difficulty > 95 and self.pl.difficulty <= 100:
            difficultyType = "Impossible"
            
        else:
            difficultyType ="Easy"
        # Establece el tipo de dificultad en el objeto Player y muestra el estado actual

        self.pl.set_difficultyType(difficultyType)    
        print("--Actual status--")
        print(f"Intelligence: {self.pl.intelligence}")
        print(f"Strong: {self.pl.strong}")
        print(f"Health: {self.pl.health}")
        print(f"Social: {self.pl.social}")
        print(f"Difficulty: {self.pl.difficultyType}")

    def give_questions(self,age,diff):
        child_questions = {
            1: [
                [  # Questions -0
                    "¿Comer el juguete?",
                    "¿Comer el polvo del suelo?",
                    "¿Comer el dulce del suelo?"
                ],
                [  # Option one -1
                    "si", "claro", "comer"
                ],
                [  # Option two -2
                    "no", "por supuesto que no","No"
                ],
                [  # Option three -3
                    "guardar", "jugar"
                ],
                [  # Option one data -4
                    5,  # difficulty
                    3,  # intelligence
                    3,  # strong
                    -20,  # health
                    0,  # social
                ],
                [  # Option two data -5
                    -1,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    0,  # health
                    0,  # social
                ],
                [  # Option three data -6
                    0,  # difficulty
                    3,  # intelligence
                    1,  # strong
                    -5,  # health
                    1,  # social
                ]
                ],
            
            2: [
                [  # Questions -0
                    "¿Jugar con bloques?",
                    "¿Leer un libro?",
                    "¿Ver caricaturas?"
                ],
                [  # Option one -1
                    "Si",
                    "Claro",
                    "Jugar"
                ],
                [  # Option two -2
                    "No",
                    "No quiero",
                    "Descansar"
                ],
                [  # Option three -3
                    "Despues",
                    "Otra vez",
                    "Dormir"
                ],
                [  # Option one data -4
                    -1,  # difficulty
                    2,  # intelligence
                    1,  # strong
                    0,  # health
                    1,  # social skills
                ],
                [  # Option two data -5
                    2,  # difficulty
                    -1,  # intelligence
                    1,  # strong
                    -2,  # health
                    1,  # social skills
                ],
                [  # Option three data -6
                    1,  # difficulty
                    1,  # intelligence
                    1,  # strong
                    0,  # health
                    1,  # social skills
                ]
                ],
            
            3: [
                [  
                    "¿Te gusta el fútbol?",
                    "¿Te gusta el fútbol?",
                    "¿Te gusta el boxeo?"
                ],
                [  
                    "SI",
                    "Claro",
                    "Por supuesto"
                ],
                [  
                    "No",
                    "No quiero",
                    "Cualquier"
                ],
                [  
                    "Otro deporte",
                    "Después",
                    "Quizas"
                ],
                [  # Option one data -4
                    -5,  # difficulty
                    1,  # intelligence
                    5,  # strong
                    5,  # health
                    5,  # social skills
                ],
                [  # Option two data -5
                    3,  # difficulty
                    3,  # intelligence
                    -2,  # strong
                    -2,  # health
                    0,  # social skills
                ],
                [  # Option three data -6
                    -5,  # difficulty
                    1,  # intelligence
                    5,  # strong
                    5,  # health
                    5,  # social skills
                ]
                ],
            
            4: [
                [  # Questions -0
                    "¿Hacer amigos?",
                    "¿Hablar con los niños?",
                    "¿Prestar tus juguetes?"
                ],
                [  # Option one -1
                    "Si",
                    "Claro",
                    "Hacer",
                    "Hablar",
                    "Prestar"
                ],
                [  # Option two -2
                    "No",
                    "No quiero",
                    "De ninguna forma"
                ],
                [  # Option three -3
                    "Luego",
                    "quizas"
                ],
                [  # Option one data -4
                    -5,  # difficulty
                    5,  # intelligence
                    1,  # strong
                    2,  # health
                    10,  # social skills
                ],
                [  # Option two data -5
                    3,  # difficulty
                    3,  # intelligence
                    -2,  # strong
                    -2,  # health
                    0,  # social skills
                ],
                [  # Option three data -6
                    -4,  # difficulty
                    4,  # intelligence
                    1,  # strong
                    2,  # health
                    7,  # social skills
                ]
                ],
            
            5: [
                [  # Questions -0
                    "¿Usar cinturón de seguridad?",
                    "¿Sentarse en el asiento de los niños?"
                ],
                [  # Option one -1
                    "Si",
                    "Claro",
                    "Usar",
                    "Sentarse"
                ],
                [  # Option two -2
                    "No",
                    "No quiero",
                    "Cualquier"
                ],
                [  # Option three -3
                    "Mas tarde",
                    "Despues",
                    "Quizás"
                ],
                [  # Option one data -4
                    10,  # difficulty
                    10,  # intelligence
                    -3,  # strong
                    -15,  # health
                    0,   # social skills
                ],
                [  # Option two data -5
                    20,  # difficulty
                    5,  # intelligence
                    -5,  # strong
                    -95,  # health
                    0,   # social skills
                ],
                [  # Option three data -6
                    15,  # difficulty
                    7,  # intelligence
                    -4,  # strong
                    -20,  # health
                    2,   # social skills
                ]
                ],
        }
        #
        easy_questions = {
            9: [
                [  # Questions -0
                    "¿Decirle a mis padres?"
                ],
                [  # Option one -1
                    "Si",
                    "Decir",
                    "Mostrar",
                    "Seguro"
                ],
                [  # Option two -2
                    "No",
                    "No quiero",
                    "Silencio"
                ],
                [  # Option three -3
                    "Mentir",
                    "Después",
                    "Quizás"
                ],
                [  # Option one data -4
                    10,  # difficulty
                    -3,  # intelligence
                    5,  # strong
                    -2,  # health
                    -3,   # social skills
                ],
                [  # Option two data -5
                    5,  # difficulty
                    5,  # intelligence
                    2,  # strong
                    0,  # health
                    5,   # social skills
                ],
                [  # Option three data -6
                    5,  # difficulty
                    7,  # intelligence
                    5  ,  # strong
                    0,  # health
                    7,   # social skills
                ]
                ],
            13: [
                [  # Questions -0
                    "¿Le preguntaras si quiere hacer equipo?"
                ],
                [  # Option one -1
                    "Si",
                    "claro",
                    "Por supuesto",
                    "Hacer"
                ],
                [  # Option two -2
                    "No",
                    "No quiero",
                    "Nah"
                    
                ],
                [  # Option three -3
                    "Quizas",
                    "Luego",
                    "Otro dia"
                ],
                [  # Option one data -4
                    1,  # difficulty
                    2,  # intelligence
                    2,  # strong
                    0,  # health
                    7,   # social skills
                ],
                [  # Option two data -5
                    2,  # difficulty
                    2,  # intelligence
                    -2,  # strong
                    0,  # health
                    -1,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    4,  # intelligence
                    2,  # strong
                    0,  # health
                    0,   # social skills
                ]
                ],
            17: [
                [  # Questions -0
                    "¿Qué haras?"
                ],
                [  # Option one -1
                    "Hablar",
                    "Golpearlo",
                    "Pegarle",
                ],
                [  # Option two -2
                    "Nada",
                    "Luego",
                ],
                [  # Option three -3
                    "Hablar",
                    "Luego",
                    "Ahora no",
                    "Algo",
                ],
                [  # Option one data -4
                    6,  # difficulty
                    -2,  # intelligence
                    4,  # strong
                    -2,  # health
                    -2,   # social skills
                ],
                [  # Option two data -5
                    5,  # difficulty
                    0,  # intelligence
                    -1,  # strong
                    0,  # health
                    -10,   # social skills
                ],
                [  # Option three data -6
                    4,  # difficulty
                    6,  # intelligence
                    -3,  # strong
                    -5,  # health
                    1,   # social skills
                ]
                ],
            21: [
                [  # Questions -0
                    "¿Cuál escogeras?"
                ],
                [  # Option one -1
                    "reclutar",
                    "reclutar personal",
                    "personal",
                ],
                [  # Option two -2
                    "paz diplomatica",
                    "paz",
                    "diplomatica"
                ],
                [  # Option three -3
                    "combate",
                    "ir",
                    "ir al combate",
                    "combatir"
                ],
                [  # Option one data -4
                    10,  # difficulty
                    10,  # intelligence
                    10,  # strong
                    12,  # health
                    15,   # social skills
                ],
                [  # Option two data -5
                    -20,  # difficulty
                    35,  # intelligence
                    -40,  # strong
                    15,  # health
                    40,   # social skills
                ],
                [  # Option three data -6
                    40,  # difficulty
                    -20,  # intelligence
                    50,  # strong
                    30,  # health
                    -20,   # social skills
                ]
                ],
            30: [
                [  # Questions -0
                    "¿Qué haras?"
                ],
                [  # Option one -1
                    "Aceptar",
                    "si",
                    "Socio",
                    "Seguro"
                ],
                [  # Option two -2
                    "No",
                    "No quiero",
                    "Rechazar"
                ],
                [  # Option three -3
                    "Empleado",
                    "Quizás"
                ],
                [  # Option one data -4
                    5,  # difficulty
                    3,  # intelligence
                    0,  # strong
                    0,  # health
                    20,   # social skills
                ],
                [  # Option two data -5
                    -5,  # difficulty
                    -5,  # intelligence
                    0,  # strong
                    5,  # health
                    -20,   # social skills
                ],
                [  # Option three data -6
                    2,  # difficulty
                    5,  # intelligence
                    2  ,  # strong
                    0,  # health
                    -10,   # social skills
                ]
                ],
            
            34: [
                [  # Questions -0
                    "¿Qué haras?"
                ],
                [  # Option one -1
                    "Pareja",
                    "Dedicar tiempo a la pareja",
                    "Esposa",
                    "Novia"
                ],
                [  # Option two -2
                    "Hija",
                    "Dedicar mas tiempo a la hija",
                    "Rechazar",
                    "Hijo",
                    "Dedicar mas tiempo a la hijo"
                ],
                [  # Option three -3
                    "Ambas",
                    "Las dos"
                ],
                [  # Option one data -4
                    0,  # difficulty
                    9,  # intelligence
                    -3,  # strong
                    0,  # health
                    -24,   # social skills
                ],
                [  # Option two data -5
                    -5,  # difficulty
                    -5,  # intelligence
                    0,  # strong
                    5,  # health
                    -20,   # social skills
                ],
                [  # Option three data -6
                    2,  # difficulty
                    5,  # intelligence
                    2  ,  # strong
                    0,  # health
                    -10,   # social skills
                ]
                ],
            39: [
                [  # Questions -0
                    "¿Qué estrategia te parece mejor?"
                ],
                [  # Option one -1
                    "ofensiva",
                    "Una estrategia ofensiva",
                    "Atacar",
                    "Atacamos",
                ],
                [  # Option two -2
                    "defensiva",
                    "tenemos que defender",
                    "Defender",
                    "Defendamos",
                ],
                [  # Option three -3
                    "La paz",
                    "Dialogo",
                    "Diplomatica",
                    "Diplomacia"
                ],
                [  # Option one data -4
                    20,  # difficulty
                    -30,  # intelligence
                    35,  # strong
                    0,  # health
                    20,   # social skills
                ],
                [  # Option two data -5
                    10,  # difficulty
                    -20,  # intelligence
                    -30,  # strong
                    0,  # health
                    0,   # social skills
                ],
                [  # Option three data -6
                    -30,  # difficulty
                    50,  # intelligence
                    -20  ,  # strong
                    0,  # health
                    10,   # social skills
                ]
                ],
            43: [
                [  # Questions -0
                   "¿Te unirás a un grupo de pacificadores para buscar una solución diplomática,liderarás una resistencia contra la opresión o te uniras al gobierno?"
                ],
                [  # Option one -1
                    "Pacificadores",
                    "Solucion Diplomatica",
                    "Diplomacia",
                    "Dialogo",
                ],
                [  # Option two -2
                    "Resistencia",
                    "Unirme a la resistencia",
                    "Contra la opresion",
                    "Fin al gobierno",
                ],
                [  # Option three -3
                    "Gobierno",
                    "Fin a la resistencia",
                    "Unirme al gobierno",
                    "contra la resistencia"
                ],
                [  # Option one data -4
                    0,  # difficulty
                    30,  # intelligence
                    -10,  # strong
                    5,  # health
                    20,   # social skills
                ],
                [  # Option two data -5
                    10,  # difficulty
                    -20,  # intelligence
                    -20,  # strong
                    -20,  # health
                    -25,   # social skills
                ],
                [  # Option three data -6 
                    10,  # difficulty
                    -20,  # intelligence
                    -20  ,  # strong
                    -20,  # health
                    -25,   # social skills
                ]
                ],
            47: [
                [  # Questions -0
                  "¿Aceptas el desafío y trabajas incansablemente por un mundo pacífico o prefieres una vida más tranquila con tu familia?"
                ],
                [  # Option one -1
                    "Desafio",
                    "Mundo",
                    "El mundo me necesita",
                ],
                [  # Option two -2
                    "Vida Tranquila",
                    "Familia",
                    "Prefiero a mi familia",
                    "Mi familia",
                    "vida"
                ],
                [  # Option three -3
                    "Ninguna",
                    "Suicidio",
                    "La vida no tiene sentido"
                ],
                [  # Option one data -4
                    20,  # difficulty
                    20,  # intelligence
                    20,  # strong
                    0,  # health
                    20,   # social skills
                ],
                [  # Option two data -5
                    -30,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    10,  # health
                    0,   # social skills
                ],
                [  # Option three data -6 
                    0,  # difficulty
                    0,  # intelligence
                    0  ,  # strong
                    -100,  # health
                    0,   # social skills
                ]
                ],
             60: [
                [  # Questions -0
                    "¿Lo tomaras?"
                ],
                [  # Option one -1
                    "Si",
                    "Claro",
                    "Por supuesto",
                    "Porque no"
                ],
                [  # Option two -2
                    "No",
                    "No puedo",
                    "Nah",
                    "Luego"
                ],
                [  # Option three -3
                    "Suicidio",
                    "Me quiero morir",
                ],
                [  # Option one data -4
                    0,  # difficulty
                    0,  # intelligence
                    -20,  # strong
                    20,  # health
                    30,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    -100,  # health
                    0,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    0,  # intelligence
                    0  ,  # strong
                    -100,  # health
                    0,   # social skills
                ]
               ],
            66: [
                [  # Questions -0
                    "¿Con quién bailaras?"
                ],
                [  # Option one -1
                    "Hija",
                    "Mi hija",
                    "Mi hija me llama"
                ],
                [  # Option two -2
                    "Mi esposa",
                    "Esposa",
                    "mi esposa me llama",
                ],
                [  # Option three -3
                    "No bailare",
                    "Me bailar",
                    "Ninguna"
                ],
                [  # Option one data -4
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    0,  # health
                    30,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    0,  # health
                    24,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    0,  # intelligence
                    0  ,  # strong
                    0,  # health
                    19,   # social skills
                ]
                ],
            72: [
                [  # Questions -0
                    "¿Con quién prefieres pasar el dolo?"
                ],
                [  # Option one -1
                    "Familia",
                    "Con mi familia",
                    "mi familia",
                    "Familiares"
                ],
                [  # Option two -2
                    "Amigos",
                    "con mis amigos",
                    "mis amigos",
                ],
                [  # Option three -3
                    "Ambos",
                    "los dos",
                ],
                [  # Option one data -4
                    0,  # difficulty
                    10,  # intelligence
                    10,  # strong
                    0,  # health
                    10,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    10,  # intelligence
                    10,  # strong
                    00,  # health
                    10,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    12,  # intelligence
                    12  ,  # strong
                    0,  # health
                    12,   # social skills
                ]
                ],
            78: [
                [  # Questions -0
                    "¿Lo gastaras en lujos?"
                ],
                [  # Option one -1
                    "Si",
                    "Por supuesto ",
                    "Claro"
                ],
                [  # Option two -2
                    "No",
                    "No",
                    "Neh",
                ],
                [  # Option three -3
                    "Mi hija",
                    "darcelo a mi hija",
                    "hija",

                ],
                [  # Option one data -4
                    0,  # difficulty
                    10,  # intelligence
                    0,  # strong
                    0,  # health
                    10,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    20,  # intelligence
                    0,  # strong
                    0,  # health
                    20,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    15,  # intelligence
                    0  ,  # strong
                    0,  # health
                    30,   # social skills
                ]
                ],
            80: [
                [  # Questions -0
                    ""
                ],
                [  # Option one -1
                    "Si",
                    "Claro",
                    "Por supuesto",
                    "vamos ",
                    "Voy"
                ],
                [  # Option two -2
                    "no",
                    "No",
                    "No quiero",
                ],
                [  # Option three -3
                    "listo",
                    "listosimo",
                ],
                [  # Option one data -4
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    -100,  # health
                    0,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    -100,  # health
                    0,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    0,  # intelligence
                    0  ,  # strong
                    -100,  # health
                    0,   # social skills
                ]
                ],
            
        }
        
        normal_questions = {
            9: [
                [  # Questions -0
                    "¿Golpear al niño de la escuela?"
                ],
                [  # Option one -1
                    "Si",
                    "Golpear",
                    "Usar",
                    "Seguro"
                ],
                [  # Option two -2
                    "No",
                    "No quiero",
                    "Cualquier"
                ],
                [  # Option three -3
                    "Ligeramente",
                    "Después",
                    "Quizás"
                ],
                [  # Option one data -4
                    10,  # difficulty
                    2,  # intelligence
                    15,  # strong
                    -2,  # health
                    5,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    5,  # intelligence
                    -1,  # strong
                    0,  # health
                    -1,   # social skills
                ],
                [  # Option three data -6
                    5,  # difficulty
                    2,  # intelligence
                    7,  # strong
                    -1,  # health
                    2,   # social skills
                ]
                ],
            13: [
                [  # Questions -0
                    "¿Lo usaras?"
                ],
                [  # Option one -1
                    "Si",
                    "claro",
                    "SI",
                    "Claro"
                ],
                [  # Option two -2
                    "No",
                    "No quiero",
                    
                ],
                [  # Option three -3
                    "Quizas",
                    
                ],
                [  # Option one data -4
                    -2,  # difficulty
                    1,  # intelligence
                    2,  # strong
                    0,  # health
                    2,   # social skills
                ],
                [  # Option two data -5
                    5,  # difficulty
                    3,  # intelligence
                    0,  # strong
                    0,  # health
                    3,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    4,  # intelligence
                    2,  # strong
                    0,  # health
                    0,   # social skills
                ]
                ],
            17: [
                [  # Questions -0
                    "¿A dondé iras?"
                ],
                [  # Option one -1
                    "Fiesta",
                    "Ir de fiesta",
                    "Salir",
                    "fiesta"
                ],
                [  # Option two -2
                    "Paque",
                    "Salir al paque",
                    
                ],
                [  # Option three -3
                    "Jugar",
                    "jugar",
                    "basquetbol",
                    "Basquetbol",
                    
                ],
                [  # Option one data -4
                    10,  # difficulty
                    -5,  # intelligence
                    -4,  # strong
                    -2,  # health
                    13,   # social skills
                ],
                [  # Option two data -5
                    5,  # difficulty
                    5,  # intelligence
                    5,  # strong
                    5,  # health
                    5,   # social skills
                ],
                [  # Option three data -6
                    9,  # difficulty
                    9,  # intelligence
                    9,  # strong
                    8,  # health
                    4,   # social skills
                ]
                ],
            21: [
                [  # Questions -0
                    "Podrias intentar salvarlo, ¿pero qué haras?"
                ],
                [  # Option one -1
                    "Si",
                    "Claro",
                    "Por supuesto",
                    "Salvarlo",
                    "Intentarlo"
                ],
                [  # Option two -2
                    "No escapar",
                    "NO",
                    "escapar",
                    
                ],
                [  # Option three -3
                    "Disparar",
                    "Cuprirlo",
                    "Correr",
                    
                ],
                [  # Option one data -4
                    20,  # difficulty
                    -10,  # intelligence
                    20,  # strong
                    -5,  # health
                    40,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    30,  # intelligence
                    0,  # strong
                    0,  # health
                    -20,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    -100,  # health
                    0,   # social skills
                ]
                ],
            30: [
                [  # Questions -0
                    "¿Qué haras?"
                ],
                [  # Option one -1
                    "Darle",
                    "Dinero",
                    "Nada",
                    "Irme",
                    "Darle dinero"
                ],
                [  # Option two -2
                    "Golpear",
                    "No",
                    "Rechazar",
                    "Amenazar"
                ],
                [  # Option three -3
                    "Convencer",
                    "Intertar hablar",
                    "hablar"
                ],
                [  # Option one data -4
                    0,  # difficulty
                    10,  # intelligence
                    4,  # strong
                    0,  # health
                    10,   # social skills
                ],
                [  # Option two data -5
                    -5,  # difficulty
                    -5,  # intelligence
                    0,  # strong
                    -100,  # health
                    -20,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    20,  # intelligence
                    10  ,  # strong
                    0,  # health
                    13,   # social skills
                ]
                ],
            34: [
                [  # Questions -0
                    "¿Qué haras?"
                ],
                [  # Option one -1
                    "Delegar responsabilidades",
                    "Delegar",
                    "Nada",
                    "Irme"
                ],
                [  # Option two -2
                    "Buscar ayuda",
                    "Ayuda",
                    "Ayuda externa "
                ],
                [  # Option three -3
                    "Podre con ambos",
                    "enfrentar ambos desafios",
                    "ambos",
                    "Todo"
                ],
                [  # Option one data -4
                    -20,  # difficulty
                    9,  # intelligence
                    -10,  # strong
                    +20,  # health
                    -30,   # social skills
                ],
                [  # Option two data -5
                    -10,  # difficulty
                    10,  # intelligence
                    -10,  # strong
                    +20,  # health
                    4,   # social skills
                ],
                [  # Option three data -6
                    20,  # difficulty
                    20,  # intelligence
                    30  ,  # strong
                    +30,  # health
                    0,   # social skills
                ]
                ],
            39: [
                [  # Questions -0
                    "¿Qué priorizaras?"
                ],
                [  # Option one -1
                    "Seguridad",
                    "La seguridad",
                    "Estar seguros",
                    "Militares"
                ],
                [  # Option two -2
                    "Paz",
                    "La Paz",
                    "La paz en la region",
                    "Gente"
                ],
                [  # Option three -3
                    "Recursos",
                    "Dinero",
                    "Todo",
                    "Gobierno"
                ],
                [  # Option one data -4
                    -20,  # difficulty
                    6,  # intelligence
                    10,  # strong
                    0,  # health
                    -50,   # social skills
                ],
                [  # Option two data -5
                    30,  # difficulty
                    0,  # intelligence
                    -10,  # strong
                    +15,  # health
                    50,   # social skills
                ],
                [  # Option three data -6
                    15,  # difficulty
                    20,  # intelligence
                    7  ,  # strong
                    4,  # health
                    0,   # social skills
                ]
                ],
            43: [
                [  # Questions -0
                    "¿Qué haras?"
                ],
                [  # Option one -1
                    "Llamar a la policia",
                    "Policia",
                    "llamar",
                ],
                [  # Option two -2
                    "Investigar",
                    "Ir a investigar",
                    "Gente"
                ],
                [  # Option three -3
                    "Nada",
                    "Quizas Luego",
                    "Ahora no",
                    "Escapar"
                ],
                [  # Option one data -4
                    0,  # difficulty
                    10,  # intelligence
                    -10,  # strong
                    0,  # health
                    -30,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    10,  # intelligence
                    10,  # strong
                    0,  # health
                    20,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    0,  # intelligence
                    0  ,  # strong
                    0,  # health
                    -15,   # social skills
                ]
                ],
            47: [
                [  # Questions -0
                    "¿Aceptas la oferta?"
                ],
                [  # Option one -1
                    "Si",
                    "A la aventura",
                    "Vamos",
                    "Africa"
                ],
                [  # Option two -2
                    "No",
                    "No puedo",
                    "Nah"
                ],
                [  # Option three -3
                    "Claro",
                    "Por supuesto",
                ],
                [  # Option one data -4
                    -10,  # difficulty
                    0,  # intelligence
                    10,  # strong
                    0,  # health
                    30,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    20,  # intelligence
                    -30,  # strong
                    0,  # health
                    -15,   # social skills
                ],
                [  # Option three data -6
                    -12,  # difficulty
                    1,  # intelligence
                    11  ,  # strong
                    1,  # health
                    31,   # social skills
                ]
                ],##falta
            51: [
                [  # Questions -0
                    "¿A dondé iras?"
                ],
                [  # Option one -1
                    "Fiesta",
                    "Party",
                    "Fiesta Exclusiva",
                ],
                [  # Option two -2
                    "Reunion",
                    "Amigo",
                    "Algo tranquilo"
                ],
                [  # Option three -3
                    "Ninguna",
                    "No saldre",
                ],
                [  # Option one data -4
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    -10,  # health
                    30,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    10,  # health
                    15,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    10,  # intelligence
                    0  ,  # strong
                    15,  # health
                    0,   # social skills
                ]
                ],
            60: [
                [  # Questions -0
                    "¿Lo tomaras?"
                ],
                [  # Option one -1
                    "Si",
                    "Claro",
                    "Por supuesto",
                    "Porque no"
                ],
                [  # Option two -2
                    "No",
                    "No puedo",
                    "Nah",
                    "Luego"
                ],
                [  # Option three -3
                    "Suicidio",
                    "Me quiero morir",
                ],
                [  # Option one data -4
                    0,  # difficulty
                    0,  # intelligence
                    -20,  # strong
                    20,  # health
                    30,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    -100,  # health
                    0,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    0,  # intelligence
                    0  ,  # strong
                    -100,  # health
                    0,   # social skills
                ]
                ],
            66: [
                [  # Questions -0
                    "¿Quiéres ir al hospital ahora?"
                ],
                [  # Option one -1
                    "Si",
                    "Por favor",
                    "Claro"
                ],
                [  # Option two -2
                    "No",
                    "No me importa",
                    "Neh",
                ],
                [  # Option three -3
                    "Luego",
                    "Despues",
                ],
                [  # Option one data -4
                    0,  # difficulty
                    20,  # intelligence
                    10,  # strong
                    0,  # health
                    0,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    -10,  # intelligence
                    0,  # strong
                    -50,  # health
                    25,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    -5,  # intelligence
                    0  ,  # strong
                    -25,  # health
                    10,   # social skills
                ]
                ],
            72: [
                [  # Questions -0
                    "¿Con quién prefieres pasar el dolo?"
                ],
                [  # Option one -1
                    "Familia",
                    "Con mi familia",
                    "mi familia",
                    "Familiares"
                ],
                [  # Option two -2
                    "Amigos",
                    "con mis amigos",
                    "mis amigos",
                ],
                [  # Option three -3
                    "Ambos",
                    "los dos",
                ],
                [  # Option one data -4
                    0,  # difficulty
                    10,  # intelligence
                    10,  # strong
                    0,  # health
                    10,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    10,  # intelligence
                    10,  # strong
                    00,  # health
                    10,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    12,  # intelligence
                    12  ,  # strong
                    0,  # health
                    12,   # social skills
                ]
                ],
            78: [
                [  # Questions -0
                    "¿Lo donaras?"
                ],
                [  # Option one -1
                    "Si",
                    "Por supuesto ",
                    "Claro"
                ],
                [  # Option two -2
                    "No",
                    "No",
                    "Neh",
                ],
                [  # Option three -3
                    "Mi hija",
                    "darcelo a mi hija",
                    "hija",

                ],
                [  # Option one data -4
                    0,  # difficulty
                    7,  # intelligence
                    0,  # strong
                    0,  # health
                    10,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    20,  # intelligence
                    0,  # strong
                    0,  # health
                    -20,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    15,  # intelligence
                    0  ,  # strong
                    0,  # health
                    15,   # social skills
                ]
                ],
            80: [
                [  # Questions -0
                    ""
                ],
                [  # Option one -1
                    "Si",
                    "Claro",
                    "Por supuesto",
                    "vamos ",
                    "Voy"
                ],
                [  # Option two -2
                    "no",
                    "No",
                    "No quiero",
                ],
                [  # Option three -3
                    "listo",
                    "listosimo",
                ],
                [  # Option one data -4
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    -100,  # health
                    0,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    -100,  # health
                    0,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    0,  # intelligence
                    0  ,  # strong
                    -100,  # health
                    0,   # social skills
                ]
                ],
           
        }
        
        hard_questions = {
            9: [
                [  # Questions -0
                    "¿Vas a decírselo al director?"
                ],
                [  # Option one -1
                    "SI",
                    "Por supuesto",
                    "Decir",
                    "Seguro"
                ],
                [  # Option two -2
                    "No",
                    "Silencio",
                    "Por supuesto que no"
                ],
                [  # Option three -3
                    "Recuperarlo",
                    "Robárselo",
                    "Recuperar lo robado",
                ],
                [  # Option one data -4
                    15,  # difficulty
                    -5,  # intelligence
                    0,  # strong
                    -15,  # health
                    -2,   # social skills
                ],
                [  # Option two data -5
                    3,  # difficulty
                    5,  # intelligence
                    2,  # strong
                    0,  # health
                    -1,   # social skills
                ],
                [  # Option three data -6
                    -8,  # difficulty
                    10,  # intelligence
                    10,  # strong
                    5,  # health
                    5,   # social skills
                ]
        
                ],
            13: [
                [  # Questions -0
                    "¿Lo aceptaras?"
                ],
                [  # Option one -1
                    "Si",
                    "claro",
                    "SI",
                    "Claro"
                ],
                [  # Option two -2
                    "No",
                    "No quiero",
                    
                ],
                [  # Option three -3
                    "Quizas",
                    
                ],
                [  # Option one data -4
                    15,  # difficulty
                    -3,  # intelligence
                    1,  # strong
                    -4,  # health
                    9,   # social skills
                ],
                [  # Option two data -5
                    -5,  # difficulty
                    3,  # intelligence
                    0,  # strong
                    0,  # health
                    3,   # social skills
                ],
                [  # Option three data -6
                    4,  # difficulty
                    4,  # intelligence
                    2,  # strong
                   -5,  # health
                    0,   # social skills
                ]
                ],
            17: [
                [  # Questions -0
                    "¿A dondé iras?"
                ],
                [  # Option one -1
                    "Jugar",
                    "jugar",
                ],
                [  # Option two -2
                    "Cocinar",
                    "cocinar",
                    "cook",
                    
                ],
                [  # Option three -3
                    "Leer",
                    "leer",
                    "Lectura",
                    
                ],
                [  # Option one data -4
                    -3,  # difficulty
                    5,  # intelligence
                    5,  # strong
                    4,  # health
                    3,   # social skills
                ],
                [  # Option two data -5
                    -5,  # difficulty
                    2,  # intelligence
                    0,  # strong
                    0,  # health
                    1,   # social skills
                ],
                [  # Option three data -6
                    4,  # difficulty
                    9,  # intelligence
                    3,  # strong
                   0,  # health
                    2,   # social skills
                ]
                ],
            21: [
                [  # Questions -0
                    "¿Intentaras desactivarla?"
                ],
                [  # Option one -1
                    "Si",
                    "claro",
                    "Salvarlos",
                    "intentarlo"
                ],
                [  # Option two -2
                    "Escapar",
                    "Salir ",
                    "No",
                    
                ],
                [  # Option three -3
                    "Dejarlos Morir",
                    
                ],
                [  # Option one data -4
                    10,  # difficulty
                    -20,  # intelligence
                    -4,  # strong
                    -70,  # health
                    20,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    20,  # intelligence
                    -13,  # strong
                    -20,  # health
                    -15,   # social skills
                ],
                [  # Option three data -6
                    4,  # difficulty
                    4,  # intelligence
                    4,  # strong
                    5,  # health
                    1,   # social skills
                ]
                ],
            30: [
                [  # Questions -0
                    "¿Qué haras?"
                ],
                [  # Option one -1
                    "Prestarle",
                    "si",
                    "Dinero",
                    "Seguro"
                ],
                [  # Option two -2
                    "No",
                    "No quiero",
                    "Rechazar",
                    "No puedo"
                ],
                [  # Option three -3
                    "No tengo ",
                    "Prestame tu",
                    "Convencerlo"
                ],
                [  # Option one data -4
                    0,  # difficulty
                    -10,  # intelligence
                    0,  # strong
                    0,  # health
                    40,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    21,  # intelligence
                    0,  # strong
                    5,  # health
                    -5,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    13,  # intelligence
                    2  ,  # strong
                    0,  # health
                    12,   # social skills
                ]
                ],
            34: [
                [  # Questions -0
                    "¿Qué decidiras priorizar?"
                ],
                [  # Option one -1
                    "Familia",
                    "Priorizar la familia",
                    "La familia es primero",
                    "Irme"
                ],
                [  # Option two -2
                    "Mision",
                    "Priorizar la mision",
                    "Mundo",
                    "El mundo",
                    "La mision"
                ],
                [  # Option three -3
                    "Compromiso",
                    "Buscar Compromiso",
                    "Buscar otra cosa",
                    "Buscar"
                ],
                [  # Option one data -4
                    0,  # difficulty
                    10,  # intelligence
                    10,  # strong
                    10,  # health
                    0,   # social skills
                ],
                [  # Option two data -5
                    30,  # difficulty
                    30,  # intelligence
                    30,  # strong
                    35,  # health
                    -40,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    -20,  # intelligence
                    -30  ,  # strong
                    0,  # health
                    -20,   # social skills
                ]
                ],  
            39: [
                [  # Questions -0
                    "¿Cómo decides motivar a tus tropas: con discursos inspiradores, recompensas o sanciones?"
                ],
                [  # Option one -1
                    "Discursos",
                    "Discursos inspiradores",
                    "Discurso",
                    "Motivacion",
                    "Hablarles"
                ],
                [  # Option two -2
                    "Recompensas",
                    "Dinero",
                    "Recompensarlos",
                    "Prometer",
                    "Riquezas"
                ],
                [  # Option three -3
                    "Miedo",
                    "Sanciones",
                    "Intimidacion",
                    "Amenzar"
                ],
                [  # Option one data -4
                    -10,  # difficulty
                    20,  # intelligence
                    5,  # strong
                    0,  # health
                    30,   # social skills
                ],
                [  # Option two data -5
                    -20,  # difficulty
                    30,  # intelligence
                    20,  # strong
                    0,  # health
                    -50,   # social skills
                ],
                [  # Option three data -6
                    -40,  # difficulty
                    40,  # intelligence
                    -60  ,  # strong
                    0,  # health
                    -30,   # social skills 
                ]
                ],  
            43: [
                [  # Questions -0
                    "¿Qué problemas priorizaras?"
                ],
                [  # Option one -1
                    "Los mundiales",
                    "El mundo es mas importante que la region",
                    "Mundo",
                    "Todos",
                ],
                [  # Option two -2
                    "La region",
                    "Regionales",
                    "Los regionales",
                    "Region",
                ],
                [  # Option three -3
                    "Ninguno",
                    "Silencio",
                    "Estoy cansado"
                ],
                [  # Option one data -4
                    10,  # difficulty
                    20,  # intelligence
                    5,  # strong
                    0,  # health
                    30,   # social skills
                ],
                [  # Option two data -5
                    20,  # difficulty
                    30,  # intelligence
                    20,  # strong
                    0,  # health
                    -50,   # social skills
                ],
                [  # Option three data -6
                    -99,  # difficulty
                    -40,  # intelligence
                    -60  ,  # strong
                    0,  # health
                    -30,   # social skills 
                ]
                ],  
            47: [
                [  # Questions -0
                    "¿Qué haras los ayudarlos o mantendras tu distancia del conflicto?"
                ],
                [  # Option one -1
                    "Visitarlos",
                    "Ayudarlos",
                    "Ayudar",
                    "Ayuda",
                ],
                [  # Option two -2
                    "Distancia",
                    "Nada",
                    "No me importa",
                    "No es mi asunto",
                    "Mantener distancia"
                ],
                [  # Option three -3
                    "Silencio",
                    "Estoy cansado"
                    "Ahora no",
                    "Nada"
                ],
                [  # Option one data -4
                    20,  # difficulty
                    20,  # intelligence
                    5,  # strong
                    0,  # health
                    30,   # social skills
                ],
                [  # Option two data -5
                    -20,  # difficulty
                    30,  # intelligence
                    -20,  # strong
                    0,  # health
                    -50,   # social skills
                ],
                [  # Option three data -6
                    -99,  # difficulty
                    -40,  # intelligence
                    -60  ,  # strong
                    0,  # health
                    -30,   # social skills 
                ]
                ],  ##falta
            51: [
                [  # Questions -0
                    "¿involucrarás en este juego político, o preferirás mantenerte al margen??"
                ],
                [  # Option one -1
                    "Involucrarme",
                    "Si",
                    "Vamos",
                    "A la aventura"
                ],
                [  # Option two -2
                    "Golpear",
                ],
                [  # Option three -3
                    "Mandenerme al margen",
                    "Margen",
                    "NO",
                    "Ignorar"
                ],
                [  # Option one data -4
                    10,  # difficulty
                    0,  # intelligence
                    -10,  # strong
                    0,  # health
                    30,   # social skills
                ],
                [  # Option two data -5
                    -20,  # difficulty
                    -10,  # intelligence
                    30,  # strong
                    0,  # health
                    -15,   # social skills
                ],
                [  # Option three data -6
                    -10,  # difficulty
                    20,  # intelligence
                    11  ,  # strong
                    3,  # health
                    -20,   # social skills
                ]
                ],
            60: [
                [  # Questions -0
                    "¿Aceptas que venda tu auto para comprarlos o mejor no comprarlos?"
                ],
                [  # Option one -1
                    "Si",
                    "Claro",
                    "Vamos",
                    "Por supuesto",
                    "Venderlo"
                ],
                [  # Option two -2
                    "No",
                    "No puedo",
                    "Nah",
                    "No venderlo"
                ],
                [  # Option three -3
                    "Claro",
                    "Por supuesto",
                ],
                [  # Option one data -4
                    -10,  # difficulty
                    12,  # intelligence
                    -10,  # strong
                    0,  # health
                    0,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    20,  # intelligence
                    -30,  # strong
                    -97,  # health
                    -15,   # social skills
                ],
                [  # Option three data -6
                   -10,  # difficulty
                    12,  # intelligence
                    -10,  # strong
                    0,  # health
                    0,   # social skills
                ]
                ],

            66: [
                [  # Questions -0
                    "¿La tomaras?"
                ],
                [  # Option one -1
                    "Si",
                    "Por favor",
                    "Claro"
                ],
                [  # Option two -2
                    "No",
                    "No puedo",
                    "Neh",
                ],
                [  # Option three -3
                    "Luego",
                    "Despues",
                ],
                [  # Option one data -4
                    0,  # difficulty
                    7,  # intelligence
                    0,  # strong
                    -20,  # health
                    10,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    10,  # intelligence
                    0,  # strong
                    0,  # health
                    5,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    30,  # intelligence
                    9  ,  # strong
                    0,  # health
                    20,   # social skills
                ]
                ],
            72: [
                [  # Questions -0
                    "¿Con quién pasaras el dolor?"
                ],
                [  # Option one -1
                    "Familia",
                    "Familiares",
                    "con familia",
                    "Mis familiares",
                ],
                [  # Option two -2
                    "Amigos",
                    "con amigos",
                    "mis amigos",
                ],
                [  # Option three -3
                    "Nadie",
                    "Solo",
                ],
                [  # Option one data -4
                    -10,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    0,  # health
                    13,   # social skills
                ],
                [  # Option two data -5
                    -10,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    0,  # health
                    8,   # social skills
                ],
                [  # Option three data -6
                    10,  # difficulty
                    0,  # intelligence
                    10  ,  # strong
                    0,  # health
                    -10,   # social skills
                ]
                ],
            78: [
                [  # Questions -0
                    "¿Qué haras con tu dinero?"
                ],
                [  # Option one -1
                    "Donarlo",
                    "Darlo",
                    "Compartirlo",
                    "Fundacion",
                    "Donar"
                ],
                [  # Option two -2
                    "Gastalo",
                    "Lujos",
                    "Gastarlo en lujos",
                ],
                [  # Option three -3
                    "Nada",
                    "Conservarlo",
                ],
                [  # Option one data -4
                    -10,  # difficulty
                    9,  # intelligence
                    0,  # strong
                    +5,  # health
                    10,   # social skills
                ],
                [  # Option two data -5
                    -10,  # difficulty
                    20,  # intelligence
                    0,  # strong
                    0,  # health
                    -30,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    -10,  # intelligence
                    0  ,  # strong
                    0,  # health
                    0,   # social skills
                ]
                ],
            80: [
                [  # Questions -0
                    ""
                ],
                [  # Option one -1
                    "Si",
                    "Claro",
                    "Por supuesto",
                    "vamos ",
                    "Voy"
                ],
                [  # Option two -2
                    "no",
                    "No",
                    "No quiero",
                ],
                [  # Option three -3
                    "listo",
                    "listosimo",
                ],
                [  # Option one data -4
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    -100,  # health
                    0,   # social skills
                ],
                [  # Option two data -5
                    0,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    -100,  # health
                    0,   # social skills
                ],
                [  # Option three data -6
                    0,  # difficulty
                    0,  # intelligence
                    0  ,  # strong
                    -100,  # health
                    0,   # social skills
                ]
                ],
            
            
        }
        #Preguntas niñez
        if age <= 5:
            return child_questions[age]
        elif diff == 1:
            return easy_questions[age]
        elif diff == 2:
            return normal_questions[age]
        else:
            return hard_questions[age]
        #
    def ask_question(self, age):
             # Decide qué conjunto de preguntas utilizar según la edad y la dificultad del jugador.
            if age <= 5:
                data = self.give_questions(age,0)
            else:# Determina la dificultad del juego y selecciona preguntas correspondientes.
                if self.pl.difficulty < 33:
                    difficulty_count = 1

                elif self.pl.difficulty >= 33 and self.pl.difficulty < 66:
                    difficulty_count = 2

                else:
                    difficulty_count = 3
                    
                data = self.give_questions(age, difficulty_count)    
         # Extrae información relevante de los datos de la pregunta seleccionada.
            question = random.choice(data[0])
            options_one = data[1]
            options_two = data[2]
            options_three = data[3]
            result_one = data[4]
            result_two = data[5]
            result_three = data[6]
            # Muestra la pregunta al jugador
            print(question)
            # Bucle para manejar la elección del jugador.
            while True:
                select = (input("++"+self.return_player_name()+": ")).lower()
                options = [string.lower() for string in options_one]
                if select in options:
                    results = result_one
                    break
                options = [string.lower() for string in options_two]
                if select in options:
                    results = result_two
                    break
                options = [string.lower() for string in options_three]
                if select in options:
                    results = result_three
                    break
                 # comandos especiales o acciones según la elección del jugador.
                time.sleep(2)
                if select == "stop game":
                    print("Sacándote de esta porquería")
                    sys.exit()
                    #easter egg
                if self.win_counter == 3:
                    print("Descubriste el huevo de Pascu")
                    print("¡Felicidades, ganaste! Te diriges al cielo")
                    sys.exit()
            
                if select == "show status":
                    self.show_status()    
                    print("**Narrator: Ahora tu decisión...")
                    
                if select == "worldylife":
                    self.win_counter += 1   
                    print(self.win_counter)
                    print("**Narrator: Entendido, ahora tu decisión...")
                    
                else:    
                    print("**Narrator: ¿Perdón? Repite tu decisión...")
                
            self.make_adjustments(results, age)
            
    def make_adjustments(self, results, age):
         #Ajusta los atributos del jugador en función de los resultados de la elección.
        self.pl.difficulty = min(max(self.pl.difficulty + results[0], 0), 100)
        self.pl.intelligence = min(max(self.pl.intelligence + results[1], 0), 100)
        self.pl.strong = min(max(self.pl.strong + results[2], 0), 100)
        self.pl.health = min(max(self.pl.health + results[3], 0), 100)
        self.pl.social = min(max(self.pl.social + results[4], 0), 100)
        # Verifica si la salud del jugador llegó a cero y maneja la situación de fallecimiento.
        if self.pl.health == 0 :
            print("__Has Muerto__")
            time.sleep(2)
            print("**God: Hey tu!")
            time.sleep(2)
            print("**God: No es un placer volver a verte.")
            time.sleep(2)
            print("**God: Supongo que tus malas decisiones te llevaron a un final temprano.")
            time.sleep(2)
            print("**God: Necesitamos decidir si vas al cielo o al infierno.")
            time.sleep(3)
             # Calcula el promedio de atributos y determina el destino del jugador
            average = (self.pl.intelligence + self.pl.strong + self.pl.social) / 3
            
            if age < 10:
                print("**God: Bueno, ¡mírate, ni siquiera has alcanzado los dos dígitos! Cielo es, chaval. Sin sorpresas.")
            elif average > 50:
                print("**God: ¡Oh, un auténtico cerebrito, un atleta fuerte y el alma de la fiesta! Al área VIP del cielo, supongo.")
            else:
                print("**God: ¡Vaya, mala suerte! Parece que es una espiral descendente hacia las profundidades ardientes. Intenta llevar malvaviscos")

            # Muestra el estado final del jugador y finaliza el juego
            self.show_status()
            sys.exit()

        

