import readchar
import os
import random
import time

pikachu_texture = """\
  ██████████████████    ██████████
▓▓  ████████████████  ░░  ████████
▓▓▓▓  ██████████████  ▓▓  ████████
▓▓▓▓▓▓      ████████  ▓▓▓▓  ██████
▓▓▓▓▓▓  ░░░░    ████  ▓▓▓▓  ██████
  ▓▓▓▓▓▓  ░░▓▓▓▓    ▓▓▓▓▓▓▓▓  ████
██  ▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ██
  ▓▓▓▓  ██  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  
  ▓▓  ████  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
██  ▓▓    ▓▓▓▓▓▓▓▓▓▓  ██▓▓▓▓▓▓▓▓  
████      ▓▓▓▓▓▓▒▒▒▒    ▓▓▓▓▓▓  ██
██████  ░░░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓  ████
██████  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ██
██████  ░░▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓    ████
██████  ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓  ██████
██████  ▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓  ▓▓  ████\
"""
pikachu_texture = pikachu_texture.split("\n")

pikachu_hurt_texture = """\
▓▓██████████████████▓▓▓▓██████████
░░▓▓████████████████▓▓▓▓▓▓████████
░░░░▓▓██████████████▓▓░░▓▓████████
░░░░░░▓▓▓▓▓▓████████▓▓░░░░▓▓██████
░░░░░░▓▓▓▓▓▓▓▓▓▓████▓▓░░░░▓▓██████
▓▓░░░░░░▓▓▓▓░░░░▓▓▓▓░░░░░░░░▓▓████
██▓▓░░░░▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓██
▓▓░░░░▓▓██▓▓░░░░░░░░░░░░░░░░░░  ▓▓
▓▓░░▓▓████▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓
██▓▓░░▓▓▓▓░░░░░░░░░░▓▓  ░░░░░░░░▓▓
████▓▓▓▓▓▓░░░░░░▒▒▒▒▓▓▓▓░░░░░░▓▓██
██████▓▓▓▓▓▓░░░░░░▒▒░░░░░░░░▓▓████
██████▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓██
██████▓▓▓▓░░░░▓▓░░░░░░░░░░▓▓▓▓████
██████▓▓░░░░░░░░▓▓░░░░░░░░▓▓██████
██████▓▓░░░░░░▓▓░░░░░░░░▓▓░░▓▓████\
"""
pikachu_hurt_texture = pikachu_hurt_texture.split("\n")

