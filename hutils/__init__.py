import datetime


def log(msg, logfile):
    f = open(logfile, "a")
    curtime = str(datetime.datetime.now())
    f.write(curtime)
    f.write("    ")
    f.write(msg) 
    f.write("\n")
    f.close()
