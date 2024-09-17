﻿define higher_center = Position(xalign=0.5, yalign=0.3)
# Declare characters used by this game. The color argument colorizes the
# name of the character.



define me = Character("...")
define anon = Character("???")
define jd = Character("Juan Doble Jr.")
define mc = Character("[player]")
define ga = Character("Gardel Amarilla")
define jm = Character("Julia Maidana")
define pc = Character("Pesto Camogli")

#-Imagenes
#Fondos
image bg negro= "images/bg/black.jpg"
image ph bg= im.Scale("images/bg/phbg.png", 1920, 1080)
image autoin= im.Scale("images/bg/autointesc.png", 1920, 1080)
image esc= im.Scale("images/bg/escuela.png", 1920, 1080)
#Personajes
image Juan doble jr neutro = "images/plhjuanjr.png"
image gardel neutro = im.Scale("images/plhgardel.png", 500, 900)
image julia neutra = im.Scale("images/plhjulia.png", 500, 900)
image pesto neutro = im.Scale("images/plhpesto.png", 600, 900)

#Variables en el sentido mas crudo posible:

default bathroom_visited = False
default polideportivo_visited = False
default pasillos_visited = False
default comedor_visited = False
default reputacion = 0

# The game starts here.

label start:

    stop music


    scene bg negro with dissolve

    # Play sound effect
    play sound "audio/carpark.wav" channel "sound"

    pause 4.5
    #Esto es cuando ve la escuela desde el auto
    scene autoin with dissolve     
    me "Se ve… anticuado?"
    anon "Chau cuidate!"
    scene esc with dissolve 
    me "Chau..."
    play sound "audio/carclose.wav"
    pause 1
    show Juan doble jr neutro at center with dissolve
    pause 0.7
    jd "¡Hola! ¿Cómo estás?"
    play music "audio/OST/1.mp3"
    jd "Soy el preceptor Juan, estoy encargado de mantener el orden en los salones y pasillos."
    jd "Podés acudir a mi si tenés algún problema, si me querés avisar algo o si tenés algún chisme. Estoy abierto a todo, con tal de sobrevivir a este trabajo."
    jd "Por las dudas, como te llamabas?"
    $ player = renpy.input("Como te llamas?")
    $ player = player.strip()
    if player == "":
        $ player = "El original"
    if player.lower() in ["pomni", "digital rizz"]:
        "when digital circus"
    if player.lower() in ["rizz", "skibidi", "chamba"]:
        "Arregla tu humor."
    if player.lower() in ["pintos"]:
        "Más vale que no me estes usurpando la identidad"
    if player.lower() in ["peron"]:
        "Chori?"
    mc "Hola! Me llamo [player]"
    jd "Bueno [player], acordate que cualquier cosa buscame que te ayudo."

    hide Juan doble jr neutro

    "A donde queres ir?"

label deciciones:

    menu:
        "Baño" if not bathroom_visited:
            "Entras al baño"
            "Te lavas la cara y sales. Te parece incómodo hablar con gente en el baño con acústica de fluidos corporales ajenos"
            $ bathroom_visited = True
            jump deciciones
        "Polideportivo" if not polideportivo_visited:
                    "Entras al polideportivo"
                    "Te encuentras con Gardel Amarilla, un alumno que pasa el 70%% de su tiempo escolar en el polideportivo."
                    show gardel neutro
                    ga "¡Eeeh! ¡Uno nuevo! ¿Qué onda? ¿Cómo te llamás…?"
                    
                    menu:
                        "¡Hola! Soy [player]. ¿Todo bien?":
                            ga "¡Así me gusta! ¿Estas para un básquet después del colegio?"
                            mc "Puede ser..."
                        "Me llamo [player]":
                            ga "Bueno [player]…¿Te gusta el basquet? Vení después de la escuela acá, así jugamos con los vagos"
                            mc "Veo..."
                        "¿Qué te importa?":
                            ga "¡Boee! Tranqui nomas, che. Estamos en familia acá, cuando quieras, vení y jugamos."
                            mc "(¿Será que piensa en algo mas que basket?)"
                    mc "Bueno, nos vemos."
                    $ polideportivo_visited = True
                    hide gardel neutro
                    jump deciciones
                            
        "Pasillos de la derecha" if not pasillos_visited:
            "Te encontras en los pasillos"
            "Recorres los pasillos y te encuentras con Julía Maidana."
            show julia neutra
            jm "¡Holaaa! ¿Vos sos el nuevo? ¿Cómo estás? Soy Juli Maidana…"
            $ renpy.music.set_volume(0.0)
            jm "..." 
            pause 4
            $ renpy.music.set_volume(1.0)
            jm "¿Tenés comida?"
            menu:
                "¡Hola! Soy [player], un gustazo… No, no tengo comida, también me cago de hambre.":
                    jm "Pucha, nadie tiene comida acá. Así no se puede."
                    jm "Ja"
                    jm "ja"
                    jm "ja."
                    jm "..."
                    pause 1
                
                "Holaa, si, ingresé la semana pasada a este colegio… Creo que si tuviera comida no te invitaría.":
                    jm "Owwww… ¿Por qué así ? *Llora * Te prometo que cuando tenga comida te convido."
                
                "Hola. No me toques, muerta de hambre.":
                    jm "¡Paraaa, fofro! Está bien, andate nomás."
           
            hide julia neutra
            mc "(Como se nota que es una escuela publica esto...)"
            $ pasillos_visited = True
            jump deciciones
        "Comedor" if not comedor_visited:
            "Vas al comedor"
            "Recorres los pasillos de la izquierda hasta llegar al comedor, ya ahí te topas con Pesto Camogli, un alumno que siempre tiene comida y Coca-Cola"
            show pesto neutro
            pc "Fua loco mira tengo una coca en una mano AAAA ME GENERO UNA IA SOCORRO"
            $ comedor_visited = True
            hide pesto neutro
            jump deciciones
    