charmander_texture = """\
████████        ██████████████████  ████
██████  ▒▒▒▒▒▒▒▒  ██████████████  ░░  ██
████  ▒▒▒▒▒▒▒▒▒▒▒▒  ████████████  ░░░░  
████  ▒▒▒▒▒▒▒▒▒▒▒▒  ████████████  ░░░░  
██  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ████████  ░░░░░░░░
  ▒▒▒▒▒▒▒▒██  ▒▒▒▒▒▒  ████████  ░░░░▓▓░░
  ▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒  ██████  ░░▓▓▓▓░░
  ▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒  ████████  ▓▓    
██  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ██████  ▒▒  ██
████    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ██  ▒▒▒▒  ██
████████      ▒▒▒▒  ▒▒▒▒▒▒    ▒▒▒▒  ████
██████████  ▓▓▓▓  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ████
██████████  ▓▓▓▓▓▓    ▒▒▒▒▒▒  ▒▒  ██████
████████  ██  ▓▓▓▓▓▓▒▒▒▒▒▒▒▒    ████████
██████████      ▓▓▓▓▒▒▒▒▒▒    ██████████
████████████████      ▒▒▒▒  ████████████\
"""
squirtle_texture = """\
██████        ██████████████████      ██
████  ▒▒▒▒▒▒▒▒    ████████████  ▒▒▒▒▒▒  
██  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ██████  ▒▒▒▒▒▒▒▒▒▒
██  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ░░    ██  ▒▒▒▒▒▒  ▒▒
  ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░  ▒▒▒▒▒▒  ▒▒▒▒
  ▒▒▒▒▒▒▒▒██  ▒▒▒▒▒▒██░░░░░░  ▒▒▒▒  ▒▒  
  ▒▒▒▒▒▒▒▒  ░░▒▒▒▒▒▒██░░░░░░  ▒▒      ██
██  ▒▒▒▒▒▒  ░░▒▒▒▒▒▒  ██░░░░░░    ██████
████    ▒▒▒▒▒▒▒▒    ▒▒▒▒██░░░░  ████████
████  ▒▒        ▒▒▒▒▒▒▒▒██░░░░  ████████
██████    ▓▓▓▓  ▒▒▒▒▒▒  ██░░░░  ████████
██████████  ▓▓▓▓        ██░░░░  ████████
████████  ▒▒  ▓▓▓▓▓▓▓▓▓▓  ██  ██████████
██████████        ▓▓▓▓▒▒  ██  ██████████
████████████████      ▒▒    ████████████
██████████████████  ▒▒▒▒▒▒  ████████████\
"""
bulbasaur_texture = """\
██████████████████████  ░░░░░░  ████████
██████████████████      ▓▓▓▓▓▓  ████████
██████████████    ▓▓  ▓▓  ▓▓  ▓▓    ████
██████  ████  ▓▓▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓▓▓  ██
████  ▒▒      ▓▓  ▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓  
████  ▒▒▒▒▒▒▒▒    ▓▓▓▓  ▓▓▓▓▓▓▓▓  ▓▓▓▓  
████  ▒▒▒▒▒▒▒▒▒▒▒▒  ▓▓  ▓▓▓▓▓▓▓▓  ▓▓▓▓  
██  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ▓▓▓▓▓▓  ▓▓  ██
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▓▓▓▓      ▒▒  
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒      ▒▒▒▒▒▒  
  ▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒██  
  ▒▒▒▒▒▒▒▒▒▒  ░░██▒▒▒▒▒▒  ▒▒  ▒▒      ██
██  ▒▒▒▒▒▒▒▒  ░░██▒▒▒▒  ▒▒▒▒▒▒  ████████
████    ▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ████████
████████                ██▒▒██  ████████
████████████████████████      ██████████\
"""
magikarp_texture = """\
██████████  ▓▓▓▓▓▓▓▓  ██████  ▒▒  ██████
██████████  ▓▓          ████  ▒▒██  ████
████████████  ▒▒▒▒░░▒▒░░    ▒▒▒▒████  ██
██████████  ▒▒▒▒▒▒▒▒░░░░░░▒▒  ▒▒████  ██
████████  ▒▒▒▒▒▒████▒▒░░▒▒░░▒▒  ██▓▓  ██
████████  ▒▒▒▒▒▒██  ██▒▒░░░░▒▒░░▓▓████  
██████  ▒▒▒▒▒▒▒▒██████▒▒░░▒▒      ████  
██████  ░░░░▒▒▒▒▒▒████▒▒    ▒▒▒▒▒▒  ▓▓▓▓
████  ░░▓▓▓▓▓▓▒▒▒▒▒▒▒▒  ▒▒▒▒████        
████  ▓▓    ▓▓░░▒▒▒▒    ████▓▓▓▓  ░░▓▓▓▓
██████      ▓▓░░▒▒  ▓▓▓▓  ▓▓██████  ░░░░
████          ▓▓░░▒▒    ▓▓  ██    ██    
██  ▓▓  ░░    ▓▓░░▒▒▒▒▒▒  ▓▓  ░░  ██████
  ▓▓  ██  ▓▓▓▓▓▓░░░░░░░░  ▓▓    ████████
  ▓▓  ████      ░░░░░░    ▓▓    ████████
██  ▓▓  ████████      ▓▓▓▓  ▓▓▓▓  ██████\
"""

texture_pokemons = [squirtle_texture.split("\n"), charmander_texture.split("\n"), bulbasaur_texture.split("\n"),
                    magikarp_texture.split("\n")]

