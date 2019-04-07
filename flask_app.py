from flask import Flask, render_template, redirect, request, session

import pandas as pd

app = Flask(__name__)
@app.route('', methods=['GET', 'POST'])


def index(display=)
    # Assign filename to variable data_file, order_file
    data_file = 'data.txt'
    #order_file = 'input.txt'
    # Import data from file to Pandas DataFrames
    data = pd.read_csv(data_file, sep=,, header=None)
    order =  #pd.read_csv(order_file, sep=t, header=None)
    # Convert order DataFrame into List
    order = #order.values.tolist()


    if request.method == 'POST'

        product_ord = request.form.get('product')
        quantity_ord= request.form.get('quantity')
        display= order_traitment(product_ord,quantity_ord, data)
    print(display)
    return render_template('index.html', order=display)

def order_traitment(product_ord,quantity_ord, data)
    Initiate order traitment
        order List
        data Pandas DataFrame
        return None

        Loop on the different orders, check error and launch the repartition function for each order.
        Finally launch the print_order_result function
    
    product_ordered = product_ord
    quantity_ordered = quantity_ord
    # Extract only pack available about the product_ordered
    pack = data.loc[data[1] == product_ordered][2].tolist()
    # Error check
    error=correct_order(pack, quantity_ordered,product_ordered)
    if error[1]
        quantity_ordered=int(quantity_ordered)
        # Get the best pack repartition for as minimum pack as possible
        repartition_res = repartition(pack, quantity_ordered)
        repartition_res = repartition_res[0]
        # Print order result
        return print_order_result(data, pack, repartition_res, product_ordered, quantity_ordered)
    else
        return error[0]


def print_order_result(data, pack, repartition_res, product_ordered, quantity_ordered)
    Print order repartition
        data Pandas DataFrame
        pack List
        repartition_res List
        product_ordered String
        quantity_ordered Int
        return None

        Display in the Bakery's order repartition to sell for each order.
        Display also the price per pack and the total price
    
    # Extract only prices about the product_ordered
    display = 
    prices = data.loc[data[1] == product_ordered][3].tolist()
    # Extract teh full name of the product_ordered (code)
    product_ordered_full_name = data.loc[data[1] == product_ordered][0].tolist()
    # Display full product name and the total ordered quantity
    display = display + Bakery order  + str(product_ordered_full_name[0]) +    + str(quantity_ordered)
    display = display + ' br '
    # Initiate empty list quantity_per_pack and price_per_pack
    quantity_per_pack = [0]  len(pack)
    price_per_pack = [0]  len(pack)
    # Double loop on repartition and pack.
    # To update quantity_per_pack and price_per_pack
    for r_index in range(len(repartition_res))
        for p_index in range(len(pack))
            if repartition_res[r_index] == pack[p_index]
                quantity_per_pack[p_index] = quantity_per_pack[p_index] + 1
                price_per_pack[p_index] = price_per_pack[p_index] + prices[p_index]
    # Display each pack and prices
    for i in range(len(quantity_per_pack))
        display = display + Pack of  + str(pack[i]) +    + str(quantity_per_pack[i]) +  =  + str(price_per_pack[i]) + $
        display = display + ' br '
    total_price = round(sum(price_per_pack), 2)
    # Display total order price
    display = display + Total  + str(total_price) + $
    # Display possible error when none repartition are available for the quantity ordered
    if total_price == 0
        display = display + This order can't be process Impossible to create a pack
    display = display + ' br '
    return display


def repartition(packs, quantity_ordered)
    repartitionn
        packs List
        quantity_ordered Int
        return List

        Find out and return the minimum used pack repartition for quantity ordered
        and for a finite available pack
    
    # Result contain [0] added pack list [1] Wrong path Flag
    result = [[], False]
    # Temporary Result
    result_temp = []
    # Temporary Pack
    pack_temp = -1
    # Loop on available pack
    for pack in packs
        # Exact pack for the desired quantity available
        # Recursion stop condition.
        if pack == quantity_ordered
            result[0].append(pack)
            result[1] = True
            # Loop Break
            break
        # if the pack fit, recursion launched
        # Recursion decreasing criteria
        elif pack  quantity_ordered
            recursive_result = repartition(packs, quantity_ordered - pack)
            # Only if recursion_result's wrong path flag not set
            if recursive_result[1] != False
                # Compare best repartition
                if not result_temp or len(result_temp)  len(recursive_result[0])
                    result_temp = recursive_result[0]
                    pack_temp = pack
            else
                # Wrong path
                result = [[], False]
        else
            # Wrong path
            result = [[], False]
    #Good path
    if pack_temp != -1
        result_temp.append(pack_temp)
        result[0] = result_temp
        # Good path
        result[1] = True
    return result

def correct_order(pack,quantity_ordered,product_ordered)
    correct_order
        packs List
        quantity_ordered Int
        product_ordered String
        return List

        Error checking
        The product  does not exist.
        Ordered quantity not valid (0)
    
    display=
    if str.isdigit(quantity_ordered)==False
        display = This order can't be process Ordered quantity is not numeric.
        return [display,False]
    elif int(quantity_ordered)  0
        display = This order can't be process Ordered quantity not valid (0).
        display = display + ' br '
        return [display,False]
    elif len(pack) == 0
        display = This order can't be process The product  + product_ordered +  does not exist.
        display = display + ' br '
        return [display,False]
    return [display,True]



if __name__ == '__main__'
    app.run()