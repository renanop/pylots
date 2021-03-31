def output_print(q, t, number_of_cycles, total_cost, product_cost, fixed_cost, holding_cost):

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