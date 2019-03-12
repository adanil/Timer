from subprocess import Popen, PIPE
from tkinter import *
import time

userPassword = ''
correctPass = False

def enterPassGui(dateTime):
    def enterPassword(event):
        global userPassword
        userPassword = entryPass.get()
        res = checkPassword(userPassword)
        if res.strip() == 'Password:':
            global correctPass
            correctPass = True
            root.destroy()
        else:
            labelPass['text'] = 'Incorrect password, try again'
            labelPass['fg'] = 'red'
            #enterPassword(event)

    dateTime = dateTime.split()
    root = Tk()
    root.title('Timer')
    labelDate = Label(root,bg = 'grey',width=25,fg = 'white')
    labelDate['text'] = dateTime[0] + ' ' +  dateTime[1] + ' ' + dateTime[2]
    labelPass = Label(root, bg='grey', width=25, fg='white')
    labelPass['text'] = 'Enter your password'
    entryPass = Entry(root, width=25, bg='orange')
    labelDate.pack()
    labelPass.pack()
    entryPass.pack()
    entryPass.bind('<Return>', enterPassword)
    root.mainloop()

def mainGui():
    def update_clock():
        currTime = time.strftime("%A %B %d %H:%M:%S %Y").split()[3]
        timeLabel.configure(text=currTime)
        root.after(1000,update_clock)
    def action(event):
        if rCheck.get() == 0:
            actTime = eneteredTime()
            actTime = [actTime[0]+':'+actTime[1]]
            if actTime == -1:
                return
            offSystem(userPassword,actTime)
        elif rCheck.get() == 1:
            actTime = eneteredTime()
            actTime = [actTime[0]+':'+actTime[1]]
            if actTime == -1:
                return
            sleepSystem(userPassword,actTime)
        elif rCheck.get() == 2:
            actTime = eneteredTime()
            actTime = [actTime[0]+':'+actTime[1]]
            if actTime == -1:
                return
            rebootSystem(userPassword)
        else:
            labelChoose['text'] = "Please try again"
            labelChoose['fg'] = 'red'
    def eneteredTime():
        timer = enterTime.get().split(':')
        try:
            if 24 > int(timer[0]) >= 0 and 60 > int(timer[1]) >= 0:
                labelChoose['text'] = "Accepted"
                labelChoose['fg'] = 'green'
                return timer
            else:
                labelChoose['text'] = "Enter correct time(for example: 15:33)"
                labelChoose['fg'] = 'red'
                return -1
        except:
            labelChoose['text'] = "Enter correct time(for example: 15:33)"
            labelChoose['fg'] = 'red'
            return -1

    root = Tk()
    root.title('Timer')
    labelChoose = Label(root,width=50,bg='orange',text='Choose variant')
    rCheck = IntVar()
    rCheck.set(3)
    radioButtonOff = Radiobutton(root,text='Off',variable=rCheck,value = 0)
    radioButtonSleep = Radiobutton(root, text='Sleep',variable=rCheck,value = 1)
    radioButtonReboot = Radiobutton(root, text='Reboot',variable=rCheck,value = 2)
    labelEnterTime = Label(root,text='Enter time')
    enterTime = Entry(root,width=5,bg='orange',fg='black')
    buttonAction = Button(root, width=50,fg = 'grey',text='Confirm')
    labelChoose.pack()
    radioButtonOff.pack()
    radioButtonSleep.pack()
    radioButtonReboot.pack()
    labelEnterTime.pack()
    enterTime.pack()
    buttonAction.pack()
    buttonAction.bind('<Button-1>',action)
    timeLabel = Label(root,width=50,bg='orange',fg='grey')
    timeLabel.pack()
    update_clock()


    root.mainloop()


def checkPassword(sudo_password):
    command = 'sudo -v'.split()
    p = Popen(['sudo', '-S'] +command, stdin=PIPE,stderr=PIPE, universal_newlines=True)
    sudo_prompt = p.communicate(sudo_password + '\n')[1]
    return sudo_prompt
def offSystem(sudo_password,time):
    command = 'sudo shutdown -h'.split()
    p = Popen(['sudo', '-S'] + command + time, stdin=PIPE,universal_newlines=True)
    sudo_prompt = p.communicate(sudo_password + '\n')[1]
def sleepSystem(sudo_password,time):
    command = 'sudo shutdown -s'.split()
    p = Popen(['sudo', '-S'] + command + time, stdin=PIPE, universal_newlines=True)
    sudo_prompt = p.communicate(sudo_password + '\n')[1]
def rebootSystem(sudo_password):
    command = 'sudo shutdown -r'.split()
    p = Popen(['sudo', '-S'] + command + time, stdin=PIPE, universal_newlines=True)
    sudo_prompt = p.communicate(sudo_password + '\n')[1]


currTime = time.strftime("%A %B %d %H:%M:%S %Y",time.gmtime())

enterPassGui(currTime)
if correctPass == True:
    mainGui()

