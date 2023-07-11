import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types
import googlemaps
import pandas as pd
from pprint import pprint
from config import token,googleapi


TOKEN = token
api_key = googleapi
gmaps = googlemaps.Client(key=api_key)
bot = telebot.TeleBot(TOKEN)


franc=[{'name': 'CoMMuna','district': 'Франківський', 'address': 'вул. Кольберга, 3а',  'photo': 'https://communa.net.ua/wp-content/uploads/2020/09/photo_2019-08-10_13-15-37.jpg', 'details': 'https://communa.net.ua/', 'description': 'Франківський  Затишний коворкінг на 300 м2. Тут є 5 офісів, 2 скайп-кімнати, 2 переговорні кімнати та 1 івент зал, 10 фіксованих місць у зоні коворкінгу, кухня, релакс-зона. Обладнаний усім необхідним для комфортної роботи: швидкісний інтернет, компактні офіси з комфортними меблями, місця для дзвінків та переговорів, затишна кухня, фудзони з безкоштовними кавою/чаєм та додатками.'},
       {'name': 'MY GLOBAL WORKSPACE','district': 'Франківський', 'address': 'вул. Кульпарківська, 59 (2-ий поверх)',
        'photo': 'https://lh3.googleusercontent.com/p/AF1QipMpiFCVDhJbqIV2uROqkyqDpkjQjrUvkobaCpC1=s1360-w1360-h1020',
        'details': 'https://www.instagram.com/myglobal_workspace',
        'description': 'Комфортний простір для роботи та нетворкінгу: Кімнати для нарад та відео-конференцій, обідня та релакс зони, карткова система доступу лише для членів Коворкінгу, повний доступ до високоякісного та безпечного Інтернету, забезпечення альтернативними засобами живлення та Інтернету (у випадку відключення електроенергії)'},
       {'name': 'Futura Hub','district': 'Франківський', 'address': 'вул. Кульпарківська, 200а',
        'photo': 'https://futura-hub.com.ua/wp-content/uploads/2021/12/IMG_2350.jpeg',
        'details': 'https://futura-hub.com.ua/category/coworking-uk/',
        'description': 'Креативний простір для твого прояву. Це великий бізнес-центр з коворкінгом, офісами, конференц-залами, ресторанами та магазинами.'},
       {'name': 'Old Amsterdam Coworking','district': 'Франківський', 'address': 'вул. Наукова, 2б',
        'photo': 'https://oldamsterdam.space/wp-content/uploads/2021/02/hero-image-001-e1614089767796.webp',
        'details': 'https://oldamsterdam.space/',
        'description': 'Коворкінг Old Amsterdam з’явився на світ як спроба створити простір для людей, щоб співпрацювати, творити, генерувати нові ідеї та почуватися як вдома. Це місце, відмінне від будь-якого іншого, саме по собі є джерелом натхнення. Додайте сюди культуру, яку ми створили довкола нього, і вам ніколи не захочеться звідси піти.'}
       ]
"""for i in range(0,len(franc)):
    franc[i].update({'place_id':gmaps.find_place(input=franc[i]['name'], input_type='textquery', fields=['place_id'])['candidates'][0]['place_id']})
for j in range(0,len(franc)):
    franc[j].update({'rating':[gmaps.place(place_id=franc[j]['place_id'], fields=['rating'])][0]['result']['rating']})
    franc[j].update({'total_count_rating':[gmaps.place(place_id=franc[j]['place_id'], fields=['user_ratings_total'])][0]['result']['user_ratings_total']})

pprint(franc)"""


