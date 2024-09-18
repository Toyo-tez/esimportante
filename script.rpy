define higher_center = Position(xalign=0.5, yalign=0.3)
# Declare characters used by this game. The color argument colorizes the
# name of the character.



define me = Character("...")
define anon = Character("???")
define jd = Character("Juan Doble Jr.")
define mc = Character("[player]")
define ga = Character("Gardel Amarilla")
define jm = Character("Julia Maidana")
define pc = Character("Pesto Camogli")
define da = Character("Directora")
define gm = Character("Gerónimo Mangel")
define iv = Character("Ivan Vergara")
define ra = Character("Reviro Arandano")
define ms = Character("Marcos Sebatti")
define ivsch = Character("Iviene Schamba")
define ch = Character("Chofer")

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
image dire neutra = "images/plhdire.png"
image ivan neutro = "images/plhivn.png"

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
            "Entras al comedor"
            "A tu izquierda ves la fila mas larga que haz visto en tu vida."
            "Te acercas y notas que era una fila para el kiosko del colegio. Te acercas aun más, y desafortunadamente justo delante tuyo, el chico frente a tí da un paso hacia atrás…"
            show pesto neutro with dissolve
            pc "Uy, perdoname, no te vi. ¡Viva Perón! Oh…Perdón, es un TOC mio, cada que me pongo nervioso grito “Viva Perón”."
            mc "No no, tranquilo, no tengo drama. ¿Puedo preguntar…? ¿Por qué tienes 8 botellas de Coca en tus manos y seguís en la fila ?"
            pc "Tengo una adicción controlada. ¡Viva Perón! ... nada de qué preocuparse."
            menu: 
                "Sos una persona interesante. ¡Nos vemos después, un gusto!":
                    pc "Nos vemos crack. Un gusto también"
                "Si vos lo decís…":
                    pc "Vos siempre confía en mí ¡Viva Perón!"
                "Un circo hay acá montado. Muertos de hambre, basquetbolistas y adictos. ¿Qué más podría pedir?":
                    pc " Y si, flaco, desde que mi abuelo no está aca esta escuela es como un filtro de raros. Somos el filtro de los raros de Posadas, para dejar libres de raros a las otras ¡Viva Perón! …escuelas."
            $ comedor_visited = True
            hide pesto neutro
            mc "(...?)"
            jump deciciones

