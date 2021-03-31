import math

def no_shortage_eoq(CS, K, D, T = 1, CM = None, I = None, warehousing = None, output = True, model = 'basic'):
    """A function that calculates the economic order quantity (EOQ) model optimal decision variables. It assumes that shortages of supply are not allowed.
    
    It returns a dictionary that contains the optimal lot size, the duration of the cicle between orders, the total cost given the time frame, the cost of the products 
    (e.g. variable cost due to purchased produtcs), the fixed costs (e.g. shipping costs) and the holding costs (e.g. insurance costs, maintenance, etc.). 
    Notice that the value of the time period demand (D) should be provided in respect of the time period T.

    TODO
    Adjust example testing
    no_shortage_eoq(CS=19, CM=1, K = 5, D=2400, output = False, model = 'basic')
    {'lotsize': 301.99337741082996, 'cycle time': 0.12583057392117916, 'total cost': 12301.993377410829, 'product cost': 12000, 'fixed cost': 150.996688705415, 'holding cost': 150.99668870541498, 'number of cycles': 7.947194142390264}        
    
    Args:
        cs (float): Fixed cost per order, or the setup cost. Typically the cost of ordering, shipping and handling, or the costs of preparing a machine
        cm (float): Holding cost per unit - Capital cost, insurance, maintenance, security, etc.
        k (float): Purchase price or production cost
        D (float): Total demand of the product, given a time frame. It must be on the same time unit as the 
        T (integer): A timeframe related to the operational cycle. Standard value is 1, for the case of planning for 1 year
        model (string): Type of model - At this type, the supported models are:
            'basic'- which assumes constant holding costs, 
            'var-holding' - which assumes holding costs proportional to the interest rate, unit fixed costs and purchase price (k).
            'var-holding-2' - which assumes holding costs proportional to the interest rate and purchase price (k) 
    """

    try:

        if model == 'basic' or model == 1:  
            q = math.sqrt(2 * CS * D/(CM * T))
            holding_cost = CM * T * q/2

        elif model == 'var-holding' or model == 2:  
            q = math.sqrt(2 * CS * D/(K * I * T))
            unit_holding_cost = (CS/q + K) * I
            holding_cost = unit_holding_cost * T * q/2

        elif model == 'var-holding-warehousing' or model == 3:
            q = math.sqrt(CS * D/((K * I * T)/2 + warehousing))
            unit_holding_cost = (CS/q + K) * I
            holding_cost = unit_holding_cost * T * q/2

        t = T*q/D
        product_cost = K*D
        number_of_cycles = D/q
        fixed_cost = CS * number_of_cycles

        if not warehousing:
            total_cost = product_cost + fixed_cost + holding_cost
            summary = {
            'lotsize': q,
            'cycle time': t,
            'total cost': total_cost,
            'product cost': product_cost,
            'fixed cost': fixed_cost,
            'holding cost': holding_cost,
            'number of cycles': number_of_cycles
        }
        else:
            warehousing_cost = warehousing * q
            total_cost = product_cost + fixed_cost + holding_cost + warehousing_cost
            summary = {
            'lotsize': q,
            'cycle time': t,
            'total cost': total_cost,
            'product cost': product_cost,
            'fixed cost': fixed_cost,
            'holding cost': holding_cost,
            'number of cycles': number_of_cycles,
            'warehousing cost': warehousing_cost
        }

        
        if output:
            print("---------------MODEL SUCCESSFULLY ATTAINED!---------------\n")
            print("**Model summary**:\n")
            print(f"Optimal lot size: {q} units")
            print(f"Cycle length: {t} time units")
            print(f"Number of cycles: {number_of_cycles} cycles")
            print(f"Total cost: {total_cost} units of the currency")
            print()
            print("The total cost is composed by the following cost drivers:")
            print(f"---> product cost: {product_cost}")
            print(f"---> fixed cost: {fixed_cost}")
            print(f"---> holding cost: {holding_cost}")


        return summary

    except:

        print("Bad parameters. Please provide the necessary parameters to the model.")
        return None
 

# print(no_shortage_eoq(CS=19, CM=1, K = 5, D=2400, output = False, model = 'basic')) -> Teste do exercicio do exemplo do modelo basico apostila virgilio
# print(no_shortage_eoq(CS = 25, K = 100, D = 800, I = 0.12, warehousing=1.5, model = 'var-holding-warehousing')) -> Ex resolvido R 3.1 da secao 3.7 da apostila


if __name__ == "__main__":
    import doctest
    doctest.testmod()

 

"""
TODO
1 - Create print_output() function
2 - Adjust docstring testing (discover why is it bugging)
3 - Start supply_shortage_eoq model
"""