galicia=[{'name': 'МолоДвіж Центр','district': 'Галицький', 'address': 'вул. Скорика, 31', 'photo': 'https://www.lvivconvention.com.ua/wp-content/uploads/2021/03/IMG_9343-scaled.jpg', 'details': 'https://linktr.ee/molodvizhcenter', 'description': 'Молодіжний простір у Львові з безкоштовним коворкінгом і лекторієм. Драйвує у руслі: побудови соціальних ліфтів, молодіжних досліджень та мережування молоді. 1 зал, 30 осіб, Найбільший зал 44м2, Площа найбільшого залу 44м2'},
         {'name': 'Coworking Think','district': 'Галицький', 'address': 'вул. Галицька, 21',
          'photo': 'https://sp-ao.shortpixel.ai/client/q_lossy,ret_img/https://coworking-think.com/wp-content/uploads/2021/01/about-2-1-1.jpg',
          'details': 'https://coworking-think.com/en/',
          'description': 'Коворкінг Think - коворкінг, розташований у центрі Львова, створений для об''єднання однодумців та людей різних професій. Силу спілкування не можна недооцінювати. Тому пріоритетом є організація якісних умов для продуктивної роботи та максимального використання потенціалу та натхнення клієнтів.'}
         ]

syhiv=[{'name': 'Lviv Open Lab','district': 'Сихівський', 'address': 'просп. Червоної Калини, 58', 'photo': 'https://city-adm.lviv.ua/images/_news/2020/10/10/LvivOpenLab/121163202_647472369273680_897274382599511015_n.jpg', 'details': 'https://tvory.notion.site/tvory/Lviv-Open-Lab-14f0e60229564799a52b69a7f6c15b33', 'description': 'Lviv Open Lab - це: - простір інноваційної освіти - коворкінг для тих, хто шукає місце для того, щоб попрацювати, повчитися чи зібратися з командою - лекторій для тих, хто хоче провести свою подію - круті лабораторії, де до науки можна доторкнутися, а не лише прочитати про неї. Основною метою простору є популяризація науки, технологій та STEAM-освіти серед підлітків та молоді, а також створення можливостей для їх розвитку і майданчику для обміну ідеями.'}]

shevchen=[{'name': 'Regus KIVSH','district': 'Шевченківський', 'address': 'вул. Шевченка, 120', 'photo': 'https://assets.iwgplc.com/image/upload/c_fill,f_auto,q_auto,g_auto:subject,ar_7:10,h_296,w_217/CentreImagery/5754/5754_2.jpg', 'details': 'https://www.regus.com/uk-UA/ukraine/lviv', 'description': 'Стильні робочі простори в центральному діловому районі Львова. Орендуйте гнучкий робочий простір в історичному районі, розташованому на захід від центру міста Львів, і станьте частиною динамічної спільноти підприємців із різноманітних галузей.'},
              {'name': 'Ustart coworking','district': 'Шевченківський', 'address': 'вул. Шевченка, 111А, БЦ «Legenda Class», 11 поверх',
               'photo': 'https://ustartcoworking.com/images/tild6436-6638-4631-b261-306365626537__img_4030.jpg',
               'details': 'https://ustartcoworking.com/',
               'description': 'Усе для Вашого максимального комфорту та продуктивності: панорама центральної частини м. Львова з висоти 11 поверху; 1400 кв.м. площі для ефективної та комфортної роботи; open space на 58 робочих місць; 9 приватних кімнат для компаній від 2 до 17 осіб'}    ]

lychakiv=[    {'name': 'KONTORA','district': 'Личаківський', 'address': 'пл. Є. Петрушевича, 5', 'photo': 'https://www.coworkbooking.com/images/1600!0/kapacita/9324/img_3269_111.jpg', 'details': 'https://kontoralviv.com/', 'description': 'Vertical City Coworking - від офісів преміум класу на 2 поверсі, до кімнат для команд та переговорів на третьому, а також серця KONTORA - просторого open-space офісу на 4-му та затишного Sky лаунжу на 5 поверсі; Flat one-level coworking - однорівневий коворкінг на вершині нового торгово-офісного центру в самому серці міста. Усе поруч - світлий лаунж та open-space офіс, кімнати для команд та переговорів, простора тераса та дах із мальовничим видом на місто.'}]
#coworkings = [{'name':"Франківський район",'list':franc},galicia,syhiv,shevchen,lychakiv]
free_wifidf=pd.read_csv("freewifilviv.csv").to_dict(orient='records')
coworkings = [
    {'name': "Шевченківський район", 'list': shevchen,
     'photo': 'https://imgur.com/a/26Q0U0t'},
    {'name': "Личаківський район", 'list': lychakiv,
     'photo': 'https://imgur.com/ZkheRVa'},
    {'name': "Сихівський район", 'list': syhiv,
     'photo': 'https://imgur.com/a/bc5Jsie'},
    {'name':"Франківський район",'list':franc,'photo':'https://imgur.com/Y47yKtC'},
    {'name': "Галицький район", 'list': galicia,
     'photo': 'https://imgur.com/a/Vx0KMNe'},

]

