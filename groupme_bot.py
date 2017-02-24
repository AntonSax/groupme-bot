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

            # Austin's Code
    def weather(cur_bot, post_author, zip_code='65401'):
        zip_code = str(zip_code)
        open_weather_map_api_key = '0f5e7a1e7682ce843b443549718b5f95'
        url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zip_code + ",us&appid=" + open_weather_map_api_key
        data = urllib.request.urlopen(url).read().decode('utf8')
        output = json.loads(data)
        cur_temp = str(int(output['main']['temp'] * (9 / 5) - 459.67))
        update_time = str(datetime.datetime.utcfromtimestamp(output['dt']).strftime('%x %I:%M:%S %p UTC'))
        name =  str(output['name'])
        cur_bot.post("Hey " + post_author + "! \n The current temperature in " + name + " is " + cur_temp + "°F.\n Last updated: " + update_time + "\n")



    '''
        #Examples from https://github.com/csparpa/pyowm/blob/master/pyowm/docs/usage-examples.md
    def weather(cur_bot, location='Rolla'):
            # Set API Key
        API_key = '0f5e7a1e7682ce843b443549718b5f95'
        owm = OWM(API_key)

            # Make sure the location is a string
        #location = str(location)
            # Returns an "observation" of weather data (NOT A FORECAST)
        obs = owm.weather_at_place(location)
            # Gets actual weather data
        w = obs.get_weather()
        temperature_f = w.get_temperature('fahrenheit')
        conditions = w.get_detailed_status()
            # Object for getting location
        l = obs.get_location()
        location_name = l.get_name()
        print("User input location: " + location)
        print("The object location: " + location_name)

        cur_bot.post("It is now " + temperature_f + "°F with " + conditions + " in " + location_name + ".")
    '''



    #def joke(cur_bot):

    # get time and date of next event
    #def next_event(cur_bot):

    #def 8ball(cur_bot):

    #def dice(cur_bot):

    # will this take as input multiple users?
    #def alarm(cur_bot, user):

    #def popular_message(cur_bot):

    #def poll(cur_bot):

    # Nerdy/Dorky Commands

    #def xkcd(cur_bot):

    # Holiday Commands

    #def days_to_xmas(cur_bot):

        #S&T Commands

    def daze(cur_bot):
        today = datetime.date.today()
        pats = datetime.date(2017, 3, 17)
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
                        '\n##sleep -- Turns off the bot for the night.' +
                        '\n##cookie <person> -- Give a cookie to somebody.' +
                        '\n##lennyface -- Post a random lenny face.' +
                        '\n##fliptable -- You flip a table.' +
                        '\n##ping -- Pong!'
                        '\n##weather -- Gets the weather' +
                        '\n##daze -- Posts how many daze until St. Pats.'
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


            elif message == '##lennyface':
                lenny_face(cur_bot=bot)


            elif message == '##fliptable' or message == '##tableflip':
                table_flip(cur_bot=bot)


            elif message == '##ping':
                ping(cur_bot=bot)


            elif message[:9] == '##weather':
                if message[10:15].isnumeric():
                    weather(zip_code=message[10:15], cur_bot=bot, post_author=name)
                elif message[10:].isalpha():
                    weather(location=message[10:], cur_bot=bot, post_author=name)
                else:
                    #weather(cur_bot=bot, location='Rolla') # for my own weather function
                    weather(zip_code='65401', cur_bot=bot, post_author=name)  # for Austin's weather function

            elif message == '##daze' or message == '##daze till pats' or message == '##days till pats' or message == '##daze till pat\'s' or message == '##daze til pats':
                daze(cur_bot=bot)

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