label nose:
    play sound "audio/Silbato.wav"
    pause 0.3
    jd "¡¡¡¡¡Pasen!!!!!!"
    "Todos los alumnos rápidamente agarran sus mochilas tiradas en el suelo y se mueven cual hormigas desesperadas por un grano de azúcar en Itaembé."
    "Sigues a la multitud y ves que todos se dirigen al polideportivo."
    "Al llegar notás que el polideportivo está dividido por secciones donde los alumnos de cada curso se tienen que formar."
    "Cuando todos ya estaban formados, Juan Doble Jr. se posiciona en el centro de todas las filas…"
    pause 0.5
    show Juan doble jr neutro with dissolve 
    jd "Hola, alumnos."
    jd "Bienvenidos a la escuela Secundaria de Innovación."
    jd "Estamos muy contentos de que hayan elegido esta escuela. Lo que estamos haciendo ahora, vamos a tener que hacerlo todos los días antes de ingresar a clases."
    jd "Sin más preámbulos, la Directora pasará a izar la bandera."
    hide Juan doble jr neutro
    "Un silencio super incómodo y duradero se hace presente en el inmenso eco del polideportivo."
    "Cuando la Directora entra nuevamente al polideportivo, comienza a decir unas palabras…"
    show dire neutra with dissolve
    da "Bueno, alumnos. Como dijo el director Juan… Estamos super felices de su elección e interés por nuestra escuela."
    da "Por favor, les pedimos respeto hacia los profesores, preceptores y hacia el personal en general. En especial vos, Mangel"
    gm "¡Vos sabés que no fue mi culpa! ¡El conserje me miró mal primero! ¡No es mi culpa haberle dejado monotributista de un zapatazo!"
    da "¡Bueno! Pasado es pasado. En cuestión, sean respetuosos, y nuevamente, muchas gracias por elegir nuestra institución."
    hide dire neutra with dissolve
    "Un vago aplauso se hizo lentamente presente en el polideportivo, mientras que la Directora sale."
    show Juan doble jr neutro with dissolve
    jd "Bueno chicos, traten de no juntarse con Mangel."
    jd "Mientras se tenga eso en claro, no va a haber problema. Si ya terminamos con las aclaraciones, estos son sus cursos…"
    hide Juan doble jr neutro with dissolve
    mc "Interesante… Los cursos no son los mismos siempre, cambian depende de la materia. ¡Bueno, un punto bueno tenia que tener este lugar!"
    "Curso por curso se van apretando cual sardinas entre 3 puertas. Son 300 pibes tratando de pasar por 4 metros de puerta."
    mc "(Ok… Invernadero. Suena a un curso decente.)"
    "Llegas al curso y te das cuenta que lo mejor que tiene aparte del sol directo en las mesas es que no tenes que pedir para salir a cargar agua por las 3 piletas al fondo."
    "Te sentás en la mesa mas al fondo, para tener a la mano el agua potable para soportar la hora y media de clase."
    "Nadie se sienta en tu mesa."
    "Hasta que llega un chico…"
    show ivan neutro with dissolve
    anon "¡Holaaa! ¿Todo bien?"
    mc " Hola. Si, si, todo bien ¿Y vos?"
    iv "No, no tuve tiempo de ir al baño antes de que suene el grito ese"
    menu:
        "Dios te ampare, hermano.":
            iv "Amén."
        "No tenía ganas de saber eso. Podes preguntarle al profe si podes pasar al baño antes de que comience a dar clases.":
            iv "Si, ya venía pensando en eso…"
        "Que me importa lo mucho que te haces encima. Perdón, pero no me interesa.":
            iv "Uy, perdon, hablo muchisimo. perdón si te incomodé."
            mc "No pasa nada."
    iv "Yyyy… ¿Cómo te llamás?"
    menu:
        "Me llamo [player]. Lo sé, un feo nombre":
            iv "Y… no es el mejor nombre, pero cumple su función."
            mc "No te entiendo"
            iv "Pocos lo hacen. Solo los entendidos."
        "Soy [player]":
            iv "Bueno, [player], vas a tener que aguantarme."
            iv "Creo que voy a sobrevivir."
        "Soy [player], pero no me llames así en público.":
            iv "No hay drama, entiendo que te moleste tu nombre, imaginate cuando gritan mi apellido en público."
    hide ivan neutro with dissolve
    #aca aparece el dire viejo
    mc "¿Quién es? -dijo susurrando- Se me hace conocid-"
    show pesto neutro with dissolve
    pc "VIVA PERON! Es el ministro de educación -respondió desde la mesa del costado- Reviro Arándano. Viene a acá cada tanto."
    hide pesto neutro with dissolve
    anon "¡¡Silencio!! Ya callense, dejen de susurrar allá atrás. No puede ser que siempre haya tanta alta de respeto. Ahora ¡Escuchen! El ministro de educación va a decir unas palabras…"
    show Juan doble jr neutro with dissolve
    jd "Ow, yo quería gritarles para que se callen 🙁"
    hide Juan doble jr neutro with dissolve
    ra "H-hola a-alumnos d-de e-esta e-escuela…"
    ra "*Inhala fuerte y mocosamente *"
    ra " Y-yo s-soy e-el m-ministro d-de"
    ra "*tose y tose *"
    ra "¡Educación!"
    ra "Me encanta venir a ver cuales son las nuevas caras de cada año. Amo ver las nuevas generaciones desde el primer día."
    mc "(Nos está mirando super extraño me hace sentir incómodo.)"
    ra " Me alegra saber que hay interés por la educación todavía, recuerden chicos que esto es un empuje hacia su vida laboral, a lo que la educación debe apuntar si me lo preguntan a mi."
    ra "Así que, sientanse orgullosos sobre su elección de venir a la escuela. Con eso dicho, disfruten su segundo año en este colegio. ¡Espero nos veamos pronto!"
    "El preceptor, luego del fin del discurso del ministro, lo sostiene de un brazo y lo acompaña a la puerta de salida."
    anon "Buenooooo, silenciooo"
    mc "(Nadie está hablando...)"
    anon "Soy el profesor Marcos Sebatti. Soy el profesor de programación, yo no jodo con nadie, así que ¡Ya! ¡Saquen sus carpetas y ponganse a escribir el título!"
    show ivan neutro
    iv "¿Qué título?"
    hide ivan neutro
    ms "¡A mí me hablas con respeto! ¡Qué ansiedad manejan las generaciones de ahora, por Buda! Ya proyecto la diapositiva."
    "Después de una hora y media de estar copiando conceptos en la carpeta, todos se sentían exhaustos, y apenas eran las 8:20 de la mañana."
    "En el primer recreo, todos hicieron una ronda involuntaria en la entrada del Invernadero…"
    show pesto neutro with dissolve
    pc "¡Dios! ¡Qué cansado estoy! Apenas la primera hora y media y ya me quedé sin hojas, tienta y ganas de seguir formando parte del sistema educacional."
    anon "Mal, Pesto. No puedo más."
    pc "Me quiero ir. ¡Pará! ¿Cómo es tu nombre? ¿y cómo sabes el mio?"
    show pesto neutro at left with easeinright
    anon "Soy Iviene Schamba. Me puedes llamar “Chofer”. Es mi apodo."
    show pesto neutro with dissolve
    pc "Qué buen apodo, loco. Chofer."
    ch "Gracias, igual tus halagos no me van a sacar las ganas de estar en mi casa y dormir."
    menu:
        "Qué desperdicio de hora. Nunca volveré a pensar en este contenido de cuarta":
            show pesto neutro with dissolve
            pc "No puedo estar más de acuerdo. Pero bueno, hay que aguantar como el profe nos aguanta."
            menu:
                "Y si, puede que tengas razón.":
                    pc "Y…De igual manera nos los tenemos que fumar."
                "Él eligió ser profesor. le pagan por aguantarnos.":
                    pc "Y…De igual manera nos los tenemos que fumar."
                "¿Qué me importa?":
                    pc "Y…De igual manera nos los tenemos que fumar."
            
        "¿Cómo llegué a pensar que esta escuela valía la pena?":
            show pesto neutro at left with easeinright
            show julia neutra at right with dissolve
            jm "Todos pensamos eso"
        "No voy a aguantar hasta el primer trimestre.":
            show ivan neutro
            iv "Nadie va a aguantar"
            ivsch "Vamos a ir desapareciendo uno por uno"
    
    show pesto neutro at left with dissolve
    show julia neutra at right with dissolve
    show ivan neutro
    pause 3
    mc "Me voy a ir a llorar afuera, en el camino planeo arrepentirme de todos mis pecados."
    hide julia neutra
    hide pesto neutro
    hide ivan neutro
    "Me dirigí hacia los baños y me di cuenta que el patio es enorme. Emprendí mi largo viaje hacia los tanques de agua, donde hice mis berrinchitos."
    mc "Yo no quiero venir más a este lugar ¡Hay gente rara, viejos mugrosos y basquetbolistas! No voy a aguantar. No es justo."
    mc "Nadie es más inteligente que yo ¿y me tengo que bancar a todos estos subdesarrollados? -Dije mientras patee un palo de madera que parecía parte desechada de las barandas."
    "Al caer el palo sonó un ruido metálico en la tierra."
    mc "¿Que es eso?"
    "Agarré el mismo palo el cual traté como me gustaría tratar a José de Calasanz y comencé a escarbar la tierra como un K-9 buscando azucar."
    "Seguí hasta que sentí que ya no había más tierra, sino una superficie hueca."
    "Continué excavando y era un tipo de botella, le di la vuelta y tenía un nombre grabado “Cápsula del tiempo 2024”"
    mc "¡Vaya por Dios! ¡Seré rico! ¡Pueden haber monedas antiguas valoradas en dólares! ¡Puede haber tecnología, declaraciones, COMIDA!"
    "Cuando la abrí con ayuda del palo, vi únicamente unas pulseras de la amistad, dos fotos viejas y medio mojadas, una carta y sticker del personaje clásico de una de las mejores series de la historia: Pomni."
    mc "¡Já! Se ve que dar malos regalos es algo más que generacional en Argentina, ya cuenta como algo biológico en nuestro ADN!"

    
    


return