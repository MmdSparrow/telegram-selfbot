import datetime as dt
import json
import jdatetime as jdt


#
# def show_list(year, month, day):
#     todo_massage = "Your list today:"
#     f = open('../source/schedule.json')
#     data = json.load(f)
#     for item in data[year][month][day]:
#         todo_massage += "\n" + item
#     f.close()
#     return todo_massage
#
# print(show_list('1400','9','23'))
#
# print("\u2713")
#
# f = open('../source/schedule.json')
# data = json.load(f)
# print(data['1400']['9']['23'][0])

# function to add to JSON
# def write_json(new_data, filename='../source/test.json'):
#     with open(filename, 'r+') as file:
#         # First we load existing data into a dict.
#         file_data = json.load(file)
#         # Join new_data with file_data inside emp_details
#         file_data["emp_details"].append(new_data)
#         # Sets file's current position at offset.
#         file.seek(0)
#         # convert back to json.
#         json.dump(file_data, file, indent=4)
#
#     # python object to be appended
#
#
# y = {"emp_name": "Nikhil",
#      "email": "nikhil@geeksforgeeks.org",
#      "job_profile": "Full Time"
#      }
#
# write_json(y)

# def done_task(year, month, day, task_number):
#     with open('../source/schedule.json', 'r+') as file:
#         file_data = json.load(file)
#         file_data[year][month][day][task_number]= file_data[year][month][day][task_number] + " \u2713"
#         file.seek(0)
#         json.dump(file_data, file, indent=4)
#
#
# done_task('1400','9','23',1)
#
# print(dt.datetime.now().)
print(jdt.datetime.now())


# from Include.staticBot.AbstractStaticBot import
from abc import ABC

import AbstractStaticBot
from telethon import TelegramClient, connection, events
import json
import jdatetime as jdt


class StaticBot(AbstractStaticBot.AbstractStaticBot, ABC):

    def __init__(self):
        # self.__
        self.__API_ID = 15396868
        self.__API_HASH = 'f2a1d666e9e243dbb6b616d9520f02e7'
        self.__CHECK_CHARACTER = '\u2713'
        self.__UNCHECK_CHARACTER = '\u2717'
        self.__ABOUT_ME = "ABOUT ME!"

        self.__ProxyServer = ""
        self.__ProxyPort = ""

    def _add_task(self):
        pass

    def _delete_task(self):
        pass

    def _show_tasks(self):
        pass

    def _show_undone_tasks(self):
        pass

    def _show_done_tasks(self):
        pass

    def _done_task(self):
        pass

    def _done_last_remaining_task(self):
        pass

    def _undone_remaining_tasks(self):
        pass

    def _copy_remaining_tasks_to_tomorrow(self):
        pass

    # def _handler(self):
    #     client = TelegramClient(
    #         'anon', self.__API_ID, self.__API_HASH
    #     )
    #
    #     # client = TelegramClient(
    #     #     'anon', self.__API_ID, self.__API_HASH,
    #     #     connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    #     #     proxy=(self.__ProxyServer, self.__ProxyPort, 'secret')
    #     # )
    #
    #     @client.on(events.NewMessage)
    #     async def my_event_handler(event):
    #         sender = await event.get_sender()
    #         is_private = event.is_private
    #
    #         if is_private:
    #             if sender.phone == '989010285337' or sender.phone == '989908210410':
    #                 if '!todo' in event.raw_text:
    #                     massage_str_array = event.raw_text.split()
    #                     message = ""
    #                     if len(massage_str_array) == 1:
    #                         message = self.__show_tasks()
    #                     elif len(massage_str_array) == 2:
    #                         message = self.__show_tasks(day=massage_str_array[1])
    #                     elif len(massage_str_array) == 3:
    #                         message = self.__show_tasks(month=massage_str_array[2], day=massage_str_array[1])
    #                     elif len(massage_str_array) == 4:
    #                         message = self.__show_tasks(year=massage_str_array[3], month=massage_str_array[2],
    #                                                     day=massage_str_array[1])
    #
    #                     await client.send_message(event.chat_id, message, link_preview=False)
    #
    #                 if '!done' in event.raw_text:
    #                     massage_str_array = event.raw_text.split()
    #                     if len(massage_str_array) == 1:
    #                         self.__done_last_remaining_task_for_today()
    #                     elif len(massage_str_array) == 2:
    #                         self.__done_task(task_number=massage_str_array[1])
    #                     elif len(massage_str_array) == 3:
    #                         self.__done_task(day=massage_str_array[2], task_number=massage_str_array[1])
    #                     elif len(massage_str_array) == 4:
    #                         self.__done_task(month=massage_str_array[3], day=massage_str_array[2],
    #                                          task_number=massage_str_array[1])
    #                     elif len(massage_str_array) == 5:
    #                         self.__done_task(year=massage_str_array[4], month=massage_str_array[3],
    #                                          day=massage_str_array[2],
    #                                          task_number=massage_str_array[1])
    #
    #                 elif '!about' == event.raw_text:
    #                     await client.send_message(event.chat_id, self.__ABOUT_ME, link_preview=False)
    #
    #                 elif '!resume' == event.raw_text:
    #                     await client.send_file(event.chat_id, '../source/resume.pdf')
    #                     await client.send_message(
    #                         event.chat_id,
    #                         "also you can see my [website](https://sayedmohammadali-mirkazemi.ir)! for more information :/",
    #                         link_preview=False)
    #
    #     client.start()
    #     client.run_until_disconnected()




    #
    # def __add_task(self, year=jdt.datetime.now().year, month=jdt.datetime.now().month, day=jdt.datetime.now().day):
    #     pass
    #
    # def __delete_task(self, year=jdt.datetime.now().year, month=jdt.datetime.now().month, day=jdt.datetime.now().day):
    #     pass
    #
    # def __show_undone_tasks(self):
    #     pass
    #
    # def __show_done_tasks(self):
    #     pass
    #
    # def __undone_remaining_tasks(self):
    #     pass
    #
    # def __copy_remaining_tasks_to_tomorrow(self):
    #     pass
    #
    # def __show_tasks(self, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
    #                  day=str(jdt.datetime.now().day)):
    #     todo_massage = "Your list today:"
    #     f = open('../source/schedule.json')
    #     data = json.load(f)
    #     for item in data[year][month][day]:
    #         todo_massage += "\n" + item
    #     f.close()
    #     return todo_massage
    #
    # def __done_task(self, task_number, year=jdt.datetime.now().year, month=jdt.datetime.now().month,
    #                 day=jdt.datetime.now().day):
    #     with open('../../source/schedule.json', 'r+') as file:
    #         file_data = json.load(file)
    #         file_data[year][month][day][task_number - 1] = file_data[year][month][day][task_number - 1] + " \u2713"
    #         file.seek(0)
    #         json.dump(file_data, file, indent=4)
    #
    # def __done_last_remaining_task_for_today(self):
    #     with open('../../source/schedule.json', 'r+') as file:
    #         file_data = json.load(file)
    #         file_data_in_today = file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day]
    #         for i in range(len(file_data_in_today)):
    #             if "\u2713" not in file_data_in_today[i]:
    #                 file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day][i] = \
    #                     file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day][
    #                         i] + " \u2713"
    #                 break
