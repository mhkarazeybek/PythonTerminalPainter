reset = '\033[0m'
style = {
    'bold': '\033[01m',
    'disable': '\033[02m',
    'underline': '\033[04m',
    'reverse': '\033[07m',
    'strikethrough': '\033[09m',
    'invisible': '\033[08m',
    '':''
}

fgColors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'orange': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'lgrey': '\033[37m',
    'dgrey': '\033[90m',
    'lred': '\033[91m',
    'lgreen': '\033[92m',
    'yellow': '\033[93m',
    'lblue': '\033[94m',
    'pink': '\033[95m',
    'lcyan': '\033[96m',
    'white': '',
    '': '',
}

bgColors = {
    'black': '\033[40m',
    'red': '\033[41m',
    'green': '\033[42m',
    'orange': '\033[43m',
    'blue': '\033[44m',
    'purple': '\033[45m',
    'cyan': '\033[46m',
    'lgrey': '\033[47m',
    '': ''
}


def painter(text, color: str = '', styles: list = [], backgroundColor: str = ''):
    """Description of this function's params
    color (str) in ['black', 'red', 'green', 'orange', 'blue', 'purple', 'cyan', 'lgrey', 'dgrey', 'lred', 'lgreen', 'yellow', 'lblue', 'pink', 'lcyan'] (Default = 'white'),
    backgroundColor (str) in ['black', 'red', 'green', 'orange', 'blue', 'purple', 'cyan', 'lgrey'],
    styles (list) in ['bold', 'disable', 'underline', 'reverse', 'strikethrough', 'invisible']"""
    print(f"{bgColors.get(backgroundColor,'')}{fgColors.get(color,'')}{''.join([style.get(i,'') for i in styles])}{text}{reset*2}{reset*len(styles)}")
