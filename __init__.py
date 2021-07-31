import h2o
import logging
import psutil
import optparse
import time
from distutils.util import strtobool
from datetime import datetime
import random, sys

def __init__(self, csv_path):
    self.csv_path = csv_path

    # Set a minimum memory size and a run time in seconds
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
