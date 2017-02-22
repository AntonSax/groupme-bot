from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
import json
import urllib.request
import groupy
import random
import datetime
import time
import tweepy

@csrf_exempt
def groupme(request):
    print(request.body.decode("utf-8"))
    groupme_response = json.loads(request.body.decode("utf-8"))
    bots = groupy.Bot.list()
    bot = bots.filter(group_id=str(groupme_response['group_id'])).first
    test_bot = bots.filter(group_id='28448048').first



    # All Purpose Commands

    def give_cookie(cur_bot, post_author, user):
        cur_bot.post(post_author + ' gives a cookie to ' + user)

    def yeezy(cur_bot):
        auth = tweepy.OAuthHandler(7LKNh9j6v5kIMc6QkI1p3FYTC, V79udZARDpnSUjY8lr9OiuK5vkUFYW8n0cbh7apU8jsEInepW4)

        try:
            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError:
            cur_bot.post('Error! Failed to get request token. Please yell at Maneesh promptly.')

        verifier = raw_input('Verifier:')

        try:
            auth.get_access_token(verifier)
        except tweepy.TweepError:
            cur_bot.post('Error! Failed to get access token. Please yell at Maneesh promptly.')

        api = tweepy.API(auth)

        stuff = api.user_timeline(screen_name = 'kaynewest', count = 100, include_rts = True)

        cur_bot.post(status.user)

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
        cur_bot.post(random.choice(flips))


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

    def weather(cur_bot, zip_code='65401'):
        zip_code = str(zip_code)
        open_weather_map_api_key = "<Insert API Key>"
        url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zip_code + ",us&appid=" + open_weather_map_api_key
        data = urllib.request.urlopen(url).read().decode('utf8')
        output = json.loads(data)
        cur_temp = str(int(output['main']['temp'] * (9 / 5) - 459.67))
        update_time = str(datetime.datetime.utcfromtimestamp(output['dt']).strftime('%x %I:%M:%S %p UTC'))
        name =  str(output['name'])
        cur_bot.post("Hey " + post_author + "! \n The current temperature in " + name + " is " + cur_temp + "°F.\n Last updated: " + update_time + "\n")

    def joke(cur_bot):

    # get time and date of next event
    def next_event(cur_bot):

    def 8ball(cur_bot):

    def dice(cur_bot):

    # will this take as input multiple users?
    def alarm(cur_bot, user):

    def popular_message(cur_bot):

    def poll(cur_bot):

    # Nerdy/Dorky Commands

    def xkcd(cur_bot):

    # Holiday Commands

    def days_to_xmas(cur_bot):

        #S&T Commands

    def daze_till_pats(cur_bot):
        today = datetime.date.today()
        pats = datetime.date(2017, 03, 17)
        difference = today - pats
        cur_bot.post(difference.days + "Daze until the BEST EVER ST. PATS!")


    # DSP Commands

    def wingman_me(cur_bot, post_author):

    def profile(cur_bot, user):

    random.seed(groupme_response['id']+str(time.time()))

    if not cache.get_or_set('sleep' + groupme_response['group_id'], False, None):

        try:
            message = groupme_response['text'].lower().strip()
            cased_message = groupme_response['text'].strip()
            name = groupme_response['name']

            elif message == '##help':
                bot.post('Here is the list of commands: ' +
                        '\n##sleep -- Turns off the bot for the night.' +
                        '\n##cookie <person> -- Give a cookie to somebody.' +
                        '\n##lennyface -- Post a random lenny face.' +
                        '\n##fliptable -- You flip a table.' +
                        '\n##ping -- Pong!' +
                        #'\n##random  -- Does a random thing.' +
                        #'\n##d<number> -- Rolls a d<number> ex: ##d20' +
                        #'\n##roll <num1>d<num2> -- Rolls <num1> d<num2> ex: ##roll 4d20')
                bot.post('Continued list of commands: ' +
                        '\n##weather <zip code> -- Gets weather for the given zip code' +
                        '\n##daze till pats -- Posts how many daze until St. Pats.'
                        #'\n##8ball -- Ask the magic 8ball a question' +
                        #'\n##xkcd <newest/random/#> -- gives the newest, random or specific xkcd comic')


            elif message == '##sleep' or '##Sleep':
                if not 7 < datetime.datetime.now().hour - 6 < 22:
                    bot.post('Going in to night mode.')
                    print('Going into night mode')
                    cache.set('night_mode' + groupme_response['group_id'], True, None)
                else:
                    bot.post('I don\'t fall asleep before 10.')


            elif message[:8] == '##cookie' or '##Cookie:
                give_cookie(cur_bot=bot, user=cased_message[9:], post_author=name)


            elif message == '##lennyface' or '##Lennyface':
                lenny_face(cur_bot=bot)


            elif message == '##fliptable' or message == '##tableflip' or '##Fliptable' or '##Tableflip:
                table_flip(cur_bot=bot)


            elif message == '##ping' or '##Ping':
                ping(cur_bot=bot)


            elif message == '##weather' or '##Weather':
                if message[10:15].isnumeric():
                    get_weather(zip_code=message[10:15], cur_bot=bot, post_author=name)
                else:
                    get_weather(zip_code='65401', cur_bot=bot, post_author=name)

            elif message == '##daze till pats' or '##daze till Pats' or '##Daze till pats' or '##Daze till Pats':
                daze_till_pats






    else:
        print("Bot is in nightmode")
        if 7 < datetime.datetime.now().hour - 6 < 22:
            print("Bot is leaving nightmode")
            cache.set('night_mode' + groupme_response['group_id'], False, None)

    return HttpResponse(bot.name)
