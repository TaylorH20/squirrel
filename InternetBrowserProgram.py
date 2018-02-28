#what do we want the program to do?
#what variables we need?
#how are we going to do it?

#open up a series of web pages.

#we need a list of urls that we need to open.

#open a web page.

#open up a series of tabs.


import webbrowser
import time
socialMediaUrls = ['http://binance.com', 'http://bittrex.com/Market/Index?MarketName=BTC-VEE', 'http://afternic.com', 'http://namebio.com', 'http://www.kucoin.com/#/trade.pro/CV-BTC', 'http://www.bitstamp.net/market/tradeview/', 'http://www.youtube.com/watch?v=F8bxkV0Gl_4', 'http://poloniex.com/marginTrading#btc_ltc', 'http://www.tradingview.com/chart/NVajtlr0/', 'http://www.tradingview.com/chart/NVajtlr0/', 'http://www.tradingview.com/chart/NVajtlr0/']


def open_tabs(url_list):
    for element in url_list:
        webbrowser.open_new_tab(element)


def main():
    webbrowser.open("www.youtube.com", new=0, autoraise=False)
    time.sleep(1)
    open_tabs(socialMediaUrls)

main()
