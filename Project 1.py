from tkinter import *
import tkinter.messagebox
import time

class MyGUI:
    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.geometry("480x500+100+100")
        self.mainWindow.title("StudyClock")
        self.fr1 = Frame(self.mainWindow, width = 480, height = 600, bg = 'black')
        self.fr1.place(x = 0, y = 0)
        self.mainWindow.resizable(False, False)
        
# Time Entry Limiter
        def ssLimiter(*args):
            if len(self.ssTime.get()) > 2:
                self.ssTime.set(self.ssTime.get()[:2])
            if (int(self.ssTime.get()) < 60) and (int(self.ssTime.get()) > -1):
                self.entrySS.config(bg = 'Silver')
            else:
                self.entrySS.config(bg = 'red')
                tkinter.messagebox.showinfo("Time Entry Error", "Enter amount of seconds between 0 and 59")
                self.ssTime.set('')
                
        def mmLimiter(*args):
            if len(self.mmTime.get()) > 2:
                self.mmTime.set(self.mmTime.get()[:2])
            if (int(self.mmTime.get()) < 60) and (int(self.mmTime.get()) > -1):
                self.entryMM.config(bg = 'Silver')
            else:
                self.entryMM.config(bg = 'red')
                tkinter.messagebox.showinfo("Time Entry Error", "Enter amount of minutes between 0 and 59")
                self.mmTime.set('')
                
        def hhLimiter(*args):
            if len(self.hhTime.get()) > 2:
                self.hhTime.set(self.hhTime.get()[:2])
            if (int(self.hhTime.get()) < 24) and (int(self.hhTime.get()) > -1):
                self.entryHH.config(bg = 'Silver')
            else:
                self.entryHH.config(bg = 'red')
                tkinter.messagebox.showinfo("Time Entry Error", "Enter amount of hours between 0 and 23")
                self.hhTime.set('')
                
        def countdownTimer():
        # Convert break interval if any to seconds
            if self.choice1.get():
                try:
                    breakInterval = ((int(self.spinBoxTime.get()) * 60))
                except:
                    tkinter.messagebox.showinfo("BREAK INTERVAL ERROR", "Incorrect break interval value\nEnter an integer between 1 - 1439 min(s)")
                else:
                    if breakInterval < 1:
                        tkinter.messagebox.showinfo("BREAK INTERVAL ERROR", "Incorrect break interval value\nEnter an integer between 1 - 1439 min(s)")
                        raise;
                self.rb4.select()
                self.rb4.flash()
            else:
                breakInterval = ((int(self.breakTime.get()) * 60))
            
        # Convert entire time value to seconds
            userSetTime = ((int(self.hhTime.get()) * 3600) + (int(self.mmTime.get()) * 60) + (int(self.ssTime.get())))
            counter = 0
            while userSetTime > -1:
                min, sec = (userSetTime // 60), (userSetTime % 60)
                hr = 0
                if min > 60:
                    hr , min = (min // 60 , min % 60)
                self.ssTime.set(sec)
                self.mmTime.set(min)
                self.hhTime.set(hr)
                
                self.mainWindow.update()
                time.sleep(1)
                if(userSetTime == 0):
                    self.ssTime.set('00')
                    self.mmTime.set('00')
                    self.hhTime.set('00')
        # Add 1 to counter to avoid having breakScheduler popping off when breakInterval = 0 
                counter += 1
        # Break Scheduler
        # If second counter is equal to breakInterval in seconds
                if (counter == breakInterval):
                # Reset counter to 0
                    counter = 0
                    tkinter.messagebox.showinfo("BREAK", "It's time to take a break.")
        # Reduce user entered time by 1 second
                userSetTime -= 1
            tkinter.messagebox.showinfo("Timer Complete", "Study Session is over")
        
        def pause():
            tkinter.messagebox.showinfo("Need a Break?", "Timer Paused\nClick OK to resume")
    
# Clock Frame
        self.fr3 = Frame(self.fr1, width = 500, height = 500, bg = 'black')
        self.fr3.place(x = -25, y = 25)
        
# Label
    # (Main Label)
        self.labelTitle = Label(self.fr3, text = "StudyClock", fg = 'Gold3', bg = 'black', font = ('Arial', 45, 'bold'))
        self.labelTitle.place(x = 50, y = 6)
        
    # (Clock Image)
        self.clockImage = PhotoImage(file = "Assets/clock.png")
        self.labelClock = Label(self.fr1, image = self.clockImage)
        self.labelClock.place(x = 365, y = 25)
# Entry Box
    # (Time Setter)
        
        self.labelTimeHH = Label(self.fr3, text = "HOUR", font = ('Arial', 14, 'bold'), bg = 'black',
                                    fg = 'white')
        self.labelTimeHH.place(x = 80, y = 205)
        
        self.labelTimeMM = Label(self.fr3, text = "MINUTE", font = ('Arial', 14, 'bold'), bg = 'black',
                                    fg = 'white')
        self.labelTimeMM.place(x = 210, y = 205)
        
        self.labelTimeSS = Label(self.fr3, text = "SECOND", font = ('Arial', 14, 'bold'), bg = 'black',
                                    fg = 'white')
        self.labelTimeSS.place(x = 345, y = 205)
        
        self.ssTime = StringVar()
        self.ssTime.trace('w', ssLimiter)
        
        self.mmTime = StringVar()
        self.mmTime.trace('w', mmLimiter)
        
        self.hhTime = StringVar()
        self.hhTime.trace('w', hhLimiter)
                
        self.entrySS = Entry(self.fr3, width = 2, font = ('Arial', 40, 'bold'),
                             textvariable = self.ssTime)
        self.entrySS.place(x = 340 , y = 100, height = 100, width = 100)
        
        self.entryMM = Entry(self.fr3, width = 2, font = ('Arial', 40, 'bold'),
                             textvariable = self.mmTime)
        self.entryMM.place(x = 200, y = 100, height = 100, width = 100)
        
        self.entryHH = Entry(self.fr3, width = 2, font = ('Arial', 40, 'bold'),
                             textvariable = self.hhTime)
        self.entryHH.place(x = 60, y = 100, height = 100, width = 100)
        
# Scales
        
        self.scaleHH = Scale(self.fr3, troughcolor = 'black', showvalue = 0, variable = self.ssTime, to = 59, length = 95)
        self.scaleHH.place(x = 445, y = 100)
        
        self.scaleMM = Scale(self.fr3, bg = 'white', troughcolor = 'black', showvalue = 0, variable = self.mmTime, to = 59, length = 95)
        self.scaleMM.place(x = 305, y = 100)
        
        self.scaleSS = Scale(self.fr3, bg = 'white', troughcolor = 'black',showvalue = 0, variable = self.hhTime, to = 23, length = 95)
        self.scaleSS.place(x = 165, y = 100)
        
    # Default Values for Time Entry
        self.entrySS.insert(END, "0")
        self.entryMM.insert(END, "0")
        self.entryHH.insert(END, "0")

# Break Scheduler Frame
        self.fr2 = Frame(self.fr1, width = 250, height = 125, bg = 'light grey')
        self.fr2.place(x = 40, y = 275)
# Radio Button
    # (Break Scheduler)
        self.breakTime = IntVar()
        
        self.labelBreak = Label(self.fr2, text = "Set a break interval", font = ('Arial', 15, 'bold','underline'), bg = 'light grey')
        self.labelBreak.place(x = 5, y = 15)
        
        self.rb1 = Radiobutton(self.fr2, text = "15 Mins  ", font = ('Arial', 11, 'bold') , variable = self.breakTime,
                               value = "15", bg = "light grey", activebackground = 'orange')
        self.rb1.place(x = 10, y = 50)
        
        self.rb2 = Radiobutton(self.fr2, text = "30 Mins  ", font = ('Arial', 11, 'bold'), variable = self.breakTime,
                               value = "30", bg = "light grey", activebackground = 'orange')
        self.rb2.place(x = 110, y = 50)
        
        self.rb3 = Radiobutton(self.fr2, text = "60 Mins  ", font = ('Arial', 11, 'bold'), variable = self.breakTime,
                               value = "60", bg = "light grey", activebackground = 'orange')
        self.rb3.place(x = 10, y = 85)
        
        self.rb4 = Radiobutton(self.fr2, text = "No Breaks", font = ('Arial', 11, 'bold'), variable = self.breakTime,
                               value = "0", bg = "light grey", activebackground = 'orange')
        self.rb4.place(x = 110, y = 85)
        
# Custom Break Frame
        self.fr4 = Frame(self.fr1, width = 150, height = 125, bg = 'grey')
        self.fr4.place(x = 290, y = 275)
        
# Check Box


        def customBreak():
            if self.choice1.get() == 1:
                self.rb1.config(state = DISABLED)
                self.rb2.config(state = DISABLED)
                self.rb3.config(state = DISABLED)
                self.rb4.config(state = DISABLED)
            elif self.choice1.get() == 0:
                self.rb1.config(state = NORMAL)
                self.rb2.config(state = NORMAL)
                self.rb3.config(state = NORMAL)
                self.rb4.config(state = NORMAL)
        self.choice1 = IntVar()
        self.choice1.set(0)
        
        self.checkButtonCustom = Checkbutton(self.fr4, text = "Custom Break", font = ('Arial', 11, 'bold'), variable = self.choice1, bg = 'grey', command = customBreak)
        self.checkButtonCustom.place(x = 5, y = 30)

# Spin Box (Additional Widget)

        def validateSpinBox():
            return 

        self.spinBoxLabel = Label(self.fr4, text = "min(s)", font = ('Arial', 13, 'bold'), bg = 'grey')
        self.spinBoxLabel.place(x = 65, y = 85)
        
        self.spinBoxTime = StringVar()
        
        self.spinBoxBreak = Spinbox(self.fr4, textvariable = self.spinBoxTime, to = 1439, from_= 1, width = 4, font = ('Arial', 13, 'bold'), validatecommand = validateSpinBox)
        self.spinBoxBreak.place(x = 10, y = 75, width = 55, height = 35)
        
# Start/Quit Button Frame
        self.fr5 = Frame(self.fr1, width = 500, height = 50, bg = 'black')
        self.fr5.place(x = 25, y = 425)
# Button
    # (Quit Button)
        self.buttonQuit = Button(self.fr5, text = "Quit", command = self.mainWindow.destroy, font = ('Calibri', 20, 'bold'), bg = 'IndianRed')
        self.buttonQuit.place(x = 150, y = 0, width = 125, height = 50)
        
    # (Start Button)
        self.buttonStart = Button(self.fr5, text = "Start", font = ('Calibri', 20, 'bold'), bg = 'SeaGreen', command = countdownTimer)
        self.buttonStart.place(x = 10, y = 0, width = 125, height = 50)

    # (Pause Button)
        self.buttonPause = Button(self.fr5, text = "Pause", command = pause, font = ('Calibri', 20, 'bold'), bg = 'Silver')
        self.buttonPause.place(x = 290, y = 0, width = 125, height = 50)
        
        
        mainloop()

        
                        
myGUI = MyGUI()
