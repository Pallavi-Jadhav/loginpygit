import guizero as g

def clear_uname():
    uname.clear()

def clear_pass():
    password.clear()


app = g.App(title='Login', height=300, width=500, layout='grid', bg='lightblue')
title = g.Text(app, text='SIGN IN', size=40, color='blue', font='Helvetica', grid=[1, 0], align='left')
uname_label = g.Text(app, text='Enter username: ', grid=[0, 2], align='left', size=15)
uname = g.TextBox(app, text='Username', grid=[1, 2], width=45, align='left')
uname.when_clicked = clear_uname
password_lbl = g.Text(app, text='Enter password: ', grid=[0, 3], size=15, align='left')
password = g.TextBox(app, text='Password', grid=[1, 3], width=45, align='left')
password.when_clicked = clear_pass

forgot_pass = g.Text(app, text='Forgot password?', color='blue', font='Helvetica', grid=[0, 4], align='left')

login_button = g.PushButton(app, text='Login', grid=[0, 5], align='left', width=10, height=1)
login_button.text_size = 10
register_button = g.PushButton(app, text='Signup', grid=[0, 6], align='left', width=10, height=1)

app.display()