interesting_places=[#{'name':"Sobors",'list': soborsdf,'photo': 'https://play-lh.googleusercontent.com/pR3AhTl1bOz8anFPzWj3O6RucXldUqrhOQVkCRpnmtfVUcHiyPC_E4Yppb8s9GjGlg'},
                    {'name':"Безкоштовний вай-фай",'list': free_wifidf,'photo': 'https://golossokal.com.ua/wp-content/uploads/2023/02/wi-fi-Lviv.webp'}]

for coworking in coworkings:
    for c in coworking['list']:
        c.update({'place_id':gmaps.find_place(input=c['name'], input_type='textquery', fields=['place_id'])['candidates'][0]['place_id']})


"""for i in range(0,len(coworkings)):
    for c in coworkings[i]['list']:
        #pprint(c)
        for j in range(0,len(c)):
            #print([gmaps.place(place_id=c['place_id'], fields=['rating'])][0]['result']['rating'])
            c.update({'rating': [gmaps.place(place_id=c['place_id'], fields=['rating'])][0]['result']['rating']})
            c.update({'total_count_rating': [gmaps.place(place_id=c['place_id'], fields=['user_ratings_total'])][0]['result']['user_ratings_total']})
            c.update({'latitude':gmaps.place(place_id=c['place_id'],fields=['geometry'])['result']['geometry']['location']['lat']})
            c.update({'longitude':gmaps.place(place_id=c['place_id'], fields=['geometry'])['result']['geometry']['location']['lng']})"""
for coworking in coworkings:
    for c in coworking['list']:
        place_id = c['place_id']

        # Make a single request to retrieve all the required fields
        place_data = gmaps.place(place_id, fields=['rating', 'user_ratings_total', 'geometry'])

        # Update the dictionary with the retrieved fields
        c.update({
            'rating': place_data['result'].get('rating'),
            'total_count_rating': place_data['result'].get('user_ratings_total'),
            'latitude': place_data['result']['geometry']['location']['lat'],
            'longitude': place_data['result']['geometry']['location']['lng']
        })
for place in interesting_places:
    for p in place['list']:
        p.update({'category': place['name']})
"""for i in range(0,len(coworkings)):
    for c in coworkings[i]['list']:
        pprint(c)"""


print(type(coworkings[0]))

places = [
    {'name': 'Оперний театр', 'address': 'проспект Свободи, 28', 'photo': 'https://lviv.vgorode.ua/img/forall/u/1530/17/a7f153a5570e9cc4ddb1e735ee91f428.jpg'},
    {'name': 'Палац Потоцьких', 'address': 'вул. Коперника, 15', 'photo': 'https://lviv.vgorode.ua/img/forall/u/1530/17/Potocki-Palace.jpg'},

]

