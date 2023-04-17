import tkinter as tk
from tkinter import messagebox
from tkinter import *

global root

root = tk.Tk()
root.configure(bg="#fff")
root.title("Main")
root.geometry("925x500+300+200")
root.resizable(False, False)

background_img = PhotoImage(file="shiplake.png")
Label(root, image=background_img, bg="white").place(x=125, y=110)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Shiplake College", fg="#9c4151", bg="white", font=("Microsoft YaHei UI Light", 22, "bold"))
heading.place(x=45, y=10)


def quit():
    root.destroy()


def check_input(input_str):
    if input_str == stored_username:
        input_window.destroy()
        global passoword_window
        password_window = tk.Toplevel(root)
        password_window.title("Password")
        password_window.geometry("925x500+300+200")
        password_window.resizable(False, False)
        password_window.configure(bg="#fff")
        header_label = tk.Label(password_window, bg="#fff", text="Sign in", width=900, height=1,
                                font=("Bombshell Pro", 18), fg="#9c4151", border=0)
        header_label.pack(pady=20)
        password_label = tk.Label(password_window, bg="#fff", text="Password:", font=("Bombshell Pro", 11,))
        password_label.pack(pady=20)
        password_entry = tk.Entry(password_window, bg="#fff", show=".", border=1, font=("Bombshell Pro", 10, "bold"))
        password_entry.pack()

        password_submit_button = tk.Button(password_window, height=1, width=20, text="Enter", bg="#9c4151", fg="white",
                                           border=0, font=("Microsoft YaHei UI Light", 8),
                                           command=lambda: check_password(password_entry.get(), password_window))
        password_submit_button.pack(pady=15)

    else:
        input_window.destroy()
        print("Login Report")
        print("")
        print("------------")
        print("")
        print("LOGIN FAILED")
        print("")
        print("Entered Username: " + input_str)
        print("")
        print("------------")
        print("Shiplake College")
        messagebox.showerror("Error", "Invalid Username", icon="error")


def logout():
    window.destroy()


def info():
    information = tk.Tk()
    information.title("Information")
    information.geometry("925x500+300+200")
    information.configure(bg="#fff")
    information.resizable(False, False)
    header_label = tk.Label(information, bg="#fff", text="Information", font=("Bombshell Pro", 20, "bold"),
                            fg="#9c4151")
    header_label.pack(pady=20)
    label2 = tk.Label(information, bg="#fff", text="When is the next update coming out?", font=("Bombshell Pro", 12),
                      fg="#9c4151")
    label2.pack(pady=20)
    label2 = tk.Label(information, bg="#fff",
                      text="This program is always being updated, the next major update is coming at 12/04/2023.",
                      font=("Bombshell Pro", 10), fg="#9c4151")
    label2.pack(pady=20)
    label2 = tk.Label(information, bg="#fff", text="What can this do?", font=("Bombshell Pro", 12), fg="#9c4151")
    label2.pack(pady=20)
    label2 = tk.Label(information, bg="#fff",
                      text="This script is a DEMO login/sign-up script for python using the Tkinter module.",
                      font=("Bombshell Pro", 10), fg="#9c4151")
    label2.pack(pady=20)


def addu():
    tt = tk.Tk()
    tt.title("Info")
    tt.geometry("250x150")
    tt.label = tk.Label(tt, text="You must use your isams login details for this to work.")
    tt.label.pack()


def Adminlog():
    password_window = tk.Toplevel(root)
    password_window.title("Admin Login")
    password_window.geometry("925x500+300+200")
    password_window.resizable(False, False)
    password_window.configure(bg="#fff")
    header_label = tk.Label(password_window, bg="#fff", text="Authorization", font=("Bombshell Pro", 20, "bold"),
                            fg="#9c4151")
    header_label.pack(pady=20)
    password_label = tk.Label(password_window, bg="#fff",
                              text="To continue please enter an administrator username and password.",
                              font=("Bombshell Pro", 11, "bold"), fg="#9c4151")
    password_label.pack(pady=20)
    user_label = tk.Label(password_window, bg="#fff", text="Username:", font=("Bombshell Pro", 12, "bold"),
                          fg="#9c4151")
    user_label.pack(pady=20)
    user_entry = tk.Entry(password_window, bg="#fff", font=("Bombshell Pro", 10, "bold"), fg="#9c4151")
    user_entry.pack()
    password_label = tk.Label(password_window, bg="#fff", text="Password:", font=("Bombshell Pro", 12, "bold"),
                              fg="#9c4151")
    password_label.pack(pady=20)
    password_entry = tk.Entry(password_window, bg="#fff", show="*", font=("Bombshell Pro", 10, "bold"), fg="#9c4151")
    password_entry.pack()

    password_submit_button = tk.Button(password_window, height=1, width=22, text="Enter", bg="#9c4151", fg="white",
                                       border=0, font=("Microsoft YaHei UI Light", 8),
                                       command=lambda: Adminpanel(password_entry.get(), user_entry.get(),
                                                                  password_window))
    password_submit_button.pack(pady=15)


