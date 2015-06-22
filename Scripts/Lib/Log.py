

ERROR = "ERROR"
WARNING = "WARNING"
INFO = "Info"
DEBUG = "Debug"
VERBOSE = "    "

log_levels = [ERROR, WARNING]

def Log(level, msg):
    global log_levels
    if level in log_levels:
        print(level + ": " + msg)
    return 0

def SetLevels(levels):
    global log_levels
    log_levels = levels
    return 0