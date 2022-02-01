import numpy as np
import matplotlib.pyplot as plt

def random_numbers(n):
    '''
    generates random n 0 or 1
    ''' 
    return [np.random.randint(0,2) for _ in range(n)]

def create_lines(val,n):
    '''
    generates an array that contains empty or filled lines for given value and length
    '''
    
    # if the given value is 0, the line starts with empty line and continues with filled line 
    # otherwise, starts with filled line and continues with empty line
    # this process repeats itself
    # to find the number of repeat, we simply find the next even integer (we add 1)
    # because the length of repeating part is 2 and we want to create at least n line
    # then we return the 0th to nth values of repeated list
    # 0 represents the empty line, 1 represents the filled line
    repeat = (n // 2) + 1

    if val == 0:
        return ([0,1]*repeat)[0:n]
    else:
        return ([1,0]*repeat)[0:n]

def random_stack_lines(n,m):
    '''
    creates lines from random numbers for given length and size
    '''

    return [create_lines(i,n) for i in random_numbers(m+1)]

def draw_hline(lines,y,color,ax,write,char):
    # draw a horizontal line
    [ax.plot([i, i + 1],[y,y],color=color) for i,v in enumerate(lines) if v == 1]

    if write == "default":
        ax.text(-1,y,f"{lines[0]}",ha='center', va='center')
    elif write == "chars":
        ax.text(-1,y,f"{char}",ha='center', va='center')

def draw_hlines(random_stack_lines,color,ax,write="default",chars=""):
    # draw horizontal lines
    [draw_hline(line,y,color,ax,write,chars[y]) for y,line in enumerate(random_stack_lines)]

def draw_vline(lines,x,color,ax,write,char):
    # draw a vertical line
    [ax.plot([x,x],[i, i + 1],color=color) for i,v in enumerate(lines) if v == 1]

    if write == "default":
        ax.text(x,-1,f"{lines[0]}",ha='center', va='center')
    elif write == "chars":
        ax.text(x,-1,f"{char}",ha='center', va='center')


def draw_vlines(random_stack_lines,color,ax,write="default",chars=""):
    # draw vertical lines
    [draw_vline(line,x,color,ax,write,chars[x]) for x,line in enumerate(random_stack_lines)]

def convert_vowel(char,ret = 1):
    # takes a character and return ret if it is a vowel
    if char.lower() in ["a","e","i","u"]:
        return ret
    else:
        return not ret

def random_hitomezashi(x,y,colorx="k",colory="k",save=True,file_name="hitomezashi-stitch.png",dpi=120):
    # creates hitomezashi stitch image for given x and y size
    # color is black by default for both vertical and horizontal lines
    # it saves the generated image to hitomezashi-stitch.png in current folder by default
    # the dpi is equal to 120 by default for generating HD images
    fig,ax = plt.subplots()
    ax.set_aspect(y/x)
 
    draw_hlines(random_stack_lines(x,y),colorx,ax)
    draw_vlines(random_stack_lines(y,x),colory,ax)
    plt.axis("off")
    if save:
        plt.savefig(file_name,dpi=dpi)
    plt.show()

def sentence_hitomezashi(sentence1,sentence2,rule,colorx="k",colory="k",save=True,file_name="hitomezashi-stitch.png",dpi=120):
    fig,ax = plt.subplots()
    x,y = len(sentence1), len(sentence2)
    ax.set_aspect(y/x)
    
    if rule == "vowel":
        hstacklines = [create_lines(convert_vowel(char),y-1) for char in sentence1]
        vstacklines = [create_lines(convert_vowel(char),x-1) for char in sentence2]

    draw_hlines(hstacklines,colorx,ax,write="chars",chars=sentence1)
    draw_vlines(vstacklines,colory,ax,write="chars",chars=sentence2)

    plt.axis("off")
    if save:
        plt.savefig(file_name,dpi=dpi)
    plt.show()
