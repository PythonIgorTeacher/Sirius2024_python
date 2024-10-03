from tkinter import *
from tkinter import ttk #для красивых виджетов
from tkinter import messagebox #для оповещения в таймере
from datetime import datetime 
from time import *

wer = Tk()
wer.attributes("-topmost",True)
wer.geometry("500x500")
wer.title("Часы by forkli")
wer.configure(bg='gray40')

#__________________________________________________________________________________________________ТЕКУЩЕЕ_ВРЕМЯ______________________________________________________________________________

style_wt_frame = ttk.Style() #стиль фрейма для отображения ТЕКУЩЕГО ВРЕМЕНИ
style_wt_frame.configure('swtf.TFrame', background='gray40')

wt_frame = ttk.Frame(wer, style='swtf.TFrame') #фрейм для отображения ТЕКУЩЕГО ВРЕМЕНИ

def update_time(): #функция для обновления времени 
    time_label.config(text=f"{datetime.now():%H:%M:%S}")
    wer.after(10, update_time) # Запланировать выполнение этой же функции через 10 мс
    

time_label = ttk.Label(wt_frame, font=("helvetica", 95), background='gray40', foreground='green yellow')
time_label.pack() #лейбл, на котором отображается ТЕКУЩЕЕ ВРЕМЯ

update_time() #запуск функции обновления времени

#______________________________________________________________________________________________________ТАЙМЕР_______________________________________________________________________________________

hour = IntVar() #создание переменных часов, минут и секунд
minute = IntVar()
second = IntVar()
hour.set('0') #присваивание им нулевого значения
minute.set('0')
second.set('0')

style_t_frame = ttk.Style() #стиль фрейма ТАЙМЕРА
style_t_frame.configure('stf.TFrame', background='gray40')
timer_frame = ttk.Frame(wer, style='stf.TFrame') #фрейм ТАЙМЕРА 

# спинбоксы часов, минут и секунд ТАЙМЕРА
hour_spinbox = ttk.Spinbox(timer_frame, from_=0, to=100, width=3, textvariable=hour, font=('Helvetica', 50)).grid(row=1, column=1, padx=5)
minute_spinbox = ttk.Spinbox(timer_frame, from_=0, to=60, width=3, textvariable=minute, font=('Helvetica', 50)).grid(row=1, column=2, padx=5)
second_spinbox = ttk.Spinbox(timer_frame, from_=0, to=60, width=3, textvariable=second, font=('Helvetica', 50)).grid(row=1, column=3, padx=5)

# надписи 'Часы' 'Минуты' 'Секунды' в ТАЙМЕРЕ
hour_label = ttk.Label(timer_frame, text='Часы', font=("helvetica", 20), background='gray40', foreground='yellow').grid(row=2, column=1, padx=5)
minute_label = ttk.Label(timer_frame, text='Минуты', font=("helvetica", 20), background='gray40', foreground='yellow').grid(row=2, column=2, padx=5)
second_label = ttk.Label(timer_frame, text='Секунды', font=("helvetica", 20), background='gray40', foreground='yellow').grid(row=2, column=3, padx=5)

exit = True
def timer(): #логика таймера
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get()) #объединение трёх переменных в одну (получается количество секунд)
        global exit
        while temp >-1 and exit:
            mins, secs = divmod(temp, 60) #разделение temp на минуты и секунды
            hours = 0
            if mins > 60: #прибавление часов, если минут больше, чем 60
                hours, mins = divmod(mins, 60) 

            hour.set("{0:2d}".format(hours)) #задаём в формат часам, минутам и секундам ТАЙМЕРА
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            wer.update() #обновление окна
            sleep(1) #задержка 1 секунда
      
            if (temp == 0): #по истечению заданного времени, создание НОВОЕ ОКНО с оповещением
                messagebox.showinfo(title=None, message='Время вышло!')
            temp -= 1 #вычитаение из temp единицу, что означает истечение одной секунды
    except: #исключение ошибок
        print('Выберите правильное значение')

def check_on_exit():
    global exit, wer
    exit = False
    wer.quit()
wer.protocol("WM_DELETE_WINDOW", check_on_exit)

style_bst = ttk.Style() #стиль КНОПКИ СТАРТА ТАЙМЕРА
style_bst.configure('bst.TButton', foreground="#0052cc", background='#ffffff', font=('Helvetica', 35, 'bold'))
bst = ttk.Button(timer_frame, text='Старт', style='bst.TButton', takefocus=False, command=timer).grid(row=3, column=1, columnspan=3, pady=25) #КНОПКА СТАРТА ТАЙМЕРА

