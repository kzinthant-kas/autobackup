import time
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

seconds_to_wait = int(os.environ["rest_seconds"])

while(True):
  subprocess.call(['sh', './process.sh'])
  time.sleep(seconds_to_wait)
