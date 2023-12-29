import luigi

from transform_and_load import TransformAndLoad


class StartETL(luigi.Task):

    def requires(self):
        return TransformAndLoad()

    def run(self):
        # Setting task status to RUNNING
        self.set_status_message('ETL process started...')
        pass

    def output(self):
        return luigi.LocalTarget('./data/transform.csv')

    # These methods run every time any task is completed without any error
    @luigi.Task.event_handler(luigi.Event.SUCCESS)
    def task_successful_callback(self):
        # You can check call back against the task using its namespace
        # if ExtractData.task_namespace == self.task_namespace: (Like this you can check)
        print("Task Successful!")
        print("Task name:{}".format(self.task_namespace))

    # This method runs every time any task is failed
    @luigi.Task.event_handler(luigi.Event.FAILURE)
    def task_failed_callback(self, exception):
        print('Task failed!', exception)
        print("Task name:{}".format(self.task_namespace))
