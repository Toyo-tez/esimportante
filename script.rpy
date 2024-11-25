#Easter-eggs
define digital = ["pomni", "kinger", "jax", "caine"]
define humor = ["rizz", "skibidi", "toilet","sigma","mewing", "mewin", "ruben tuesta", "chamba"]
define maidana = ["sofia", "sofi", "sofi maidana"]
define camogli = ["camogli", "camougli", "camo", "martin camogli", "martín camogli"]
define pacheco = ["fio", "fiore", "pacheco", "fiorella"]
define amarilla = ["amarilla", "samu", "samuel"]
define schoffen = ["schofen", "schoffen", "sebastian"]
define vargas = ["ivan", "vargas", "ivi", "ivisigma", "ivandelta"]
#Posiciones
define higher_center = Position(xalign=0.5, yalign=0.9)
define almost_right = Position(xalign=0.7)
define lower_right = Position(xpos=0.9, ypos=1.45)
define almost_left =Position(xalign=0.4)
define seba =Position(xalign=0.9, ypos=1.45)
define ivanaula=Position(xalign=0.8, ypos=0.78)
define reviroaula=Position(xalign=0.5, ypos=0.61)
define marcosaula=Position(xalign=0.42, ypos=0.7)
define higher_right=Position(xalign=0.9, ypos=0.75)
define catastrofeaula= Position(xalign=0.42, ypos=0.6)
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
define ms = Character("Marcela Secatti")
define ivsch = Character("Iviene Schamba")
define ch = Character("Chofer")
define pg = Character("Pionera Gallego")
define cp = Character("Catástrofe Pastos")
define vf = Character("Viviana Forrales")
define mujer1 = Character("Mujer Random")
define hombre1 = Character("Hombre Random")
define operadora = Character("911")
define policia1 = Character("Oficial")

