#!/usr/bin/python
# -*- coding: UTF8 -*-
"""
Aigor 0.1 Bot conversacional en español con traducción en vivo
usando el traductor online de Google, pyaiml y Festival.
Copyright (C) 2011  hashashin mail: gentoo dot power at gmail dot com    
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses.
"""

import aiml
import os.path
from festival import say
from xgoogle.translate import Translator


#preparamos para usar el traductor luego
translate = Translator().translate
#creamos el "cerebro" del bot cargando los aiml de alice o el cerebro existente
k = aiml.Kernel()
# si existe el fichero lo cargamos directamente
if os.path.isfile("cerebro.brn"):
    k.bootstrap(brainFile = "cerebro.brn")
#si no existe lo creamos con std-startup.xml
else: 
    k.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
#si modificamos los aiml habrá que borrar cerebro.brn para recrearlo
    k.saveBrain("cerebro.brn")
#cargamos el cerebro
    k.loadBrain("cerebro.brn")

#Configuración del bot
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

#saludo inicial y muestra la entrada de órdenes
print("Escribe quit o salir para cerrar el programa\n")
print("¿Soy Aigor que puedo hacer por tí?")
say("soy Aigor que puedo hacer por t'i?")
#bucle principal
#como Festival no entiende utf-8 he usado latin1
while True:
    user_input = raw_input("Pregunta > ")
    if user_input == "quit" or user_input == "salir":
        break
    else:
#Traduce la entrada a ingles para que la entienda el bot
        trans = translate(user_input, lang_to="en").encode('latin1')
#busca la respuesta        
        answer = k.respond(trans)
#Traduce la respuesta a español(o cualquier otro soportado por Google)        
        traans = translate(answer, lang_to="es").encode('latin1')
#Imprime/dice la respuesta        
        print(traans).decode('latin1')
        say(traans)
