import datetime
import platform

def log(msg):
    
    cur_sys = platform.system()   # cur_sys = ['Windows', 'Linux', etc.]
    if cur_sys == 'Windows':
        logfile = 'D:/research/Logs/ExecutionLog/embermd.txt'
    elif cur_sys == 'Linux':
        logfile = '/home/mira/research/Logs/ExecutionLog/embermd.txt'
    else:
        raise RuntimeError('unknown system')

    curtime = str(datetime.datetime.now())
    with open(logfile, "a") as f:    
        f.write("\n\n")
        f.write("[time: {}]".format(curtime))
        f.write("\n")
        f.write("message: " + msg)

def get_research_dataset_dir():
    cur_sys = platform.system()   # cur_sys = ['Windows', 'Linux', etc.]
    if cur_sys == 'Windows':
        return 'D:/research/dataset'
    elif cur_sys == 'Linux':
        return '/home/mira/research/dataset'
    else:
        raise RuntimeError('unknown system')