#-Imagenes
#Fondos
image bg negro= "images/bg/black.jpg"
image ph bg= im.Scale("images/bg/phbg.png", 1920, 1080)
image autoin= im.Scale("images/bg/autointesc.png", 1920, 1080)
image esc= im.Scale("images/bg/escuela.png", 1920, 1080)
image pasillos= im.Scale("images/bg/pasillos.jpeg", 1920, 1080)
image formacion=im.Scale("images/bg/formacion.jpeg", 1920, 1080)
image poli=im.Scale("images/bg/poli.jpeg", 1920, 1080)
image aula=im.Scale("images/bg/aula.jpeg", 1920, 1080)
image patio=im.Scale("images/bg/patiouwu.jpg", 1920, 1080)
image sotano= im.Scale("images/bg/fondosotano.jpg", 1920, 1080)
#Personajes
image Juan doble jr neutro = "images/plhjuanjr.png"
image gardel neutro = im.Scale("images/plhgardel.png", 500, 900)
image julia neutra = im.Scale("images/plhjulia.png", 500, 900)
image pesto neutro = im.Scale("images/plhpesto.png", 600, 900)
image pesto aula = im.Scale("images/plhpesto.png", 350, 600)
image dire neutra = "images/plhdire.png"
image ivan neutro = "images/plhivn.png"
image ivan aula = im.Scale("images/plhivn.png", 300, 600)
image reviro neutro = im.Scale("images/plhreviro.png", 500, 900)
image reviro aula = im.Scale("images/plhreviro.png", 120, 240)
image schamba neutro = im.Scale ("images/plhesch.png", 450, 1400)
image marcos aula = im.Scale("images/plhseba.png", 120, 390)
image pionera = im.Scale("images/pionera.png", 900, 900)
image catastrofe aula =im.Scale("images/profegeo.png", 120, 230)

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
    if any(keyword in player.lower() for keyword in digital):
        "when digital circus"
    if any(keyword in player.lower() for keyword in humor):
        "Arregla tu humor."
    if player.lower() in ["pintos"]:
        "Más vale que no me estes usurpando la identidad"
    if player.lower() in ["peron"]:
        "Chori?"
    if player.lower() in ["fio", "fiore", "pacheco", "fiorella",]:
        "Un nombre bastante homosexual"
    if player.lower() in ["ivan", "vargas", "ivi", "ivisigma", "ivandelta"]:
        "Probablemente sos femboy no?"
    if player.lower() in ["chapa", "chapa-women", "barrios", "Chillko"]:
        "Rebota las balas 🗣️‼️"
    if player.lower() in ["lautanga", "obregon", "mautaro", "lautaro"]:
        "Te-te-te-te-te-teto"
    if player.lower() in ["jereeeuva", "jereuva", "jere", "jeremias"]:
        "Vos escribiste esta aberracion?"
    if player.lower() in ["zac50sld", "schofen", "schoffen", "sebastian"]:
        "TU ABUELO SE COMIO UN TRAVA AJSJASJASJ"
    if player.lower() in ["damian", "rivas", "marco", "marcman", "Kroogen13", "Kroogen"]:
        "1-0 AJAJJAJAJAJ"
        "1-0 AJAJJAJAJAJ, a donde quedo boca"
    if player.lower() in ["sofia", "sofi", "sofi maidana"]:
        "Fofro"
    if player.lower() in ["camogli", "camougli", "camo", "martin camogli", "martín camogli"]:
        "VIVA PERON"
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
                    scene poli with dissolve
                    "Entras al polideportivo"
                    "Te encuentras con Gardel Amarilla, un alumno que pasa el 70%% de su tiempo escolar en el polideportivo."
                    show gardel neutro
                    ga "¡Eeeh! ¡Uno nuevo! ¿Qué onda? ¿Cómo te llamás…?"
                    
                    menu:
                        "¡Hola! Soy [player]. ¿Todo bien?":
                            if any(keyword in player.lower() for keyword in amarilla):
                                ga "Tenes el mismo nombre que mi abuelo!"
                            ga "¡Así me gusta! ¿Estas para un básquet después del colegio?"
                            mc "Puede ser..."
                        "Me llamo [player]":
                            if any(keyword in player.lower() for keyword in amarilla):
                                ga "Tenes el mismo nombre que mi abuelo!"
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
            scene pasillos with dissolve
            "Te encontras en los pasillos"
            "Recorres los pasillos y te encuentras con Julía Maidana."
            show julia neutra
            jm "¡Holaaa! ¿Vos sos el nuevo? ¿Cómo estás? Soy Juli Maidana…"
            $ renpy.music.set_volume(0.0)
            jm "..." 
            pause 3.5
            $ renpy.music.set_volume(1.0)
            jm "¿Tenés comida?"
            menu:
                "¡Hola! Soy [player], un gustazo… No, no tengo comida, también me cago de hambre.":
                    if any(keyword in player.lower() for keyword in maidana):
                        jm "Weee, tenes el mismo nombre que mi abuela!"
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
            mc "No no, tranquilo, no tengo drama. ¿Puedo preguntar…? ¿Por qué tienes 8 botellas de Coca en tus manos y seguís en la fila?"
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
    scene poli with dissolve
    "Al llegar notás que el polideportivo está dividido por secciones donde los alumnos de cada curso se tienen que formar."
    "Cuando todos ya estaban formados, Juan Doble Jr. se posiciona en el centro de todas las filas…"
    scene formacion with dissolve
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
    scene aula with dissolve
    "Llegas al curso y te das cuenta que lo mejor que tiene aparte del sol directo en las mesas es que no tenes que pedir para salir a cargar agua por las 3 piletas al fondo."
    "Te sentás en la mesa mas al fondo, para tener a la mano el agua potable para soportar la hora y media de clase."
    "Nadie se sienta en tu mesa."
    "Hasta que llega un chico…"
    show ivan aula at ivanaula with dissolve
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
            if any(keyword in player.lower() for keyword in vargas):
                iv "Pero tenes el mismo nombre que mi abuelo!"
            iv "Y… no es el mejor nombre, pero cumple su FUNCIÓN."
            mc "No te entiendo"
            iv "Pocos lo hacen. Solo los entendidos."
        "Soy [player]":
            if any(keyword in player.lower() for keyword in vargas):
                iv "El mismo nombre que mi abuelo!"
            iv "Bueno, [player], vas a tener que aguantarme."
            iv "Creo que voy a sobrevivir."
        "Soy [player], pero no me llames así en público.":
            if any(keyword in player.lower() for keyword in vargas):
                iv "Uh, te llamas igual que mi abuelo"
            iv "No hay drama, entiendo que te moleste tu nombre, imaginate cuando gritan mi apellido en público."
    hide ivan neutro with dissolve
    show reviro aula at reviroaula with dissolve
    pause 1.5
    mc "¿Quién es? -dijo susurrando- Se me hace conocid-"
    hide reviro neutro
    show pesto aula at ivanaula
    pc "VIVA PERON! Es el ministro de educación -respondió desde la mesa del costado- Reviro Arándano. Viene a acá cada tanto."
    hide pesto neutro with dissolve
    anon "¡¡Silencio!! Ya callense, dejen de susurrar allá atrás. No puede ser que siempre haya tanta alta de respeto. Ahora ¡Escuchen! El ministro de educación va a decir unas palabras…"
    show Juan doble jr neutro with dissolve
    jd "Ow, yo quería gritarles para que se callen 🙁"
    hide Juan doble jr neutro with dissolve
    show reviro neutro with dissolve
    ra "H-hola a-alumnos d-de e-esta e-escuela…"
    ra "*Inhala fuerte y mocosamente *"
    ra " Y-yo s-soy e-el m-ministro d-de"
    ra "*tose y tose *"
    ra "¡Educación!"
    ra "Me encanta venir a ver cuales son las nuevas caras de cada año. Amo ver las nuevas generaciones desde el primer día."
    mc "(Nos está mirando super extraño me hace sentir incómodo.)"
    ra " Me alegra saber que hay interés por la educación todavía, recuerden chicos que esto es un empuje hacia su vida laboral, a lo que la educación debe apuntar si me lo preguntan a mi."
    ra "Así que, sientanse orgullosos sobre su elección de venir a la escuela. Con eso dicho, disfruten su segundo año en este colegio. ¡Espero nos veamos pronto!"
    hide reviro neutro with dissolve
    "El preceptor, luego del fin del discurso del ministro, lo sostiene de un brazo y lo acompaña a la puerta de salida."
    show marcos aula at marcosaula with dissolve
    anon "Buenooooo, silenciooo"
    mc "(Nadie está hablando...)"
    anon "Soy el profesor Marcela Secatti. Soy el profesor de programación, yo no jodo con nadie, así que ¡Ya! ¡Saquen sus carpetas y ponganse a escribir el título!"
    iv "¿Qué título?"
    ms "¡A mí me hablas con respeto! ¡Qué ansiedad manejan las generaciones de ahora, por Buda! Ya proyecto la diapositiva."
    "Después de una hora y media de estar copiando conceptos en la carpeta, todos se sentían exhaustos, y apenas eran las 8:20 de la mañana."
    "En el primer recreo, todos hicieron una ronda involuntaria en la entrada del Invernadero…"
    hide marcos aula
    show pesto neutro with dissolve
    pc "¡Dios! ¡Qué cansado estoy! Apenas la primera hora y media y ya me quedé sin hojas, tinta y ganas de seguir formando parte del sistema educacional."
    anon "Mal, Pesto. No puedo más."
    pc "Me quiero ir. ¡Pará! ¿Cómo es tu nombre? ¿y cómo sabes el mio?"
    show pesto neutro at left with easeinright
    show schamba neutro at lower_right with easeinright
    anon "Soy Iviene Schamba. Me puedes llamar “Chofer”. Es mi apodo."
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
            show julia neutra at almost_right with dissolve
            jm "Todos pensamos eso"
        "No voy a aguantar hasta el primer trimestre.":
            show ivan neutro
            iv "Nadie va a aguantar"
            ivsch "Vamos a ir desapareciendo uno por uno"
    
    show pesto neutro at left with dissolve
    show julia neutra at almost_right with dissolve
    show ivan neutro at almost_left
    pause 3
    mc "Me voy a ir a llorar afuera, en el camino planeo arrepentirme de todos mis pecados."
    hide julia neutra
    hide pesto neutro
    hide ivan neutro
    hide schamba neutro
    "Me dirigí hacia los baños y me di cuenta que el patio es enorme. Emprendí mi largo viaje hacia los tanques de agua, donde hice mis berrinchitos."
    scene patio with dissolve
    mc "Yo no quiero venir más a este lugar ¡Hay gente rara, viejos mugrosos y basquetbolistas! No voy a aguantar. No es justo."
    mc "Nadie es más inteligente que yo ¿y me tengo que bancar a todos estos subdesarrollados? -Dije mientras patee un palo de madera que parecía parte desechada de las barandas."
    "Al caer el palo sonó un ruido metálico en la tierra."
    mc "¿Que es eso?"
    "Agarré el mismo palo el cual traté como me gustaría tratar a José de Calasanz y comencé a escarbar la tierra como un K-9 buscando azucar."
    "Seguí hasta que sentí que ya no había más tierra, sino una superficie hueca."
    "Continué excavando y era un tipo de botella, le di la vuelta y tenía un nombre grabado “Cápsula del tiempo 2024”"
    mc "¡Vaya por Dios! ¡Seré rico! ¡Pueden haber monedas antiguas valoradas en dólares! ¡Puede haber tecnología, declaraciones, COMIDA!"
    "Cuando la abrí con ayuda del palo, vi únicamente unas pulseras de la amistad, dos fotos viejas y medio mojadas, una carta y sticker del personaje clásico de una de las mejores series de la historia: Pomni."
    if any(keyword in player.lower() for keyword in digital):
        mc "(Mis papas me pusieron el nombre por un personaje de esta serie...)"
        mc "(Todavia no entiendo como se dio mi concepcion considerando eso...)"
    mc "¡Já! Se ve que dar malos regalos es algo más que generacional en Argentina, ya cuenta como algo biológico en nuestro ADN!"
    "Con decepción en tu mente, agarraste las fotos primero para ver de quién se trataba."
    mc "(A ver, quiénes son los inmortalizados…)"
    "Ves la primer foto, notas un conjunto de chicos, 32 en total, posando alegremente con un cartel sobre todas sus cabeza con un mensaje “2022”."
    "La siguiente foto es 2 años después de la primera, era como la primera, pero faltaba una de las chicas que posaban, el cartel con el mensaje “PROMO 2024”  y en el marco de la foto habían notitas como “Te extrañamos” “En memoria de Agus”."
    mc "(¿Agus?... ¿Agustina? ¿Qué le habrá pasado?)"
    mc "(Probablemente haya muerto entre el 2022 y el 2024, teniendo en cuenta el “En memoria de Agus”.)"
    "Dejas a un lado las fotos y te concentras en las pulceras, para ver si tienen algún nombre o inicial."
    mc "(Bah. Son pulseras normales, solo los colores son diferentes.)"
    "Y para dejar lo mejor para el final, agarras finalmente la carta. La abres y lees lo siguiente:"
    "“Nunca pensamos ni imaginamos que tendríamos que  escribir una carta como esta, pero la situación lo amerita. Está carta está escrita por toda la PROMO 2024 en memoria de Agustina..."
    "Fruta traicionera, nos la arrebataste de las manos, era nuestra amiga, nuestra compañera y familia. Entraste para robar e irte. No te lo vamos a perdonar”."
    pause 2.5
    mc "(¿”Entraste para robar”? ¿”Fruta traicionera”? ¿Qué significa esto? ¿Por qué quisieron escribir esto? ¿Con qué utilidad?)"
    "Te quedas pensando encorvado en el suelo sucio del patio casi abandonado de la escuela, tratando de deducir de quien estan hablando y por qué gastarán su tiempo escribiendo una carta asi."
    mc "Claramente, Agustina desapareció o fue asesinada. La carta expresa eso, un robo, un arrebatamiento. Ahora bien, ¿Quién es el culpable? No se si voy a llegar a algo con esta información pero es mejor que estar en la escuela."
    "¿Qué sigue? Es tu primer día de clases y ya estás descubriendo un caso de desaparición. Pero, qué hacer a partir de ahora. Ya tienes la información mínima para empezar un caso de investigación digna de un fiscal, con la diferencia de que sos un nene de 14 años."
    "¿Qué opciones tengo? Aparte de hablarlo con un adulto no creo que sea una mejor idea quedarme acá arrodillado sospechosamente en el patio con objetos que deberían ser investigados o mínimo colgados por ser parte de la historia de inicio de esta escuela."
    "Tengo que guardar esto por ahora, tapar el hueco y disimularlo. Voy a guardar estas cosas en mi mochila mientras pienso a quién contárselo con la certeza de no ser uno más de los desaparecidos por saber demasiado…"
    "Juntas todas las cosas en uno de los bolsillos de tu mochila y vas para el patio interno de la escuela. Ya ahi, ves que una de tus compañeras está hablando con el prece Juan Doble Jr."
    show pionera at left with dissolve
    show Juan doble jr neutro at higher_right with dissolve
    "Recuerdas que en la clase anterior la profesora Marcela le preguntó su nombre y ella respondió con un “Soy Pionera Gallego”. Te acercas porque el preceptor te pareció agradable y Pionera te cayó bien porque le respondió directamente a la profesora."
    mc "Holaaaa. ¿Qué tal? ¿Puedo meterme a su charla? ¿De qué hablan?"
    pg "Hola broo. Estamos hablando de los chismes de primer año, siempre se mandan las mayores cagadas."
    jd "No, si, si. Son unas plagas. Llegan como gatos a una nueva casa y comienzan a arañar todo. Cada principio de año parece que la escuela se destruye, comienzas a ver focos rotos, los trabas de los baños… AHEM las trabas dejan de funcionar"
    jd "Los vidrios se rompen, las paredes también, de la nada hay agujeros en los techos, todo mal. Es como abrir un baño público en el centro y pensar que no van a robar los rollos de papel, es más, eso pasa acá."
    pg "Ja Ja. Si, si. Son unos rompe iphroda estos. Todas las semanas desaparece algo o se rompe algo. Ja Ja. Y vos… ¿Tenes algún chisme?"
    menu:
        "No se si llamarlo chisme…":
            pg "Boeeeeeee si tiene, si tiene, prece. dale dale, contanos."
        "Nop, no tengo nada, por eso vine a hablar con ustedes.":
            pg "Ja Ja. Primer día y ya sabe con quien ir para ser chismoso. ¡Así me gusta! Pero ¿seguro que no tenes nada para contarnos?"
        "Es mi primer día y ¿pretenden que tenga chismes? ¡Tan aburridas son sus vidas que tienen que rellenarlas con dramas ajenos!":
            pg "¡Y si bro! Si no, ¿Para qué está la escuela? Para dejar de aburrirse de su propia vida. Aun así, ¿no tenes ningun chisme para aportar a nuestro humilde merendero de drama ajeno?"
    mc "Bueeeeeeno. No tengo un chisme como tal, pero tengo indicios de un posible chisme."
    pg "Dale dale, desmenuzalo."
    mc "Bueno, miren. Se que desde el 2019 esta escuela existe. Y según mis papás que vinieron a esta escuela de nenes. Hay una cápsula del tiempo enterrada en el patio. Prece…¿Puede llegar a haber algún proyecto o algo así para encontrar esa cápsula?"
    "Hay un silencio extraño y largamente incomodo en donde el prece mira fijamente al suelo"
    jd "Yo creo que puede haber un proyecto en un futuro, pero dudo muchísimo. Ya que, entre los años 2023 y 2025, hubo una invasión de hormigas y los exterminadores recomendaron no solo fumigar, sino que cambiar el suelo completamente."
    jd "Ergo, sacar toda la tierra contaminada por las hormigas y nuevamente llenar el patio de buena tierra para el jardín y el campus de agronomía."
    mc "Mmmmm. Interesante. ¿Y qué pasa si alguien la encuentra? Digo. Pudo haber quedado bajo tierra."
    jd "Creo yo que si alguien la encuentra, no sería nada bueno…"
    mc "¿Por?"
    jd "Eeeh. Que se yo. Seguramente van a venir los de Canal 12 y no me gusta que estén con las cámaras."
    mc "Aaah. Si, si, entiendo. Tiene sentido. (No lo tiene)"
    pg "Wow. Yo me estoy enterando de todo esto ahora. ¿Cápsula del tiempo? ¡Qué copado! ¿Qué cosas habrá adentro?"
    jd "Ya es hora de pasar a las aulas. * Silbato termonuclear*"
    play sound ("audio/Silbato.wav")
    pause 0.1
    play sound ("audio/Silbato.wav")
    pause 0.1
    play sound ("audio/Silbato.wav")
    pause 0.1
    play sound ("audio/Silbato.wav")
    pause 0.1
    play sound ("audio/Silbato.wav")
    pause 0.1
    play sound ("audio/Silbato.wav")
    pause 0.1
    play sound ("audio/Silbato.wav")
    pause 0.1
    play sound ("audio/Silbato.wav")
    pause 0.1
    play sound ("audio/Silbato.wav")
    pause 0.1
    play sound ("audio/Silbato.wav")
    pause 0.1
    jd "¡Escuchen! 5to A Maker, 5to B laboratorio, 5to C ex-puff, 5to D artística, 5to E Patio, 5to F invernadero, 5to G techo, 5to H comedor, 5to I polideportivo..."
    jd "1ero A informática"
    hide pionera with dissolve
    hide Juan doble jr neutro with dissolve
    "Todos empiezan a moverse hacia sus aulas."
    "Me sente en la mesa cuya población es 0. Hasta que llega Vergara y se sienta a mi lado."
    "(Debería comenzar a hacer amistades, necesito poder contar lo que encontré en el patio. Es útil desquitarse con una amistad, además si me atrapan, arrastro a alguien conmigo.)"
    "(Mmmm. ¿En quién puedo confiar?)"
    "(¿En quién podría comenzar a invertir tiempo para generar una amistad y contárselo todo? Tiene que ser alguien de confianza, que no sea de lengua suelta. Y obvio, que tenga un grado de madurez.)"
    "Mire a Vergara"
    "(Nah. Es de las personas que dice “Mi papa dice que no está”. Así que toca buscar a alguien más…)"
    "(Pionera es buena es buena opción, pero teniendo en cuenta que mi primer acercamiento a ella fue por un chisme, deduzco que ella ya es chismosa, y justamente eso es lo que quiero evitar.)"
    "(Por otro lado, Pesto parece ser copado, pero parece que habla mucho. Me veo obligado a socializar con más gente, que asco.)"

    "Pasa la hora y media de clase y es recreo. Voy directo hacia Doble Jr."
    show Juan doble jr neutro at higher_center with dissolve
    "(Bueno... Él es la única opción por ahora, además parece ser una persona madura y reservada, me viene bien para esta ocasión, pero debo conocerlo más todavía. Probemos hablar con él ahora. A ver qué dice.)"
    mc "Holaa. Volví."
    jd "Hola, alumno. ¿Todo bien?"
    mc "Si si, todo bien. S-solo te queria decir que me pongo nervioso cuando hay mucha gente a mi alrededor. E-es solo para comunicartelo *le agarra la remera el prece y se tapa la cara de la vergüenza*"
    jd "Em... tranquilo *le saca la mano de su chomba*, a mi tambien me pasa (?) Solo no me toques."
    mc "Esta bien..."
    mc "(¡BIEN! Ya implante mi caracter sumiso al prece, ahora va a confiar en mi y me protegerá. Que capo que soy.)"
    "Un grupo de chicos super acelerados se acerca al prece para conversar con el"
    "El prece pensando en lo que le dije es verdad les dice al grupo de chicos"

    jd "¡Hey hey! ¡Uno a la vez! Su compañer@ se pone nervioso, necesita su espacio"
    mc "(Muy bien, prece, aprendiste rápido. Ya está confirmado, es de confiar. Por lo menos un poco. Puedo ver que se preocupa por mi a pesar que dije una mentira.)"
    jd "Bien, chicos si no necesitan nada aprovechen y vayan al baño, disfruten los pocos minutos de recreo que les quedan. ¡Dale! ¡Dale!"
    mc "(Okey, tengo que ir a ver el patio, necesito saber si alguien descubrió algo más o si hay mucha gente agrupada en el agujero que dejé.)"
    hide Juan doble jr neutro
    "Salí del patio interno del colegio, me fuí hacia la zona del fondo, justo al lado de los tanques de agua."
    "Ya allí, me dirigí para nada disimuladamente hacia el agujero. Me incliné a ver si había algo más pero no, parece que en ese agujero solo había encontrado la capsula, por suerte nadie se acerco"
    play sound ("audio/Silbato.wav")
    pause 0.3
    jd "¡¡PASEEEEEEEEEEEEN!!"

    "Me fui por las puertas del patio hacia el aula designada"
    scene pasillos
    mc "(REZO para que no haya otra clase de programación o robotica)"
    mc "(¡Señor Jesús, te lo pido por favor, voy al baño y me inclino si quieres, regalame una hora y media de cualquier otra materia que no sea robótica ¡Por favor!)"
    mc "(Encima ir al curso informatica es una ruleta rusa...)"

    pc "Che, Vergara, [player]! ¡Vengan a nuestra mesa!"
    "En esa mesa también estaban Julia e Iviene, me sente con ellos"
    scene aula
    mc "Hola chicos, gracias por invitarnos"
    iv "Si, chicos. Por fin tengo un grupo de amigos de secundaria"

    jm "Ja" 
    jm "ja"
    jm "ja."
    jm "Tranquilo, todos estamos igual de emocionados."
    mc "(Che, pero estamos en segundo año, porque no tendran grupo a estas alturas del año?)"
    pc "Eu, chavales. ¿Creen que tenemos- ¡Viva Perón!- robótica en esta hora? "
    jm "Creo que sí, sino no estariamos en esta aula..."

    "Irrumpe una profesora entrando abruptamente al aula"

    show catastrofe aula at catastrofeaula
    anon "¡BUEEEEEEEN DÍA! Soy la profe de Geografía. 
    Me llamo Catástrofe Pastos. 
    Espero que hayan tenido un relindo día..."
    pause 0.5
    cp "hasta ahora." 
    cp "¿Cómo están?"
    mc "(DIOS POR FIN ALGO QUE NO ES ROBOTICA, GRACIAS ZEUS)"

    "La clase pasa de manera disfrutable, llegando al recreo"

    mc "(Bueno, ahora siento como que la clase no dura lo suficiente, parece que depende del profesor)"
    mc "(Igualmente tengo que ir con el prece, no se si es lo correcto contarle...)"
    mc "(Pero a este punto necesito desquitarme, necesito llevarme a alguien conmigo)"

    scene pasillos with dissolve

    "Decidi ir con el profesor"
    show Juan doble jr neutro at higher_center with dissolve
    mc "Hola, prece. Perdon que siempre le moleste, pero necesito contarle algo."
    jd "¿Qué pasó?"
    mc "Escuchame, prece. Encontre la cápsula del tiempo en el patio hace unas horas, y necesitaba contarselo a alguien."
    jd "¡¿EH?!"
    mc "Si mire..."
    "Abrís la mochila usando tu espalda como pared para que nadie mas que el prece vea lo que esta dentro de la mochila."
    "Juan Doble Jr abre la cápsula y encuentra las cartas."
    mc "Son cartas del año 2024 si no estoy mal. Las puede leer si quiere, pero no acá."
    jd "Entiendo tu situación, estás en un lugar muy comprometido, pero tranquilo, esto se queda conmigo, hablemos afuera, pero no ahora."
    jd "Escúchame atentamente… Te voy a retirar de tu siguiente clase, es la ultima del dia, asi que va a ser tan sospechoso, y voy a llevar afuera donde me vas a mostrar donde encontraste la cápsula y me vas a contar todo, voy a leer las cartas y hablamos alla y solo alla."
    jd "¿Esta claro?"
    mc "Si si, gracias Prece"
    jd "No es nada, guarda todo y disfruta del recreo, despues vemos"
    hide Juan doble jr neutro with dissolve

    
    "El recreo termina y empiezan de nuevo las clases, todo va de acorde a lo planeado y vamos a donde se encontro la capsula"
    scene patio with dissolve
    show Juan doble jr neutro at higher_center with dissolve
    mc "Mire, aca es donde encontramos la cápsula"
    jd "Ajá, a ver mostrame la capsula"

    "Le das la capsula y comienza a leer las cartas"

    jd "Wow… Perdon, es un poco emocionante, tengo sentimientos encontrados, esto no está bien, tenemos un aparente crimen acá escrito."
    jd "Voy a estar mas pendiente de las conversaciones entre los miembros del personal del colegio."
    jd "No prometo nada, pero esto puede ser peligroso. No se si llamar a la policia, viendo que aparentemente el ministro es el responsable de esto, debe de haber algun infiltrado en la policia, por ahora dejemoslo entre nosotros."
    mc "Si, me parece bien"
    hide Juan doble jr neutro
    "Se van del patio, [player] vuelve a su clase y juan va a la sala de profes."
    mc "(Finalmente me lo pude sacar de encima, pero todavia tengo la capsula encima...)"
    scene bg negro with dissolve

    "Pasa un día, cuando [player] va al colegio se encuentra con la noticia de la desaparición de Jeronimo Mangel"
    scene formacion with dissolve
    mc "(¡¿Otra victima más?!)"

    scene pasillos with dissolve
    "Te acercas al mostrador de la entrada."
    mc "(Lo que me faltaba, la única persona en la que confiaba se fue. ¡Perfecto!)"
    mc "(No pienso hablar con ella. Si para preguntarle a qué aula tenemos que ir se pone de mal humor, no me quiero ni imaginar cómo se pondrá cuando le pregunte cómo está.)"
    mc "(¿Será que el preceptor también es un desaparecido?)"

    # Escena: Desayuno
    scene pasillos
    "Se hace la hora del desayuno. Notas que hay más cantidad de pan que de costumbre, tanto que sobra."
    mc "(¿Será que calcularon mal la cantidad ayer y ahora hicieron una cantidad más apropiada para los alumnos?)"

    "Al retirarte del comedor, te diriges al patio con pocas esperanzas de que el día mejore."
    "De repente, escuchas un ruido proveniente de la cocina."
    anon "¡No! ¡La gran...!"
    "Casi inmediatamente se escucha un golpe y el sonido de fragmentos cayendo."
    mc "(¿Qué? Pero si el grito vino de la cocina... ¿Por qué el golpe se escucha desde la sala del módem?)"

    # Escena: Pasillo y descubrimiento
    "Te acercas al casi inhabitado pasillo. Antes de asomarte a la sala del módem, revisas si alguien te está viendo."
    mc "(Nadie me ve. ¡Bien!)"
    "Abres la puerta de la diminuta habitación y la cierras tras de ti. El frío te invade."
    mc "(¿Huh?)"
    "Encuentras un casi imperceptible picaporte al costado del gigantesco módem."
    mc "(Si muero hoy, que sea a lo grande...)"
    "Con valentía, jalas del picaporte y descubres que el módem es en realidad una puerta."

    # Escena: Pasillo cuesta abajo
    "Te adentras en un pasillo cuesta abajo que lleva a unas escaleras."
    scene bg negro with dissolve
    mc "(No veo nada.)"
    "Prendes la linterna de tu celular y empiezas a bajar las escaleras."
    mc "(¡NO HAY NI UN BENDITO FOCO, NO HAY CABLES NI NADA, ESTÁ SUPER MAL DISEÑADA!)"

    # Escena: Puerta de madera
    "Al final de las escaleras ves una puerta de madera vieja, pero resistente."
    "Con un poco de esfuerzo, logras abrirla. Detrás, solo encuentras oscuridad hasta que iluminas con tu linterna."

        # Escena: Descubrimiento en la sala del módem
    scene sotano with dissolve
    mc "(¿Qué? ¿Qué caraj— es esto?)"
    "Abres la puerta y ves a todos los desaparecidos allí. Escuálidos, un olor horripilante se adueña de la escalera."
    mc "(¿El pan del desayuno?)"
    "Entre la multitud, notas a Jerónimo a lo lejos llorando, con las manos embarradas de masa. Hay cuerpos tumbados alrededor de las mesas donde todos están amasando en la oscuridad."

    # Final bueno: Los desaparecidos reaccionan
    "De repente, los desaparecidos empiezan a gritar."
    mc "¡Cálmense! ¡No soy un peligro si ustedes no lo son para mí!"
    "En ese momento, una chica sale de la multitud. Su aspecto es extraño: parece joven y vieja a la vez, completamente pálida y con ojos hipersensibles a la luz."
    anon "H-Hola, soy Ayuda."
    mc "¿Qué? ¿Ayuda?"
    anon "Sí, así me llamo. Es que esas fueron las últimas palabras de mi mamá antes de dejarme aquí con los demás secuestrados. Mi mamá se llamaba Agustina."
    mc "..."
    anon "Es mucho que procesar. Todos aquí abajo somos los desaparecidos por 'La Fruta'. No sabemos quién es; siempre viene enmascarado con una máscara de frutas. Cada día lleva una diferente: uvas, bananas, lo que sea. Le tenemos terror."
    mc "(Este es el escondite de los desaparecidos... ¿Por qué no gritaron para que los rescaten?)"
    anon "En nombre de todos, digo que fuimos amenazados por La Fruta, y hasta recién pensábamos que todos ahí arriba lo sabían."

    # Preguntas sobre el ministro y el preceptor
    mc "¿Por casualidad... sabrían decirme si el ministro de Educación bajó aquí alguna vez?"
    anon "No, jamás bajó que yo sepa. Él es más joven que yo. Aunque no lo parezca, aquí abajo se escuchan todas las conversaciones de las habitaciones superiores..."
    mc "(Preceptoría y la sala de profesores.)"
    anon "Por eso, cada vez que viene el ministro, podemos escucharlo tanto a él como al resto. Su voz no es igual a la de La Fruta ni a la de ninguno de los que lo acompañan."
    mc "¿Y saben algo de un tal Juan Doble Jr.?"
    mujer1 "¿El preceptor de ayer? No bajó aquí, jamás. Y desde ayer no lo escuchamos arriba."
    mc "(Así que si es un desaparecido, no está acá... ¡Ah, sí! ¡Miren!)"

    # Muestra la cápsula del tiempo
    "Sacas de tu mochila la cápsula del tiempo y muestras las cartas."
    anon "Perdón, no sé leer. Jamás vi letras."
    hombre1 "Yo sí sé leer."
    mc "No se moleste, yo las leeré para todos."

        # Escena: Lectura de la carta
    "Comienzas a leer la carta en voz alta. Mientras lo haces, Ayuda empieza a llorar."
    mc "Tranquilos. Yo resolveré esto ahora. Quédense aquí, no hagan ningún ruido. Prometo resolver todo ya."
    "Te giras hacia la salida, decidido. Subes rápidamente por las escaleras, sales de la sala del módem y corres hacia el baño para hacer una llamada."

    # Llamada a la policía
    mc "¿Hola?"
    "Una operadora responde al otro lado de la línea."
    operadora "Buenas, 911. ¿Cuál es su emergencia?"
    mc "Hola, soy una persona que encontró un sótano lleno de víctimas de desapariciones y secuestros. Estoy en la Escuela Secundaria de Innovación. Por favor, vengan rápido."
    operadora "Ya hay tres unidades en camino. En solo diez minutos habrá personal con quien podrá hablar."
    mc "Muchas gracias."

    # Llegada de la policía
    "Minutos después, la policía llega al colegio. Les muestras lo que encontraste y dónde. Pronto, los oficiales toman control de la situación."
    policia1 "¿Usted es la persona más antigua aquí?"
    anon "Sí, sí lo soy."
    policia1 "¿Qué nos puede contar sobre todo esto?"
    anon "Este sótano existe desde antes de que yo naciera. No sé en qué año nací ni quién es mi papá. Tampoco sé el apellido de mi mamá, pero alguien en el Ministerio de Educación—excepto el ministro, porque descartamos todas las dudas posibles—creó este sótano para este fin."
    mc "(¿El Ministerio de Educación? ¿Quién podría estar detrás de esto?)"
    anon "Tampoco sabemos quién es el culpable. El o los responsables siempre entraron enmascarados. Solo sabemos que cada tanto bajaban y elegían a uno de nosotros para llevárselo. Nunca más los volvimos a ver."
    policia1 "¿Y eran utilizados únicamente para hacer el pan del colegio? ¿No tenían otra función más que esperar a que 'La Fruta' viniera?"
    anon "Así es…"
    policia1 "Bueno, muchísimas gracias por su cooperación."

    # Ayuda revela una pista
    "Mientras los oficiales terminan de tomar declaraciones, Ayuda te llama aparte."
    anon "Ese sujeto sabe más de lo que aparenta."
    mc "¿Cómo lo sabes?"
    anon "Porque dijo el nombre 'La Fruta'... sin que yo lo mencionara ni que él preguntara."
    mc "(¿Qué? ¿Cómo pudo saberlo? Esto no tiene sentido...)"
    "La revelación te deja pensando mientras observas cómo los oficiales continúan con la investigación."
    "Así termina el final bueno, con un misterio, pero los desaparecidos fueron encontrados. Despues de todo, para el segundo dia de segundo año de secundaria, esto es lo mas entretenido que te puede pasar."
    "FIN."
    return






return