@bot.message_handler(commands=['start','menu'])
def send_welcome(message):
    #markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    #markup.add(types.KeyboardButton("Коворкінги", callback_data='coworkings'),
    #             types.KeyboardButton("Цікаві місця", callback_data='places'))
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 3  # встановлюємо ширину рядка кнопок в 1, щоб кнопки виводилися по одній на рядок
    keyboard.add(InlineKeyboardButton("Коворкінги", callback_data='coworkings'),
                 InlineKeyboardButton("Корисні місця", callback_data='places'))

    # відправляємо бокове меню з доступними командами замість повідомлення
    bot.send_photo(message.chat.id, photo='https://imgur.com/a/gNNyBt8', caption= "Виберіть, про що ви бажаєте дізнатися більше:",
                   reply_markup=keyboard)
    #bot.send_message(message.chat.id, "Виберіть, про що ви бажаєте дізнатися більше:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def send_info(call):
    if call.data == 'coworkings':
        keyboard = InlineKeyboardMarkup()
        for c in coworkings:
            keyboard.add(InlineKeyboardButton(c['name'], callback_data=c['name']))
        # Додамо кнопку "Назад" до меню
        keyboard.add(InlineKeyboardButton("Назад", callback_data='back'))
        #bot.edit_message_text("Виберіть коворкінг:", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard)
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               media=types.InputMediaPhoto(media="https://www.wework.com/ideas/wp-content/uploads/sites/4/2019/12/20190917_WeWork_Carrera11b-99-25_Colombia_007_v1-1120x630.jpg",
                                                           caption="Виберіть район у якому ви хочете знайти коворкінг:"),
                               reply_markup=keyboard)
        #bot.send_message(call.message.chat.id, "Виберіть коворкінг:", reply_markup=keyboard)
    elif call.data == 'places':
        keyboard = InlineKeyboardMarkup()
        for p in interesting_places:
            keyboard.add(InlineKeyboardButton(p['name'], callback_data=p['name']))
        # Додамо кнопку "Назад" до меню
        keyboard.add(InlineKeyboardButton("Назад", callback_data='back'))
        # bot.edit_message_text("Виберіть коворкінг:", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard)
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                               media=types.InputMediaPhoto(
                                   media='https://lviv.travel/image/blocks/02/b6/02b6c944fb4c9cc8e84b8a690679c1e965980322_1613400787.png?w=600&crop=768%2C576%2C343%2C0',
                                   caption="Виберіть категорію корисних або цікавих місць:"),
                               reply_markup=keyboard)
        #bot.send_message(call.message.chat.id, "Виберіть цікаве місце:", reply_markup=keyboard)
    elif call.data == 'back':
        # При натисканні кнопки "Назад" повертаємо користувача до головного меню
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton("Коворкінги", callback_data='coworkings'),
                     InlineKeyboardButton("Корисні місця", callback_data='places'))
        #bot.edit_message_text("Виберіть, що ви бажаєте дізнатися більше:", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard)
        #bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption="Виберіть, що ви бажаєте дізнатися більше:", reply_markup=keyboard)
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,media=types.InputMediaPhoto(media="https://imgur.com/a/gNNyBt8",caption="Виберіть, що ви бажаєте дізнатися більше:"),
                               reply_markup=keyboard)
    elif call.data == 'backtoprev':
        keyboard = InlineKeyboardMarkup()
        #print(call.message.caption)
        for c in coworkings:
            if c['name'].split()[0] in call.message.caption:

                correctdistrict=c
                for j in sorted(c['list'], key=lambda x: x['rating'], reverse=True):
                    keyboard.add(InlineKeyboardButton(f"{j['name']} - {j['rating']} \u2605", callback_data=j['name']))
                #keyboard.add(InlineKeyboardButton("Назад до меню", callback_data='back'))

        keyboard.add(InlineKeyboardButton("Назад до попереднього меню", callback_data='coworkings'),InlineKeyboardButton("Назад до головного меню", callback_data='back'))
        bot.edit_message_media(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            media=types.InputMediaPhoto(media=correctdistrict["photo"], caption=f"{correctdistrict['name']}"),
            reply_markup=keyboard
        )
    elif call.data == 'backtoprevplace':
        keyboard = InlineKeyboardMarkup()
        #print(call.message.caption)
        for c in interesting_places:
            if c['name'].split()[0] in call.message.caption:

                correctdistrict=c
                for j in c['list']:
                    keyboard.add(InlineKeyboardButton(f"{j['name']} - {j['rating']} \u2605", callback_data=j['name']))
                #keyboard.add(InlineKeyboardButton("Назад до меню", callback_data='back'))

        keyboard.add(InlineKeyboardButton("Назад до попереднього меню", callback_data='places'),InlineKeyboardButton("Назад до головного меню", callback_data='back'))
        bot.edit_message_media(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            media=types.InputMediaPhoto(media=correctdistrict["photo"], caption=f"{correctdistrict['name']}"),
            reply_markup=keyboard
        )
    elif call.data=='deleteloc':
        bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.id)
    elif call.data=='placeloc':
        keyboard=InlineKeyboardMarkup()
        for c in coworkings:
            if c['name'].split()[0] in call.message.caption:
                for j in c['list']:
                    if j['name'] in call.message.caption:
                        keyboard.add(InlineKeyboardButton(f"Закрити розташування {j['name']}", callback_data='deleteloc'))
                        bot.send_location(chat_id=call.message.chat.id,latitude=j['latitude'],longitude=j['longitude'],reply_markup=keyboard)
    elif call.data == 'placelocplace':
        keyboard = InlineKeyboardMarkup()
        for c in interesting_places:
            for j in c['list']:
                if j['name'] in call.message.caption:
                    keyboard.add(InlineKeyboardButton(f"Закрити розташування {j['name']}",
                                                      callback_data='deleteloc'))
                    bot.send_location(chat_id=call.message.chat.id, latitude=j['latitude'],
                                      longitude=j['longitude'], reply_markup=keyboard)
    #keyboard.add(InlineKeyboardButton("Назад до меню", callback_data='back'))

        """keyboard.add(InlineKeyboardButton("Назад до попереднього меню", callback_data='coworkings'),InlineKeyboardButton("Назад до головного меню", callback_data='back'))
        bot.edit_message_media(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            media=types.InputMediaPhoto(media=correctdistrict["photo"], caption=f"{correctdistrict['name']}"),
            reply_markup=keyboard
        )"""

    else:
        keyboard = InlineKeyboardMarkup()

        """for c in coworkings:
            if call.data == c['name']:

                for j in c['list']:
                    keyboard.add(InlineKeyboardButton(j['name'], callback_data=j['name']))

                keyboard.add(InlineKeyboardButton("Назад до меню", callback_data='back'))
                #bot.send_photo(call.message.chat.id, photo=c['photo'],caption=f"{c['name']}\nОпис: {c['description']}\nДеталі: {c['details']}\nАдреса: {c['address']}",reply_markup=keyboard)
                #bot.edit_message_media(chat_id=call.message.chat.id,message_id=call.message.message_id,media=types.InputMediaPhoto(media=c["photo"],caption=f"{c['name']}\nОпис: {c['description']}\nДеталі: {c['details']}\nАдреса: {c['address']}"),reply_markup=keyboard)
                bot.edit_message_media(chat_id=call.message.chat.id,message_id=call.message.message_id,media=types.InputMediaPhoto(media=c["photo"],caption=f"{c['name']}"),reply_markup=keyboard)
            for j in c['list']:
                if call.data==j['name']:
                    keyboard1=InlineKeyboardMarkup()
                    #keyboard1.add("Назад до попереднього меню",callback_data='')
                    keyboard1.add(InlineKeyboardButton("Назад до головного меню", callback_data='back'))
                    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                           media=types.InputMediaPhoto(media=j["photo"],
                                                                       caption=f"{j['name']}\nОпис: {j['description']}\nДеталі: {j['details']}\nАдреса: {j['address']}"),
                                           reply_markup=keyboard1)

                #bot.send_message(call.message.chat.id, reply_markup=keyboard,text='try')

                # Додамо кнопку "Назад" до меню"""
        for c in coworkings:
            if call.data == c['name']:
                for j in sorted(c['list'],key=lambda x: x['rating'],reverse=True):
                    keyboard.add(InlineKeyboardButton(f"{j['name']} - {j['rating']} \u2605", callback_data=j['name']))

                keyboard.add(InlineKeyboardButton("Назад до попереднього меню", callback_data='coworkings'),InlineKeyboardButton("Назад до головного меню", callback_data='back'))
                print(call.data)
                bot.edit_message_media(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    media=types.InputMediaPhoto(media=c["photo"], caption=f"{c['name']}"),
                    reply_markup=keyboard
                )
        keyboard1 = InlineKeyboardMarkup()

        #keyboard1.add(InlineKeyboardButton()

        for c in coworkings:
            for j in c['list']:
                if call.data == j['name']:
                    keyboard1.add(InlineKeyboardButton("*клац*",url=j['details']))
                    keyboard1.add(InlineKeyboardButton(f"Отримати розташування {j['name']}",callback_data='placeloc'))
                    keyboard1.add(InlineKeyboardButton("Назад до попереднього меню", callback_data='backtoprev'),
                                  InlineKeyboardButton("Назад до головного меню", callback_data='back'))
                    bot.edit_message_media(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        media=types.InputMediaPhoto(
                            media=j["photo"],
                            caption=f"*{j['name']}*\n\n*Рейтинг*: {j['rating']}\u2605\n*Район*: {j['district']}\n*Кількість відгуків на Google Maps*: {j['total_count_rating']}\n*Адреса*: {j['address']}\n\n*Опис*: {j['description']}\n*Деталі*: [перейти на сайт]({j['details']})",parse_mode='Markdown'
                        ),
                        reply_markup=keyboard1
                    )




        """for p in places:
            if call.data == p['name']:
                keyboard = InlineKeyboardMarkup()
                keyboard.add(InlineKeyboardButton("Назад до меню", callback_data='back'))
                #bot.send_photo(call.message.chat.id, photo=p['photo'])
                #bot.send_message(call.message.chat.id, f"{p['name']}\nАдреса: {p['address']}")
                bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                       media=types.InputMediaPhoto(media=p["photo"],
                                                                   caption=f"{p['name']}\nАдреса: {p['address']}"),
                                       reply_markup=keyboard)
                # Додамо кнопку "Назад" до меню"""
        keyboardplaces=InlineKeyboardMarkup()
        for p in interesting_places:
            if call.data == p['name']:
                for s in p['list']:
                    keyboardplaces.add(InlineKeyboardButton(f"{s['name']} - {s['rating']} \u2605", callback_data=s['name'],row_width=15))

                keyboardplaces.add(InlineKeyboardButton("Назад до попереднього меню", callback_data='places'),InlineKeyboardButton("Назад до головного меню", callback_data='back'))
                print(call.data)
                bot.edit_message_media(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    media=types.InputMediaPhoto(media=p["photo"], caption=f"{p['name']}"),
                    reply_markup=keyboardplaces
                )
        keyboardplaces1 = InlineKeyboardMarkup()

        #keyboard1.add(InlineKeyboardButton()

        for p in interesting_places:
            for s in p['list']:
                if call.data == s['name']:
                    keyboardplaces1.add(InlineKeyboardButton(f"Отримати розташування {s['name']}",callback_data='placelocplace'))
                    keyboardplaces1.add(InlineKeyboardButton("Назад до попереднього меню", callback_data='backtoprevplace'),
                                  InlineKeyboardButton("Назад до головного меню", callback_data='back'))
                    bot.edit_message_media(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        media=types.InputMediaPhoto(
                            media=s["photo"],
                            caption=f"*{s['name']}*\n\n*Категорія*: {s['category']}\n*Рейтинг*: {s['rating']}\u2605\n*Кількість відгуків на Google Maps*: {s['total_count_rating']}\n*Адреса*: {s['address']}\n\n",parse_mode='Markdown'
                        ),
                        reply_markup=keyboardplaces1
                    )

bot.polling()
"""Коворкінги:
Франківський: CoMMuna,  MY GLOBAL WORKSPACE, Futura Hub, Old Amsterdam Coworking
Галицький: МолоДвіж Центр, Coworking Think,
Сихівський: Lviv Open Lab,
Шевченківський: Regus KIVSH, Ustart coworking
Личаківський: KONTORA
Цікаві місця:"""
