# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define detective = Character("Detetive")
define freud_paganini = Character("Freud Paganini")
define francisco_ferdinand = Character("Francisco Ferdinand")
define cesar_nogueira = Character("César Nogueira")
define antonio_borges = Character("Antônio Borges")
define leonardo_silva = Character("Leonardo Silva")
define oliver_oliveira = Character("Oliver Oliveira")
define vicente_barbosa = Character("Vicente Barbosa")

transform midleft:
    xalign 0.10 yalign 0.35

transform left:
    xalign 0.10 yalign 0.45

transform right:
    xalign 0.90 yalign 0.45

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene detective-room
    play music "sounds/introduction.mp3"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    detective "'A dificuldade faz a vida'... É o que meu pai costumava me dizer. Nunca duvidei de sua sabedoria, mas agora… Me pergunto se realmente é verdade."

    scene photo-aprox
    show caroline-dias at midleft
    detective "Caroline Dias, 23 anos… Uma garota incrível, com um futuro próspero pela frente. Uma policial morta, é o que ela é agora. Morta a facadas em seu carro, no estacionamento de um supermercado." 
    detective "Parecia ter parado para comprar algo durante o trajeto para casa, depois do expediente…"

    scene detective-room
    hide caroline-dias
    with fade
    detective "Nenhum suspeito aparente. Não namorava, nem tinha casos. Bom relacionamento com a família, apenas os pais idosos. Poucos amigos, histórias batendo, mesmo depois de diversos interrogatórios."
    detective "Cogitei queima de arquivo. É comum nesse ramo, mas ao que parece, nem os chacais da corporação são culpados disso."

    scene photo-aprox
    show carlos-santana at midleft
    detective "A coisa só piorou a partir daí. Carlos Santana, um policial duvidoso, na casa dos 30, morto a tiros em uma avenida próxima. Os tiros foram silenciados, já que não houveram relatos de tiroteio na vizinhança."

    scene detective-room
    hide carlos-santana
    with fade
    detective "Carlos não era um exemplo de agente… Constantemente estava envolto em problemas de conduta, mas a diretoria sempre arquivava os casos."

    scene photo-aprox
    detective "Depois, o ápice do caso: Marcos Nogueira, chefe de operações investigativas, encontrado morto com diversas perfurações de faca na sua sala particular na delegacia…" 
    detective "Era um horário em que ninguém da equipe de investigações deveria estar presente na sala."
    detective "Poucas pessoas na delegacia… Conjunto noturno. Todos atualmente  temporariamente afastados e sob investigação constante."
    detective "Alguns relataram que viram movimento nos fundos da delegacia. Alguém correndo nas sombras. Ninguém viu seus atributos físicos, no entanto."
    detective "A delegacia está caótica como nunca… Nunca vi nada igual. A paranoia e o medo reinam. "
    detective "Preciso fazer algo, mas por enquanto… Não tenho nada. Há momentos na vida em que esperar é a única opção."
    detective "Não gosto disso… mas é o que tenho."

    stop music

    scene workstation-talk-a
    play music "sounds/detective-workstation.mp3"

    show freud-paganini at right
    freud_paganini "Olá Morgan. Um caos e tanto por aqui, não?"
    hide freud-paganini

    show detective at left
    detective "Sim."
    hide detective

    show freud-paganini at right
    freud_paganini "A coisa parece séria. Não acredito que o Marcos morreu de maneira tão brutal." 
    freud_paganini "Mal chego de férias, e sou recebido com isso… Vai entender os planos do destino, hehe."
    hide freud-paganini

    menu:
        "Não deveria usar esse tom nessa situação, Freud. É coisa séria.":
            jump badTone
            label badTone:
                show detective at left
                detective "Não deveria falar assim nessa situação. As coisas estão sérias como nunca."
                hide detective

                show freud-paganini at right
                freud_paganini "É, acho que você tem razão... Trabalho é trabalho."
                hide freud-paganini

        "Sim. Um belo presente de boas-vindas.":
            jump welcomeGift
            label welcomeGift:
                show detective at left
                detective "Realmente, um belo presente de boas vindas."
                hide detective

                show freud-paganini at right
                freud_paganini "Não é? Pelo menos tive a chance de passar uma semana legal com a patroa."
                hide freud-paganini
        
        "Ignorar":
            jump ignore
            label ignore:
                show detective at left
                detective "..."
                hide detective

                show freud-paganini at right
                freud_paganini "Foram umas férias e tanto..."
                hide freud-paganini
        
    show freud-paganini at right
    freud_paganini "Bom, tenho que ir Morgan. Vou me atualizar do caso, e ver no que posso contribuir."
    hide freud-paganini

    show detective at left
    detective "Boa sorte Freud."
    hide detective

    scene workstation-talk-b

    show francisco-ferdinand at right
    francisco_ferdinand "Investigador, tem um minuto?"
    hide francisco-ferdinand

    show detective at left
    detective "Sim senhor."
    hide detective

    show francisco-ferdinand at right
    francisco_ferdinand "Um dos agentes noturnos parece saber de alguma coisa. Embora ele tenha negado, dá pra perceber que ele não quer falar. Tenta descobrir o que é."
    francisco_ferdinand "O agente Nogueira e o agente Borges estão lá. Quando chegar, diga a eles para virem até mim. Tenho outros assuntos para eles."
    hide francisco-ferdinand

    show detective at left
    detective "Outros assuntos?"
    hide detective

    show francisco-ferdinand at right
    francisco_ferdinand "Sim, senhor Morgan. Tenho que alocar agentes para cobrir o máximo de pistas possíveis, mesmo as pouco prováveis."
    francisco_ferdinand "Não é nada que eles precisem de sua ajuda, se é o que quer saber. Por enquanto, se preocupe em conseguir as respostas do policial."
    hide francisco-ferdinand

    menu:
        "Sim, claro.":
            jump still
            label still:
                show detective at left
                detective "Sim, claro. Estou indo."
                hide detective

        "Se são novas informações, acho pertinente eu saber, senhor Ferdinand.":
            jump question
            label question:
                show detective at left
                detective "Senhor Ferdinand, Se são novas informações, acho justo que-"
                hide detective

                show francisco-ferdinand at right
                francisco_ferdinand "Eu julgo o que é pertinente você saber, agente. Faça o que te foi comandado."
                hide francisco-ferdinand

                show detective at left
                detective "…"
                detective "Sim senhor."
                hide detective

    scene interrogatory-room-talk-a

    show cesar-e-antonio at right
    cesar_nogueira "Sim, agente Silva, mas você não está nos levando a lugar algum."
    cesar_nogueira "Quer saber? Eu não tenho tempo para sua insegurança, agente Silva… Ou você fala o que você viu, ou então-"
    hide cesar-e-antonio

    scene interrogatory-room-talk-b

    show detective at left
    detective "…"
    hide detective

    show cesar-e-antonio at right
    cesar_nogueira "O que você quer Morgan?"
    hide cesar-e-antonio

    menu:
        "Com licença senhores. Eu assumo o caso a partir de agora":
            jump gentle
            label gentle:
                show detective at left
                detective "Com licença senhores. Eu assumo o caso a partir de agora."
                hide detective

                show cesar-e-antonio at right
                cesar_nogueira "O interrogado é assunto nosso, detetive."
                hide cesar-e-antonio

                show detective at left
                detective "O chefe tem outros assuntos para vocês, agente César Nogueira e agente Borges. Ele me enviou aqui para tomar conta do caso."
                hide detective

        "Saiam. O interrogado é assunto meu agora.":
            jump rude
            label rude:
                show detective at left
                detective "Saim. O interrogado é tarefa minha a partir de agora."
                hide detective

                show cesar-e-antonio at right
                cesar_nogueira "Engraçado, porque ele foi colocado na nossa responsabilidade."
                hide cesar-e-antonio

                show detective at left
                detective "Não está mais. Ferdinand tem outra tarefa para vocês."
                hide detective
    
    show cesar-e-antonio at right
    cesar_nogueira "Hunf… Vamos Borges. Vamos ver o que Ferdinand tem pra gente."
    antonio_borges "Certo."
    hide antonio-borges

    scene interrogatory-room-talk-c

    show detective at left
    detective "E então… Leonardo Silva, 32 anos, casado, esperando um filho…"
    detective "Bom, nos registros, foi dito por você que você estava no segundo andar do departamento, exatamente em frente a uma janela que dá ampla visão por onde o possível assassino fugiu."
    detective "Você diz estar fumando no momento do ocorrido."
    hide detective

    show leonardo-silva at right
    leonardo_silva "Sim… Eu só estava fumando."
    hide leonardo-silva
    
    show detective at left
    detective "Você afirma não ter visto detalhes do assassino enquanto estava na janela, mesmo ela sendo a melhor posição para observar os fundos da delegacia."
    hide detective

    show leonardo-silva at right
    leonardo_silva "E-eu já disse, Morgan. Eu não estava prestando atenção… Apenas… Olha, estou com problemas em casa. Eu não estou com a cabeça no lugar, e estava fumando para relaxar um pouco."
    leonardo_silva "Não me atentei aos arredores. E-eu… Só não quero mais problemas…"
    hide leonardo-silva

    menu:
        "Se não contar o que sabe, você vai ser considerado cúmplice":
            jump accomplice
            label accomplice:
                show detective at left
                detective "Se esconder o que viu, vão te considerar como cúmplice. Vão te acusar de estar escondendo informações relevantes para a resolução do caso."
                detective "Provas não são necessárias para isso. Na prática, ambos sabemos isso."
                hide detective

        "Se não contar o que sabe, você pode morrer":
            jump youCanDie
            label youCanDie:
                show detective at left
                detective "Leonardo… Todos sabem que você sabe de algo. Algo que não quer contar. Eu sugiro que pense melhor, porque talvez, o caminho que você está escolhendo tomar, te faça morrer. Talvez pior."
                detective "Você sabe do que eu estou falando. Você já viu isso antes."
                hide detective

        "O culpado precisa pagar":
            jump theKillerMustPay
            label theKillerMustPay:
                show detective at left
                detective "O culpado precisa pagar, Leonardo. Você devia conhecer a Caroline, a primeira vítima disso tudo. Ela foi morta de maneira brutal. O próximo pode ser eu, ou mesmo você."
                detective "Se você reconheceu o fugitivo, preciso que diga."
                hide detective

    show leonardo-silva at right
    leonardo_silva "Eu…"
    leonardo_silva "Eu não tenho certeza, mas… Acho que o fugitivo… O assassino… Usava um relógio."
    leonardo_silva "Não era qualquer relógio. Eu… Eu acho que era um relógio de prata com fundo verde. O relógio do Vicente…"
    leonardo_silva "O seu relógio de prata eu conhecia de longe… Sid & Coster. Era um baita relógio."
    hide leonardo-silva

    show detective at left
    detective "É… Vicente Barbosa então… O velho Vicente… Ainda lembro onde ele mora. Vou ver o que ele tem a dizer."
    detective "Isso não é um interrogatório formal, Leonardo. Não precisa se preocupar, você está liberado."
    hide detective

    show leonardo-silva at right
    leonardo_silva "…"
    leonardo_silva "Certo, Morgan... Boa sorte."
    hide leonardo-silva

    scene police-station-corridor-talk-a

    show detective at left
    detective "..."
    hide detective

    show oliver-oliveira at right
    oliver_oliveira "Senhor! Senhor!"
    hide oliver-oliveira

    show detective at left
    detective "Oliver… Falei que você ficaria de folga essa semana. Por que você está aqui?"
    hide detective

    show oliver-oliveira at right
    oliver_oliveira "Desculpe senhor Morgan, mas não posso ficar parado com tanta coisa acontecendo nos últimos tempos."
    oliver_oliveira "A Carol… Mesmo o Carlos e o Marcos agora… A justiça tem que ser feita."
    hide oliver-oliveira

    show detective at left
    detective "Hunf… Vamos. Encontramos um suspeito, finalmente."
    hide detective

    show oliver-oliveira at right
    oliver_oliveira "Quem é senhor Morgan? Um serial-killer de meia idade com obsessão em policiais? Ou então algum jovem buscando vingança por seu pai, que foi sentenciado a décadas inteiras de prisão?"
    hide oliver-oliveira

    show detective at left
    detective "O que eu te disse sobre manter estereótipos durante as investigações? Os resultados raramente são distintos, mas desapegar-se do senso comum é o que nos faz premeditar o inesperado."
    hide detective

    show oliver-oliveira at right
    oliver_oliveira "Desculpe senhor Morgan. O senhor tem razão."
    hide oliver-oliveira

    show detective at left
    detective "…"
    detective "Estamos indo a casa de um velho conhecido. Vicente Barbosa."
    hide detective

    show oliver-oliveira at right
    oliver_oliveira "Ele não tinha se aposentado?"
    hide oliver-oliveira

    show detective at left
    detective "Sim. Não sei ao certo o motivo, mas ele achou melhor sair da vida de policial. Talvez o risco não valesse a pena."
    detective "É o que veremos. Quando chegarmos lá."
    hide detective

    scene police-station-corridor-talk-b

    show francisco-ferdinand at right
    francisco_ferdinand "Detetive… "
    hide francisco-ferdinand

    show detective at left
    detective "…"
    detective "Senhor Ferdinand."
    hide detective

    show francisco-ferdinand at right
    francisco_ferdinand "Conseguiu algo do agente Silva?"
    hide francisco-ferdinand

    menu:
        "Nada útil. O fugitivo usava relógio.":
            jump lie
            label lie:
                $ hideTheTruth = True

                show detective at left
                detective "Ele não disse muita coisa relevante. Apenas que tinha visto o reflexo de um relógio no pulso do fugitivo."
                detective "Não creio que ele esteja escondendo mais nada."
                hide detective
                
                show francisco-ferdinand at right
                francisco_ferdinand "Hum… As coisas não serão mais fáceis dessa maneira… Mas é um começo, não acha?"
                francisco_ferdinand "Sabe Morgan, tenho algumas ressalvas quanto a você, mas não duvido da sua competência."
                francisco_ferdinand "Só não se esqueça de excluir aquele 'interrogatório' do seu relatório."
                hide francisco-ferdinand

        "Vicente Barbosa. Tudo indica que ele é nosso suspeito.":
            jump truth
            label truth:
                $ hideTheTruth = None

                show detective at left
                detective "Vicente Barbosa. Nosso suspeito."
                detective "Ele disse que o fugitivo estava usando um relógio. Um relógio bastante memorável, pelo que ele disse."
                detective "Se ele estiver certo, Vicente Barbosa é o nosso suspeito."
                hide detective

                show francisco-ferdinand at right
                francisco_ferdinand "Cirúrgico em obter informações como sempre. Muito bom Morgan."
                francisco_ferdinand "Aliás, para onde estão indo?"
                hide francisco-ferdinand

                show detective at left
                detective "Para lá, senhor. Trabalhamos juntos em diversos casos. Posso assumir essa parte da investigação."
                hide detective

                show francisco-ferdinand at right
                francisco_ferdinand "Nada disso detetive."
                francisco_ferdinand "O César dará conta do recado dessa vez. Vocês também tinham bastante contato. Me pergunto se isso não afetaria os resultados da investigação…"
                francisco_ferdinand "Deixe-me ver… Está perto do fim do expediente. Pegue algumas pastas e as leve para casa. Preciso que você averigue os depoimentos dos policiais investigados. Fique livre para investigar qualquer um que te liberte suspeitas."
                francisco_ferdinand "Vicente Barbosa… O endereço do desgraçado ainda deve constar nos arquivos. Mandarei o Nogueira e o Borges assim que retornarem."
                hide francisco-ferdinand
    
    show detective at left
    detective "Fez bem em não falar nada, Oliver."
    detective "Vamos."
    hide detective

    scene apartment-corridor-talk-a

    show oliver-oliveira at right
    oliver_oliveira "Acho que o apartamento dele era o 41, não é?"
    hide oliver-oliveira

    show detective at left
    detective "Sim."
    hide detective

    scene apartment-corridor-talk-b

    "TOC TOC TOC"

    show vicente-barbosa at right
    vicente_barbosa "Ah… Quem é?"
    hide vicente-barbosa

    show detective at left
    detective "Morgan, velho amigo."
    hide detective

    show vicente-barbosa at right
    vicente_barbosa "..."
    vicente_barbosa "O que você quer Morgan?"
    hide vicente-barbosa

    show detective at left
    detective "Apenas esclarecer algumas coisas."
    hide detective

    show vicente-barbosa at right
    vicente_barbosa "Hum… Portas abertas para os amigos, é o que dizem. Entrem."
    hide vicente-barbosa

    scene vicente-apartment-talk-a

    show vicente-barbosa at right
    vicente_barbosa "Já faz algum tempo Morgan."
    hide vicente-barbosa

    show detective at left
    detective "Sim Vicente."
    hide detective

    show vicente-barbosa at right
    vicente_barbosa "Não é uma visita casual, então o que você quer?"
    hide vicente-barbosa

    show detective at left
    detective "Você deve ter ficado sabendo dos casos da delegacia. A Caroline, o Carlos, e agora o Marcos."
    hide detective

    show vicente-barbosa at right
    vicente_barbosa "É… Eu acompanho os noticiários."
    hide vicente-barbosa

    show detective at left
    detective "O assassino foi visto fugindo da delegacia. Ele tinha um relógio, Vicente. Um relógio que você conhece bem. Sid & Coster."
    hide detective

    show vicente-barbosa at right
    vicente_barbosa "…"
    vicente_barbosa "Então é isso? Você vem até minha casa, me chamar de assassino porque o assassino usava um relógio como o meu…"
    hide vicente-barbosa

    show oliver-oliveira at left
    oliver_oliveira "Até hoje, nunca vi ninguém usar um Sid & Coster além de você, Vicente. Você é nosso principal suspeito!"
    hide oliver-oliveira

    show vicente-barbosa at right
    vicente_barbosa "Melhor controlar seu garoto Morgan."
    hide vicente-barbosa

    show detective at left
    detective "Você tem o relógio, Vicente?"
    hide detective

    show vicente-barbosa at right
    vicente_barbosa "Hunf. Empacotei aquele relógio... Artigo de coleção. Minha conquista pessoal."
    vicente_barbosa "Nunca mais usei desde então. Mas se quer ver… Pois bem."
    hide vicente-barbosa

    scene vicente-apartment-talk-b

    show oliver-oliveira at left
    oliver_oliveira "Empacotar um relógio usado… Conversa fiada…"
    hide oliver-oliveira

    show vicente-barbosa at right
    vicente_barbosa "!!!"
    vicente_barbosa "Droga! Armaram pra mim!"
    hide vicente-barbosa

    show oliver-oliveira at right
    oliver_oliveira "É… Eu sei que armaram…"
    hide oliver-oliveira

    show vicente-barbosa at right
    vicente_barbosa "Armaram, Morgan! Armaram!"
    vicente_barbosa "A embalagem foi aberta. Eu lacrei. Para coleção!"
    vicente_barbosa "..."
    vicente_barbosa "AQUI!"
    vicente_barbosa "..."
    vicente_barbosa "Exatamente como o seu…"
    hide vicente-barbosa

    scene vicente-apartment-talk-c

    show oliver-oliveira at right
    oliver_oliveira "Cuidado, seu maluco!"
    hide oliver-oliveira

    show vicente-barbosa at right
    vicente_barbosa "Você Oliver… Você armou pra mim."
    hide vicente-barbosa

    show oliver-oliveira at right
    oliver_oliveira "Eu estou do seu lado. Esse fio de cabelo caiu agora."
    hide oliver-oliveira

    show detective at left
    detective "..."
    hide detective

    show vicente-barbosa at right
    vicente_barbosa "Saiam da minha casa! Os dois!"
    hide vicente-barbosa

    show detective at left
    detective "Acalme-se. Nós estamos saindo."
    hide detective

    scene outside-vicente-building

    show oliver-oliveira at right
    oliver_oliveira "Eu não deveria me aproximar tanto durante os casos… Desse jeito coisas assim não aconteceriam…"
    oliver_oliveira "Você sabe senhor Morgan. Cometer tais atrocidades… Eu não faria isso. Você me conhece!"
    oliver_oliveira "Meu cabelo caiu ali, senhor Morgan. Não estou mentindo!"
    hide oliver-oliveira

    menu:
        "Eu sei que não foi você, Oliver.":
            jump comprehensive
            label comprehensive:
                show detective at left
                detective "Eu sei, Oliver."
                detective "Não… Não diga nada ao Ferdinand, nem à diretoria. As coisas podem piorar caso você diga."
                hide detective

                show oliver-oliveira at right
                oliver_oliveira "Sim… Sei do que são capazes..."
                oliver_oliveira "Canalhas."
                hide oliver-oliveira

        "...":
            jump suspecting
            label suspecting:
                show detective at left
                detective "..."
                hide detective

                show oliver-oliveira at right
                oliver_oliveira "Precisa acreditar em mim senhor Morgan."
                hide oliver-oliveira

                show detective at left
                detective "..."
                detective "É… Eu preciso."
                hide detective

    scene detective-workstation
    play music "sounds/detective-workstation.mp3"
    detective "Parece que eu já tenho informação o suficiente para tomar uma decisão… Eu gostaria de poder investigar mais, mas dada a situação… Tenho que fazer algo."

    if hideTheTruth == True:
        detective "Não posso deixar mais agentes morrerem."
        menu:
            "Acusar Vicente":
                jump badEnding
                label badEnding:
                    scene death
                    play music "sounds/ending.mp3"
                    "Uma semana depois"
                    
                    show detective at left
                    detective "..."
                    hide detective

                    show oliver-oliveira at right
                    oliver_oliveira "Olá, senhor Morgan"
                    hide oliver-oliveira

                    show detective at left
                    detective "Olá Oliver."
                    hide detective

                    show oliver-oliveira at right
                    oliver_oliveira "Parece que chegamos ao fim… O assassino foi encontrado, e punido."
                    hide oliver-oliveira

                    show detective at left
                    detective "Vicente… Não informei a diretoria sobre ele ser o principal suspeito… Ainda assim, ele foi morto na prisão."
                    hide detective

                    show oliver-oliveira at right
                    oliver_oliveira "É realmente uma pena… Vou levar a morte dele em minha consciência."
                    hide oliver-oliveira

                    show detective at left
                    detective "Não se culpe por acusar o culpado, Oliver."
                    hide detective

                    show oliver-oliveira at right
                    oliver_oliveira "…"
                    oliver_oliveira "Ele não era o culpado."
                    hide oliver-oliveira

                    show detective at left
                    detective "?"
                    hide detective

                    ". . ."
                    "Após o detetive se virar, ele é morto. No fim, o culpado sempre foi Oliver."

            "Investigar Oliver":
                jump goodEnding
                label goodEnding:
                    scene detective-room
                    play music "sounds/ending.mp3"
                    detective "Oliver Oliveira… Meu bom ajudante…"
                    detective "Lembro de quando entrou na corporação. Seu sorriso e ímpeto de justiça me fizeram acreditar que as coisas não precisavam ser tão ruins."
                    detective "É uma pena… Mas o desejo por justiça às vezes corrompe os melhores."
                    detective "Depois de alguns dias seguindo ele, descobri sua base de operações. Preso em flagrante."
                    detective "Oliver era o assassino… Acabar com os corruptos. Trazer justiça. Esse era o seu plano."
                    detective "O Carlos e o Marcos certamente tinham seus nomes envolvidos. Quanto a Caroline Dias… Bom, ela não fazia parte da sujeira da corporação, mas havia descoberto o segredo dele."
                    detective "No seu julgamento, ele disse que ela foi a única a quem ele gostaria de não ter matado."
                    detective "Hoje, ele foi encontrado morto na prisão. Eu conheço bem os mandantes…"
                    detective "Vicente no fim esteve certo. Fiz bem em não informar ao subchefe sobre ele ser o principal suspeito. Por causa disso, ele continua vivo hoje."

    else:
        detective "Os chacais da delegacia não vão esperar muito até darem cabo do Vicente..."
        menu:
            "Arquivar o Caso":
                jump worstEnding
                label worstEnding:
                    scene death
                    play music "sounds/ending.mp3"
                    "Uma semana depois"
                    
                    show detective at left
                    detective "..."
                    hide detective

                    show oliver-oliveira at right
                    oliver_oliveira "Olá, senhor Morgan"
                    hide oliver-oliveira

                    show detective at left
                    detective "Olá Oliver."
                    hide detective

                    show oliver-oliveira at right
                    oliver_oliveira "Parece que chegamos ao fim… O assassino foi encontrado, e punido."
                    hide oliver-oliveira

                    show detective at left
                    detective "Vicente..."
                    detective "Morto. Às ordens de Ferdinand... Ao menos, ele não matará mais ninguém..."
                    hide detective

                    show oliver-oliveira at right
                    oliver_oliveira "É realmente uma pena… Vou levar a morte dele em minha consciência."
                    hide oliver-oliveira

                    show detective at left
                    detective "Não se culpe por acusar o culpado, Oliver."
                    hide detective

                    show oliver-oliveira at right
                    oliver_oliveira "…"
                    oliver_oliveira "Ele não era o culpado."
                    hide oliver-oliveira

                    show detective at left
                    detective "?"
                    hide detective

                    ". . ."
                    "Após o detetive se virar, ele é morto. No fim, o culpado sempre foi Oliver."

            "Investigar Oliver":
                jump normalEnding
                label normalEnding:
                    scene detective-room
                    play music "sounds/ending.mp3"
                    detective "Oliver Oliveira… Meu bom ajudante…"
                    detective "Informar ao subchefe Ferdinand sobre o Vicente foi um erro. Ele foi morto pouco tempo depois que eu e Oliver saímos de lá."
                    detective "Ao menos, consegui encontrar o culpado…"
                    detective "Depois de alguns dias seguindo ele, descobri sua base de operações. Preso em flagrante."
                    detective "Oliver era o assassino… Acabar com os corruptos. Trazer justiça. Esse era o seu plano."
                    detective "O Carlos e o Marcos certamente tinham seus nomes envolvidos. Quanto a Caroline Dias… Bom, ela não fazia parte da sujeira da corporação, mas havia descoberto o segredo dele."
                    detective "No seu julgamento, ele disse que ela foi a única a quem ele gostaria de não ter matado."
                    detective "Hoje, ele foi encontrado morto na prisão. Eu conheço bem os mandantes…"

    # This ends the game.

    return