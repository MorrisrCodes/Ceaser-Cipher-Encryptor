import dearpygui.dearpygui as dpg
import random as rd

dpg.create_context()
dpg.create_viewport(title='Ceaser Cipher Encryptor', width=460, height=215)

with dpg.window(label="Encryptor", width=600, height=215, pos=(0, 0), collapsed=True):
    dpg.add_text("Before")
    dpg.add_input_text(default_value="Enter text here")
    dpg.add_button(label="Encrypt")
    
    dpg.add_text('')
    dpg.add_text('Encrypted Text')
    dpg.add_input_text(default_value="*****")
    dpg.add_text('key')
    dpg.add_input_text(default_value="*****")
    

with dpg.window(label="Decryptor", width=600, height=200, pos=(0, 18), collapsed=True):
    dpg.add_text("Before")
    dpg.add_input_text(default_value="Enter text here")

    dpg.add_input_text(default_value="Enter key here")
    dpg.add_button(label="Decrypt")

    dpg.add_text('')
    dpg.add_text('Decrypted Text')
    dpg.add_input_text(default_value="*****")

with dpg.window(label="Instructions", width=600, height=200, pos=(0, 36), collapsed=False):
    dpg.add_text("Welcome to Ceaser Cipher Encryptor!")
    dpg.add_text("Click the drop down menu of the service you would like to use.")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()