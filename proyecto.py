import pywhatkit as kit
import random

lines = open('textos.txt', mode="r", encoding="utf-8").read().splitlines()
linea = random.choice(lines)



kit.sendwhatmsg_instantly("+573156704902",linea,10)



