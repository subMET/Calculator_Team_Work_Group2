import datetime

def create_file():
    file = open('log.txt','w')
    now = datetime.datetime.now()
    file.write(f'File created: {str(now)} \n')
    file.close()

def add_record(data):
    file = open('log.txt','a')
    now = datetime.datetime.now()
    file.write(f'{data} : {str(now)} \n')
    file.close()