#______________________________________________________________________________________________________СЕКУНДОМЕР_______________________________________________________________________________________
class Secondomer(): #логика секундомера
    def __init__(self):
        self.counter = 0 #атрибут, в котором будет сохранено время (в секундах)
        self.running = None #атрибут для запуска и остановки секундомера

    def start(self): #запуск секундомер
        self.running = True
        self.run() #запуск отсчёта времени
        
    def run(self): #отсчёт времени СЕКУНДОМЕРА
        if self.running == True:       
            self.counter += 1 #прибавление одной секунды
            sm_time['text'] = self.counter #сохранение значения атрибута в текст невидимого Labal'а, чтобы не обращаться опять к self.counter 
            sm_hour['text'] = int(int(sm_time['text'])//3600) #вывод в правильном формате часов, минут и секунд
            sm_min['text'] = int(int((sm_time['text'])/60)%60)
            sm_sec['text'] = int(int(sm_time['text'])%60)
            wer.after(1000, self.run) #задержка перед запуском этого метода
            
    def stop(self): #остановка секундомера
        self.running = False
        self.run() #запуск отсчёта времени ещё раз, чтобы он прекратился

    def reset(self): #обнуление времени и атрибута
        self.counter = 0
        sm_time['text'] = 0
        sm_hour['text'] = 0
        sm_min['text'] = 0
        sm_sec['text'] = 0
sm = Secondomer() #обращение к классу с помощью короткой переменной

sm_time = ttk.Label(wer, text=sm.counter) #НЕВИДИМЫЙ Labal для правильного отображения времени

style_sm_frame = ttk.Style() #стиль фрейма для отображения ВРЕМЯ СЕКУНДОМЕРА
style_sm_frame.configure('stsm.TFrame', background='gray40')
sm_frame = ttk.Frame(wer, style='stsm.TFrame') #фрейм для отображения ВРЕМЯ СЕКУНДОМЕРА

style_tsm = ttk.Style() #стиль фрейма для отображения ВРЕМЯ СЕКУНДОМЕРА
style_tsm.configure('stsm.TLabel', foreground='yellow', background='gray40', font=('Helvetica', 90, 'bold'))

sm_hour = ttk.Label(sm_frame, text=sm_time, style='stsm.TLabel') #Label'ы для отображения времени СЕКУНДОМЕРА
sm_min = ttk.Label(sm_frame, text=sm_time, style='stsm.TLabel')
sm_sec = ttk.Label(sm_frame, text=sm_time, style='stsm.TLabel')

style_smn = ttk.Style() #стиль фрейма для отображения ВРЕМЯ СЕКУНДОМЕРА
style_smn.configure('ssmn.TLabel', foreground='gray80', background='gray40', font=('Helvetica', 15, 'bold'))

name_hour = ttk.Label(sm_frame, text='Часы', style='ssmn.TLabel').grid(row=1, column=0, padx=25) #надписи 'Часы' 'Минуты' 'Секунды' в СЕКУНДОМЕРЕ
name_min = ttk.Label(sm_frame, text='Минуты', style='ssmn.TLabel').grid(row=1, column=1, padx=25)
name_sec = ttk.Label(sm_frame, text='Секунды', style='ssmn.TLabel').grid(row=1, column=2, padx=25)

sm_hour.grid(row=0, column=0, padx=25) #отображение Часов, Минут и Секунд
sm_min.grid(row=0, column=1, padx=25)
sm_sec.grid(row=0, column=2, padx=25)

sm_hour['text'] = 0 #по умолчанию, время нулевое
sm_min['text'] = 10
sm_sec['text'] = 0

style_sm_button = ttk.Style() #стиль фрейма для отображения ВРЕМЯ СЕКУНДОМЕРА
style_sm_button.configure('ssm.TButton', font=('Helvetica', 10, 'bold'))

style_btn_sm_frame = ttk.Style() #стиль фрейма для отображения КНОПОК СЕКУНДОМЕРА
style_btn_sm_frame.configure('sbtn_smf.TFrame', background='gray40')
btn_sm_frame = ttk.Frame(wer, style='sbtn_smf.TFrame') #фрейм для отображения КНОПОК СЕКУНДОМЕРА

start = ttk.Button(btn_sm_frame, text='Старт', takefocus=False, style='ssm.TButton', command=sm.start).grid(row=1, column=0, padx=10)
stop = ttk.Button(btn_sm_frame, text='Стоп', takefocus=False, style='ssm.TButton', command=sm.stop).grid(row=1, column=1, padx=10)
reset = ttk.Button(btn_sm_frame, text='Сброс', takefocus=False, style='ssm.TButton', command=sm.reset).grid(row=1, column=2, padx=10)

#_____________________________________________________________________________________________________МЕНЮ_________________________________________________________________________________________________________________________

style_btn_menu = ttk.Style() #стиль кнопок из меню
style_btn_menu.configure('TButton', foreground="red", background='#0052cc', font=('Helvetica', 40))

style_menu_frame = ttk.Style() #стиль фрейма меню
style_menu_frame.configure('snf.TFrame', background='gray40')
menu_frame = ttk.Frame(wer, style='snf.TFrame') #фрейм меню


menu_frame.pack(anchor='center', expand=True) #отображение фрейма меню (при запуске программы)



#_____________________________________________________________________________________________КНОПКА_ВОЗВРАТА_В_МЕНЮ_________________________________________________________________________________________________________________________

style_bmb_frame = ttk.Style() #стиль фрейма КНОПКИ ВОЗВРАТА В МЕНЮ
style_bmb_frame.configure('sbmbf.TFrame', background='yellow')

bmb_frame = ttk.Frame(style='sbmbf.TFrame') #фрейм КНОПКИ ВОЗВРАТА В МЕНЮ


def back_to_menu(): #логика кнопки 'Назад'
    wer.after_cancel(update_time) #остановка обновления времени
    wt_frame.pack_forget()  #закрытие ВСЕХ фреймов
    bmb_frame.pack_forget()
    timer_frame.pack_forget()
    sm_frame.pack_forget()
    btn_sm_frame.place_forget()
    menu_frame.pack(anchor='center', expand=True) #отображение фрейма меню

style_bmb_menu = ttk.Style() #стиль кнопки ВОЗВРАТ В МЕНЮ
style_bmb_menu.configure('bmb.TButton', foreground="#0052cc", background='#ffffff', font=('Helvetica', 25))

back_menu_button = ttk.Button(bmb_frame, text='Назад', takefocus=False, style='bmb.TButton', command=back_to_menu).pack() #КНОПКА ВОЗВРАТА В МЕНЮ 


#_________________________________________________________________________________________________ОТОБРАЖЕНИЕ_ТЕКУЩЕГО_ВРЕМЕНИ_____________________________________________________________________________

def world_time(): #текущее время
    menu_frame.pack_forget() #скрытие фрейма с меню
    bmb_frame.pack(side=BOTTOM, anchor=E) #отображение кнопки 'Назад'
    wt_frame.pack(anchor='center', expand=True) #отображение фрейма ТЕКУЩЕЕ ВРЕМЯ

#_____________________________________________________________________________________________________ОТОБРАЖЕНИЕ_ТАЙМЕРА_____________________________________________________________________________

def timer(): #таймер
    menu_frame.pack_forget() #скрытие фрейма с меню
    bmb_frame.pack(side=BOTTOM, anchor=E) #отображение кнопки 'Назад'
    timer_frame.pack(anchor='center', expand=True) #отображение фрейма ТАЙМЕР
    hour.set('0') #присваивание времени ТАЙМЕРА нулевых значений
    minute.set('10')
    second.set('0')

#____________________________________________________________________________________________________ОТОБРАЖЕНИЕ_СЕКУНДОМЕРА______________________________________________________________________________

def secmer(): #секундомер
	menu_frame.pack_forget() #скрытие фрейма с меню
	bmb_frame.pack(side=BOTTOM, anchor=E) #отображение кнопки 'Назад'
	sm_frame.pack(anchor='center', expand=True) #отображение фрейма СЕКУНДОМЕРА
	btn_sm_frame.place(x=95, y=350) #отображение фрейма КНОПОК СЕКУНДОМЕРА

#_________________________________________________________________________________________________________КНОПКИ_МЕНЮ_________________________________________________________________________________________________________________________

btn_1 = ttk.Button(menu_frame, text='Текущее время', takefocus=False, style="TButton", padding=5, command=world_time).pack(pady=25) #просто кнопки, отображаемые в меню
btn_2 = ttk.Button(menu_frame, text='Секундомер', takefocus=False, style="TButton", padding=5, command=secmer).pack(pady=25) #не, ну а что мне тут ещё писать после часа добавления комментариев?)
btn_3 = ttk.Button(menu_frame, text='Таймер', takefocus=False, style="TButton", padding=5, command=timer).pack(pady=25) #я же не мог оставить код таким постным, надо было добавить пасхалку (а внизу мой смайлик))

wer.mainloop() #обновление окна