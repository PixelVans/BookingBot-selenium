from booking.booking import Booking

try
    with Booking() as bot:
        bot.land_first_page()
        bot.close_modal_if_present()
        bot.change_currency(currency='USD')
        bot.close_modal_if_present()
        bot.select_place_to_go(input("Enter your destination"))
        bot.select_dates(check_in_date=input("Enter your check in date in this format: YYY-MM-DD >"),
                         check_out_date=input("Enter your check out date in this format: YYY-MM-DD >"))
        bot.select_adults(input("Enter the number of people >"))
        bot.click_search()
        bot.close_modal_if_present()
        bot.apply_filtrations()
        
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
  


