def ask_and_sum():
    """
    This function asks the user for two numbrts, converts them to floats, and prints their sum.
    """
    num1 = int(input("Adad aval ra vared konid: "))
    num2 = int(input("Adad dovom ra vared konid: "))
    sum = num1 + num2
    return(f"majmo adad {num1} va {num2} barabar ba {sum} mibashad.")

print(ask_and_sum())