from abc import ABC, abstractmethod
import jdatetime as jdt


class AbstractStaticBot(ABC):

    @abstractmethod  # .add
    def _add_task(self, task, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                  day=str(jdt.datetime.now().day)): pass

    @abstractmethod  # .del
    def _delete_task(self, task_number, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                     day=str(jdt.datetime.now().day)): pass

    @abstractmethod  # .show
    def _show_tasks(self, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                    day=str(jdt.datetime.now().day)): pass

    @abstractmethod  # .showd
    def _show_done_tasks(self, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                         day=str(jdt.datetime.now().day)): pass

    @abstractmethod  # .showu
    def _show_undone_tasks(self, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                           day=str(jdt.datetime.now().day)): pass

    @abstractmethod
    def _split_add_task_command(self, task_command): pass

    @abstractmethod  # .done
    def _done_task(self, task_number, year=str(jdt.datetime.now().year), month=str(jdt.datetime.now().month),
                   day=str(jdt.datetime.now().day)): pass

    @abstractmethod  # .done
    def _done_last_remaining_task_for_today(self): pass

    @abstractmethod
    def _undone_remaining_tasks(self): pass

    # it replaces not append
    @abstractmethod  # .copy
    def _copy_remaining_tasks_to_tomorrow(self): pass

    @abstractmethod
    def handler(self): pass

    @abstractmethod  # .help
    def _help(self): pass


