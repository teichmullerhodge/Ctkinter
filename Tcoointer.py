#gui that reads the user input and gives data about a given currency

import requests
import json
import customtkinter
import tkinter
import random
import time
import locale


from CTkColorPicker import *
from bs4 import BeautifulSoup
from PIL import Image



bar_list = []
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # USA USA USA 


def set_progress_color_value(value, progressbar):

    max_value = 0
    min_value = float('inf') # I was using sys.maxsize, yeah i'm drunk.
    for values in bar_list:

        if values > max_value:
            max_value = values
        if values < min_value: #i'm sure they are
            min_value = values


    if value == max_value:
        progressbar.configure(progress_color='green')
        progressbar.set(1)
    elif value == min_value:
        progressbar.configure(progress_color='red')
        progressbar.set(0.33)
    else:
        progressbar.configure(progress_color='#ff6c00')
        progressbar.set(0.66)






def get_price(coin):

    url = f'https://www.google.com/finance/quote/{coin}-USD'

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        div_element = soup.find('div', class_='YMlKec fxKbKc') #THE CLASS THAT GIVES THE PRICEEEEEEEEEEE
        #print(soup) off course you don't want to print this.


        if div_element: 
            
            value = div_element.text
            cprice_label.configure(text=f'${value}')




def get_crypto_info(coinsymbols): #This function returns data about market cap and percentage changes 
                                    #the coinsymbols must be a string like: 'BTC,ETH,XMR,ADA' containing the symbols of the coins

    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

    parameters = {

    'symbol' : coinsymbols,
    'convert' : 'USD'
}

    headers = {

    'Accepts' : 'application/json',
    'X-CMC_PRO_API_KEY' : 'NOT GIVING YOU THIS'
}

    response = requests.get(url, params=parameters, headers=headers)

    symbols = parameters['symbol'].split(',')

    if response.status_code == 200:
        
        data = response.json()
    
        for sym in symbols:
    
            sym_data = data['data'][sym][0]['quote']['USD']
            sym_price = sym_data['price']
            sym_market_cap = sym_data['market_cap']
            sym_total_supply = data['data'][sym][0]['total_supply']
            sym_percent_change_7d = sym_data['percent_change_7d']
            sym_percent_change_30d = sym_data['percent_change_30d']


            formatted_market_cap = locale.currency(sym_market_cap, grouping=True)
            formatted_price = locale.currency(sym_price, grouping=True)


            week_change_value = sym_price - (sym_percent_change_7d / 100) * sym_price
            month_change_value = sym_price - (sym_percent_change_30d / 100) * sym_price

            formatted_price_week = locale.currency(week_change_value, grouping=True)
            formatted_price_month = locale.currency(month_change_value, grouping=True)




            cprice_label.configure(text=f'{formatted_price}')
            market_cap_label.configure(text=f'{formatted_market_cap}', text_color='blue')

            print(f"PRICES: {sym_price}, {week_change_value}, {month_change_value}")

            bar_list.append(sym_price)
            bar_list.append(week_change_value)
            bar_list.append(month_change_value)

            set_progress_color_value(sym_price, cvalue_progressbar)
            set_progress_color_value(week_change_value, week_value_progressbar)
            set_progress_color_value(month_change_value, month_value_progressbar)

            del bar_list[:]

            if sym_percent_change_7d < 0:
                sym_percent_change_7d_ns = str(sym_percent_change_7d)
                sym_percent_change_7d_ns = sym_percent_change_7d_ns.replace("-", "")
                sym_percent_change_7d_ns = float(sym_percent_change_7d_ns)
                week_percentage.configure(text=f'+{sym_percent_change_7d_ns:.2f}', text_color='green')
            else:
                week_percentage.configure(text=f'-{sym_percent_change_7d:.2f}', text_color='red')


            if sym_percent_change_30d < 0:
                sym_percent_change_30d_ns = str(sym_percent_change_30d)
                sym_percent_change_30d_ns = sym_percent_change_30d_ns.replace("-", "")
                sym_percent_change_30d_ns = float(sym_percent_change_30d_ns)
                month_percentage.configure(text=f'+{sym_percent_change_30d_ns:.2f}', text_color='green')
            else:
                month_percentage.configure(text=f'-{sym_percent_change_30d:.2f}', text_color='red')



    

    else:
        print(f"Failed with status code: {response.status_code}")

#window configuration

app = customtkinter.CTk()
app.title("Tkoointer")
app.geometry('450x600')
app.configure(fg_color='#ffffff')

#Images used in the buttons


