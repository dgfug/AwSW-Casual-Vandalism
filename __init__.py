from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Casual Vandalism", "0.1", "Ryann1706")

    def mod_load(self):
       ml = modinfo.get_mods()["MagmaLink"].import_ml()

       ml.find_label("lorem3") \
        .search_say("If this is the facility, then the place indicated is... the school. Or, rather, somewhere between the school and the administrative building.") \
        .hook_to("Ryann_Lorem_GetBrick") \
        .search_say("Here we are. The X on the map is right between these two buildings, so it must be around here somewhere.") \
        .link_from("Ryann_Lorem_GetBrick_end")

       ml.find_label("lorem3") \
        .search_menu("Look inside the windows.").branch() \
        .search_say("As Lorem flew up to the windowsill with a few flaps of his wings, I turned to the right to look inside the windows of the administrative building") \
        .hook_to("Ryann_Lorem_Search") \
        .search_say("Nothing.") \
        .link_from("Ryann_Lorem_Search_end")
        
       ml.find_label("lorem3") \
        .search_menu("Look inside the windows.").branch_else() \
        .search_say("The curtains were closed, but through a small gap, I could barely see inside.") \
        .link_from("Ryann_Lorem_NormalWindow")
        
       ml.find_label("lorem3") \
        .search_say("Did you find anything?") \
        .link_from("Ryann_Lorem_LoremBrick")
        

    def mod_complete(self):
        pass
