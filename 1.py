import os
import datetime
import time
import shutil

if os.path.exists('./newfolder'):
    shutil.rmtree('newfolder')
os.mkdir('newfolder')
os.chdir('./newfolder')

for i in range(10):
    time_now = datetime.datetime.now()
    time_now_f = time_now.strftime('%H%M%S')
    f = open(f'report {time_now_f}.txt', 'w')
    f.close()
    time.sleep(2)

