import telebot
import emoji
import requests, datetime


bot = telebot.TeleBot("1652337761:AAGJ0InzXjooH3Sm7yFnIMW5-6tOSlfxQXY", parse_mode=None)
#there we initialize dictionaries for each print
pressure_for_print = {}
humidity_for_print = {}
wind_for_print = {}
geoactivity_for_print = {}
wind_max_for_print = {}
humidity_for_print_2 = {}
pressure_for_print_2 = {}
wind_for_print_2 = {}
geoactivity_for_print_2 = {}
wind_max_for_print_2 = {}
temperature_for_print ={}
temperature_for_print_2={}
   
resp = None

def time(data): #in this function we get necessary date
    try:
        data_for_pr = datetime.datetime.today()
        delta_for_lol = datetime.timedelta(days=1)
        data_for_pr_2 = data_for_pr + (delta_for_lol * (data - 1))
        date_today_for_pr = str(data_for_pr_2.day) + "-" + str(data_for_pr_2.month) + "-" + str(data_for_pr_2.year)
        return date_today_for_pr
    except:
        pass



def thread_function(city, daysp):
    # function which make requests to Gismeteo api
    try:
        global resp

        # we give for each variable it's unit of measurement
        temperature, wind_speed_min, pressure, humidity, geoactivity = ['C'], ['m/s'], ['hg_mm'], ['%'], ['points']


        header = {'X-Gismeteo-Token' : '60abcc10912897.62122015'}
                
        
        #language
        lang = 'en'

        #get city's ID
        url = f"https://api.gismeteo.net/v2/search/cities/?{lang}=en&query={city}"
        resp = requests.request("GET", url, headers=header)

        if len(resp.json()['response']['items'])==0:
            return 1

        print(resp.json()['response']['items'][0]['name'])
        # request process
        url = f"https://api.gismeteo.net/v2/weather/forecast/{resp.json()['response']['items'][0]['id']}/?days={daysp}"
        response = requests.request("GET", url, headers=header)

        ##distribute information to appropriate dictionaries
        for i in range(0, 8*daysp, 8):
            temp, wind, pres, hum, geo = [], [], [], [], []
            for j in range(8):

                pres.append(response.json()['response'][i+j]['pressure']['mm_hg_atm'])
                temp.append(response.json()['response'][i+j]['temperature']['air']['C'])
                wind.append(response.json()['response'][i+j]['wind']['speed']['m_s'])
                hum.append(response.json()['response'][i+j]['humidity']['percent'])
                geo.append(response.json()['response'][i+j]['gm'])
            

            temperature.append(temp)
            pressure.append(pres)
            wind_speed_min.append(wind)
            humidity.append(hum)
            geoactivity.append(geo)

        # Here we check value of each variable and give corresponding print
        for z_1 in range(1, daysp):
            count_20 = 0
            for z_2 in humidity[z_1]:
                count_20 += 1
                if count_20 == 6:
                    if z_2 == '-':
                        humidity_for_print[str(time(z_1))] = f"⚪️There is no information about humidity for today"
                    else:                  
                        if int(z_2) > 75:
                            humidity_for_print[str(time(z_1))] =emoji.emojize("HUMIDITY:cloud_with_rain:")+f"\n🟡Humidity on this day at 15:00 can reach {z_2}%, which is an excess of the norm"
                        elif int(z_2) < 30:
                            humidity_for_print[str(time(z_1))] =emoji.emojize("HUMIDITY:cloud_with_rain:")+f"\n🟡Humidity on this day at 15:00 can reach {z_2}%, which is less than normal"
                        else:
                            humidity_for_print[str(time(z_1))] =emoji.emojize("HUMIDITY:cloud_with_rain:")+f"\n🟢Humidity on this day at 15:00 can reach {z_2}%, which is normal"
                elif count_20 == 8:
                    if z_2 == '-':
                        humidity_for_print_2[str(time(z_1))] = f"⚪️There is no information about humidity for today"
                    else:                  
                        if int(z_2) > 75:
                            humidity_for_print_2[str(time(z_1))] = f"🟡Humidity on this day at 21:00 can reach {z_2}%, which is an excess of the norm"
                        elif int(z_2) < 30:
                            humidity_for_print_2[str(time(z_1))] = f"🟡Humidity on this day at 21:00 can reach {z_2}%, which is less than normal"
                        else:
                            humidity_for_print_2[str(time(z_1))] = f"🟢Humidity on this day at 21:00 can reach {z_2}%, which is normal"


        for p_1 in range(1, daysp):
            count_21 = 0
            for p_2 in pressure[p_1]:
                count_21 += 1
                if count_21 == 6:
                    if p_2 == '-':
                        pressure_for_print[str(time(p_1))] = f"⚪️There is no information about pressure for today"
                    else:               
                        if int(p_2) > 765:
                            pressure_for_print[str(time(p_1))] =emoji.emojize("PRESSURE:thermometer:") +f"\n🟡The pressure value on this day at 15:00 is greater than the norm (760) and is: {p_2} hg_mm "
                        elif int(p_2) < 755:
                            pressure_for_print[str(time(p_1))] =emoji.emojize("PRESSURE:thermometer:") + f"\n🟡The pressure value on this day at 15:00 is lower than the norm (760) and is: {p_2} hg_mm "
                        else:
                            pressure_for_print[str(time(p_1))] =emoji.emojize("PRESSURE:thermometer:") + f"\n🟢The pressure value on this day at 15:00 is normal and is: {p_2} hg_mm "

                elif count_21 == 8:
                    if p_2 == '-':
                        pressure_for_print_2[str(time(p_1))] = f"⚪️There is no information about pressure for today"
                    else:                
                        if int(p_2) > 765:
                            pressure_for_print_2[str(time(p_1))] = f"🟡The pressure value on this day at 21:00 is greater than the norm (760) and is: {p_2} hg_mm "
                        elif int(p_2) < 755:
                            pressure_for_print_2[str(time(p_1))] = f"🟡The pressure value on this day at 21:00  is lower than the norm (760) and is: {p_2} hg_mm "
                        else:
                            pressure_for_print_2[str(time(p_1))] = f"🟢The pressure value on this day at 21:00 is normal and is: {p_2} hg_mm "


        for w_1 in range(1, daysp):
            count_22 = 0
            for w_2 in wind_speed_min[w_1]:
                count_22 += 1
                if count_22 == 6:
                    if w_2 == '-':
                        wind_for_print[str(time(w_1))] = f"🟢There is no wind today"
                    else:
                        if int(w_2) <= 3:
                            wind_for_print[str(time(w_1))] =emoji.emojize("WIND:tornado:")+f"\n🟢Wind on this day at 15:00 on average is {w_2}m/s,there is almost no wind"
                        elif int(w_2) > 3 and int(w_2) <= 8:
                            wind_for_print[str(time(w_1))] =emoji.emojize("WIND:tornado:")+ f"\n🟢Wind on this day at 15:00 on average is {w_2}m/s,there is a little breeze"
                        elif int(w_2) > 8 and int(w_2) <= 13:
                            wind_for_print[str(time(w_1))] =emoji.emojize("WIND:tornado:")+ f"\n🟡Wind on this day at 15:00 on average is {w_2}m/s,it is windy "
                        elif int(w_2) > 13 and int(w_2) <= 18:
                            wind_for_print[str(time(w_1))] =emoji.emojize("WIND:tornado:")+ f"\n🟠Wind on this day at 15:00 on average is {w_2}m/s,very strong wind,better stay at home"
                        elif int(w_2) > 18:
                            wind_for_print[str(time(w_1))] =emoji.emojize("WIND:tornado:")+ f"\n🔴Wind on this day at 15:00 on average is {w_2}m/s,don't go outside,it is dangerous"

                elif count_22 == 8:
                    if w_2 == '-':
                        wind_for_print[str(time(w_1))] = f"🟢There is no wind today"
                    else:
                        if int(w_2) <= 3:
                            wind_for_print_2[str(time(w_1))] = f"🟢Wind on this day at 21:00 on average is {w_2}m/s,there is almost no wind"
                        elif int(w_2) > 3 and int(w_2) <= 8:
                            wind_for_print_2[str(time(w_1))] = f"🟢Wind on this day at 21:00 on average is {w_2}m/s,there is a little breeze"
                        elif int(w_2) > 8 and int(w_2) <= 13:
                            wind_for_print_2[str(time(w_1))] = f"🟡Wind on this day at 21:00 on average is {w_2}m/s,it is windy "
                        elif int(w_2) > 13 and int(w_2) <= 18:
                            wind_for_print_2[str(time(w_1))] = f"🟠Wind on this day at 21:00 on average is {w_2}m/s,very strong wind,better stay at home"
                        elif int(w_2) > 18:
                            wind_for_print_2[str(time(w_1))] = f"🔴Wind on this day at 21:00 on average is {w_2}m/s,don't go outside,it is dangerous"


        for g_1 in range(1, daysp):
            count_23 = 0
            for g_2 in geoactivity[g_1]:
                count_23 += 1
                if count_23 == 6:
                    if g_2 == '-':
                        geoactivity_for_print[str(time(g_1))] = f"🟢⚪️There is no information about geoactivity for today"
                    else:
                        if int(g_2) > 0 and int(g_2) <= 4:
                            geoactivity_for_print[str(time(g_1))] =emoji.emojize("GEOACTIVITY:cyclone:")+f"\n🟢The geoactivity value on this day at 15:00 can reach {g_2} points,there are almost no Magnetic storms "
                        elif int(g_2) == 5:
                            geoactivity_for_print[str(time(g_1))] =emoji.emojize("GEOACTIVITY:cyclone:")+ f"\n🟡The geoactivity value on this day at 15:00 can reach {g_2} points,it is a weak storm"
                        elif int(g_2) == 6:
                            geoactivity_for_print[str(time(g_1))] =emoji.emojize("GEOACTIVITY:cyclone:")+ f"\n🟠The geoactivity value on this day at 15:00 can reach {g_2} points,it is moderate storm,but better stay home"
                        elif int(g_2) >= 7:
                            geoactivity_for_print[str(time(g_1))] =emoji.emojize("GEOACTIVITY:cyclone:")+ f"\n🔴The geoactivity value on this day at 15:00 can reach {g_2} points,it is strong storm,stay home!"

                elif count_23 == 8:
                    if g_2 == '-':
                        geoactivity_for_print_2[str(time(g_1))] = f"⚪️There is no information about geoactivity for today"
                    else:
                        if int(g_2) > 0 and int(g_2) <= 4:
                            geoactivity_for_print_2[str(time(g_1))] = f"🟢The geoactivity value on this day at 21:00 can reach {g_2} points,there are almost no Magnetic storms"
                        elif int(g_2) == 5:
                            geoactivity_for_print_2[str(time(g_1))] = f"🟡The geoactivity value on this day at 21:00 can reach {g_2} points,it is a weak storm"
                        elif int(g_2) == 6:
                            geoactivity_for_print_2[str(time(g_1))] = f"🟠The geoactivity value on this day at 21:00 can reach {g_2} points,it is moderate storm,but better stay home"
                        elif int(g_2) >= 7:
                            geoactivity_for_print_2[str(time(g_1))] = f"🔴The geoactivity value on this day at 21:00 can reach {g_2} points,it is strong storm,stay home"


        for t_1 in range(1, daysp):
            count_24 = 0
            for t_2 in temperature[t_1]:
                count_24 += 1
                if count_24 == 6:
                    if t_2 == '-':
                        temperature_for_print[str(time(t_1))] = f"⚪️There is no information about temperature for today"
                    else:                  
                        if int(t_2) >29 :
                            temperature_for_print[str(time(t_1))] =emoji.emojize("TEMPERATURE:fire:")+f"\n🔴Temperature on this day at 15:00 can reach {t_2}, Dangerously hot day!"
                        elif int(t_2) >24 and int(t_2) <=29 :
                            temperature_for_print[str(time(t_1))] =emoji.emojize("TEMPERATURE:fire:")+ f"\n🟠Temperature on this day at 15:00 can reach {t_2}, Pretty hot day"
                        elif int(t_2) >18 and int(t_2) <=24 :
                            temperature_for_print[str(time(t_1))] =emoji.emojize("TEMPERATURE:fire:")+ f"\n🟡Temperature on this day at 15:00 can reach {t_2}, Warm day"
                        elif int(t_2) >14 and int(t_2) <=18 :
                            temperature_for_print[str(time(t_1))] =emoji.emojize("TEMPERATURE:fire:")+ f"\n🟢Temperature on this day at 15:00 can reach {t_2},Nice average temperature day"
                        elif int(t_2) <=14 and  int(t_2)>5 :
                            temperature_for_print[str(time(t_1))] =emoji.emojize("TEMPERATURE:fire:")+ f"\n🔵Temperature on this day at 15:00 can reach {t_2},Quite cold day"
                        elif int(t_2) <=5:
                            temperature_for_print[str(time(t_1))] =emoji.emojize("TEMPERATURE:fire:")+ f"\n🔵Temperature on this day at 15:00 can reach {t_2},Really cold day!"
                elif count_24 == 8:
                    if t_2 == '-':
                        temperature_for_print_2[str(time(t_1))] = f"⚪️There is no information about temperature for today"
                    else:                  
                        if int(t_2) > 29:
                            temperature_for_print_2[str(time(t_1))] = f"🔴Temperature on this day at 21:00 can reach {t_2}, Dangerously hot day!"
                        elif int(t_2) >24 and int(t_2) <=29 :
                            temperature_for_print_2[str(time(t_1))] = f"🟠Temperature on this day at 21:00 can reach {t_2}, Pretty hot day"
                        elif int(t_2) >18 and int(t_2) <=24 :
                            temperature_for_print_2[str(time(t_1))] = f"🟡Temperature on this day at 21:00 can reach {t_2}, Warm day"
                        elif int(t_2) >14 and int(t_2) <=18 :
                            temperature_for_print_2[str(time(t_1))] = f"🔵Temperature on this day at 21:00 can reach {t_2},Nice average temperature day"
                        elif int(t_2) <=14 and int(t_2)>5 :
                            temperature_for_print_2[str(time(t_1))] = f"🔵Temperature on this day at 21:00 can reach {t_2},Quite cold day"
                        elif int(t_2) <=5:
                            temperature_for_print[str(time(t_1))] = f"🔵Temperature on this day at 21:00 can reach {t_2},Really cold day!"

        return (temperature_for_print,temperature_for_print_2,humidity_for_print, humidity_for_print_2, pressure_for_print, pressure_for_print_2, wind_for_print,
                wind_for_print_2, geoactivity_for_print, geoactivity_for_print_2)
                
    except:
        pass


