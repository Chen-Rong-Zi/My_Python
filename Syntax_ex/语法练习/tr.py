import ui

def button_tapped(sender):
    sender.title = 'Hello'

view = ui.View()                                      
view.name = 'Demo'                                    
view.background_color = 'white'                       
button = ui.Button(title='Tap me!')                   
button.center = (view.width * 0.05, view.height * 0.05) 
button.flex = 'LRTB'                                  
button.action = button_tapped                         
view.add_subview(button)                              
view.present('sheet')  
