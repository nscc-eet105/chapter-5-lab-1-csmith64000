# Chris Smith, Chapter 5 Lab 1, 06/23/25



STATE_TAX_RATE = .051
COUNTY_TAX_RATE = .024  #tax rate is 2.4% not 2.5

def main():
    print('This program will calculate your taxes!\n')

    sale = float(input('How much is the cost of your purchase? '))
    state_tax = calculate_state_tax(sale, STATE_TAX_RATE) #needs state_tax defined
    county_tax = calculate_county_tax(sale , COUNTY_TAX_RATE) # didnt match line22 had sale&countytaxrate in the wrong order
    total_cost = sale + state_tax + county_tax

    print('\nSale amount: $', format(sale, '.2f'), sep = '')
    print('State tax  : $', format(state_tax, '.2f'), sep = '')
    print('County tax : $', format(county_tax, '.2f'), sep = '')
    print('Total cost : $', format(total_cost, '.2f'), sep = '')

def calculate_state_tax(sales_amount, tax_rate):
	return(sales_amount * tax_rate)
	
def calculate_county_tax(amount, rate):
	return(amount * rate) # return instead of taxes=ammount

main()
