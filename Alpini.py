import telebot
from telebot import types
import string
import random
from random import choice
import os

token = '580vd7r-SjxAPMYKYJSWRM4Q'
bot = telebot.TeleBot(token)

about_us = 'Узнать подробнее, Вы можете посетив наш сайт по 📲 ' + '[ссылке](https://www.alpinicoffee.com/)'

starts = 'Пожалуйста, нажмите на интересующую Вас кнопку.'

cash = 'Отправьте скриншот опубликованного отзыва в интернет-магазине для проверки со стороны модератора.' \
       '\n\n Для этого нажмите на скрепку 📎 и прикрепите скриншот.'

facts = ['Кофе находится на втором месте среди самых продаваемых продуктов в мире после нефти.', 'Первая итальянская кофейня Cafe Florian появилась в Венеции на площади Сан-Марко в первой половине XVII века. Заведение работает до сих пор.', 'Самый популярный сорт кофе в мире — арабика. Его пьют 70% любителей напитка.', 'Способ приготовления кофе «Американо» появился во время Второй мировой войны. Американские военные не могли пить крепкий европейский кофе и просили разбавить его водой.', 'Чтобы получить смертельную дозу кофеина, нужно выпить 100 чашек кофе.', 'Больше всего кофе пьют финны. В среднем один житель Финляндии выпивает пять чашек в день.', 'Кофеин — это особое вещество для защиты от насекомых и привлечения опылителей, которое вырабатывают кофейные деревья.', 'Первую эспрессо-машину изобрел итальянец Луиджи Беццера в 1901-м. Именно тогда в Италии зародилась культура эспрессо-баров и привычка пить кофе стоя.', 'Продолжительность жизни кофейного дерева составляет около 70 лет.', 'По легенде кофе открыли в Эфиопии. Пастух Калди заметил, что его козы очень энергичны и не спят всю ночь после того, как поедят ягоды с неизвестного ему дерева.', 'Растворимый кофе придумал бельгиец по имени Джордж Вашингтон в 1906-м для нужд американской армии.', 'Кофеин широко применяют в уходовой косметике. Он уменьшает отечность, тонизирует сосуды, укрепляет клеточные мембраны и стимулирует синтез липидов.', 'Из остатков кофейных ягод делают муку.', 'Чашка таиландского кофе Black Ivory стоит 50 долларов. Его производят слоны: животные едят кофейные зерна и опорожняются.', ' В «кофе без кофеина» содержится небольшое количество кофеина.', 'Самый крупный производитель кофе в мире — Бразилия.', 'Каждый год в мире выпивается около 500 миллиардов чашек кофе. Большинство за завтраком.', 'Главный герой фильма «Пока не сыграл в ящик», которого сыграл актер Джек Николсон, всюду возил с собой дорогую кофемашину или термос, чтобы пить любимый сорт кофе — «Копи-лювак». Его получают путем ферментации кофейных зерен в кишечнике зверьков мусангов. Они едят их, переваривают и опорожняются, превращая зерна в гурманский и дорогой сорт.', 'В 1511-м кофе запретили в Мекке: тогда город находился под властью османов. Считалось, что напиток стимулирует праздность и радикальное мышление.', ' Не больше пяти чашек кофе в день может выпивать спортсмен во время участия в Олимпиаде. Кофеин числится в списке запрещенных веществ Международного олимпийского комитета (МОК).', 'Екатерина II была настоящим кофеманом. Императрица выпивала по пять чашек крепкого кофе в день.', 'Пить кофе с лимоном или цитрусами придумали в Риме. Напиток называется Espresso Romano.', 'Молотый кофе появился в XIII веке в восточных странах.', 'В Эфиопии принято добавлять к кофе соль.', 'В XVII и XVIII веках кофе запрещали в разных европейских странах. Например, в Швеции запретили не только напиток, но и посуду для него.', 'Плоды кофейного дерева до сих пор собирают вручную. Один рабочий на плантации собирает около 100 килограмм урожая за один день.', 'Скраб из молотого кофе или его гущи — один из самых популярных пилингов для тела в мире. Содержащийся в нем кофеин имеет свойство расщепления жира.', 'Кофе с пенкой остывает намного медленнее, чем без нее. Она удерживает тепло напитка.', 'Спелые красные ягоды кофейного дерева называют вишней в профессиональных кругах.', 'В мире существует около 100 видов кофе.', 'Диетологи утверждают о необходимости употребления дополнительного стакана воды на одну выпитую чашечку кофе. Именно так подают в приличных заведениях эспрессо, ристретто и лунго.', 'Кофеин не столь сильный окрашиваемый агент, по сравнению с танином, содержащемся в чае. Несколько чашек кофе в день могут повлиять только на верхний тонкий слой, покрывающий зубы, но никак не проникнуть в эмаль.', 'У кофе четыре биологических вида. Coffee Arabica (Арабика), Coffee Robusta (Робуста), Coffee Liberica (Либерика), Coffee Excelsa (Эк-сельса). Последние два практически не имеют коммерческого применения и широкого спроса у потребителей.', 'Необходимая температура для выращивания кофе 15—28ºC круглый год. Поэтому кофе выращивают только в странах, расположенных вдоль экватора планеты и где преобладают суточные перепады температур. Чем чаще перепады температур, тем лучше становится вкус кофе. Поэтому так ценится кофе, выращенный в высокогорных регионах.', 'В мире Арабика считается самым лучшим сортом кофе, но внутри него существует деление на несколько сотен видов в зависимости от региона произрастания, вкусовых качеств, размеров зерна и других характеристик. Если точнее, то Арабика – это не сорт кофе, а вид кофейного растения.', 'Основным преимуществом робусты является содержание кофеина, что в два раза больше чем в зернах арабики, а также неприхотливость к климату. Больше всего рабусты выращивают во Вьетнаме, Индии и Бразилии.']

