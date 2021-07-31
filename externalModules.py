def isitanint(x):
    try:
        int(x)
    except ValueError:
        return False
    return True

def severityCheck(x):
    if(x > 0 or x <= 3):
        return True
    else:
        return False