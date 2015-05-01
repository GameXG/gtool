#!/usr/bin/python
# -*- coding: utf-8 -*-
# utf-8 中文编码

__author__ = 'GameXG'


from flask import Flask, g, request,render_template

app = Flask(__name__)
app.debug = True


def a(b):
    res = u''
    c=b.encode("utf-32le")
    for d in range(len(c)/4):
        e=d*4
        f=''
        h=0
        for g in range(4):
            f+=c[e+g]
            h+=ord(c[e+g]) * 0x100 ** g
        i = f.decode("utf-32le")

        j = i.encode("gb18030",errors = 'ignore')
        l=0
        for k in range(len(j)):
            l += ord(j[k])*(0x100**(len(j)-1-k))

        res+= u"%s\tgb18030:%s\tutf-32le:%s\r\n"%(i,l,h)
    return res

@app.route('/', methods=['GET', 'POST'])
def hello():
    bg=None
    if request.method == 'POST':
        bg = a(request.form['text'])
    return render_template('index.html', bg=bg)
