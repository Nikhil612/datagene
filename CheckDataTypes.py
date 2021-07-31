import pandas as pd
import base64
import numpy as np
import h2o
import logging
import psutil
import random
import sys
from pandas.api.types import is_numeric_dtype
from pandas.api.types import CategoricalDtype
from pandas.api.types import is_object_dtype

class DataGene():

    def __init__(self, csv_path):
        self.csv_path = csv_path

        if h2o.init(start_h2o=True):
            # continue
            # Set a minimum memory size and a run time in seconds
            # def ActivateH2O():
            min_mem_size = 6
            run_time = 222

            # Use 50% of availible resources
            pct_memory = 0.5
            virtual_memory = psutil.virtual_memory()
            min_mem_size = int(round(int(pct_memory * virtual_memory.available) / 1073741824, 0))
            print(min_mem_size)

            # 65535 Highest port no
            # Start the H2O server on a random port
            port_no = random.randint(5555, 55555)

            #  h2o.init(strict_version_check=False,min_mem_size_GB=min_mem_size,port=port_no) # start h2o
            try:
                h2o.init(strict_version_check=False, min_mem_size_GB=min_mem_size, port=port_no)  # start h2o
            except:
                logging.critical('h2o.init')
                h2o.download_all_logs(dirname=logs_path, filename=logfile)
                h2o.cluster().shutdown()
                sys.exit(2)

    def checkDtype(csv_path):

        df = pd.read_csv(csv_path)
        numeric_columns = []
        column_index = []
        non_numeric_columns = []
        object_columns = []
        column_index2 = []
        column_index1 = []
        for column in df.columns:
          if is_numeric_dtype(df[column].dtype) == True:
              numeric_columns.append(column)
              column_index.append(df.columns.get_loc(column))
          elif is_object_dtype(df[column].dtype) == True:
              object_columns.append(column)
              column_index2.append(df.columns.get_loc(column))
          else:
              non_numeric_columns.append(column)
              column_index1.append(df.columns.get_loc(column))

        print(numeric_columns)
        print(object_columns)
        print(non_numeric_columns)


        RealData = df[numeric_columns]

        # function that takes in a dataframe and creates a text link to
        # download it (will only work for files < 2MB or so)
        csv = RealData.to_csv()
        b64 = base64.b64encode(csv.encode())
        payload = b64.decode()
        html = '<a download="{filename}" href="data:text/csv;base64,{payload}" target="_blank">{title}</a>'
        html = html.format(payload=payload,title="Download CSV file",filename="RealData.csv")
        return HTML(html)
