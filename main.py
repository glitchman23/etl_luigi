# luigid --background --logdir ./logs
# python <this_file_name> <task_name>

import luigi
import datetime
from load import WriteSellersCodsToSQL, WriteOrdersCodsToSQL


class BuildTasks(luigi.Task):
    date = luigi.DateSecondParameter(default=datetime.datetime.now())

    def requires(self):
        return [WriteSellersCodsToSQL(self.date), WriteOrdersCodsToSQL(self.date)]


if __name__ == '__main__':
    luigi.build([BuildTasks()])
