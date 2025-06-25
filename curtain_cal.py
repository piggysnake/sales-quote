import math

def price(w, h, x):
    y = 0;
    m = 0;
    extra = 0;
    
    if x == 's':
        y = math.ceil((w * 2.5)/2.8)
    if x == 'p':
        y = math.ceil((w*2.2)/2.8)

    if 3<=h<= 4:
        extra = 100
        
    elif 4 < h <= 5:
        extra = 200
        
    elif h > 5:
        extra = 300

    m = y*(h + 0.3)
    price = math.floor(m*90+extra)
    
    return price

def sheer_s(w,h):
    mini = 0;
    maxi = math.floor(w*2.5*90)
    if h <= 3:
        if w <=3:
            mini = 450;
        elif 3 < w <= 4:
            mini = 650
        elif 4 < w <= 6:
            mini = 900  
    
    return f"{mini} ~ {maxi}"

def sheer_p(w,h):
    mini = 0;
    maxi = math.floor(w*2.2*90)
    if h <= 3:
        if w <=3:
            mini = 450;
        elif 3 < w <= 4:
            mini = 650
        elif 4 < w <= 6:
            mini = 900  
    
    return f"{mini} ~ {maxi}"
        
def roller(w, h):
    if w <= 1.0:
        w = 1
    if h <= 1.0:
        h = 1
    
    price = math.floor(w*h*110)
    return price

def shutter_f(w, h):
    return math.floor(w*h*380)

def shutter_n(w,h):
    return math.floor(w*h*580)


def curtain_p(w,h):
    mini = math.floor(w*2.2*110)
    medi = math.floor(w*2.2*120)
    maxi = math.floor(w*2.2*130)
    return f"{mini} ,{medi}, {maxi}"

def curtain_s(w,h):
    mini = math.floor(w*2.5*110)
    medi = math.floor(w*2.5*120)
    maxi = math.floor(w*2.5*130)
    return f"{mini} ,{medi}, {maxi}"
    
    
