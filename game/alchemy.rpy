init python:
    class Transmuter(object):
        def __init__(self,entities=[],features=[]):
            self.features = features
            self.entities = entities
            self.entity = none
            self.feature = none
            self.result = []
            
        def set_entity(self,entity):
            self.entity = entity
            renpy.restart_interaction()
            
        def set_feature(self,feature):
            self.feature = feature
            renpy.restart_interaction()
            
        def reset(self):
            self.entity = none
            self.feature = none     
            # self.result = []
            renpy.restart_interaction()
       
        def has(self,element):
            if element in self.features or element in self.entities:
                return true
       
        def claim(self,element):
            if element[0].islower():
                if element not in self.features:
                    self.features.append(element)
            else:
                if element not in self.entities:
                    self.entities.append(element)
            renpy.restart_interaction()
            
        def transmute(self):
            recipe_not_found = true
            if self.entity and self.feature:
                for key in links:
                    materials = links[key]['materials']
                    if self.entity in materials and self.feature in materials:
                        self.result = [x for x in links[key]['output']]
                        self.reset()
                        recipe_not_found = false
                        break
                        
            if recipe_not_found:
                self.result = []
                
            renpy.restart_interaction()    
            

screen alchemy:
    vbox box_wrap true align(0.01,0.5) spacing 10:
        text "Аттрибуты" align align_center 
        null
        for key in t.features:
            textbutton key action Function(t.set_feature,key) align align_center xminimum 300
            
    vbox box_wrap true align(0.99,0.5) spacing 10:
        text "Сущности" align align_center 
        null
        for key in t.entities:
            textbutton key action Function(t.set_entity,key) align align_center xminimum 300
            
    vbox align align_center spacing 50:
        hbox spacing 50 align align_center :
            if t.feature:
                text "%s"%t.feature align align_center 
            else:
                text " --- " align align_center 

            if t.entity:
                text "%s"%t.entity align align_center 
            else:
                text " --- " align align_center 
                
        textbutton "{size=+20}Трансмутировать" action Function(t.transmute) align align_center 
        
        if len(t.result):
            hbox spacing 50 align align_center:
                for result in t.result:
                    if t.has(result):
                        text "{size=40}%s"%result align align_center 
                    else:
                        textbutton "{size=40}%s"%result action Function(t.claim,result) align align_center 
        else:
            text " --- " align align_center 
            
        textbutton "Сканировать" action Function(t.set_feature,"Сканер") xminimum 300 align align_center 

            
            
            
            
            
            
            
            
            
            
            
            
            