charmander_hurt_texture = """\
████████▓▓▓▓▓▓▓▓██████████████████▓▓████
██████▓▓▒▒▒▒▒▒▒▒▓▓██████████████▓▓▓▓▓▓██
████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓████████████▓▓▓▓▓▓▓▓
████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓████████████▓▓▓▓▓▓▓▓
██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████████▓▓▓▓▓▓▓▓▓▓
▓▓▒▒▒▒▒▒▒▒  ▓▓▒▒▒▒▒▒▓▓████████▓▓▓▓▓▓░░▓▓
▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓██████▓▓▓▓░░░░▓▓
▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓████████▓▓░░▓▓▓▓
██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████▓▓▒▒▓▓██
████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓▒▒▒▒▓▓██
████████▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓████
██████████▓▓░░░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓████
██████████▓▓░░░░░░▓▓▓▓▒▒▒▒▒▒▓▓▒▒▓▓██████
████████▓▓██▓▓░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓████████
██████████▓▓▓▓▓▓░░░░▒▒▒▒▒▒▓▓▓▓██████████
████████████████▓▓▓▓▓▓▒▒▒▒▓▓████████████\
"""
squirtle_hurt_texture = """\
██████▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓██
████▓▓▒▒▒▒▒▒▒▒▓▓▓▓████████████▓▓▒▒▒▒▒▒▓▓
██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██████▓▓▒▒▒▒▒▒▒▒▒▒
██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▓▓▒▒
▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒
▓▓▒▒▒▒▒▒▒▒  ▓▓▒▒▒▒▒▒  ▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓▓
▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒  ▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██
██▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓  ▓▓▓▓▓▓▓▓▓▓██████
████▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒  ▓▓▓▓▓▓████████
████▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒  ▓▓▓▓▓▓████████
██████▓▓▓▓░░░░▓▓▒▒▒▒▒▒▓▓  ▓▓▓▓▓▓████████
██████████▓▓░░░░▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓████████
████████▓▓▒▒▓▓░░░░░░░░░░▓▓  ▓▓██████████
██████████▓▓▓▓▓▓▓▓░░░░▒▒▓▓  ▓▓██████████
████████████████▓▓▓▓▓▓▒▒▓▓▓▓████████████
██████████████████▓▓▒▒▒▒▒▒▓▓████████████\
"""
bulbasaur_hurt_texture = """\
██████████████████████▓▓▓▓▓▓▓▓▓▓████████
██████████████████▓▓▓▓▓▓░░░░░░▓▓████████
██████████████▓▓▓▓░░▓▓░░▓▓░░▓▓░░▓▓▓▓████
██████▓▓████▓▓░░░░▓▓░░░░▓▓░░▓▓░░░░░░▓▓██
████▓▓▒▒▓▓▓▓▓▓░░▓▓░░░░░░▓▓░░░░▓▓░░░░░░▓▓
████▓▓▒▒▒▒▒▒▒▒▓▓▓▓░░░░▓▓░░░░░░░░▓▓░░░░▓▓
████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓░░░░░░░░▓▓░░░░▓▓
██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░▓▓░░▓▓██
▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░▓▓▓▓▓▓▒▒▓▓
▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓
▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒  ▓▓
▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓  ▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓██
██▓▓▒▒▒▒▒▒▒▒▓▓▓▓  ▒▒▒▒▓▓▒▒▒▒▒▒▓▓████████
████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓████████
████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒  ▓▓████████
████████████████████████▓▓▓▓▓▓██████████\
"""
magikarp_hurt_texture = """\
██████████▓▓░░░░░░░░▓▓██████▓▓▒▒▓▓██████
██████████▓▓░░▓▓▓▓▓▓▓▓▓▓████▓▓▒▒  ▓▓████
████████████▓▓▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒▒▒    ▓▓██
██████████▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▒▒    ▓▓██
████████▓▓▒▒▒▒▒▒    ▒▒▓▓▒▒▓▓▒▒▓▓  ░░▓▓██
████████▓▓▒▒▒▒▒▒  ▓▓  ▒▒▓▓▓▓▒▒▓▓░░    ▓▓
██████▓▓▒▒▒▒▒▒▒▒      ▒▒▓▓▒▒▓▓▓▓▓▓    ▓▓
██████▓▓▓▓▓▓▒▒▒▒▒▒    ▒▒▓▓▓▓▒▒▒▒▒▒▓▓░░░░
████▓▓▓▓░░░░░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒    ▓▓▓▓▓▓▓▓
████▓▓░░▓▓▓▓░░▓▓▒▒▒▒▓▓▓▓    ░░░░▓▓▓▓░░░░
██████▓▓▓▓▓▓░░▓▓▒▒▓▓░░░░▓▓░░      ▓▓▓▓▓▓
████▓▓▓▓▓▓▓▓▓▓░░▓▓▒▒▓▓▓▓░░▓▓  ▓▓▓▓██▓▓▓▓
██▓▓░░▓▓▓▓▓▓▓▓░░▓▓▒▒▒▒▒▒▓▓░░▓▓▓▓▓▓██████
▓▓░░▓▓██▓▓░░░░░░▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓████████
▓▓░░▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓████████
██▓▓░░▓▓████████▓▓▓▓▓▓░░░░▓▓░░░░▓▓██████\
"""