def Adminpanel(password_str, user_str, password_window):
    if user_str == "Administrator" and password_str == stored_password:
        global window
        password_window.destroy()
        welcome_window.destroy()
        window = tk.Toplevel(root)
        window.title("Admin Panel")
        window.geometry("925x500+300+200")
        window.resizable(False, False)
        window.configure(bg="#fff")
        heading = Label(window, text="Welcome, " + stored_username + "", fg="#9c4151", bg="white",
                        font=("Microsoft YaHei UI Light", 24, "bold"))
        heading.pack(pady=20)
        button = tk.Button(window, text="View users", height=1, width=22, bg="#9c4151", fg="white", border=0,
                           font=("Microsoft YaHei UI Light", 8), command=users)
        button.pack(pady=15)
        button = tk.Button(window, text="Add/Remove users", height=1, width=22, bg="#9c4151", fg="white", border=0,
                           font=("Microsoft YaHei UI Light", 8), command=addu)
        button.pack(pady=15)
        logout_button = tk.Button(window, text="Log out", height=1, width=22, bg="#9c4151", fg="white", border=0,
                                  font=("Microsoft YaHei UI Light", 8), command=logout)
        logout_button.pack(pady=15)
        quit_button = tk.Button(window, text="Quit", height=1, width=22, bg="#9c4151", fg="white", border=0,
                                font=("Microsoft YaHei UI Light", 8), command=quit)
        quit_button.pack(pady=15)

    else:
        print("Login report")
        print("")
        print("------------")
        print("")
        print("ADMIN LOGIN FAILED.")
        print("")
        print("Attempted Admin Username: " + user_str)
        print("Attempted Admin Password: " + password_str)
        print("")
        print("------------")
        print("Shiplake College")
        input_window.destroy
        messagebox.showerror("Error", "Invalid password or username.", icon="error")


def users():
    adm_win = tk.Tk()
    adm_win.title("Tools")
    adm_win.geometry("250x350")
    adm_win.resizable(False, False)
    adm_win.configure(bg="#fff")
    header_label = tk.Label(adm_win, text="Admin Tools", fg="#9c4151", bg="white", border=0,
                            font=("Microsoft YaHei UI Light", 14))
    header_label.pack(pady=20)
    label = tk.Label(adm_win, text="Users in current session:", fg="#9c4151", bg="white", border=0,
                     font=("Microsoft YaHei UI Light", 11))
    label.pack(pady=10)
    label = tk.Label(adm_win, text="Username: " + stored_username + "", fg="#9c4151", bg="white", border=0,
                     font=("Microsoft YaHei UI Light", 11))
    label.pack(pady=8)
    label = tk.Label(adm_win, text="Password: " + stored_password + "", fg="#9c4151", bg="white", border=0,
                     font=("Microsoft YaHei UI Light", 11))
    label.pack(pady=8)
    label = tk.Label(adm_win, text="More Admin Tools:", fg="#9c4151", bg="white", border=0,
                     font=("Microsoft YaHei UI Light", 11))
    label.pack(pady=10)
    button = tk.Button(adm_win, text="Add/Remove users", height=1, width=22, bg="#9c4151", fg="white", border=0,
                       font=("Microsoft YaHei UI Light", 8), command=addu)
    button.pack(pady=15)


