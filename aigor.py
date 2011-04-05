#!/usr/bin/python
# -*- coding: UTF8 -*-
import aiml
import os.path
from festival import say
from xgoogle.translate import Translator

translate = Translator().translate
k = aiml.Kernel()
if os.path.isfile("cerebro.brn"): # si existe el fichero...
    k.bootstrap(brainFile = "cerebro.brn")
else: #si no existe lo creamos con std-startup.xml 
    k.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    k.saveBrain("cerebro.brn")
    k.loadBrain("cerebro.brn")

##Configuración del bot
k.setBotPredicate("name","Aigor") 
k.setBotPredicate("gender","male") 
k.setBotPredicate("master","hashashin") 
k.setBotPredicate("birthday","2011") 
k.setBotPredicate("birthplace","Barcelona") 
k.setBotPredicate("boyfriend","you") 
k.setBotPredicate("favoritebook","Don't Read Me") 
k.setBotPredicate("favoritecolor","transparent") 
k.setBotPredicate("favoriteband","rubber") 
k.setBotPredicate("favoritefood","patterns") 
k.setBotPredicate("favoritesong","your voice") 
k.setBotPredicate("favoritemovie","your life story") 
k.setBotPredicate("forfun","talk to you") 
k.setBotPredicate("friends","you") 
k.setBotPredicate("girlfriend","you") 
k.setBotPredicate("kindmusic","all") 
k.setBotPredicate("location","here") 
k.setBotPredicate("looklike","you") 
k.setBotPredicate("question","What?") 
k.setBotPredicate("sign","none") 
k.setBotPredicate("talkabout","anything") 
k.setBotPredicate("wear","nothing") 
k.setBotPredicate("website","http://serveramd.dyndns.org") 
k.setBotPredicate("email","hash@serveramd.dyndns.org") 
k.setBotPredicate("language","any") 
k.setBotPredicate("msagent","no")

print("Escribe quit o salir para cerrar el programa\n")
print("¿Soy Aigor que puedo hacer por tí?")
say("soy Aigor que puedo hacer por t'i?")
while True: 
    user_input = raw_input("Pregunta > ")
    trans = translate(user_input, lang_to="en").encode('latin1')
    if user_input == "quit" or user_input == "salir":
        break
    answer = k.respond(trans)
    traans = translate(answer, lang_to="es").encode('latin1')
    print(traans).decode('latin1')
    say(traans)
