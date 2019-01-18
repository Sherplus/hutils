import datetime
import platform

class Utils:
    def __init__(self, logfile=None):
        if logfile == None:
            cur_sys = platform.system()   # cur_sys = ['Windows', 'Linux', etc.]
            if cur_sys == 'Windows':
                self.logfile = 'D:\\research\\Logs\\ExecutionLog\\embermd.txt'
            elif cur_sys == 'Linux':
                self.logfile = '/home/mira/research/Logs/ExecutionLog/embermd.txt'
            else:
                raise RuntimeError('unknown system')
        else:
            self.logfile = logfile

    def set_logfile(self, new_logfile):
        self.logfile = new_logfile

    def log(self, msg, printt=True):
        if printt:
            print(msg)
        curtime = str(datetime.datetime.now())
        with open(self.logfile, "a") as f:    
            f.write("\n\n")
            f.write("[time: {}]".format(curtime))
            f.write("\n")
            f.write("message: " + msg)

    def get_research_dataset_dir(self):
        cur_sys = platform.system()   # cur_sys = ['Windows', 'Linux', etc.]
        if cur_sys == 'Windows':
            return 'D:\\research\\dataset'
        elif cur_sys == 'Linux':
            return '/home/mira/research/dataset'
        else:
            raise RuntimeError('unknown system')
