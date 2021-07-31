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

def subEventWeight(x):
    if(x == 'Low'):
        return 0.5
    elif(x == 'High'):
        return 1.5
    elif(x == 'exceededLimit'):
        return 2
    else:
        return 1