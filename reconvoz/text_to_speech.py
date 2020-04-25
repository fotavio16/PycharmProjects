from gtts import gTTS
import os

#text = 'Amy normally hated Monday mornings, but this year was different. She was waiting outside the classroom when her friend Tara arrived.'
text = 'Ana normalmente odiava as manhãs de segunda-feira, mas este ano foi diferente. Ela estava esperando do lado de fora da sala de aula quando sua amiga Sandra chegou.'
#language = 'en'
language = 'pt-br'

fala = gTTS(text=text, lang=language, slow=False)
fala.save("voice2.mp3")

os.system("start voice2.mp3")
