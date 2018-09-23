# Здесь основные предустановки и функции безотносительные к игре.
# Он у меня кочует из проекта в проект и может быть свободно распространён.

transform notify_effect:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0
        
# кастомный экран уведомления        
screen custom_notify(txt):
    frame at notify_effect:
        align(0.5,0.0)  
        background Frame('gui/notify.jpg',10,10)
        text ('{size=+30}%s{/size}'%txt) align(0.5,0.5)
    timer 3.0 action Hide('custom_notify')

init -10 python: 

##################### Системные установки #####################

    import os,pygame,math,sys,random,bisect,yaml
    import copy as cp
    import xml.etree.ElementTree as xmldb
    from collections import OrderedDict
    
    # установка окна игры по центру
    # полезно если запускается не в полный экран
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    
    sys.setdefaultencoding('utf-8')
    
    # лень писать заглавные
    true = True
    false = False
    none = None
    
    result = True
    
    DebugTools_last_jump = ''
    
    align_center = (0.5,0.5)
     
    def is_sequence(arg):
        return (not hasattr(arg, "strip") and
                hasattr(arg, "__getitem__") or
                hasattr(arg, "__iter__"))

     
    # округление
    def math_round(number):
        integer,fraction = math.modf(number)
        if fraction >= 0.5:
            integer = math.ceil(number)
        else:
            integer = math.floor(number)
        return int(integer)

    # получить знак числа
    def sign(number):
        if number > 0:
            return 1
        elif number < 0:
            return -1
        else:
            return 0
    
    # эта функция не делает ничего, совсем ничего...
    def do_nothing():
        pass
    
    # боремся с целочисленным по умолчанию делением
    def divide(n1,n2):
        try:
            return float(n1)/float(n2)
        except:
            debug([n1,n2])
   
    # функция заменяет в строке квадратные и фигурные скобки 
    # на угловые чтобы не конфликтовать с текстовыми тегами
    # и операторами форматирования
    def toSafeString(s):
        s = str(s)
        s = s.replace("[","<")
        s = s.replace("]",">")
        s = s.replace("{","<")
        s = s.replace("}",">")   
        return s           

    def str_to_id(string):
        result = u''
        for char in string:
            result += u'%d'%ord(char)
        return result
    
    def ensure_positive(number):
        if number < 0: return 0
        else: return number
        
    
    def chance(value, limit=100, show=False):
        '''Returns True if value is <= a random integer between 1 and limit.

        If limit is 100, this means that a value of 60 has a 60% chance for True
        '''
        number = random.randint(1, int(limit))
        if number <= value:
            result = True
        else:
            result = False
        if config.developer and show:
            notify(u"Resulted in %d from %d, limit - %d, and result - %s." % (number, limit, value, result))
        return result
            
    def dice(sides, add=[],sub=[]):
        value = random.randint(1, int(sides))
        for modificator in add:
            value += modificator
        for modificator in sub:
            value -= modificator
        if value <= 1: return 1
        if value >= sides: return sides
        return value    
    
     
    # выбрать случайный вариант из предложенных
    def select(variants,show=false):
        result = renpy.random.choice(variants)
        if config.developer and show:
            notify(u"Выбрано '%s'."%str(result))
        return result
    
    # выяснить что за нафиг путём записи нужных сообщений в файл
    # хотя вообще-то wtf = Write To File, но пользоватьей приходится
    # когда думаешь WTF?! в другой расшифровке...
    def wtf(message,logfile="bughunt.txt"):
        file = open(os.path.join(config.gamedir,logfile),"w+")
        file.write(str(message)+"\n")                
        file.close()
        
        
    # обёртка над оповещалкой
    def notify(message,style=False):
        if style: 
            msg = "{=%s}{size=+10}%s"%(style,toSafeString(message))
            # renpy.notify(u"%s"%msg) 
            renpy.show_screen('custom_notify',txt=msg)
        else:
            # renpy.notify(u"{size=+10}%s"%toSafeString(message))          
            renpy.show_screen('custom_notify',txt=toSafeString(message))        
    
    
    # безопасный джамп
    # если метки нет, игра не вылетит а просто сообщит об этом
    def jump(labelname):
        global DebugTools_last_jump
        if renpy.has_label(labelname):
            # notify("jump %s"%labelname)
            store.debugTools_last_label = labelname
            DebugTools_last_jump = labelname
            renpy.restart_interaction()
            renpy.jump(labelname)
        else:
            notify(u"Метки '%s' не существует."%labelname) 
            
            

    def listdir(dir):
        return os.listdir(os.path.join(config.gamedir,dir))
        
    def debug(obj):
        raise Error, str(obj)
        
    def exist(path):
        return os.path.exists(os.path.join(config.gamedir,path))  

    def listdir(path):
        if exist(path):
            return os.listdir(os.path.join(config.gamedir,path))
        else:
            return []
     
    def copy(what):
        return cp.deepcopy(what)
     
    # анализ строк и превращение их в целые, дробные, и логические значения
    def parse(string):
        try:
            value = int(string)
        except TypeError:
            value = string
        except AttributeError:
            value = string
        except ValueError:
            try:
                value = float(string)
            except ValueError:
                if string.lower() in ['true','yes','on']:
                    value = True
                elif string.lower() in ['false','no','off','none']:
                    value = False
                else:
                    value = string
        return value
    
    # Первая часть работы с базами данных - автокласс
    # Универсальная структура данных
    class Structure(object):
        def __init__(self,namespace=None,**additional_pars): 
            self.id = ''
            if namespace:
                for key in namespace:
                    self.set(key,namespace[key])
            for key in additional_pars:
                self.set(key,additional_pars[key])
        
        def namespace(self): return self.__dict__
        def has(self,par): return self.__dict__.has_key(par)
        def set(self,par,value): self.__dict__[par] = value
        def mod(self,par,value): self.__dict__[par] += value
                
        def __getitem__(self, key):
            return self.__dict__[key]
        def __setitem__(self, key, value):
            self.__dict__[key] = value
    
    # вторая часть движка для работы с базами
    # разбор файла и загрузка его в словарь
    # выловленный в инете скрипт разбора ини доработан
    # для работы ещё и с хмл 
    def dict_from_config_file(file, raw=false, vars=None): 
        result = dict()

        if file[-3:] == 'ini':
            """Convert an INI file to a dictionary""" #from cherrypy 
            inifile = ConfigParser() 
            inifile.read(renpy.loader.transfn(file))     # Parse config file 
         
            # Load INI file into a dict 
            for section in inifile.sections(): 
                result[section] = dict() 
                result[section]['id'] = section
                for option in inifile.options(section): 
                    v = inifile.get(section, option, raw, vars) 
                    result[section][option] = parse(v)
                    
        elif file[-3:] == 'xml':
            tree = xmldb.parse(renpy.loader.transfn(file)).getroot()
            for node in tree:
                if not node.attrib.has_key('id'): node.attrib['id'] = node.tag 
                result[node.attrib['id']] = parse(node.attrib)
                result[node.attrib['id']]['xml'] = node
                
        elif file.endswith('.yaml') or file.endswith('.yml'): 
            with open(renpy.loader.transfn(file)) as config_file:
                result = yaml.load(config_file.read().replace('\t',''))
                
        return result    
    
    # Преобразование xml в многоуровневый словарь
    # Особое требование - ноды должны иметь разные имена или иметь аттрибут id который будет использован как ключ
    # иначе в результирующем словаре окажется только последняя нода так как перезапишут друг друга
    # обращение: каждая нода - словарь. Чтобы получить доступ к подуровню
    # обратиться к нему как в вложеннуму словарю
    # чтобы получить доступ к аттрибуту - обратиться к словарю attr вложенному в 
    # нужную ноду, 
    # "db/buildings.xml" - result['smallbrothel1']['small']['attr']['type'] выдаст 'empty'
    def xml_to_dict(filename):
        tree = xmldb.parse(renpy.loader.transfn(filename)).getroot()
        result = parse_xml_nodes(tree)
        return result 

    def parse_xml_nodes(node):
        result = {}
        for n in node:
            if n.attrib.has_key('id'):
                n.tag = n.attrib['id']
            
            result[n.tag] = dict(attr = n.attrib)
            for key in result[n.tag]:
                result[n.tag][key] = parse(result[n.tag][key])
            
            result[n.tag].update(parse_xml_nodes(n))
            
        return result
     
    # Третья часть движка для работы с базами
    # превращаем словари в объекты и обрабатываем значения
    # 'true','yes','on','false','no','off' - станут логическими
    # числа без точки - станут целыми
    # числа с точкой - станут дробными
    # строки - строками и останутся =)
    # за это отвечает функция parse() определённая ранее
    # Параметры:
    # dic - можно вставить в существующий словарь, или использовать новый
    # entity - класс который создавать, имненно ссылка на тип существующего класса
    # perform_init - выполнить метод "init" ( не __init__ ) после загрузки 
    def load_database(file,dic = None, entity = Structure, perform_init = False):
        db = dict_from_config_file(file)
        group_id = file.split('/')[-1].split('.')[0]
        if not dic:
            dictionary = dict()
        else:
            dictionary = dic
        for entry in db:
            dictionary[entry] = entity()
            dictionary[entry].id = entry 
            dictionary[entry].group = group_id 
            for key in db[entry]:
                dictionary[entry].__dict__[key] = parse(db[entry][key])

        
        if perform_init: 
            for entry in dictionary:        
                dictionary[entry].init()

        return dictionary

    # покажет позицию курсора если вывести рисунок cursorPosition
    # show cursorPosition on bottom
    def cursorPositionFunction(st, at):
        x,y = pygame.mouse.get_pos()
        return Text("{size=+10}%d - %d"%(x,y)), .1   
            
            
            
            
    # ресайз картиники с сохранением соотношения сторон            
    def ProportionalScale(img, maxwidth, maxheight):
        currentwidth, currentheight = get_size(img)
        xscale = float(maxwidth) / float(currentwidth)
        yscale = float(maxheight) / float(currentheight)
        
        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale
            
        newwidth = currentwidth * minscale
        newheight = currentheight * minscale
        
        return im.FactorScale(img,minscale,minscale)

        
    def resize(img, x=400, y=400):        
        return ProportionalScale(img, x, y)   
        
    def eq_resize(img, size):        
        return ProportionalScale(img, size, size)     
    
    
    def get_size(d):
        d = renpy.easy.displayable(d)
        w, h = renpy.render(d, 0, 0, 0, 0).get_size()
        w, h = int(round(w)), int(round(h))
        return w, h
        
    def getMousePosition(anchor=false):
        xreal, yreal = renpy.get_physical_size()
        xpos, ypos = pygame.mouse.get_pos()
        xcoef = divide(config.screen_width,xreal)
        ycoef = divide(config.screen_height,yreal)
        x = xpos * xcoef
        y = ypos * ycoef
        xanchor = divide(x, xreal)
        yanchor = divide(y, yreal)
        if anchor: 
            return int(x),int(y),xanchor,yanchor
        else:
            return int(x),int(y)
            
    # # # Сторонние # # # 
    
    def weighted_random(choice_options):
        """
        :param choice_options: list of tuples (option, weight), где option - возвращаемый вариант, а weight - вес варианта. Чем больше, тем вероятнее что он выпадет.
        :return: option, или None, если сделать выбор не удалось.
        Пример использования:
        coin_flip = weighted_random([("орёл", 1), ("решка",1)])
        """
        if len(choice_options) > 0:
            # Складываем вес всех доступных энкаунтеров
            accumulated = []
            total = 0
            for option, weight in choice_options:
                assert weight >= 0
                accumulated.append(weight + total)
                total += weight
            # Проверяем, что суммарный вес не равен нулю.
            if total == 0:
                return None
            r = random.random() * accumulated[-1]
            return choice_options[bisect.bisect(accumulated, r)][0]
        return None
    
    # кастомная анимация (anim.Filmstrip)        
    class FilmStrip(renpy.Displayable):
        def __init__(self, image, framesize, gridsize, delay, frames=None, loop=True, reverse=False, **kwargs):
            super(FilmStrip, self).__init__(**kwargs)
            width, height = framesize
            self.image = Image(image)
            cols, rows = gridsize
        
            if frames is None:
                frames = cols * rows
        
            i = 0
        
            # Arguments to Animation
            args = [ ]
        
            for r in range(0, rows):
                for c in range(0, cols):
        
                    x = c * width
                    y = r * height
        
                    args.append(Transform(self.image, crop=(x, y, width, height)))
        
                    i += 1
                    if i == frames:
                        break
        
                if i == frames:
                    break
                    
            # Reverse the list:
            if reverse:
                args.reverse()
                
                
            self.width, self.height = width, height
            self.frames = args
            self.delay = delay
            self.index = 0
            self.loop = loop
        
        def render(self, width, height, st, at):
            if not st:
                self.index = 0
            
            t = self.frames[self.index]
            
            if self.index == len(self.frames) - 1:
                if self.loop:
                    self.index = 0
                else:
                    return renpy.Render(0, 0)
            else:
                self.index = self.index + 1
            
            child_render = renpy.render(t, width, height, st, at)
            render = renpy.Render(self.width, self.height)
            render.blit(child_render, (0, 0))
            renpy.redraw(self, self.delay)
            return render
            
        def visit(self):
            return [self.image]     

            
            
    # анимация - взрыв частиц 
    class ParticleBurst(renpy.Displayable):
        def __init__(self, displayable, crops, neg_range=(-8, -1), pos_range=(1, 8), **kwargs):
            """
            Crops the displayable and sends the bits flying...
            """
            super(ParticleBurst, self).__init__(**kwargs)
            self.displayable = displayable
            self.crops = crops # This is doubled...
            
            self.args = None
            
            self.neg_range = neg_range
            self.pos_range = pos_range
            
            self.width = 0
            self.height = 0
        
        def render(self, width, height, st, at):
            if not st:
                self.args = None
            
            if not self.args:
                t = Transform(self.displayable)
                child_render = renpy.render(t, width, height, st, at)
                self.width, self.height = child_render.get_size()
                
                # Size of one crop:
                crop_xsize = int(round(self.width / float(self.crops)))
                crop_ysize = int(round(self.height / float(self.crops)))
                
                # The list:
                i = 0
                args = OrderedDict()
                half = self.crops / 2.0
                choices = range(*self.neg_range) + range(*self.pos_range)
            
                for r in xrange(self.crops):
                    for c in xrange(self.crops):
            
                        x = c * crop_xsize
                        y = r * crop_ysize
                        
                        # direction = choice(choices), choice(choices)
                        if r < half and c < half: # -x, y
                            # direction = (0, 0)
                            # direction = (randint(*self.neg_range), randint(*self.neg_range))
                            direction = (random.randint(*self.neg_range), random.randint(*self.neg_range))
                        elif r > half and c < half: # -x, -y
                            # direction = (0, 0)
                            direction = (random.randint(*self.neg_range), random.randint(*self.pos_range))
                        elif r < half and c > half: # x, y
                            # direction = (0, 0)
                            direction = (random.randint(*self.pos_range), random.randint(*self.neg_range))
                        elif r > half and c > half: # x, -y
                            direction = (0, 0)
                            direction = (random.randint(*self.pos_range), random.randint(*self.pos_range))
                        else: # Anything in the cross in the middle...
                            if r > half:
                                
                                direction = (0, random.randint(*self.pos_range))
                            elif c > half:
                                direction = (random.randint(*self.pos_range), 0)
                            elif r < half:
                                direction = (0, random.randint(*self.neg_range))
                            else:
                                direction = (random.randint(*self.neg_range), 0)
                        # direction = choice(range(randint(*self.neg_speed), randint(*self.pos_speed))), choice(range(randint(*self.neg_speed), randint(*self.pos_speed)))
                        
                        args[(Transform(t, rotate=random.randint(0, 90), crop=(x, y, crop_xsize, crop_ysize)))] = {"coords": [x, y], "direction": direction}
                self.args = args
                
            render = renpy.Render(self.width, self.height)
            for r in self.args:
                cr = renpy.render(r, width, height, st, at)
                coords = self.args[r]["coords"]
                direction = self.args[r]["direction"]
                render.blit(cr, tuple(coords))
                coords[0] = coords[0] + direction[0]
                coords[1] = coords[1] + direction[1]
            renpy.redraw(self, 0)
            return render

           
label _instant_exit: 
    $renpy.quit()
 
# добавляет в нижний левый угол несколько полезных на стадии разаработки примочек
# X - мгновенный выход, в обход диалога подтверждения
# R - перекомпиляция игры
# также отображает текущие координаты курсора
screen debugTools:
    tag debugTools
    if config.developer and debug_use_reload_panel:
        hbox spacing 10:        
            xalign 0.0
            yalign 0.0
            button:
                text "X"
                action ui.callsinnewcontext("_instant_exit")
            button:
                text "R"
                action ui.callsinnewcontext("_save_reload_game")
            # button:
                # text "T"
                # action Jump('region_full_view')
            
            # frame align (0.5, 0.5):
                # text "[debugTools_last_label]" align (0.5, 0.5) size 25
            # frame align (0.5, 0.5):    
                # text "%s"%DebugTools_last_jump align (0.5, 0.5) size 25
            
            # add(DynamicDisplayable(cursorPositionFunction)) yalign 0.5
            
# init -1 python hide:
    # def label_callback(name, abnormal):
        # store.debugTools_last_label = name
    # config.label_callback = label_callback