hurt_texture_pokemons = [squirtle_hurt_texture.split("\n"), charmander_hurt_texture.split("\n"),
                         bulbasaur_hurt_texture.split("\n"), magikarp_hurt_texture.split("\n")]

info_bar = """\
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ██████████████████████ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 █▀ ██████████████████████ ▀█ 
 █▀ ████████████████████████ ▀█ 
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ██████████████████████████ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
██████████████████████████████████████████████████████████████████████████████████████\
"""
info_bar = info_bar.split("\n")

medal_texture = """\
 _______________ 
|@@@@|     |####|
|@@@@|     |####|
|@@@@|     |####|
\@@@@|     |####/
 \@@@|     |###/ 
  \@@|_____|##/  
       (O)       
    ▄▀▀▀▀▀▀▀▄    
  ▄▀  * * *  ▀▄  
 █  *       *  █ 
█ ~  POKEMON  ~ █
█ ~  CHAMPION ~ █
 █  *       *  █ 
  ▀▄  * * *  ▄▀  
    ▀▄▄▄▄▄▄▄▀    \
"""
medal_texture = medal_texture.split("\n")

level_pikachu = 0

X_AXIS = 0
Y_AXIS = 1

map_definition = """\
###__________
###__________
###__########
_____########
_____________
_____________
###__________
###__########
###__########
###__########\
"""

map_definition = [list(row) for row in map_definition.split("\n")]

MAP_HEIGHT = len(map_definition)
MAP_WIDTH = len(map_definition[0])

AMOUNT_OF_TRAINERS = 4

my_coord = [0, 4]
end_game = False

pokemon_trainers = []

while len(pokemon_trainers) < AMOUNT_OF_TRAINERS:
    new_trainer = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]

    if new_trainer != my_coord and new_trainer not in pokemon_trainers \
            and map_definition[new_trainer[Y_AXIS]][new_trainer[X_AXIS]] != "#":

        pokemon_trainers.append(new_trainer)

