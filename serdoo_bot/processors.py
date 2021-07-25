from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.inlinekeyboardbutton import InlineKeyboardButton
from django_tgbot.types.inlinekeyboardmarkup import InlineKeyboardMarkup
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.update import Update
from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot


state_manager.set_default_update_types(update_types.Message)


@processor(state_manager, from_states=state_types.Reset, message_types=[message_types.Text])
def send_keyboards(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    text = str(update.get_message().get_text())

    if text.lower() in ['normal', 'regular keyboard']:
        send_normal_keyboard(bot, chat_id)
    elif text.lower() in ['inline']:
        send_inline_keyboard(bot, chat_id)
    elif text.lower() in ['start']:
        send_leaving_form(bot, chat_id)
    elif text.lower() in ['mekdi']:
        get_name(bot, chat_id , state)
    else:
        send_options(bot, chat_id)


@processor(state_manager, from_states=state_types.All, update_types=[update_types.CallbackQuery])
def handle_callback_query(bot: TelegramBot, update, state):
    chat_id = update.get_chat().get_id()
    callback_data = update.get_callback_query().get_data()
    bot.answerCallbackQuery(update.get_callback_query().get_id(), text='you Selected: {}'.format(callback_data))
    print(callback_data)
    if callback_data in ['leaving']:
        send_destination_form(bot , chat_id)
    elif callback_data in ['dest']:
        send_departureDate_form(bot , chat_id)
   
    elif callback_data in ['date']:
        select_trips_list(bot , chat_id)
   
    
    
@processor(
    state_manager, from_states='asked_for_name', 
    update_types=[update_types.Message, update_types.EditedMessage], 
    message_types=message_types.Text, 
    success='asked_for_email', fail=state_types.Keep
)
def get_name(bot, update, state):
    pass


def send_normal_keyboard(bot, chat_id):
    bot.sendMessage(
        chat_id,
        text='Here is a keyboard for you!',
        
        
       
        reply_markup=ReplyKeyboardMarkup.a(
            one_time_keyboard=True,
            resize_keyboard=True,
            selective=True,
            
            keyboard=[
                [KeyboardButton.a('🚒️ Book Your Seat'), KeyboardButton.a('💺️ My seat')],
                [KeyboardButton.a('⛈ Feedback'), KeyboardButton.a('🕖️ Settings')],
                [KeyboardButton.a('❔ Help') , KeyboardButton.a('👥 About us') ]
            ]
        )
        
    )


def send_inline_keyboard(bot, chat_id):
    bot.sendMessage(
        chat_id,
        text='Here is my suggestion for nice groups!',
        reply_markup=InlineKeyboardMarkup.a(
            inline_keyboard=[
                   [
                    InlineKeyboardButton.a('😎  Who Made The Rules', url='https://t.me/WhoMadeTheRules'),
                    InlineKeyboardButton.a('📞  Ethio Telecom', url='https://t.me/ethio_telecom'),
                   ],
                   [
                    InlineKeyboardButton.a('🇪🇹️ Tikvah Ethiopia', url='https://t.me/tikvahethiopia'),
                    InlineKeyboardButton.a('🤣️ Habesha Meme', url='https://t.me/officialHabeshanMeme'),
                   ],
                [
                    InlineKeyboardButton.a('⭐️  Callback Button', callback_data='you are @The Right Place')
                    
                ],
                
            ]
        )
    )


def send_options(bot, chat_id):
    bot.sendMessage(
        chat_id,
        text='I can send you two different types of keyboards!\n type  `normal` or `inline` and you will have one of them \n CAUTION\n SPELL THEM CORRECTLY!!! ;)',
        parse_mode=bot.PARSE_MODE_MARKDOWN
    )
def  send_leaving_form(bot, chat_id):
    bot.sendMessage(
        chat_id,
        text='select Leaving citiy from the list \n\n',
        reply_markup=InlineKeyboardMarkup.a(
            inline_keyboard=[
                   [
                    InlineKeyboardButton.a('Addis Abeba', callback_data = 'leaving'),
                    InlineKeyboardButton.a('Hawassa', callback_data= 'leaving'),
                    InlineKeyboardButton.a('Bahirdar', callback_data='leaving'),
                   ],
                   [
                    InlineKeyboardButton.a('Bahirdar', callback_data='leaving'),
                    InlineKeyboardButton.a('Nazret', callback_data='leaving'),
                    InlineKeyboardButton.a('Nazret', callback_data='leaving'),
                   ],
                   [
                    InlineKeyboardButton.a('Jimma', callback_data='leaving'),
                    InlineKeyboardButton.a('Welayita', callback_data='leaving'),
                    InlineKeyboardButton.a('Jimma', callback_data='leaving'),
                    
                   ],
                    [
                    InlineKeyboardButton.a('Silale', callback_data='leaving'),
                    InlineKeyboardButton.a('Gonder', callback_data='leaving'),
                    InlineKeyboardButton.a('Gonder', callback_data='leaving')
                    
                    
                   ],
                    [
                    InlineKeyboardButton.a('Debre_tabore', callback_data='leaving'),
                    InlineKeyboardButton.a('Debre_markos', callback_data='leaving'),
                    InlineKeyboardButton.a('Gonder', callback_data='leaving')
                    
                    
                   ],
                
            ]
        )
     
    )
def  send_destination_form(bot, chat_id):
    bot.sendMessage(
        chat_id,
        text='\n\n\n select Destination citiy from the list \n\n ',
        reply_markup=InlineKeyboardMarkup.a(
            inline_keyboard=[
                   [
                    InlineKeyboardButton.a('Addis Abeba', callback_data = 'dest'),
                    InlineKeyboardButton.a('Hawassa', callback_data= 'dest'),
                    InlineKeyboardButton.a('Bahirdar', callback_data='dest'),
                   ],
                   [
                    InlineKeyboardButton.a('Bahirdar', callback_data='dest'),
                    InlineKeyboardButton.a('Nazret', callback_data='dest'),
                    InlineKeyboardButton.a('Nazret', callback_data='dest'),
                   ],
                   [
                    InlineKeyboardButton.a('Jimma', callback_data='dest'),
                    InlineKeyboardButton.a('Welayita', callback_data='dest'),
                    InlineKeyboardButton.a('Jimma', callback_data='dest'),
                    
                   ],
                    [
                    InlineKeyboardButton.a('Silale', callback_data='dest'),
                    InlineKeyboardButton.a('Gonder', callback_data='dest'),
                    InlineKeyboardButton.a('Gonder', callback_data='dest')
                    
                    
                   ],
                    [
                    InlineKeyboardButton.a('Debre_tabore', callback_data='dest'),
                    InlineKeyboardButton.a('Debre_markos', callback_data='dest'),
                    InlineKeyboardButton.a('Gonder', callback_data='dest')
                    
                    
                   ],
                
            ]
        )
     
    )
def  send_departureDate_form(bot, chat_id):
    bot.sendMessage(
        chat_id,
        text='\n\n\n select Departure Date from the list \n\n ',
        reply_markup=InlineKeyboardMarkup.a(
            inline_keyboard=[
                   [
                    InlineKeyboardButton.a('mon 26', callback_data = 'date'),
                    InlineKeyboardButton.a('tue 27', callback_data= 'date'),
                    InlineKeyboardButton.a('wed 28', callback_data='date'),
                   ],
                   [
                    InlineKeyboardButton.a('thu 29', callback_data='date'),
                    InlineKeyboardButton.a('fri 30', callback_data='date'),
                    InlineKeyboardButton.a('sat 31', callback_data='date'),
                   ],
                   [
                    InlineKeyboardButton.a('sun 1', callback_data='date'),
                    InlineKeyboardButton.a('mon 2', callback_data='date'),
                   
                    
                   ],
                  
                
            ]
        )
     
    )
def  select_trips_list(bot, chat_id):
    bot.sendMessage(
        chat_id,
        text='\n\n\n select bus type from the list \n\n ',
        reply_markup=InlineKeyboardMarkup.a(
            inline_keyboard=[
                   [
                    InlineKeyboardButton.a('🚌 Alpha  \n 2:30am    11:pm \n 500etb', callback_data = 'date'),
                    InlineKeyboardButton.a('tue 27', callback_data= 'date'),
                    InlineKeyboardButton.a('wed 28', callback_data='date'),
                   ],
                   [
                    InlineKeyboardButton.a('thu 29', callback_data='date'),
                    InlineKeyboardButton.a('fri 30', callback_data='date'),
                    InlineKeyboardButton.a('sat 31', callback_data='date'),
                   ],
                   [
                    InlineKeyboardButton.a('sun 1', callback_data='date'),
                    InlineKeyboardButton.a('mon 2', callback_data='date'),
                   
                    
                   ],
                  
                
            ]
        )
     
    )
    
    
    
    
    
