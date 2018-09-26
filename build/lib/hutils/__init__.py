import datetime


def log(msg, logfile):
    curtime = str(datetime.datetime.now())
    with open(logfile, "a") as f:    
        f.write("\n\n")
        f.write("[time: {}]".format(curtime))
        f.write("\n")
        f.write("message: " + msg)
