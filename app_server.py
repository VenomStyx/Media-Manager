#  _____                           _       
# |_   _|                         | |      
#   | | _ __ ___  _ __   ___  _ __| |_ ___ 
#   | || '_ ` _ \| '_ \ / _ \| '__| __/ __|
#  _| || | | | | | |_) | (_) | |  | |_\__ \
#  \___/_| |_| |_| .__/ \___/|_|   \__|___/
#                | |                       
#                |_|                       
# -----------------------------------------------------------------------     


from time import sleep
from resources.config import settings_core
from resources.server import mm_server



#  _   _            _       _     _           
# | | | |          (_)     | |   | |          
# | | | | __ _ _ __ _  __ _| |__ | | ___  ___ 
# | | | |/ _` | '__| |/ _` | '_ \| |/ _ \/ __|
# \ \_/ / (_| | |  | | (_| | |_) | |  __/\__ \
#  \___/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/
# -----------------------------------------------------------------------                         


settings = settings_core()
server = mm_server()



#   ___              _ _           _   _             
#  / _ \            | (_)         | | (_)            
# / /_\ \_ __  _ __ | |_  ___ __ _| |_ _  ___  _ __  
# |  _  | '_ \| '_ \| | |/ __/ _` | __| |/ _ \| '_ \ 
# | | | | |_) | |_) | | | (_| (_| | |_| | (_) | | | |
# \_| |_/ .__/| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|
#       | |   | |                                    
#       |_|   |_|                                    
# ----------------------------------------------------------------------- 

########## APPLICATION LOOP
#####
while True:

    ## Process Pending Posts
    server.process_pending_scheduled_posts()

    ## Sleep for the specified amount of time
    sleep(settings.processing_delay_in_seconds)