@bot.message_handler(commands=['help']) #/help command shows what weather information means
def the_information(message):
    try:
        bot.send_message(message.chat.id, "🔹Increase in air humidity:\nIt worsens the health of asthmatics, heart patients and people with joint diseases\
                                       \n\n🔹Lowering atmospheric pressure:\nAsthmatics and heart patients have shortness of breath, weakness, feeling of shortness of breath. A sharp decrease in blood pressure in hypotensive patients.\
                                       \n\n🔹Increase in atmospheric pressure:\nHypertensive patients react painfully, the risk of heart attack and stroke increases\
                                       \n\n🔹Magnetic storm:\nAll weather-sensitive people suffer. Blood pressure surges, headaches, interruptions in the work of the heart, irritability and feelings of anxiety \n \n🔹Frost: \nDifficulty breathing in asthmatics. In hypertensive patients, blood pressure rises, and the heart may ache. ")
    except:
        pass


@bot.message_handler(commands=['start']) #/start command is used to show user what he should write
def start(message):
    bot.send_message(message.chat.id, 'Enter the city and number of days(1-10) for which you want to receive the forecast  \n"City" + "days"(For example Baku 7)')



ids = {}

@bot.message_handler(content_types=['text'])
def main(message):
    print(message.text)
    global ids
    try:
        #Here we have made Anti-spam defender, if user writes more than 40 times ,he will get temporary 1 hour ban

        if message.from_user.id not in ids:
            ids[message.from_user.id] = [1, datetime.datetime.today()]
        elif ids[message.from_user.id][0] >= 40:  # message limit (messages)
            if (datetime.datetime.now() - ids[message.from_user.id][1]).total_seconds() >= 3600:  # time limit (seconds)
                ids[message.from_user.id] = [1, datetime.datetime.today()]
            else:
                bot.send_message(message.chat.id, text="You have been temporary banned for 1 hour because of spam!")
                return
        else:
            ids[message.from_user.id][0] += 1
    
        def listing(dictionary):  # This function creates a list of variables of a dictionary
            try:
                f = []  #f variable is a list where all values are stored
                v = list(dictionary.values())

                for x in range(len(v)):
                    f.append('{}'.format(v[x]))

                return f
            except: pass


        message_lowered = message.text.lower()  # lowering each letter

        mes = message_lowered.split()  # getting rid of spaces anf creating a list of words

        print(message.from_user.first_name,message_lowered) #This line is for see in terminal messages and sender's name

        if len(mes)>1 and mes[-1].isdigit() == True:

            if int(mes[-1])>10 or int(mes[-1])<1: #if there are more than 10 and less than 1 the bot will ask user to enter days in interval 1-10
                bot.send_message(message.chat.id, 'Please enter 1-10 days')
                return True

            bot.send_message(message.chat.id, 'Please wait...')
            bot.send_message(message.chat.id, 'Collecting information...')
            bot.send_message(message.chat.id, 'Wind,humidity,pressure,geoactivity...')

            days=mes.pop(-1) #days entered by user

            weather = thread_function(' '.join(mes), int(days) + 1)

            if weather != 1: #thread_function returns 1 if the city is not found or user wrote it in wrong way
                h = []  # a new list of information about weather for each day

                for f in range(len(weather)):
                    h.append(listing(weather[f]))

                for lol in range(int(days)): #send inormation for each day
                        bot.send_message(message.chat.id,
                                        '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(list(weather[0].keys())[lol],
                                                                                            h[0][lol], h[1][lol],
                                                                                            h[2][lol], h[3][lol],
                                                                                            h[4][lol], h[5][lol],
                                                                                            h[6][lol], h[7][lol],
                                                                                            h[8][lol], h[9][lol]))

                bot.send_message(message.chat.id,emoji.emojize("Supported by Gismeteo:collision:"))
                bot.send_message(message.chat.id,"Write /help in order to get information for asthmatics, hypertensive patients and for meteosensitive people in general")
                # clear dictionaries
                pressure_for_print.clear()
                humidity_for_print.clear()
                wind_for_print.clear()
                geoactivity_for_print.clear()
                wind_max_for_print.clear()
                humidity_for_print_2.clear()
                pressure_for_print_2.clear()
                wind_for_print_2.clear()
                geoactivity_for_print_2.clear()
                wind_max_for_print_2.clear()
                temperature_for_print.clear()    
                temperature_for_print_2.clear()  

            else:
                bot.send_message(message.chat.id, "I'm sorry but there's no such city or you wrote it in a wrong way")

        else:
            bot.send_message(message.chat.id, 'Please enter the city and days in form like: \n"City" + "days"(For example Baku 7)')

    except:pass
     

if __name__ == '__main__':
    bot.polling(none_stop=True) #bot will work none stop