from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
import random as r
import smtplib as s
from tkinter import messagebox
import mysql.connector


window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')
window.resizable(0, 0)
window.title('Login and Registration Page')

#==== mysql connection statement  ====

Conn_obj= mysql.connector.connect(host = "localhost", user = "root", password="Hishma@123", database='authentication1')
mydb= Conn_obj.cursor()




# Window Icon Photo

icon = PhotoImage(file='images\\pic-icon.png')
window.iconphoto(True, icon)

LoginPage = Frame(window)
RegistrationPage = Frame(window)

for frame in (LoginPage, RegistrationPage):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(LoginPage)


        
         

# =====================================================================================================================
# =====================================================================================================================
# ==================== LOGIN PAGE =====================================================================================
# =====================================================================================================================
# =====================================================================================================================


design_frame3 = Listbox(LoginPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame3.place(x=75, y=106)

design_frame4 = Listbox(LoginPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=676, y=106)

# ====== Email ====================
#===email_entry = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
#email_entry.place(x=134, y=170, width=256, height=34)
#email_entry.config(highlightbackground="black", highlightcolor="black")
#email_label = Label(design_frame4, text='• Username', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
#email_label.place(x=130, y=140)

# ==== Password ==================
password_entry1 = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
password_entry1.place(x=134, y=250, width=256, height=34)
password_entry1.config(highlightbackground="black", highlightcolor="black")
password_label = Label(design_frame4, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
password_label.place(x=130, y=220)


# function for show and hide password
def password_command():
    if password_entry1.cget('show') == '•':
        password_entry1.config(show='')
    else:
        password_entry1.config(show='•')


# ====== checkbutton ==============
checkButton = Checkbutton(design_frame4, bg='#f8f8f8', command=password_command, text='show password')
checkButton.place(x=140, y=288)

# ========= Buttons ===============
SignUp_button = Button(LoginPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175)

# ===== Welcome Label ==============
welcome_label = Label(design_frame4, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)

# ======= top Login Button =========
login_button = Button(LoginPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', cursor='hand2')
login_button.place(x=845, y=175)

login_line = Canvas(LoginPage, width=60, height=5, bg='#1b87d2')
login_line.place(x=840, y=203)



otp= "".join([str(r.randint(0,9)) for i in range(4)])
def send():
    try:
        #otp= "".join([str(r.randint(0,9)) for i in range(4)])
        server= s.SMTP('smtp.gmail.com',587)
        server.starttls()
        
        password= 'yotdrdlbcqkhdvdy'
        server.login('zainabisrar99@gmail.com',password)
        msg='Hello, Your OTP is '+str(otp)
        server.sendmail("zainabisrar99@gmail", email_entry1.get(), msg)
        messagebox.showinfo("Send OTP via Email", f"OTP sent to {email_entry1.get()}")
        server.quit()
        
    except :
             messagebox.showinfo("Send OTP via Email","Could not send the OTP mail")


# ====== Email ====================
email_entry1 = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
email_entry1.place(x=134, y=170, width=256, height=34)
email_entry1.config(highlightbackground="black", highlightcolor="black")
#email_label = Label(design_frame4, text='• Username', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
#email_label.place(x=130, y=140)
send_button = Button(design_frame4, text="Send OTP", font=("yu gothic ui bold",12), bd=3, command=send ,bg='#1b87d2',fg='#f8f8f8')

send_button.place(x=400, y=170, width=100, height=34)
#=====otp verification========
def otpverify():
    if password_entry1.get()==otp:
        
        messagebox.showinfo("verified","Password is verified")
    else:
        
         messagebox.showerror("Error","not verified") 

# ==== LOGIN  down button ============
loginBtn1 = Button(design_frame4, fg='#f8f8f8', text='Login', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=otpverify)
loginBtn1.place(x=133, y=340, width=256, height=50)         
   

# ==== SEND OTP button ===========
#loginBtn1 =Button(design_frame4, fg='#f8f8f8', text='Send OTP' , bg='#1b87d2', font=("yu gothic ui bold", 15),
       #            cursor='hand2', activebackground='#1b87d2')
#loginBtn1.place(x=400, y=170, width=100, height=30)


# ======= ICONS =================

# ===== Email icon =========
email_icon = Image.open('images\\email-icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=105, y=174)

# ===== password icon =========
password_icon = Image.open('images\\pass-icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
password_icon_label.image = photo
password_icon_label.place(x=105, y=254)

# ===== picture icon =========
picture_icon = Image.open('images\\pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=280, y=5)

# ===== Left Side Picture ============
side_image = Image.open('images\\vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame3, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=0, y=0)


# ===================================================================================================================
# ===================================================================================================================
# === FORGOT PASSWORD  PAGE =========================================================================================
# ===================================================================================================================
# ===================================================================================================================


def forgot_password():
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title('Forgot Password')
    win.iconbitmap('images\\aa.ico')
    win.configure(background='#f8f8f8')
    win.resizable(0, 0)

    # ====== Email ====================
    email_entry2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
    email_entry2.place(x=40, y=30, width=256, height=34)
    email_entry2.config(highlightbackground="black", highlightcolor="black")
    email_label2 = Label(win, text='•Username', fg="#89898b", bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
    email_label2.place(x=40, y=0)

    # ====  New Password ==================
    new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    new_password_entry.place(x=40, y=110, width=256, height=34)
    new_password_entry.config(highlightbackground="black", highlightcolor="black")
    new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=80)

    # ====  Confirm Password ==================
    confirm_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    confirm_password_entry.place(x=40, y=190, width=256, height=34)
    confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
    confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                   font=("yu gothic ui", 11, 'bold'))
    confirm_password_label.place(x=40, y=160)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1b87d2', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2')
    update_pass.place(x=40, y=240, width=256, height=50)


forgotPassword = Button(design_frame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8', command=lambda: forgot_password(), cursor="hand2")
forgotPassword.place(x=290, y=290)


# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================


# =====================================================================================================================
# =====================================================================================================================
# ==================== REGISTRATION PAGE ==============================================================================
# =====================================================================================================================
# =====================================================================================================================



design_frame7 = Listbox(RegistrationPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame7.place(x=75, y=106)

design_frame8 = Listbox(RegistrationPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame8.place(x=676, y=106)

# ==== Full Name =======
name_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
name_entry.place(x=284, y=150, width=286, height=34)
name_entry.config(highlightbackground="black", highlightcolor="black")
name_label = Label(design_frame8, text='•Full Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
name_label.place(x=280, y=120)
full_name= name_entry.get()

# ======= Email ===========
email_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
email_entry.place(x=284, y=220, width=286, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_label = Label(design_frame8, text='•Username', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=280, y=190)

# ====== Password =========
MAX_LEN= 12

# Symbols used in password
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']


#====== reg Password ======
password_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
password_entry.place(x=284, y=295, width=286, height=34)
password_entry.config(highlightbackground="black", highlightcolor="black")
password_label = Label(design_frame8, text='• Password', fg="#89898b", bg='#f8f8f8',
                       font=("yu gothic ui", 11, 'bold'))
password_label.place(x=280, y=265)

# ====== Confirm Password =============
confirmPassword_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
confirmPassword_entry.place(x=284, y=385, width=286, height=34)
confirmPassword_entry.config(highlightbackground="black", highlightcolor="black")
confirmPassword_label = Label(design_frame8, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                              font=("yu gothic ui", 11, 'bold'))
confirmPassword_label.place(x=280, y=355)


def password_checker():
    val = True
    if len(password_entry.get()) < 6:
        messagebox.showerror("Error",'length should be at least 6')
        val = False
    if len(password_entry.get()) > MAX_LEN:
        messagebox.showerror("Error",'length should be not be greater than 12')
        val = False
         
    if not any(num.isdigit() for num in password_entry.get()):
        messagebox.showerror("Error",'Password should have at least one numeral')
        val = False
         
    if not any(up.isupper() for up in password_entry.get()):
        messagebox.showerror("Error",'Password should have at least one uppercase letter')
        val = False
         
    if not any(low.islower() for low in password_entry.get()):
        messagebox.showerror("Error",'Password should have at least one lowercase letter')
        val = False
         
    if not any(sym in SYMBOLS for sym in password_entry.get()):
        messagebox.showerror("Error",'Password should have at least one special symbol')
        val = False
    if confirmPassword_entry.get()!=password_entry.get():
      messagebox.showerror("Error","The specified password do not match")
      val=False 
    name=name_entry.get()
    email=email_entry.get()
    pwd=password_entry.get()   
    if val==True:
        messagebox.showinfo("Information","Password is valid and successfully registered.")
        sql="INSERT INTO userinfo (fullname,username,pwd)VALUES(?,?,?)",(name,email,pwd)
        mydb.execute(sql)
        Conn_obj.commit()
        mydb.execute("SELECT * FROM userinfo")
        result=mydb.fetchall()
        for i in result:
                print(i)
    else:
        messagebox.showwarning("Warning","Password is invalid")  
def password_command2():
    if password_entry.cget('show') == '•':
        password_entry.config(show='')
    else:
        password_entry.config(show='•')


checkButton = Checkbutton(design_frame8, bg='#f8f8f8', command=password_command2, text='show password')
checkButton.place(x=290, y=330)




    

# ========= Buttons ====================
SignUp_button = Button(RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175)

SignUp_line = Canvas(RegistrationPage, width=60, height=5, bg='#1b87d2')
SignUp_line.place(x=1100, y=203)

# ===== Welcome Label ==================
welcome_label = Label(design_frame8, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)

# ========= Login Button =========
login_button = Button(RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(LoginPage), cursor='hand2')
login_button.place(x=845, y=175)

# ==== SIGN UP down button ============
signUp2 = Button(design_frame8, fg='#f8f8f8', text='Sign Up', bg='#1b87d2', font=("yu gothic ui bold", 15),
                 cursor='hand2', activebackground='#1b87d2', command=password_checker)
signUp2.place(x=285, y=435, width=286, height=50)

# ===== password icon =========
password_icon = Image.open('images\\pass-icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
password_icon_label.image = photo
password_icon_label.place(x=255, y=300)

# ===== confirm password icon =========
confirmPassword_icon = Image.open('images\\pass-icon.png')
photo = ImageTk.PhotoImage(confirmPassword_icon)
confirmPassword_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
confirmPassword_icon_label.image = photo
confirmPassword_icon_label.place(x=255, y=390)

# ===== Email icon =========
email_icon = Image.open('images\\email-icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=255, y=225)

# ===== Full Name icon =========
name_icon = Image.open('images\\name-icon.png')
photo = ImageTk.PhotoImage(name_icon)
nameIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
nameIcon_label.image = photo
nameIcon_label.place(x=252, y=153)

# ===== picture icon =========
picture_icon = Image.open('images\\pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=280, y=5)

# ===== Left Side Picture ============
side_image = Image.open('images\\vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame7, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=0, y=0)


# =====================================================================================================================
# =====================================================================================================================
# ==================== DATABASE CONNECTION ============================================================================
# =====================================================================================================================
# =====================================================================================================================


window.mainloop()
