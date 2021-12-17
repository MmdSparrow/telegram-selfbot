from telethon import TelegramClient, connection, events
from Include.staticBot.AbstractStaticBot import AbstractStaticBot
import json
import jdatetime as jdt


class StaticBot(AbstractStaticBot):

    def __init__(self):
        # self.__
        self.__API_ID = 15396868
        self.__API_HASH = 'f2a1d666e9e243dbb6b616d9520f02e7'
        self.__CHECK_CHARACTER = '\u2713'
        self.__UNCHECK_CHARACTER = '\u2717'
        self.__ABOUT_ME = "ABOUT ME!"
        self.__HELP = "For more information on a specific command, type .help command-name\n" +\
                      "**.add**         Add task to list.\n" +\
                      "**.copy**        Copy all remaining tasks to list of tomorrow.\n" +\
                      "**.del**         Delete a task by index.\n" +\
                      "**.done**        Mark the task as done.\n" +\
                      "**.show**        Show tasks list.\n" +\
                      "**.showd**       Show all finished tasks in the list.\n" +\
                      "**.showu**       show all remaining tasks in the list.\n"

        self.__ProxyServer = ""
        self.__ProxyPort = ""

    def _add_task(self, task, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                  day=str(jdt.datetime.now().day)):
        with open('../../source/schedule.json', 'r+') as file:
            file_data = json.load(file)
            file_data[year][month][day].append(task)
            file.seek(0)
            json.dump(file_data, file)
            file.close()

    def _delete_task(self, task_number, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                     day=str(jdt.datetime.now().day)):
        with open('../../source/schedule.json', 'r+') as file:
            file_data = json.load(file)
            file_data[year][month][day].remove(task_number)
            file.seek(0)
            json.dump(file_data, file)
            file.close()

    def _show_tasks(self, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                    day=str(jdt.datetime.now().day)):
        f = open('../source/schedule.json')
        data = json.load(f)
        if len(data[year][month][day]) == 0:
            todo_massage = "You don't defined any task for this day!"
        else:
            todo_massage = "Your task list:"
            for item in data[year][month][day]:
                todo_massage += "\n" + item
        f.close()
        return todo_massage

    def _show_done_tasks(self, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                         day=str(jdt.datetime.now().day)):
        f = open('../source/schedule.json')
        data = json.load(f)
        if len(data[year][month][day]) == 0:
            todo_massage = "You don't defined any task for this day!"
        else:
            todo_massage = "Your done task list:"
            for item in data[year][month][day]:
                if self.__CHECK_CHARACTER in item:
                    todo_massage += "\n" + item
        f.close()
        if todo_massage == "Your done task list:":
            todo_massage = "U do nothing in this day! shame on u :/"
        return todo_massage

    def _show_undone_tasks(self, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                           day=str(jdt.datetime.now().day)):
        f = open('../source/schedule.json')
        data = json.load(f)
        if len(data[year][month][day]) == 0:
            todo_massage = "You don't defined any task for this day!"
        else:
            todo_massage = "Your undone task list:"
            for item in data[year][month][day]:
                if self.__UNCHECK_CHARACTER in item:
                    todo_massage += "\n" + item
        f.close()
        if todo_massage == "Your undone task list:":
            todo_massage = "Well done! u complete all tasks for this day."
        return todo_massage

    def _done_task(self, task_number, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                   day=str(jdt.datetime.now().day)):
        with open('../../source/schedule.json', 'r+') as file:
            file_data = json.load(file)
            file_data[year][month][day][task_number - 1] = file_data[year][month][day][
                                                               task_number - 1] + " " + self.__CHECK_CHARACTER
            file.seek(0)
            json.dump(file_data, file)
            file.close()

    def _done_last_remaining_task_for_today(self):
        with open('../../source/schedule.json', 'r+') as file:
            file_data = json.load(file)
            file_data_in_today = file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day]
            for i in range(len(file_data_in_today)):
                if self.__CHECK_CHARACTER not in file_data_in_today[i]:
                    file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day][i] = \
                        file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day][
                            i] + " " + self.__CHECK_CHARACTER
                    break
        file.close()

    def _undone_remaining_tasks(self):
        pass

    def _copy_remaining_tasks_to_tomorrow(self):
        with open('../../source/schedule.json', 'r+') as file:
            file_data = json.load(file)
            file_data_in_today = file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day]
            for i in range(len(file_data_in_today)):
                if self.__CHECK_CHARACTER not in file_data_in_today[i]:
                    file_data[jdt.datetime.now().year][jdt.datetime.now().month][str(jdt.datetime.now().day + 1)][i] = \
                        file_data[jdt.datetime.now().year][jdt.datetime.now().month][jdt.datetime.now().day][i]
            file.seek(0)
            json.dump(file_data, file)
            file.close()

    def handler(self):
        client = TelegramClient(
            'anon', self.__API_ID, self.__API_HASH
        )

        # client = TelegramClient(
        #     'anon', self.__API_ID, self.__API_HASH,
        #     connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
        #     proxy=(self.__ProxyServer, self.__ProxyPort, 'secret')
        # )

        @client.on(events.NewMessage)
        async def my_event_handler(event):
            sender = await event.get_sender()
            is_private = event.is_private

            if is_private:
                if sender.phone == '989010285337' or sender.phone == '989908210410':
                    massage_str_array = event.raw_text.split()

                    if massage_str_array[0] == '.add':
                        pass
                    elif massage_str_array[0] == '.copy':
                        pass
                    elif massage_str_array[0] == '.del':
                        pass
                    elif massage_str_array[0] == '.done':
                        pass
                    elif massage_str_array[0] == '.help':
                        pass
                    elif massage_str_array[0] == '.show':
                        pass
                    elif massage_str_array[0] == '.showd':
                        pass
                    elif massage_str_array[0] == '.showu':
                        pass




                    if massage_str_array[0] == '.todo':
                        message = ""
                        if len(massage_str_array) == 1:
                            message = self._show_tasks()
                        elif len(massage_str_array) == 2:
                            message = self._show_tasks(day=massage_str_array[1])
                        elif len(massage_str_array) == 3:
                            message = self._show_tasks(month=massage_str_array[2], day=massage_str_array[1])
                        elif len(massage_str_array) == 4:
                            message = self._show_tasks(year=massage_str_array[3], month=massage_str_array[2],
                                                       day=massage_str_array[1])

                        await client.send_message(event.chat_id, message, link_preview=False)

                    if '!done' in event.raw_text:
                        if len(massage_str_array) == 1:
                            self._done_last_remaining_task_for_today()
                        elif len(massage_str_array) == 2:
                            self._done_task(task_number=massage_str_array[1])
                        elif len(massage_str_array) == 3:
                            self._done_task(day=massage_str_array[2], task_number=massage_str_array[1])
                        elif len(massage_str_array) == 4:
                            self._done_task(month=massage_str_array[3], day=massage_str_array[2],
                                            task_number=massage_str_array[1])
                        elif len(massage_str_array) == 5:
                            self._done_task(year=massage_str_array[4], month=massage_str_array[3],
                                            day=massage_str_array[2],
                                            task_number=massage_str_array[1])

                    elif '!about' == event.raw_text:
                        await client.send_message(event.chat_id, self.__ABOUT_ME, link_preview=False)

                    elif '!resume' == event.raw_text:
                        await client.send_file(event.chat_id, '../source/resume.pdf')
                        await client.send_message(
                            event.chat_id,
                            "also you can see my [website](https://sayedmohammadali-mirkazemi.ir)! for more information :/",
                            link_preview=False)

        client.start()
        client.run_until_disconnected()

    def help(self):
        pass

