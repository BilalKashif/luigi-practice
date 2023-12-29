import time

import luigi
import pandas as pd


class ExtractData(luigi.Task):
    # This defines the input for the task
    # It's just the wrapper around the requires() function
    task_namespace = 'ExtractDataTask'

    def input(self):
        return luigi.LocalTarget('data/data.txt')

    # Ths method have the business logic of the task
    def run(self):
        # setting task namespace to identify it in callback functions
        # Setting task status to RUNNING
        self.set_tracking_url('http://localhost:8082')
        self.set_status_message('Extracting data...')
        self.set_progress_percentage(50)
        # Just to demonstrate the task takes some time to complete
        time.sleep(10)
        pd.read_json(self.input().path).to_csv(self.output().path, index=False)
        self.set_status_message('Data extracted successfully!')
        self.set_progress_percentage(100)

    def output(self):
        return luigi.LocalTarget('./data/extract.csv')
