# from telethon import TelegramClient, connection, events
# import json
# import jdatetime as jdt
#
# API_ID = 15396868
# API_HASH = 'f2a1d666e9e243dbb6b616d9520f02e7'
# client = TelegramClient(
#     'anon', API_ID, API_HASH
# )
# # client = TelegramClient(
# #     'anon', API_ID, API_HASH,
# #     connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
# #     proxy=('mtproxy.example.com', 2002, 'secret')
# # )
# ABOUT_ME_MASSAGE = "about me!"
#
#
# def show_task_list(year=jdt.datetime.now().year, month=jdt.datetime.now().month, day=jdt.datetime.now().day):
#     todo_massage = "Your list today:"
#     f = open('../source/schedule.json')
#     data = json.load(f)
#     for item in data[year][month][day]:
#         todo_massage += "\n" + item
#     f.close()
#     return todo_massage
#
#
# def check_task(task_number, year=jdt.datetime.now().year, month=jdt.datetime.now().month, day=jdt.datetime.now().day):
#     with open('../source/schedule.json', 'r+') as file:
#         file_data = json.load(file)
#         file_data[year][month][day][task_number - 1] = file_data[year][month][day][task_number - 1] + " \u2713"
#         file.seek(0)
#         json.dump(file_data, file, indent=4)
#
#
# def check_last_unchecked_task_today():
#     with open('../source/schedule.json', 'r+') as file:
#         file_data = json.load(file)
#         file_data_in_today = file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day]
#         for i in range(len(file_data_in_today)):
#             if "\u2713" not in file_data_in_today[i]:
#                 file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day][i] = \
#                     file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day][i] + " \u2713"
#                 break
#
#
# @client.on(events.NewMessage)
# async def my_event_handler(event):
#     sender = await event.get_sender()
#     is_private = event.is_private
#
#     if is_private:
#         if sender.phone == '989010285337' or sender.phone == '989908210410':
#             if '!todo' in event.raw_text:
#                 massage_str_array = event.raw_text.split()
#                 message = ""
#                 if len(massage_str_array) == 1:
#                     message = show_task_list()
#                 elif len(massage_str_array) == 2:
#                     message = show_task_list(day=massage_str_array[1])
#                 elif len(massage_str_array) == 3:
#                     message = show_task_list(month=massage_str_array[2], day=massage_str_array[1])
#                 elif len(massage_str_array) == 4:
#                     message = show_task_list(year=massage_str_array[3], month=massage_str_array[2],
#                                              day=massage_str_array[1])
#
#                 await client.send_message(event.chat_id, message, link_preview=False)
#
#             if '!done' in event.raw_text:
#                 massage_str_array = event.raw_text.split()
#                 if len(massage_str_array) == 1:
#                     check_last_unchecked_task_today()
#                 elif len(massage_str_array) == 2:
#                     check_task(task_number=massage_str_array[1])
#                 elif len(massage_str_array) == 3:
#                     check_task(day=massage_str_array[2], task_number=massage_str_array[1])
#                 elif len(massage_str_array) == 4:
#                     check_task(month=massage_str_array[3], day=massage_str_array[2], task_number=massage_str_array[1])
#                 elif len(massage_str_array) == 5:
#                     check_task(year=massage_str_array[4], month=massage_str_array[3], day=massage_str_array[2],
#                                task_number=massage_str_array[1])
#
#             elif '!about' == event.raw_text:
#                 await client.send_message(event.chat_id, ABOUT_ME_MASSAGE, link_preview=False)
#
#             elif '!resume' == event.raw_text:
#                 await client.send_file(event.chat_id, '../source/resume.pdf')
#                 await client.send_message(
#                     event.chat_id,
#                     "also you can see my [website](https://sayedmohammadali-mirkazemi.ir)! for more information :/",
#                     link_preview=False)
#
#
# client.start()
# client.run_until_disconnected()
