import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template


app=Flask(__name__)

@app.route('/')
def show_entries():

    res=requests.get('http://dispatch.dti.ad.jp/cgi-bin/isys/dispatch.cgi/isys-req')
    #res.encoding='EUC-JP'
    soup=BeautifulSoup(res.text,'html.parser')
    #entries=soup.select('a')[0].get_text()
    entries=[]
    for news in soup.select('a'):
        entries.append(news.get_text())

    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)