telephone = 'Для получения кэшбека, укажите номер Вашего мобильного телефона.\nКэшбек зачислится на счёт мобильного телефона.'

email = '\n\nВы также можете указать свой E-mail для получения доступа к эксклюзивным акциям и скидкам Alpinico.'

vahan = "2142492675" # alpinico

@bot.message_handler(commands=['vahanni'])
def vahanni(message):
    bot.send_message(message.from_user.id, f'{message.from_user.first_name}, приветствую тебя в окне рассылки. \nДля отправки рассылки всем участникам, необходимо написать текст рассылки, а затем отправить сообщение\nP.S. не забудь все внимательно перепроверить')
    bot.register_next_step_handler(message, send_text)

def send_text(message):
    text = message.text
    f = open('file.txt', 'r')
    data = f.readlines()
    for i in data:
        bot.send_message(i, text)
    f.close()

@bot.message_handler(commands=['start', 'help'])
def start(message):
    f = open('file.txt', 'a')
    user_id = message.from_user.id
    f.write(str(user_id) + '\n')
    f.close()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, f'{message.from_user.first_name}, на связи Alpinico bot', reply_markup=markup, parse_mode='Markdown')
    btn1 = types.KeyboardButton('Получить кэшбэк')
    btn2 = types.KeyboardButton('О нас')
    btn3 = types.KeyboardButton('Поддержка Alpinico')
    btn4 = types.KeyboardButton('Интересный факт о кофе')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, starts, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(content_types=['photo'])
def photo(message):                                     #получение фото
    bot.forward_message(vahan, message.chat.id, message.message_id)
    bot.reply_to(message, 'Спасибо!\n' + telephone)
    bot.register_next_step_handler(message, get_phone)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Получить кэшбэк':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, cash, reply_markup=markup, parse_mode='Markdown')

    elif message.text == "О нас":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, about_us, reply_markup=markup, parse_mode='Markdown')

    elif message.text == "Поддержка Alpinico":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Для обращения в техническую поддержку, нажмите на @Alpinico.', reply_markup=markup, parse_mode='Markdown')

    elif message.text == "Интересный факт о кофе":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        for i in range(1):
            bot.send_message(message.from_user.id, random.choice(facts))

    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Получить кэшбэк')
        btn2 = types.KeyboardButton('О нас')
        btn3 = types.KeyboardButton('Поддержка Alpinico')
        btn4 = types.KeyboardButton('Интересный факт о кофе')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, starts, reply_markup=markup)

def get_phone(message):
    telephone = message.text
    bot.forward_message(vahan, message.chat.id, message.message_id)
    bot.reply_to(message, 'Ваше сообщение отправлено на модерацию, кэшбэк придет в течение дня. Приятного кофепития ☕')
    bot.send_message(message.from_user.id, email)
    bot.register_next_step_handler(message, get_email)

def get_email(message):
    email = message.text
    bot.forward_message(vahan, message.chat.id, message.message_id)
    bot.reply_to(message, 'Благодарим!')

bot.infinity_polling()



