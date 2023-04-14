from telethon import TelegramClient, events
from lingua import isocode
from detector import get_language_code

MESSAGE = 'Українізація в дії.\n\n' \
          'Це повідомлення було видалено автоматично через використання російської мови.\n\n' \
          'Будь ласка, спробуйте ще раз написати повідомлення українською мовою.\n\n' \
          'Більше інформації – [ukrainisation.com](https://ukrainisation.com)'

api_id = int(input("Please enter your app_id: "))
api_hash = input("Please enter your app_hash: ")

client = TelegramClient('personal', api_id, api_hash)


@client.on(events.NewMessage())
async def handler(event: events.NewMessage.Event):
    if not event.is_private:
        return

    language = get_language_code(event.raw_text)

    if language == isocode.IsoCode639_3.RUS:
        await event.respond(MESSAGE)
        await event.client.delete_messages(event.chat_id, [event.id])


client.start()
client.run_until_disconnected()
