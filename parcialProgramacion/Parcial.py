import random
import os

class JuegoAdivinanza:
    def __init__(self):
        self.numeroSecreto = random.randint(1, 100)
        self.intentos = 0

    def validarNumero(self, num):
        self.intentos += 1
        if num > self.numeroSecreto:
            return "El número dado es mayor."
        elif num < self.numeroSecreto:
            return "El número dado es menor."
        else:
            return "El número dado es el correcto."

    def reiniciar(self):
        self.numeroSecreto = random.randint(1, 100)
        self.intentos = 0


class Jugador:
    def __init__(self, name):
        self.name = name
        self.history = []
        self.loadHistory()

    def registerGame(self, attempts, won):
        accuracy = (1 / attempts) * 100 if attempts != 0 else 0
        self.history.append((attempts, won, accuracy))

    def showStats(self):
        totalGames = len(self.history)
        totalWins = sum(1 for game in self.history if game[1])
        if totalGames > 0:
            winRate = (totalWins / totalGames) * 100
            averageAccuracy = sum(game[2] for game in self.history) / totalGames
            return (f"Partidas jugadas: {totalGames}, Partidas ganadas: {totalWins}, "
                    f"Tasa de victorias: {winRate:.2f}%, Promedio de exactitud: {averageAccuracy:.2f}%")
        else:
            return "No se ha jugado ninguna partida."

    def saveHistory(self):
        allHistories = self.loadAllHistories()
        allHistories[self.name] = self.history
        with open('estadisticas.txt', 'w') as file:
            for player, history in allHistories.items():
                for attempts, won, accuracy in history:
                    file.write(f"{player},{attempts},{won},{accuracy:.2f}\n")

    @staticmethod
    def loadAllHistories():
        histories = {}
        if os.path.exists('estadisticas.txt') and os.path.getsize('estadisticas.txt') > 0:
            with open('estadisticas.txt', 'r') as file:
                for line in file:
                    player, attempts, won, accuracy = line.strip().split(',')
                    if player not in histories:
                        histories[player] = []
                    histories[player].append((int(attempts), won == 'True', float(accuracy)))
        return histories

    def loadHistory(self):
        histories = self.loadAllHistories()
        self.history = histories.get(self.name, [])


def menu():
    playerName = input("Introduce tu nombre: ")
    currentPlayer = Jugador(playerName)
    while True:
        strInput = """
Menú del juego:
a) Comenzar una nueva partida.
b) Ver las estadísticas del jugador.
c) Salir del juego.
Selecciona una opción: """
        selectedOption = input(strInput).upper()
        if selectedOption == "A":
            theGame(currentPlayer)
        elif selectedOption == "B":
            print(currentPlayer.showStats())
        elif selectedOption == "C":
            currentPlayer.saveHistory()
            print("¡Hasta luego!")
            break
        else:
            print("Por favor, selecciona una opción válida.")


def theGame(player):
    game = JuegoAdivinanza()
    while True:
        try:
            number = int(input("Introduce un número (preferiblemente entre 1 y 100): "))
            result = game.validarNumero(number)
            print(result)
            if result == "El número dado es el correcto.":
                player.registerGame(game.intentos, True)
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")


# Ejecutar el menú
menu()