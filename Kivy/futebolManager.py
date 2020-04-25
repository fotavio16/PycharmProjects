from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from random import randint
from time import sleep, strftime
from datetime import date

from partida import jogada
from equipe import montaEquipe

#Builder.load_file('toolbox.kv')
#Builder.load_file('drawingspace.kv')
#Builder.load_file('generaloptions.kv')
#Builder.load_file('statusbar.kv')

class Placar(Widget):
    segundos = 0
    hoje = StringProperty()
    scoreA = StringProperty()
    equipeA = StringProperty()
    scoreB = StringProperty()
    equipeB = StringProperty()
    estadio = StringProperty()
    escudoA = StringProperty()
    escudoB = StringProperty()
    time = StringProperty()

    # Atributos Jogadores:
    # (id, nome, time, posição, idade, altura, passe, chute, mentalidade, defesa, velocidade, drible)
    timeCasa = montaEquipe('Vasco da Gama','442')
    print(timeCasa)


    def __init__(self, **kwargs):
        super(Placar, self).__init__(**kwargs)
        self.hoje = date.today().strftime("%d, %b %Y")
        self.estadio = "Maracana"
        self.equipeA = "Vasco da Gama"
        self.escudoA = "vasco.png"
        self.equipeB = "Fluminense"
        self.escudoB = "fluminense.png"
        self.scoreA = str(randint(0,0))
        self.scoreB = str(randint(0,0))
        self.time = self.montaRelogio(0,0)

        timeCasa = montaEquipe('Vasco da Gama', '442')
        print(timeCasa)

        # Variáveis de controle
        self.etapa = 1
        self.posseCasa = True

        self.evento = Clock.schedule_interval(self.update, 2)



    def update(self, nap):
        # Atualiza relógio
        acelerador = 50 # Multiplicador do intervalo de jogo
        self.segundos += nap+acelerador
        m, s = divmod(self.segundos, 60)
        self.time = self.montaRelogio(int(m),int(s))

        if self.segundos > 90 * 60:
            print("Tempo regular encerrado!")
            self.evento.cancel()


        # Define cada jogada
        venceu = jogada(self.etapa, self.posseCasa)
        if venceu == True:
            if self.etapa < 3:
                self.etapa += 1
                # Comentário
                if self.posseCasa:
                    print(f'Avança a equipe da Casa. Etapa {self.etapa}.')
                else:
                    print(f'Avança a equipe Visitante. Etapa {self.etapa}.')
            else: # Etapa é 3 vamos ver se houve gol
                # Comentário
                if self.posseCasa:
                    print(f'Prepara o chute atacante Local. Etapa {self.etapa}.')
                else:
                    print(f'Prepara o chute atacante Visitante. Etapa {self.etapa}.')
                direcaoChute = randint(0,100)
                if direcaoChute < 30:
                    print("Chutou para fora!")
                elif direcaoChute < 60:
                    print("O chute bateu na trave.")
                else: # É gol
                    if self.posseCasa == True:
                        print(f'É gol do {self.equipeA}.')
                        self.incrementaA()
                    else:
                        print(f'É gol do {self.equipeB}.')
                        self.incrementaB()
                self.etapa = 1
                self.posseCasa = not self.posseCasa
        else:
            self.etapa = 1
            self.posseCasa = not self.posseCasa
            print(f'Perde a posse de bola.')
            if self.posseCasa:
                print(f'Bola com a equipe da Casa. Etapa {self.etapa}.')
            else:
                print(f'Bola com a equipe Visitante. Etapa {self.etapa}.')


    def incrementaA(self):
        self.scoreA = str(int(self.scoreA) + 1)

    def incrementaB(self):
        self.scoreB = str(int(self.scoreB) + 1)

    def montaRelogio(self, min, seg):
        if min < 10:
            relogio = '0' + str(min) + ':'
        else:
            relogio = str(min) + ':'
        if seg < 10:
            relogio = relogio + '0' + str(seg)
        else:
            relogio = relogio + str(seg)
        return relogio

class ManagerApp(App):
    def build(self):
        return Placar()



if __name__=="__main__":
    ManagerApp().run()
