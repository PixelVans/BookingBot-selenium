from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.close_modal_if_present()
    bot.change_currency(currency='USD')
    bot.close_modal_if_present()
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2025-02-22',
                     check_out_date='2025-02-26')
    bot.select_adults(4)
    bot.click_search()
    bot.close_modal_if_present()
    bot.apply_filtrations()
  
