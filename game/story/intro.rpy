﻿label intro:
    "Я ворвался в комнату, жадно рассматривая всё вокруг."
    "Она выглядит так же шикарно, как я себе представлял. Меньшего от своих анонимных заказчиков я не ожидал."
    "Правда, немного старомодно."
    "Но что угодно лучше тех комнат при лабораториях, что выделяет государство."
    "И, готов поспорить, местный ИИ готовит лучше, чем сто сорокалетняя тётя Блюма из нашей столовой."
    "Всё-таки не зря я пошел в учёные. Учитывая, чем я тут буду заниматься."
    "Не зря я проводил недели в лаборатории и пропускал все вечеринки. Не зря демонстрировал феноменальные успехи в университете, а потом в научном центре."
    "Не зря согласился прийти на очень странную и подозрительную встречу."
    show assistent at right as a with dissolve
    show mh1 at left as mh with dissolve
    #далее можно задать вопросы
    "..."
    ii "Доброе утро, Мистер Алан."
    ii "В мои обязанности входит ввести вас в курс дела, помогать Вам проводить исследования, заниматься поддержкой Вашего жизнеобеспечения."
    ii "Как Вы уже знаете, согласно нашему контракту Вы не можете покидать здание, пока не сдадите работу."
    ii "Мы находимся в бронированном, звукоизоляционном двухэтажном здании."
    ii "На этом этаже находится Ваша комната, душевая комната и кухня. Этажом ниже находится лаборатория."
    ii "Также Вам не позволено звонить или писать кому-либо. Никто не должен знать где Вы и чем Вы занимаетесь. Все ваши действия за рабочей машиной будут отслеживаться для спокойствия моего босса."
    #зациклить это меню
    menu:
        "Сколько длится контракт?":
            ii "Контракт будет завершен тогда, когда мы получим нужный результат."
        "Как тебя зовут?":
            ii "Зовите меня Ассистент."
        "Почему я?":
            ii "У Вас огромный опыт в проведении… необычных и смелых экспериментов."
            ii "Кроме того, согласно нашим данным, у вас нет близких, которые будут волноваться, если вы пропадёте на некоторое время."
            ii "В научном центре ваши таланты высоко ценят, но рядом с вами бояться даже находиться."
            ii "Наверняка это связано с тем, что однажды вы вывели вирус, лишающий людей чувства юмора и не доглядели за ним. Чуть не началась эпидемия."
            "О, этот случай."
            "Я тогда чуть не попал в тюрьму. К счастью, только я мог создать противоядие достаточно быстро, и в обмен на лекарство меня всё же оставили на свободе."
            ii "Также вас не любят за Ваш непредсказуемый характер. Это мне известно."
            ii "Я веду к тому, что вряд ли кто-то спохватится за вами в ближайшее время."
            ii "А нам как раз нужен человек, который может выполнить наше поручение и не вызывать шум своим исчезновением. Вы подходите идеально."
        "К чему такая засекреченность?":
            ii "Как Вы знаете, негуманные эксперименты преследуются законом. Особенно строгие ограничения существуют на эксперименты с человекоподобными, разумными существами."
            ii "Именно поэтому проект засекречен. За то, чем мы будем заниматься, можно попасть в тюрьму на всю жизнь."
            ii "Теперь, когда Вы часть этого проекта, в Ваших же интересах скрывать ото всех, что тут происходит."
        "ИИ умеют врать?":
            ii "Я не уполномочен отвечать на этот вопрос."
    gg "Окей."
    show mh2 as mh with dissolve
    gg "Приступим!"
    hide mh with dissolve
    
    # *фон лаборатории*
    show mh1 at left as mh with dissolve
    "Я зашел в лабораторию и присвистнул."
    "Тут есть всё, о чём может мечтать учёный."
    # *появляется ассистент*
    show assistent at right as a with dissolve

    ii "Мы выполнили Вашу просьбу. Приобрели компьютер и привычное Вам программное обеспечение."
    "И правда. Теперь я заметил старый добрый компьютер с большим красивым монитором. Такими уже давно никто не пользуется, но у меня они вызывают ностальгические чувства, напоминающие университетские годы, когда я только знакомился с генной инженерией."
    "И, собственно, я очень уж привык работать в одной программе, которая до сих пор подходит для моих целей."
    ii "Здесь мы будем заниматься выведением вида, подобного человеческим самкам."
    ii "Наша первостепенная задача получить хоть какой-то живой экземпляр девушки, который в дальнейшем можно усовершенствовать."
    ii "Чтобы заказчик был доволен, она должна быть оригинальной, красивой и… не опасной. Она не должна вести себя отталкивающе и в идеале должна быть обучаемой."
    
    #далее можно задать вопросы
    
    #далее можно задать вопросы
    #тоже зациклить
    menu:
        "Что будет после того, как нам удастся получить экземпляр?":
            ii "Мы должны будем провести серию экспериментов, чтобы составить модель поведения испытуемой."
        "Что будет, если девушка не понравится заказчику?":
            ii "Она будет уничтожена и мы начнём всё сначала."
        "Могу ли я контактировать с девушкой?":
            ii "Все нужные взаимодействия с девушкой буду проводить я."
            ii "После того, как её безопасность будет полностью протестирована, вам нужно будет провести финальное тестирование."
            gg "Финальное тестирование?"
            ii "Проверить, насколько человеку безопасно с ней взаимодействовать. Максимально близко."
            gg "О-о-о..."
    gg "Я всё понял."
    "Благодаря Ассистенту я разобрался в расположении вещей в лаборатории довольно быстро."
    "Несколько часов мы провели, подготавливая эмбрион нашей будущей девушки к генной модификация и последующему взращиванию."
    hide a
    hide mh
    with dissolve
    jump deck_genes

