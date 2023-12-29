import time

import luigi
import pandas as pd

from extract import ExtractData


class TransformAndLoad(luigi.Task):

    task_namespace = 'TransformTask'

    def requires(self):
        return ExtractData()

    def input(self):
        return luigi.LocalTarget('data/extract.csv')

    def run(self):
        # Setting task status to RUNNING
        self.set_tracking_url('http://localhost:8082')
        self.set_status_message('Transforming the data...')
        self.set_progress_percentage(50)
        # Just to demonstrate the task takes some time to complete
        time.sleep(10)
        df = pd.read_csv(self.input().path)
        # Dropping one column from the data (Transforming the data)
        df.drop(['id'], axis=1, inplace=True)
        # Hare I'm loading the transformed data into a csv file
        # But in real world scenario you will load the data into a database
        df.to_csv(self.output().path, index=False)
        self.set_status_message('Data transformed and loaded successfully!')
        self.set_progress_percentage(100)

    def output(self):
        return luigi.LocalTarget('./data/transform.csv')