def Changelog():
    window = tk.Toplevel(root)
    window.title("Change log")
    window.geometry("925x500+300+200")
    window.resizable(False, False)
    window.configure(bg="#fff")
    header_label = tk.Label(window, text="Change log", fg="#9c4151", bg="white", border=0,
                            font=("Microsoft YaHei UI Light", 14))
    header_label.pack(pady=20)
    label = tk.Label(window, text="V0.45 Slight Graphic Updates.", bg="#fff")
    label.pack(pady=5)
    label = tk.Label(window, text="V0.56 GUI Improvements.", bg="#fff")
    label.pack(pady=5)
    label = tk.Label(window, text="V0.67 Signup added.", bg="#fff")
    label.pack(pady=5)
    label = tk.Label(window, text="V0.75 Removed signup popup window.", bg="#fff")
    label.pack(pady=5)
    label = tk.Label(window, text="V0.89 Remove settings button due to glitch (It may return soon)", bg="#fff")
    label.pack(pady=5)
    label = tk.Label(window, text="V1.0 Background color fixed.", bg="#fff")
    label.pack(pady=5)
    label = tk.Label(window, text="V1.2 Added signup popup window back (Its much better now).", bg="#fff")
    label.pack(pady=5)
    header_label = tk.Label(window, text="Coming soon..", fg="#9c4151", bg="white", border=0,
                            font=("Microsoft YaHei UI Light", 12), )
    header_label.pack(pady=20)
    label = tk.Label(window, text="Better GUI Design", bg="#fff")
    label.pack(pady=5)
    label = tk.Label(window, text="More options", bg="#fff")
    label.pack(pady=5)


def check_password(password_str, password_window):
    if password_str == stored_password:
        global welcome_window
        password_window.destroy()
        welcome_window = tk.Tk()
        welcome_window.configure(bg="#fff")
        welcome_window.title("Account")
        welcome_window.geometry("925x500+300+200")
        welcome_window.resizable(False, False)
        heading = Label(welcome_window, text="Welcome, " + stored_username + "", fg="#9c4151", bg="white",
                        font=("Microsoft YaHei UI Light", 24, "bold"))
        heading.pack(pady=20)
        button = tk.Button(welcome_window, height=1, width=22, text="Credits", bg="#9c4151", fg="white", border=0,
                           font=("Microsoft YaHei UI Light", 8), command=Credits)
        button.pack(pady=15)
        button = tk.Button(welcome_window, height=1, width=22, text="Change Log", bg="#9c4151", fg="white", border=0,
                           font=("Microsoft YaHei UI Light", 8), command=Changelog)
        button.pack(pady=15)
        button = tk.Button(welcome_window, height=1, width=22, text="Administrator Panel", bg="#9c4151", fg="white",
                           border=0, font=("Microsoft YaHei UI Light", 8), command=Adminlog)
        button.pack(pady=15)
        button = tk.Button(welcome_window, height=1, width=22, text="Info", bg="#9c4151", fg="white", border=0,
                           font=("Microsoft YaHei UI Light", 8), command=info)
        button.pack(pady=15)
        button = tk.Button(welcome_window, height=1, width=22, text="About us", bg="#9c4151", fg="white", border=0,
                           font=("Microsoft YaHei UI Light", 8), command=aboutus)
        button.pack(pady=15)
        button = tk.Button(welcome_window, height=1, width=22, text="Log out", bg="#9c4151", fg="white", border=0,
                           font=("Microsoft YaHei UI Light", 8), command=homelogout)
        button.pack(pady=15)
        print("Login Report")
        print("")
        print("------------")
        print("")
        print("LOGIN SUCCEEDED")
        print("")
        print("Entered Password: " + password_str)
        print("")
        print("------------")
        print("Shiplake College")

    else:
        print("Login Report")
        print("")
        print("------------")
        print("")
        print("LOGIN FAILED")
        print("")
        print("")
        print("Attempted Password: " + password_str)
        print("")
        print("------------")
        print("Shiplake College")
        input_window.destroy
        messagebox.showerror("Error", "Invalid Password", icon="error")


def prompt_input():
    global input_window
    input_window = tk.Toplevel(root)
    input_window.title("Username")
    input_window.geometry("925x500+300+200")
    input_window.resizable(False, False)
    input_window.configure(bg="#fff")
    header_label = tk.Label(input_window, text="Sign in", width=900, height=1, font=("Bombshell Pro", 18), bg="#fff",
                            fg="#9c4151", border=0)
    header_label.pack(pady=20)
    input_label = tk.Label(input_window, text="Username:", font=("Bombshell Pro", 11,), bg="#fff")
    input_label.pack(pady=20)
    input_entry = tk.Entry(input_window)
    input_entry.pack(pady=7)

    input_submit_button = tk.Button(input_window, height=1, width=22, text="Login", bg="#9c4151", fg="white", border=0,
                                    font=("Microsoft YaHei UI Light", 8),
                                    command=lambda: check_input(input_entry.get()))
    input_submit_button.pack(pady=10)


