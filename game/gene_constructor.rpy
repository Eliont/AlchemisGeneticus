init python:
    class Gene(object):
        def __init__(self,data,id,group):
            for property in data:
                setattr(self,property,data[property])
                
            self.id = id
            self.group = group
            
            

    class Creature(object):
        def __init__(self):
            self.genes = {}
            self.type = none
            self.growth = []
            self.groups = ['chassis','diet','skin','color','behavior','brain','cognitive','bust']
        
        def has_gene(self,group,gene):
            if self.genes.has_key(group):
                if self.genes[group] == gene:
                    return true
        
        def gene_string(self):
            letters = []
            for group in self.groups:
                if self.genes.has_key(group):
                    letters.append(self.genes[group]['letter'].capitalize())
                else:
                    letters.append('*')
                
            return ' | '.join(letters)
            
        def validate(self):
            # a/b => b => c => Холстаурус
            # c/d => a/b => b => Альраун
            # c/d => a => a => Флоукельп
            if not self.genes.has_key('chassis'):
                return "Нежизнеспособно"
            if not self.genes.has_key('diet'):
                return "Нежизнеспособно"
            if not self.genes.has_key('skin'):
                return "Нежизнеспособно"
            
            for creature_id in creatures:
                gene_pattern = creatures[creature_id]['pattern']
                if self.genes['chassis']['letter'] in gene_pattern['chassis'] and self.genes['diet']['letter'] in gene_pattern['diet'] and self.genes['skin']['letter'] in gene_pattern['skin']:
                    self.type = creature_id
                    return creatures[creature_id]['name']
            
            self.type = none
            
            return "Нежизнеспособно"  

        
        def start(self):
            self.growth = []
            mutations = []
            survived = true
            
            if not self.type:
                self.growth.append("Ассистент: похоже, составленная ДНК жизнеспособна. Давайте попробуем ещё раз.")
                renpy.invoke_in_new_context(self.growth_log) 
                return
                
            for group in self.groups:
                if not self.genes.has_key(group):
                    self.growth.append("Ассистент: похоже, составленная ДНК жизнеспособна. Давайте попробуем ещё раз.")
                    renpy.invoke_in_new_context(self.growth_log) 
                    return
            
            data = creatures[self.type]
            t_min = data['temperature']['min']
            t_max = data['temperature']['max']
            
            ph_min = data['ph']['min']
            ph_max = data['ph']['max']
            
            if gene_constructor_temperature < t_min:
                survived = chance(data['temperature']['survive'])
                if not survived:
                    self.growth.append("Ассистент: Эмбрион погиб - слишком низкая температура")
                else:
                    for mutation in data['temperature_mutation']:
                        if mutation['value'] == 'below':
                            mutations.append((mutation['group'],mutation['id']))
            
            if gene_constructor_temperature > t_max:
                survived = chance(data['temperature']['survive'])
                if not survived:
                    self.growth.append("Ассистент: Эмбрион погиб - слишком высокая температура")
                else:
                    for mutation in data['temperature_mutation']:
                        if mutation['value'] == 'above':
                            if chance(mutation['chance']):
                                mutations.append((mutation['group'],mutation['id']))
            
            if gene_constructor_ph < ph_min:
                survived = chance(data['ph']['survive'])
                if not survived:
                    self.growth.append("Ассистент: Эмбрион погиб - слишком низкая ph")
                else:
                    for mutation in data['ph_mutation']:
                        if mutation['value'] == 'below':
                            if chance(mutation['chance']):
                                mutations.append((mutation['group'],mutation['id']))
            
            if gene_constructor_ph > ph_max:
                survived = chance(data['ph']['survive'])
                if not survived:
                    self.growth.append("Ассистент: Эмбрион погиб - слишком высокая ph")
                else:
                    for mutation in data['ph_mutation']:
                        if mutation['value'] == 'above':
                            if chance(mutation['chance']):
                                mutations.append((mutation['group'],mutation['id']))
            
            if survived:
                mutation_string = []
                for m in mutations:
                    group,gene_id = m
                    genes[group][gene_id]['unlocked'] = true
                    mutation_string.append(genes[group][gene_id]['name'])
                    
                if len(mutations):
                    self.growth.append('Мутация: ' + ' '.join(mutation_string))
                self.growth.append("Ассистент: Зачатие произошло успешно. Пора поместить плод в камеру развития.")
            
            renpy.invoke_in_new_context(self.growth_log)
            
            # renpy.restart_interaction()  
        
        def growth_log(self):
            _window_show()
            for line in self.growth:
                narrator(line)
            _window_hide()
            
        def gene_add(self,gene,group):
            self.genes[group] = gene
            renpy.restart_interaction()
            
        def gene_not_found(self,gene,group):
            notify(gene['name']+' отсутствует в генохранилище')
            renpy.restart_interaction()        
            

screen framed_textbutton(txt,action,align=(0.5,0.5)):
    frame align align background Solid((0,0,0,128)) xminimum 150:
        textbutton txt action action align (0.5,0.5)

 

screen gene_constructor:
    vbox spacing 10 align (0.5,0.01):
        text "%s"%creature.gene_string() align align_center 
        text "Прогноз: %s"%creature.validate() align align_center 
    
    vbox spacing 20 xalign 0.5 ypos 200:
        hbox align align_center spacing 10:
            for group in creature.groups:
                vbox align align_center spacing 10:
                    for gene_id in genes[group]:
                        if genes[group][gene_id]['unlocked']:
                            if creature.has_gene(group,genes[group][gene_id]):
                                use framed_textbutton(txt="{color=#0f0}%s"%genes[group][gene_id]['name'],action=Function(creature.gene_add,gene=genes[group][gene_id],group=group))
                            else:
                                use framed_textbutton(txt="%s"%genes[group][gene_id]['name'],action=Function(creature.gene_add,gene=genes[group][gene_id],group=group))
                        else:
                            use framed_textbutton(txt="{color=#0ff}%s"%genes[group][gene_id]['name'],action=Function(creature.gene_not_found,gene=genes[group][gene_id],group=group))
                            
        text "Эмбриональная жидкость" align align_center
        
        hbox spacing 100 align align_center:
            vbox spacing 20 align align_center:
                text "Температура: %d"%gene_constructor_temperature align align_center
                frame background Solid((255,255,255,150)) align (0.5,0.5):
                    bar:
                        value VariableValue("gene_constructor_temperature", 40, step=1)
                        xalign 0.5 yalign 0.5 
                        xmaximum 400 
                        changed renpy.restart_interaction
                        thumb_shadow None
                        
                        
            vbox spacing 20 align align_center:
                text "ph: %d"%gene_constructor_ph align align_center
                frame background Solid((255,255,255,150)) align (0.5,0.5):
                    bar:
                        value VariableValue("gene_constructor_ph", 10, step=1)
                        xalign 0.5 yalign 0.5 
                        xmaximum 400 
                        changed renpy.restart_interaction
                        thumb_shadow None
    
    use framed_textbutton(txt="{size=+20}Запуск",action = Function(creature.start),align = (0.5,0.92))


            
            
            
            
            
            
            
            
            
            
            