theme_image = customtkinter.CTkImage(Image.open('theme.jpg'), size=(26,26))
reload_image = customtkinter.CTkImage(Image.open('reload.png'), size=(20,20))
btc_image = customtkinter.CTkImage(Image.open('btc.png'), size=(26,26))
eth_image = customtkinter.CTkImage(Image.open('eth.png'), size=(26,26))
tron_image = customtkinter.CTkImage(Image.open('tron.png'), size=(26,26))
brl_usa_image = customtkinter.CTkImage(Image.open('euabr.png'), size=(20,20))


#Widgets



sample_btc_button = customtkinter.CTkButton(app, width=21, text='', image=btc_image, fg_color='white', hover_color='#f5f5f5')
sample_btc_button.grid(row=0, column=0, sticky='w', padx=10)

sample_eth_button = customtkinter.CTkButton(app, width=21, text='', image=eth_image, fg_color='white', hover_color='#f5f5f5')
sample_eth_button.grid(row=0, column=0)

sample_tron_button = customtkinter.CTkButton(app, width=21, text='', image=tron_image, fg_color='white', hover_color='#f5f5f5')
sample_tron_button.grid(row=0, column=0, sticky='e')




price_info = customtkinter.CTkLabel(app, text="Value", font=('Ubuntu Mono', 15))
price_info.grid(row=0, column=1, padx=10)


week_info = customtkinter.CTkLabel(app, text="%7d", font=('Ubuntu Mono', 15))
week_info.grid(row=0, column=2, padx=10)


month_info = customtkinter.CTkLabel(app, text="%30d", font=('Ubuntu Mono', 15))
month_info.grid(row=0, column=3, padx=10)



market_cap_info = customtkinter.CTkLabel(app, text="Market cap", font=('Ubuntu Mono', 15))
market_cap_info.grid(row=0, column=4, padx=10)



cprice_label = customtkinter.CTkLabel(app, text='PRICE', font=('Ubuntu Mono', 25), text_color='green')
cprice_label.grid(row=1, column=1, padx=10)



week_percentage = customtkinter.CTkLabel(app, text='%7D', font=('Ubuntu Mono', 15))
week_percentage.grid(row=1, column=2, padx=10)



month_percentage = customtkinter.CTkLabel(app, text='%30D', font=('Ubuntu Mono', 15))
month_percentage.grid(row=1, column=3, padx=10)


market_cap_label = customtkinter.CTkLabel(app, text="$$$", font=('Ubuntu Mono', 15))
market_cap_label.grid(row=1, column=4, padx=10)


type_label = customtkinter.CTkLabel(app, text='Type the currency')
type_label.grid(row=1, column=0)

currency_entry = customtkinter.CTkEntry(app)
currency_entry.grid(row=2, column=0, padx=10, sticky='n')


request_button = customtkinter.CTkButton(app, text='Get coin data', fg_color='#ff6c00', command=lambda: get_crypto_info(currency_entry.get()))
request_button.grid(row=2, column=0, padx=10, sticky='n', pady=35)



refresh_button = customtkinter.CTkButton(app, text="", image=reload_image, command=lambda: get_price(currency_entry.get()), width=5, fg_color='white')
refresh_button.grid(row=2, column=0, padx=10, sticky='n', pady=70)




cvalue_progressbar = customtkinter.CTkProgressBar(app, progress_color='#ff6c00', orientation='vertical', width=20, fg_color='#ffffff')
cvalue_progressbar.grid(row=2, column=1, padx=10)

clabel = customtkinter.CTkLabel(app, text='current')
clabel.grid(row=3, column=1, padx=10)

week_value_progressbar = customtkinter.CTkProgressBar(app, progress_color='#ff6c00', orientation='vertical', width=20, fg_color='#ffffff')
week_value_progressbar.grid(row=2, column=2) #middle bar

wlabel = customtkinter.CTkLabel(app, text='7d')
wlabel.grid(row=3, column=2)

month_value_progressbar = customtkinter.CTkProgressBar(app, progress_color='#ff6c00', orientation='vertical', width=20, fg_color='#ffffff')
month_value_progressbar.grid(row=2, column=3)


monthlabel = customtkinter.CTkLabel(app, text='30d')
monthlabel.grid(row=3, column=3, sticky='e')

get_crypto_info('BTC') #DEFAULT CRYPTO

#I HOPE YOU HAVE THE IMAGE FILES, CAUSE IF YOU DON'T THEM JUST ERASE THE LINES.
#I'M GOING TO ADD AN app.after() line to read data from time to time 

app.mainloop()
