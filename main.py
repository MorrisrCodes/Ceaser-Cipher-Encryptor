import dearpygui.dearpygui as dpg
import random as rd


#encrypt logic
letters = {0:'z', 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y'}
letters_reversed = {v: k for k, v in letters.items()}

def encrypt(text, key):
    encrypted = ''
    text = text.lower()
    for i in text:
        if i == ' ':
            encrypted += ' '
            continue
        index = letters_reversed[i]
        encrypted += (letters[(index + key) % 26]).upper()
    return encrypted

def encrypt_callback():
    key = rd.randint(1, 25)
    text = dpg.get_value("input_text")
    encrypted = encrypt(text, key)
    dpg.set_value("output_text", encrypted)
    dpg.set_value("key", key)


#decrypt logic


#gui
dpg.create_context()
dpg.create_viewport(title='Ceaser Cipher Encryptor', width=460, height=215)

with dpg.window(label="Encryptor", width=600, height=215, pos=(0, 0), collapsed=True):
    dpg.add_text("Before")
    dpg.add_input_text(default_value="Enter text here", tag = 'input_text')
    dpg.add_button(label="Encrypt", callback=encrypt_callback)
    
    dpg.add_text('')
    dpg.add_text('Encrypted Text')
    dpg.add_input_text(default_value="*****", tag = 'output_text')
    dpg.add_text('key')
    dpg.add_input_text(default_value="*****", tag = 'key')
    

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
    dpg.add_text("Ceaser Cipher can only encrypt letters, so spell numbers.")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()