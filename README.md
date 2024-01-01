# Luigi Practice
## 1. Introduction
In this project a simple pipeline is created using Luigi. The pipeline consists of three tasks:
1. Extracting the data from `data.txt` file in the `data` folder and store it in `extract.csv` file.
2. Transform and load the data in `tranform.csv` file.

**I've added 10seconds delay in the tasks to see the pipeline visualization.**

## 2. Running the pipeline
**Python version 3.12.0**  
First install the dependencies using `requirements.txt` file.
```bash
pip install -r requirements.txt
```
Then run the pipeline using the following command:
```bash
PYTHONPATH='.' luigi --module etl_helper StartETL --local-scheduler
```

### To see the pipeline visualization
First run this command:
```bash
luigid
```
Then open `http://localhost:8082` in your browser.
After that run the previous command without `--local-scheduler` option.  
```bash
PYTHONPATH='.' luigi --module etl_helper StartETL
```
