def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)
# 2
def get_size(w,h,d):
    return [2*h*w+2*h*d+2*w*d, w*h*d]
# 3
def get_min_max(seq): 
    min=seq[0]
    max=seq[0]
    for i in seq:
        if i>max:
            max=i
        if i<min:
            min=i
    return (min,max)
