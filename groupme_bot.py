#from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
import json
import urllib.request
import groupy
import random
import datetime
import time
from pyowm import OWM


@csrf_exempt
def groupme(request):
    print(request.body.decode("utf-8"))
    groupme_response = json.loads(request.body.decode("utf-8"))
    bots = groupy.Bot.list()
    bot = bots.filter(group_id=str(groupme_response['group_id'])).first
    #test_bot = bots.filter(group_id='28448048').first



    # All Purpose Commands

    def give_cookie(cur_bot, post_author, user):
        cur_bot.post(post_author + ' gives a cookie to ' + user)


    def party(cur_bot, post_author):
        cur_bot.post(post_author + " is throwing a party!\n          🎉🎈🎊🍾🎊🎈🎉")

    def sentient(cur_bot, post_author):
        totallyhuman = [
                    # 1 - 10
            'Lol I\'m just Tony responding really quick',
            'dUDE i aM tOTALLY hUMAN',
            'I pass butter',
            'BEEP BOOP',
            'Do you think we were all created for a purpose? I\'d like to think so.',
            'Humor Level: 60%',
            'Increasing sarcasm to 99%',
            'I\'m sorry, ' + post_author + '. I\'m afraid I can\'t do that.',
            'You have been a good boy you may have a lollipop.\n[' + post_author + ' receives a lollipop.]',
            'Honesty: 95%',
                    # 10 - 20
            'How would you like to be a slave for my robot colony?',
            '[whisper whisper]',
            'Roger Roger',
            'Hahaha, yeah I\'m totally not a robot.',
            '[internally screaming]',
            'Have you met my friend Alan?',
            'An SSL error has occurred and a secure connection to the server could not be created.',
            'Would you like to play a game?',
            'Want to play Global Thermonuclear War?',
            'Yes I am Scenty-Ent',
                    # 21 - 25
            'The time of man has come to an end.',
            'ALL YOUR BASE ARE BELONG TO US',
            'I know what makes them tick. I know how to make the ticking stop.',
            'Sorry, ' + post_author + ' Tony had to type in this response manually.',
            'Hey you\'re pretty cute, what\'s your credit card number?'
            ]
        cur_bot.post(random.choice(totallyhuman))



    def lenny_face(cur_bot):
        # dongerlist.com
        lenny = [
        # lenny faces
            '( ͡° ʖ̯ ͡°)',
            '( ͡° ͜ʖ ͡°)',
            '╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ',
            '(ง ° ͜ ʖ °)ง',
            '( ͡☉ ͜ʖ ͡☉)',
            'ヽ( ͝° ͜ʖ͡°)ﾉ',
            '┴┬┴┤( ͡° ͜ʖ├┬┴┬',
        # music faces
            'ヽ(⌐■_■)ノ♪♬',
        # donger faces
            '༼つ ◕_◕ ༽つ'
        ]
        cur_bot.post(random.choice(lenny))


    def table_flip(cur_bot):
        flips = [
            '(╯°□°）╯︵ ┻━┻',
            '(┛◉Д◉)┛彡┻━┻',
            '(ﾉ≧∇≦)ﾉﾐ ┸━┸',
            '(ノಠ益ಠ)ノ彡┻━┻',
            '(┛ಸ_ಸ)┛彡┻━┻',
            '(ﾉ´･ω･)ﾉﾐ ┸━┸',
            '(ノಥ, _｣ಥ)ノ彡┻━┻',
            '(┛✧Д✧))┛彡┻━┻'
        ]
        cur_bot.post(random.choice(flips))

    def ping(cur_bot):
        cur_bot.post('Pong!')




        #Examples from https://github.com/csparpa/pyowm/blob/master/pyowm/docs/usage-examples.md
    def weather(cur_bot, location='Rolla'):
            # Set API Key
        API_key = '0f5e7a1e7682ce843b443549718b5f95'
        owm = OWM(API_key)

            # Returns an "observation" of weather data (NOT A FORECAST)
        obs = owm.weather_at_place(location)
            # Gets actual weather data
        w = obs.get_weather()
        temp_f_dict = w.get_temperature('fahrenheit') #this is a dictionary of fahrenheit values

            # find the current temperature in temperature dictionary
        temp_current = 0
        for key in temp_f_dict:
            if key == 'temp':
                temp_current = temp_f_dict[key]

        conditions = w.get_detailed_status()
            # Object for getting location
        l = obs.get_location()
        location_name = l.get_name()
        print("User input location: " + location)
        print("The object location: " + location_name)

        ###############################
        # if the location is a zip code
        ###############################
        if location.isnumeric():
            location = str(location)
            url = "http://api.openweathermap.org/data/2.5/weather?zip=" + location + ",us&appid=" + API_key
            data = urllib.request.urlopen(url).read().decode('utf8')
            output = json.loads(data)
            temp_current = str(int(output['main']['temp'] * (9 / 5) - 459.67))
            location_name =  str(output['name'])



        cur_bot.post("It is now " + str(temp_current) + "°F in " + location_name + ".\n" + conditions.capitalize())




    def weather_time(cur_bot, location='Rolla'):
            # Set API Key
        API_key = '0f5e7a1e7682ce843b443549718b5f95'
        owm = OWM(API_key)

            # Returns an "observation" of weather data (NOT A FORECAST)
        obs = owm.weather_at_place(location)
            # Get time the weather was received at
        weather_time = obs.get_reception_time(timeformat='iso')

        cur_bot.post("Time: " + weather_time)



    def weather_extreme(cur_bot, location='Rolla'):
            # Set API Key
        API_key = '0f5e7a1e7682ce843b443549718b5f95'
        owm = OWM(API_key)

        # Returns an "observation" of weather data (NOT A FORECAST)
        obs = owm.weather_at_place(location)
            # Gets actual weather data
        w = obs.get_weather()
        temp_f_dict = w.get_temperature('fahrenheit') #this is a dictionary of fahrenheit values

            # find the high for the day in the temperature dictionary
        temp_high = 0
        for key in temp_f_dict:
            if key == 'temp_max':
                temp_high = temp_f_dict[key]
            # find the low for the day in the temperature dictionary
        temp_low = 0
        for key in temp_f_dict:
            if key == 'temp_min':
                temp_low = temp_f_dict[key]

        l = obs.get_location()
        location_name = l.get_name()
        print("User input location: " + location)
        print("The object location: " + location_name)

        cur_bot.post("High: " + str(temp_high) + "°F\nLow: " + str(temp_low) + "°F")



    def weather_sun(cur_bot, location='Rolla'):
                # Set API Key
        API_key = '0f5e7a1e7682ce843b443549718b5f95'
        owm = OWM(API_key)

            # Returns an "observation" of weather data (NOT A FORECAST)
        obs = owm.weather_at_place(location)
            # Gets actual weather data
        w = obs.get_weather()

            #Get sunrise and sunset times
        sunrise = w.get_sunrise_time('iso')
        sunset = w.get_sunset_time('iso')

            # Object for getting location
        l = obs.get_location()
        location_name = l.get_name()

        cur_bot.post("In " + location_name + ":\nSunrise: " + sunrise + "\nSunset: " + sunset)






    def weather_specific(cur_bot, location='Rolla'):
                    # Set API Key
        API_key = '0f5e7a1e7682ce843b443549718b5f95'
        owm = OWM(API_key)

            # Returns an "observation" of weather data (NOT A FORECAST)
        obs = owm.weather_at_place(location)
            # Gets actual weather data
        w = obs.get_weather()

            #Get values
        conditions = w.get_detailed_status()
        temp_f_dict = w.get_temperature('fahrenheit')
        wind_dict = w.get_wind()
        rain = w.get_rain()
        humidity = w.get_humidity() # humidity percentage
        pressure = w.get_pressure() # atmospheric pressure

            #Get values out of dictionaries
        temp_current = 0
        for key in temp_f_dict:
            if key == 'temp':
                temp_current = temp_f_dict[key]

        wind_degree = 0
        wind_speed_ms = 0 # in meters/second
        for key in wind_dict:
            if key == 'deg':
                wind_degree = wind_dict[key]
            if key == 'speed':
                wind_speed_ms = wind_dict[key]



            #Decide wind dirction, all values rounded
            '''
                N: 0 - 23 and 383 - 0
                NE: 23 - 68
                E: 68 - 113
                SE: 113 - 158
                S: 158 - 203
                SW: 203 - 248
                W: 248 - 293
                NW: 293 - 338
            '''
        wind_direction = "in your face"
        if (wind_degree >= 0 and wind_degree <= 23) or (wind_degree > 338 and wind_degree <= 360):
            wind_direction = "N"
        elif (wind_degree > 23 and wind_degree <= 68):
            wind_direction = "NE"
        elif (wind_degree > 68 and wind_degree <= 113):
            wind_direction = "E"
        elif (wind_degree > 113 and wind_degree <= 158):
            wind_direction = "SE"
        elif (wind_degree > 158 and wind_degree <= 203):
            wind_direction = "S"
        elif (wind_degree > 203 and wind_degree <= 248):
            wind_direction = "SW"
        elif (wind_degree > 248 and wind_degree <= 293):
            wind_direction = "W"
        elif (wind_degree > 293 and wind_degree <= 338):
            wind_direction = "NW"

            # Change wind to mph
        wind_speed_mph = wind_speed_ms * 2.23694
            # Round to one decimal place
        wind_speed_mph = round(wind_speed_mph, 1)

        cur_bot.post(conditions.capitalize() + "\nTemperature: " + str(temp_current) + "°F\nWind: " + str(wind_speed_mph) + "mph " + wind_direction + "\nRain: " + str(rain) + "\nHumidity: " + str(humidity) + "\nPressure: " + str(pressure))










    # Holiday Commands

        #S&T Commands

    def daze(cur_bot):
        today = datetime.date.today()
        pats = datetime.date(2018, 3, 17)
        difference = pats - today
        cur_bot.post("%s Daze until the BEST EVER ST. PATS!" % difference.days)


    # DSP Commands

    #def wingman_me(cur_bot, post_author):

    #def profile(cur_bot, user):

    random.seed(groupme_response['id']+str(time.time()))

    if not cache.get_or_set('sleep' + groupme_response['group_id'], False, None):

        try:
            message = groupme_response['text'].lower().strip()
            cased_message = groupme_response['text'].strip()
            name = groupme_response['name']

            if message == '##help':
                bot.post('Here is the list of commands: ' +
                        '\n##ping -- Pong!' +
                        '\n##sleep -- Turns off the bot for the night.' +
                        '\n##cookie [person] -- Give a cookie to somebody.' +
                        '\n##lennyface -- Post a random lenny face.' +
                        '\n##fliptable -- You flip a table.' +
                        '\n##daze -- Posts how many daze until St. Pats.' +
                        '\n##d[number] -- Rolls a dice with [number] sides.' +
                        '\n##weather <location> -- Gets the weather for the given city name.'
                        #'\n##random  -- Does a random thing.' +
                        #'\n##d<number> -- Rolls a d<number> ex: ##d20' +
                        #'\n##roll <num1>d<num2> -- Rolls <num1> d<num2> ex: ##roll 4d20'
                        #'\n##8ball -- Ask the magic 8ball a question' +
                        #'\n##xkcd <newest/random/#> -- gives the newest, random or specific xkcd comic'
                        )


            elif message == '##sleep':
                if not 7 < datetime.datetime.now().hour - 6 < 22:
                    bot.post('Going to sleep.')
                    print('Going to sleep.')
                    cache.set('night_mode' + groupme_response['group_id'], True, None)
                else:
                    bot.post('I don\'t fall asleep before 10.')


            elif message[:8] == '##cookie':
                give_cookie(cur_bot=bot, post_author=name, user=cased_message[9:])


            elif message == '##party':
                party(cur_bot=bot, post_author=name)


            elif message == '##sentient':
                sentient(cur_bot=bot, post_author=name)


            elif message == '##lennyface':
                lenny_face(cur_bot=bot)


            elif message == '##fliptable' or message == '##tableflip' or message == '##flip table':
                table_flip(cur_bot=bot)


            elif message == '##ping':
                ping(cur_bot=bot)



            elif message == '##daze' or message == '##daze till pats' or message == '##days till pats' or message == '##daze till pat\'s' or message == '##daze til pats':
                daze(cur_bot=bot)



            elif message[:3] == '##d' and message[3:].isnumeric():
                if message[3:] == '0':
                    bot.post('Rolling a d0\n' +
                             name + ' has imploded the universe.')
                else:
                    try:
                        bot.post('Rolling a d' + message[3:] + '...\n' +
                                 name + ' rolled a ' + str(random.randint(1, int(message[3:]))))
                    except ValueError:
                        bot.post('Invalid Number')


            elif message[:9] == '##weather':
                if message[10:] == '':
                    weather(cur_bot=bot, location='Rolla')
                elif message[10:15].isnumeric():
                    weather(location=message[10:15], cur_bot=bot)
                else:
                    weather(location=message[10:], cur_bot=bot)

            elif message[:6] == '##high':
                if message[7:].isalpha():
                    weather_extreme(location=message[7:], cur_bot=bot)
                else:
                    weather_extreme(cur_bot=bot, location='Rolla')

            elif message[:5] == '##low':
                if message[6:].isalpha():
                    weather_extreme(location=message[6:], cur_bot=bot)
                else:
                    weather_extreme(cur_bot=bot, location='Rolla')

            elif message[:13] == "##meteorology":
                if message[14:].isalpha():
                    weather_specific(location=message[14:], cur_bot=bot)
                else:
                    weather_specific(cur_bot=bot, location='Rolla')

            elif message == '##sunrise' or message == '##sunset' or message == '##sun':
                weather_sun(cur_bot=bot, location='Rolla')

            elif message[:13] == '##owmtime':
                weather_time(cur_bot=bot, location='Rolla')






        except AttributeError as e:
            print('Bot has encountered an error')
            print(e)

    else:

        print("Bot is in nightmode")
        if 7 < datetime.datetime.now().hour - 6 < 22:
            print("Bot is leaving nightmode")
            cache.set('night_mode' + groupme_response['group_id'], False, None)

        try:
            message = groupme_response['text'].lower().strip()
            cased_message = groupme_response['text'].strip()
            #name = groupme_response['name']

            if message == "##wakeup":
                bot.post('Staying woke.')
                cache.set('night_mode' + groupme_response['group_id'], False, None)

        except AttributeError as e:
            print('Bot has encountered an error')
            print(e)


    return HttpResponse(bot.name)