label deck_genes: 
    scene deck with dissolve
    
    #только при первом появлении:
    "Перед Вами доска, на которой Вы будете выбирать генофонд будущего существа."
    "Чтобы получить живое существо, Вам нужно составить правильную цепочку ДНК."
    "На основе ДНК будет выращен эмбрион. При невалидной ДНК эмбрион не сможет начать развиваться."
    "Обратите внимание, что некоторые гены действуют только в комбинации с определёнными другими генами. "
    "Каждый блок отвечает за определённую характеристику существа. Пока что вы не знаете, какой блок за что отвечает."
    "Удачи!"

    "Прождав несколько часов, я вернулся в лабораторию."

    $success = False
    
    #Если ДНК невалидна:
    if success:
        ii "Похоже, составленная ДНК недееспособна. Попробуем ещё раз."
        #если было две попытки (две и не больше двух)
        gg "Я понял!"
        gg "Похоже, первый модуль отвечает за будущий скелет девушки. Будет она её органическая основа растительной или мышечной."
        #если было три попытки
        ii "Сканирование завершено."
        ii "Второй блок генов отвечает, может ли организм синтезировать органические вещества, или поглощает уже готовые."
        "Другими словами, для растительного существа мне бы скорее всего понадобился ген гетеротрофии, а для животного — автотрофии."
        #если было четыре попытки
        ii "Я завершил сканирование."
        ii "Третий блок отвечает за кожный покров организма."
        ii "Похоже, Акваплантин и Хербакреатин работают только в связке с геном Фитогербарин, а Пушистисохорнин только у теплокровных существ."
        jump deck_genes
    else:
        jump embrion_period

label embrion_period:
    "Зачатие произошло успешно. Пора поместить плод в камеру развития."
    "Теперь важно выбрать правильные условия для эмбриональной жидкости."
    centered "Очень важно выращивать эмбрион в подходящей ему среде."
    centered "Если Вы выставите температуру и кислотность правильно, ваш эмбрион сможет развиться во взрослую особь."
    centered "Но не отчаивайтесь! В некоторых случаях небольшие отклонения от нормы могут привести к интересным мутациям."
    centered "В любом случае, вы всегда можете попробовать ещё раз."
    #покажите выбор параметров
    "Я настроил параметры. Осталось ждать."

    #тут типа переход такой - тёмная вспышка

    "Я зашел в лабораторию, предвкушая результат."
    #если первый раз
    "Неужели получится? Не слишком ли просто?"
    #else
    "Может, именно в этот раз всё произойдёт."

    $fail_t = False
    $fail_ph = False

    if fail_t:
        ii "Похоже, эмбрион был повреждён из-за неправильной температуры среды."
        ii "Я ожидал от вас больше."
        "Я фыркнул."
        jump after_fail_embrion
    elif fail_ph:
        ii "Похоже, эмбрион был повреждён из-за неправильной ph среды."
        ii "А мне говорили, что вы гений..."
        gg "А мне говорили, что я получу робота, который будет мне {b}помогать{/b}."
        jump after_fail_embrion
    else:
        ii "Похоже, у вас получилось это сделать."
        "Пока Ассистент сохранял своё беспристрастное выражение лица, я понёсся к капсуле."
        #*звук спускающейся воды*
        "Эмбриональная жидкость медленно полилась в водосток."
        "Страшно представить, куда её сольют и как она может повлиять на местные растения."
        "Хотел бы я провести несколько экспериментов на эту тему. Сразу после 245-ти других экспериментов в моём списке."
        #*звук открывающейся капсулы*
        "Я затаил дыхание."
        "Вот-вот я своё создание, каким же оно получится?"
        #распределение по тянкам
        jump plant_scenario