while not end_game:

    os.system("clear")

    print("██" + "███" * MAP_WIDTH + "██")

    for coordinate_y in range(MAP_HEIGHT):

        print("██", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "   "

            if map_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "▓▓▓"

            if my_coord[X_AXIS] == coordinate_x and my_coord[Y_AXIS] == coordinate_y:
                char_to_draw = "{☺}"

            for trainer in pokemon_trainers:
                if trainer[X_AXIS] == coordinate_x and trainer[Y_AXIS] == coordinate_y:
                    char_to_draw = "{☻}"
                    if my_coord[X_AXIS] == trainer[X_AXIS] and my_coord[Y_AXIS] == trainer[Y_AXIS]:
                        char_to_draw = "☺↔☻"

            print(char_to_draw, end="")

        print("██")

    print("██" + "███" * MAP_WIDTH + "██")

    if my_coord in pokemon_trainers:
        print("¿Quieres enfrentarte a este entrenador nivel {}?".format
              (pokemon_trainers.index([my_coord[X_AXIS], my_coord[Y_AXIS]])+1+level_pikachu))
        print("ENTER para luchar")

    direction = readchar.readkey()
    new_position = None

    if direction == "w":
        new_position = [my_coord[X_AXIS], (my_coord[Y_AXIS]-1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_coord[X_AXIS], (my_coord[Y_AXIS]+1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_coord[X_AXIS]-1) % MAP_WIDTH, my_coord[Y_AXIS]]

    elif direction == "d":
        new_position = [(my_coord[X_AXIS]+1) % MAP_WIDTH, my_coord[Y_AXIS]]

    elif direction == "q":
        end_game = True

    elif direction == "g":

        if my_coord in pokemon_trainers:
            battle_number = pokemon_trainers.index([my_coord[X_AXIS], my_coord[Y_AXIS]]) + level_pikachu
            info_pokemons = [["Squirtle", "♂", 3, 20, 20],
                             ["Charmander", "♀", 6, 45, 45],
                             ["Bulbasaur", "♀", 9, 80, 80],
                             ["Magikarp", "♂", 99, 999, 999]]

            POKEMON_ATTACKS = [[["Pistola Agua", "Burbuja", "Hidrobomba"], [2, 4, 5]],
                               [["Arañazo", "Lanzallamas", "Furia Dragón"], [7, 8, 12]],
                               [["Látigo Cepa", "Placaje", "Hoja Afilada"], [15, 18, 21]],
                               [["Salpicadura", "Placaje"], [24, 70]]]

            info_pikachu = [["Pikachu", "♀", 3, 21, 21],
                            ["Pikachu", "♀", 5, 40, 40],
                            ["Pikachu", "♀", 9, 75, 75],
                            ["Pikachu", "♀", 15, 115, 115]]

            pikachu_attacks = [[["Descansar", "Placaje"], [5, 3]],
                               [["Descansar", "Placaje", "Bola trueno"], [11, 9, 12]],
                               [["Descansar", "Placaje", "Bola trueno", "Impactrueno"], [19, 12, 20, 15]],
                               [["Descansar", "Placaje", "Bola trueno", "Impactrueno"], [47, 27, 35, 32]]]
            menu_pos = 0
            menu_height = len(pikachu_attacks[level_pikachu][0])
            event_part = 0
            event_magikarp = False
            in_game = True
            pikachu_attacked = False
            opponent_attacked = False
            win = False

            step = 1
            # only animation
            for number in range(len(info_bar) - 1):
                os.system("clear")
                for frame in range(4 - number, 8 - number):

                    if frame > 4:
                        print(info_bar[4])
                    elif frame == 1:
                        print(
                            " " + (info_pikachu[level_pikachu][0] + " " + info_pikachu[level_pikachu][1]).ljust(20)
                            + "LVL: "
                            + f"{info_pikachu[level_pikachu][2]}".rjust(3)
                            + info_bar[frame]
                            + (info_pokemons[battle_number][0] + " " + info_pokemons[battle_number][1]).ljust(20)
                            + "LVL:"
                            + f"{info_pokemons[battle_number][2]}".rjust(3) + " ")
                    elif frame == 2:
                        print(" HP:" + "▓" * int((info_pikachu[level_pikachu][3] * 15) / info_pikachu[level_pikachu][4])
                              + "░" * (15 - (int((info_pikachu[level_pikachu][3] * 15) /
                                                 info_pikachu[level_pikachu][4]))) + " "
                              + (f"{info_pikachu[level_pikachu][3]}"
                                 + "/" + f"{info_pikachu[level_pikachu][4]}").center(7)
                              + info_bar[frame]
                              + "HP:" + "▓" * int((info_pokemons[battle_number][3] * 15)
                                                  / info_pokemons[battle_number][4])
                              + "░" * (15 - (int((info_pokemons[battle_number][3] * 15)
                                                 / info_pokemons[battle_number][4])))
                              + " " + (
                                          f"{info_pokemons[battle_number][3]}" + "/"
                                          + f"{info_pokemons[battle_number][4]}").center(
                            7) + " ")
                    else:
                        print(info_bar[frame])

                for texture in range(len(pikachu_texture)):
                    print(pikachu_texture[texture].ljust(43, "█")
                          + texture_pokemons[battle_number][texture].rjust(43, "█"))

                time.sleep(0.2)

            while in_game:
                os.system("clear")

                for frame in range(len(info_bar) - 1):

                    if frame == 1:
                        print(" " + (info_pikachu[level_pikachu][0] + " " + info_pikachu[level_pikachu][1]).ljust(20)
                              + "LVL:" + f"{info_pikachu[level_pikachu][2]}".rjust(3)
                              + info_bar[frame]
                              + (info_pokemons[battle_number][0] + " " + info_pokemons[battle_number][1]).ljust(20)
                              + "LVL:"
                              + f"{info_pokemons[battle_number][2]}".rjust(3) + " ")
                    elif frame == 2:
                        print(" HP:" + "▓" * int((info_pikachu[level_pikachu][3] * 15) / info_pikachu[level_pikachu][4])
                              + "░" * (15 - (int((info_pikachu[level_pikachu][3] * 15)
                                                 / info_pikachu[level_pikachu][4]))) + " "
                              + (f"{info_pikachu[level_pikachu][3]}" + "/"
                                 + f"{info_pikachu[level_pikachu][4]}").center(7)
                              + info_bar[frame]
                              + "HP:" + "▓" * int((info_pokemons[battle_number][3] * 15)
                                                  / info_pokemons[battle_number][4])
                              + "░" * (15 - (int((info_pokemons[battle_number][3] * 15)
                                                 / info_pokemons[battle_number][4])))
                              + " " + (
                                          f"{info_pokemons[battle_number][3]}" + "/" +
                                          f"{info_pokemons[battle_number][4]}").center(7) + " ")
                    else:
                        print(info_bar[frame])

                if pikachu_attacked:

                    for texture in range(len(pikachu_texture)):
                        print(
                            pikachu_texture[texture].ljust(43, "█")
                            + hurt_texture_pokemons[battle_number][texture].rjust(
                                43, "█"))
                    if event_part == 6:

                        print("╔" + "═" * 84 + "╗")
                        print("║ MAGIKARP ... ".ljust(85) + "║")
                        print("║ Magikarp se seco por estar tanto tiempo fuera del agua...".ljust(85) + "║")
                        print("║" + " " * 84 + "║")
                        print("╚" + "═" * 84 + "╝")
                        time.sleep(3)
                    else:
                        print("╔" + "═" * 84 + "╗")
                        print(("║ PIKACHU USA " + pikachu_attacks[level_pikachu][0][menu_pos].upper()).ljust(
                            77) + info_text.ljust(8)
                              + "║")
                        print("║" + " " * 84 + "║")
                        print("║" + " " * 84 + "║")
                        print("║" + " " * 84 + "║")
                        print("╚" + "═" * 84 + "╝")
                        step = 3
                        time.sleep(0.5)

                    if info_pokemons[battle_number][3] == 0:
                        in_game = False
                        win = True
                        step = 0

                elif opponent_attacked:

                    for texture in range(len(pikachu_texture)):
                        print(
                            pikachu_hurt_texture[texture].ljust(43, "█")
                            + texture_pokemons[battle_number][texture].rjust(43, "█"))
                    print("╔" + "═" * 84 + "╗")
                    print(("║ " + info_pokemons[battle_number][0].upper() + " USA "
                           + POKEMON_ATTACKS[battle_number][0][pokemon_attack].upper()).ljust(77) + info_text.ljust(
                        8) + "║")
                    print("║" + " " * 84 + "║")
                    print("║" + " " * 84 + "║")
                    print("║" + " " * 84 + "║")
                    print("╚" + "═" * 84 + "╝")
                    step = 3
                    time.sleep(0.5)

                    if info_pikachu[level_pikachu][3] == 0:
                        in_game = False
                        step = 0

                elif event_magikarp:
                    for texture in range(len(pikachu_texture)):
                        print(pikachu_texture[texture].ljust(43, "█")
                              + texture_pokemons[battle_number][texture].rjust(43, "█"))
                    if event_part == 0:
                        print("╔" + "═" * 84 + "╗")
                        print("║ MAGIKARP SE SIENTE CONFUNDIDO ".ljust(85) + "║")
                        print("║" + " " * 84 + "║")
                        print("║" + " " * 84 + "║")
                        print("╚" + "═" * 84 + "╝")

                    elif event_part == 1:
                        print("╔" + "═" * 84 + "╗")
                        print("║ MAGIKARP SE SIENTE MAS CONFUNDIDO... ".ljust(85) + "║")
                        print("║ Magikarp comienza a tener calor ".ljust(85) + "║")
                        print("║" + " " * 84 + "║")
                        print("╚" + "═" * 84 + "╝")

                    elif event_part == 2:
                        print("╔" + "═" * 84 + "╗")
                        print("║ MAGIKARP SE SIENTE AUN MAS CONFUNDIDO ".ljust(85) + "║")
                        print("║ Magikarp esta hirviendo del calor ".ljust(85) + "║")
                        print("║" + " " * 84 + "║")
                        print("╚" + "═" * 84 + "╝")

                    elif event_part == 3:
                        print("╔" + "═" * 84 + "╗")
                        print("║ MAGIKARP SE SIENTE MUY MAREADO ".ljust(85) + "║")
                        print("║ Magikarp ESTA ARDIENDO!!!! ".ljust(85) + "║")
                        print("║" + " " * 84 + "║")
                        print("╚" + "═" * 84 + "╝")

                    elif event_part == 4:
                        print("╔" + "═" * 84 + "╗")
                        print("║ MAGIKARP ... ".ljust(85) + "║")
                        print("║" + " " * 84 + "║")
                        print("║" + " " * 84 + "║")
                        print("╚" + "═" * 84 + "╝")
                    step = 5
                    time.sleep(5)
                    event_part += 1
                    event_magikarp = False

                else:
                    for texture in range(len(pikachu_texture)):
                        print(pikachu_texture[texture].ljust(43, "█")
                              + texture_pokemons[battle_number][texture].rjust(43, "█"))

                if step == 1:

                    print("╔" + "═" * 84 + "╗")
                    for attack in range(menu_height):

                        print("║", end="")
                        if attack == menu_pos:
                            print(("►" + pikachu_attacks[level_pikachu][0][attack] + "◄").center(84), end="")
                        else:
                            print(pikachu_attacks[level_pikachu][0][attack].center(84), end="")
                        print("║")
                    print("╚" + "═" * 84 + "╝")

                    menu_selector = readchar.readkey()

                    if menu_selector == "w":
                        menu_pos -= 1
                        menu_pos %= menu_height
                    elif menu_selector == "s":
                        menu_pos += 1
                        menu_pos %= menu_height
                    elif menu_selector == "g":
                        step = 2
                    elif menu_selector == "q":
                        break

                elif step == 2:

                    if menu_pos == 0:
                        action_value = random.randint(pikachu_attacks[level_pikachu][1][0] - 1,
                                                      pikachu_attacks[level_pikachu][1][0]
                                                      + 1)
                        info_pikachu[level_pikachu][3] = info_pikachu[level_pikachu][3] + action_value

                        if info_pikachu[level_pikachu][3] > info_pikachu[level_pikachu][4]:
                            action_value = action_value - (info_pikachu[level_pikachu][3]
                                                           - info_pikachu[level_pikachu][4])
                            info_pikachu[level_pikachu][3] = info_pikachu[level_pikachu][4]
                        info_text = "[+{}HP]".format(action_value)

                        print("╔" + "═" * 84 + "╗")
                        print(("║ PIKACHU USA " + pikachu_attacks[level_pikachu][0][menu_pos].upper()).ljust(77)
                              + info_text.ljust(8) + "║")
                        print("║" + " " * 84 + "║")
                        print("║" + " " * 84 + "║")
                        print("║" + " " * 84 + "║")
                        print("╚" + "═" * 84 + "╝")
                        step = 4
                        time.sleep(2.5)

                        if level_pikachu == 3:
                            event_magikarp = True
                    else:
                        print("╔" + "═" * 84 + "╗")
                        print(("║ PIKACHU USA " + pikachu_attacks[level_pikachu][0][menu_pos].upper()).ljust(85) + "║")
                        print("║" + " " * 84 + "║")
                        print("║" + " " * 84 + "║")
                        print("║" + " " * 84 + "║")
                        print("╚" + "═" * 84 + "╝")
                        time.sleep(2)
                        action_value = (random.randint(pikachu_attacks[level_pikachu][1][menu_pos] - 1,
                                                       pikachu_attacks[level_pikachu][1][menu_pos] + 1))
                        info_pokemons[battle_number][3] = info_pokemons[battle_number][3] - action_value
                        info_text = "[-{}HP]".format(action_value)
                        if info_pokemons[battle_number][3] < 0:
                            info_pokemons[battle_number][3] = 0
                        pikachu_attacked = True

                elif step == 3:
                    os.system("clear")
                    if pikachu_attacked:
                        pikachu_attacked = False
                        step = 4
                    elif opponent_attacked:
                        opponent_attacked = False
                        step = 1

                elif step == 4:
                    pokemon_attack = random.randint(0, len(POKEMON_ATTACKS[battle_number][0]) - 1)
                    print("╔" + "═" * 84 + "╗")
                    print(("║ " + info_pokemons[battle_number][0].upper() + " USA "
                           + POKEMON_ATTACKS[battle_number][0][pokemon_attack].upper()).ljust(85) + "║")
                    print("║" + " " * 84 + "║")
                    print("║" + " " * 84 + "║")
                    print("║" + " " * 84 + "║")
                    print("╚" + "═" * 84 + "╝")
                    time.sleep(2)
                    action_value = (random.randint(POKEMON_ATTACKS[battle_number][1][pokemon_attack] - 1,
                                                   POKEMON_ATTACKS[battle_number][1][pokemon_attack] + 1))
                    info_pikachu[level_pikachu][3] = info_pikachu[level_pikachu][3] - action_value
                    info_text = "[-{}HP]".format(action_value)
                    if info_pikachu[level_pikachu][3] < 0:
                        info_pikachu[level_pikachu][3] = 0
                    opponent_attacked = True

                elif step == 5:
                    if event_part == 5:
                        event_part += 1
                        info_pokemons[battle_number][3] = 0
                        pikachu_attacked = True
                    else:
                        step = 1
            time.sleep(3)
            os.system("clear")

            if win and level_pikachu == 3:
                print("╔" + "═" * 84 + "╗")
                print("║" + "VICTORIA".center(84) + "║")
                print("║" + " " * 84 + "║")
                for medal in medal_texture:
                    print("║" + f"{medal}".center(84) + "║")
                print("║" + " " * 84 + "║")
                print("║" + "Felicidades, ganaste a todos los entrenadores".center(84) + "║")
                print("║" + "Gracias por jugar".center(84) + "║")
                print("╚" + "═" * 84 + "╝")
                end_game = True

            elif win:
                level_pikachu += 1
                pokemon_trainers.remove([my_coord[X_AXIS], my_coord[Y_AXIS]])
                print("╔" + "═" * 84 + "╗")
                print("║" + "VICTORIA".center(84) + "║")
                print("║" + " " * 84 + "║")
                print("║" + "TU PIKACHU AH SUBIDO DE NIVEL".center(84) + "║")
                print("║" + " " * 84 + "║")
                print("║" + ("Nivel: " + f"{info_pikachu[level_pikachu-1][2]}".ljust(2) + " → " +
                      f"{info_pikachu[level_pikachu][2]}").center(84) + "║")
                print("║" + ("Vida : " + f"{info_pikachu[level_pikachu - 1][3]}".ljust(2) + " → " +
                             f"{info_pikachu[level_pikachu][3]}").center(84) + "║")
                print("║" + " " * 84 + "║")
                print("║" + ("┌" + "─"*15 + "┬" + "─"*15 + "┐").center(84) + "║")
                print("║" + ("│" + "ATAQUES".center(15) +"│"+ "DAÑO/CURA".center(15) +"│").center(84) + "║")
                print("║" + ("├" + "─" * 15 + "┼" + "─" * 15 + "┤").center(84) + "║")
                for attack in range(len(pikachu_attacks[level_pikachu][0])):
                    print("║" + ("│" + f"{pikachu_attacks[level_pikachu][0][attack]}".center(15) + "│"
                          + f"{pikachu_attacks[level_pikachu][1][attack]}".center(15) + "│").center(84) + "║")
                print("║" + ("└" + "─" * 15 + "┴" + "─" * 15 + "┘").center(84) + "║")
                print("╚" + "═" * 84 + "╝")

            else:
                print("╔" + "═" * 84 + "╗")
                print("║" + " " * 84 + "║")
                print("║" + "DERROTA".center(84) + "║")
                print("║" + " " * 84 + "║")
                print("╚" + "═" * 84 + "╝")

            input("Presiona Enter para continuar...")

    if new_position:
        if map_definition[new_position[Y_AXIS]][new_position[X_AXIS]] != "#":
            my_coord = new_position
