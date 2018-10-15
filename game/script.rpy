define gg = Character("Учёный")
define ii = Character("Ассистент")

init python:
    _game_menu_screen = None
    config.developer = True
    debug_use_reload_panel = True

    gene_constructor_temperature = 30
    gene_constructor_ph = 8
    
    # ============== ПЕРЕМЕННЫЕ ====================
    $ spray_tested = False
    $ sprinkler_system_tested = False
    $ paddl_tested = False
    $ whip_tested = False
    $ electricity_tested = False
    $ anal_vibrator_tested = False
    $ XL_vibrator_tested = False

    $ intro_teaching_passed = False

    $ first_posing_try = True
    $ posing_teached = False

    $ first_blowjob_try = True
    $ blowjob_teached = False

    $ intro_to_itself = False

    $ way_to_touch = 'None' #не знает как экспериментуемой нравится чтобы её трогали

    $ max_experimets_count = 5

label main_menu:
    return   

label start:
    scene lab with dissolve
    show screen debugTools
    
    call intro from _call_intro
    
    window hide
    
    python:
        # links = dict_from_config_file('db/reactions.yaml')
        # t = Transmuter(entities=['Хомяк','Кот','Рыбка','Попугайчик'])
        genes = dict_from_config_file('db/genes.yml')
        creatures = dict_from_config_file('db/creatures.yml')
        creature = Creature()
                
    # show screen alchemy
    show screen gene_constructor
    
    python:
        while True:
            ui.interact()

    return
