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
def decrypt(text, key):
    decrypted = ''
    text = text.lower()
    for i in text:
        if i == ' ':
            decrypted += ' '
            continue
        index = letters_reversed[i]
        decrypted += letters[(index - key) % 26]
    return decrypted

def decrypt_callback():
    text = dpg.get_value("d_input_text")
    key = int(dpg.get_value("d_key"))
    decrypted = decrypt(text, key)
    dpg.set_value("d_output_text", decrypted)

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
    dpg.add_input_text(default_value="Enter text here", tag = "d_input_text")

    dpg.add_input_text(default_value="Enter key here", tag = "d_key")
    dpg.add_button(label="Decrypt", callback=decrypt_callback)

    dpg.add_text('')
    dpg.add_text('Decrypted Text')
    dpg.add_input_text(default_value="*****", tag = 'd_output_text')

with dpg.window(label="Instructions", width=600, height=200, pos=(0, 36), collapsed=False):
    dpg.add_text("Welcome to Ceaser Cipher Encryptor!")
    dpg.add_text("Click the drop down menu of the service you would like to use.")
    dpg.add_text("Ceaser Cipher can only encrypt letters, so spell numbers.")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()