label after_fail_embrion:
    "Блин! Теперь начинать всё сначала."
    jump deck_genes

label plant_scenario:
    #"Гибберлин" - похотливое растение (отдельная характеристика).
    #Также растение бывает злым ("Мизогенин"), добрым ("Филоксон"), ласковым ("Аморсон") и "обычным".
    $assistent_points = 0
    $scientist_points = 0
    
    #Для травяной тян и водоросли-тян:
    "Из темноты сверкнула <вставь нужный цвет> пара глаз."
    #(если в первом блоке "Фитогербарин"):
    "Девушка выходила медленной полухромой походкой."
    "Она практически не обращала внимания на меня и Ассистента. Её взгляд был обращён к свету."
    "Это было почти обидно."
    "Вообще-то я тут, вот он я, кто тебя придумал и создал..."
    "Впрочем, этого она знать не может, а для понимания того, что свет даёт тепло и энергию, достаточно весьма примитивных инстинктов."
    gg "Она… Растение? Животное?"
    gg "О! Надо придумать ей имя."
    $full_name = "Жасмин/Аля"
    $short_name = "Жасмин/Аля"
    #(если травяная): Жасмин.
    #(если водоросль): Алярия. Аля.
    gg "Пускай её зовут [full_name]."
    gg "Как тебе, робот?"
    ii "Мне всё равно, как её зовут или не зовут. А вот ко мне прошу обращаться так: Ассистент."
    "Я улыбнулся. Какой ранимый робот..."
    ii "Я собираюсь сделать несколько анализов общего характера. Это займёт несколько часов."
    ii "Мне нужно, чтобы Вы не мешали мне сканировать. Никакого человеческого дыхания, звуков и запахов быть не должно."
    gg "И что я буду делать всё это время?"
    ii "Идите-ка пообедать. Я оставил на столе несколько блюд, сделанных по программе \"Быстрый завтрак для людей, ведущих малоподвижный образ жизни\"."
    "Я возмутился."
    gg "Вообще-то я регулярно занимался в шлеме виртуальной реальности. Я прошёл 252 игры!"
    gg "Ты хоть представляешь, как много для этого нужно приседать и поднимать эти контроллеры?!"
    "Ассистент вытолкал меня из камеры."
    "Готов поспорить, местные ИИ готовят лучше тёти Зины из нашей столовой... "
    #вспышка тьмы
    "Еда и правда оказалась вкусной."
    "Я незаметно перебрался с тарелкой в лабораторию, чтобы понаблюдать за роботом и моим детищем."
    "Ассистент крутился вокруг девушки с разными приборами, пока та стояла в ведре с водой под лампой."
    "Наевшись, я откинулся на спинку такого удобного кресла."
    "Ох.. Кресло.."
    "Какое же ты мягкое..."
    #темнота
    ii "Я взял все нужные образцы."
    gg "А?"
    "От внезапного пробуждения я чуть не грохнулся со стула."
    ii "Пора заняться делом."
    gg "Да, пора бы!"
    "Я придал своему голосу максимально деловой тон."
    ii "Сперва мы можем проделать с ней несколько экспериментов."
    ii "На реакцию, на обучаемость..."
    ii "Потом перейдём к следующему этапу."
    "Ассистент дал мне немного времени, чтобы я начеркал, чем мы можем заняться с эксперементуемой."
    "Зовите меня старомодным, но я взял листик с ручкой."
    "Не знаю, сколько времени прошло. Когда весь мой листик был исписан хаотичными надписями и рисунками, я обвёл названия будущих экспериментов в кружочек."
    #зациклить менюшку, что можно выбирать всё пока варианты не закончатся
    jump first_set

label first_set:
    #по истечению этого количества экспериментов игрока выкинет в следущей части сюжета
    $experiments_left = 5
    "Что же выбрать? Как насчёт..."
    menu:
        "“Боль и наслаждение”":
            pass
        "“Знакомство со своим видом”":
            pass
        "“Прикосновения”":
            pass
        "“Позирование”":
            pass
        "“Отсос”":
            pass
        "“Ублажение”":
            pass
        "“Двойное ублажение”":
            pass

    pass
    return