def Credits():
    input_window = tk.Toplevel(root)
    input_window.title("Credits")
    input_window.geometry("925x500+300+200")
    input_window.resizable(False, False)
    input_window.configure(bg="#fff")
    header_label = tk.Label(input_window, text="Credits:", width=900, height=1, font=("Bombshell Pro", 18), bg="#fff",
                            fg="#9c4151", border=0)
    header_label.pack(pady=20)
    input_label = tk.Label(input_window, text="Creater/Coder: Archie McPherson (7L)", bg="#fff")
    input_label.pack(pady=20)
    input_label = tk.Label(input_window, text="Made using python in Visual Studio 2022", bg="#fff")
    input_label.pack(pady=20)


def aboutus():
    display_window = tk.Toplevel(root)
    display_window.title("Credits")
    display_window.geometry("925x500+300+200")
    display_window.resizable(False, False)
    display_window.configure(bg="#fff")
    header_label = tk.Label(display_window, text="About us", width=900, height=1, font=("Bombshell Pro", 18), bg="#fff",
                            fg="#9c4151", border=0)
    header_label.pack(pady=20)
    display_label = tk.Label(display_window, text="We are a college located in shiplake, The headmaster is Mr T Howe.",
                             bg="#fff")
    display_label.pack(pady=20)
    display_label = tk.Label(display_window, text="We are very keen in rowing and music.", bg="#fff")
    display_label.pack(pady=20)
    display_label = tk.Label(display_window,
                             text="We have great departments including: Music, DET, Art, Languages, IT and P.E",
                             bg="#fff")
    display_label.pack(pady=20)
    display_label = tk.Label(display_window,
                             text="We have a very good IT department as you may see by this amazing application.",
                             bg="#fff")
    display_label.pack(pady=20)
    display_label = tk.Label(display_window,
                             text="About me: I am 12 years old, I go to Shiplake College. I love IT and I code: Python, Lua and Scratch (I know, Scratch is blocks not code).",
                             bg="#fff")
    display_label.pack(pady=20)


def destroy_window():
    new.destroy()


def sign_up():
    global new
    new = tk.Tk()
    new.title("Sign Up")
    new.geometry("250x215")
    new.configure(bg="#fff")
    new.resizable(False, False)
    new.label = tk.Label(new, text="Thanks for signing up!", font=("Calibri", 13), bg="#fff", fg="#9c4151")
    new.label.pack(pady=15)
    new.label = tk.Label(new, text="I understand that any administrator", font=("Calibri", 10), bg="#fff", fg="#9c4151")
    new.label.pack(pady=15)
    new.label = tk.Label(new, text="can view my username and password", font=("Calibri", 10), bg="#fff", fg="#9c4151")
    new.label.pack(pady=15)
    tick_var = tk.BooleanVar()
    tick_button = tk.Checkbutton(new, text="I agree", variable=tick_var, command=destroy_window, bg="#fff")
    tick_button.pack(pady=12, padx=12)
    username = username_label.get()
    password = password_label.get()
    global stored_username, stored_password
    stored_username = username
    stored_password = password


def homelogout():
    welcome_window.destroy()


######---------------------------------
def on_enter(e):
    username_label.delete(0, "end")


def on_leave(e):
    username = username_label.get()
    if username == "":
        username_label.insert(0, "Username")


username_label = Entry(frame, width=20, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
username_label.place(x=30, y=80)
username_label.insert(0, "Username")
username_label.bind("<FocusIn>", on_enter)
username_label.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


#######--------------------------------
def on_enter(e):
    password_label.delete(0, "end")


def on_leave(e):
    password = password_label.get()
    if password == "":
        password_label.insert(0, "Password")


password_label = Entry(frame, width=20, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
password_label.place(x=30, y=150)
password_label.insert(0, "Password")
password_label.bind("<FocusIn>", on_enter)
password_label.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

#######################################

Button(frame, width=39, pady=7, text="Sign up", bg="#9c4151", fg="white", border=0, command=sign_up, ).place(x=35,
                                                                                                             y=204)
label = Label(frame, text="Already have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

#######################################
sign_in = Button(frame, width=6, text="Sign in", border=0, bg="white", cursor="hand2", fg="#9c4151",
                 command=prompt_input)
sign_in.place(x=220, y=270, )
#######################################


root.mainloop()
