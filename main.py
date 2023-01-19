import random
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

def pass_gen():
    textbox.delete(index1='0.0', index2='100.0')
    uppercase_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
    numbers = '0123456789'
    special_symbols = '!@#$%^&*_-=+;:,.?/'
    all_symbols = uppercase_letters + lowercase_letters + numbers + special_symbols

    length = int(slider.get())

    def f(a, b):
        for char in a:
            if char in b:
                return True
        return False

    flag = True
    while flag: 
        password = ''
        for _ in range(length):
            password += random.choice(all_symbols)
        if len(password) == length and f(password, uppercase_letters) and f(password, lowercase_letters) and f(password, numbers) and f(password, special_symbols):
            flag = False
    textbox.insert('0.0',text=str(password))

app = customtkinter.CTk()
app.geometry('500x350')
app.title('Password generator')

frame = customtkinter.CTkFrame(master=app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text='Password Generator', font=('Roboto', 36, 'bold'))
label.pack(padx=20, pady=20)

textbox = customtkinter.CTkTextbox(master=frame, width=315, height=20, )
textbox.pack(padx=20, pady=20)
 
slider = customtkinter.CTkSlider(master=frame, from_=8, to=40)
slider.pack(padx=10, pady=20)
slider.set(12)

button = customtkinter.CTkButton(master=frame, command=pass_gen, text='Generate', width=150, height=50, font=('Roboto', 16, 'bold'))
button.pack(padx=10, pady=10)

app.mainloop()