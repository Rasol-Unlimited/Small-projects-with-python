def ask_count_num():
    numbercount = int(input("che tedad adad ra mikhahid ba ham jam konid? "))
    if numbercount <= 0:
        print("adad balatar az 0 vared konid.")
        ask_count_num()
        return
    count = 0
    total_sum = 0
    while count != numbercount :
        number = int(input(f"adad {count+1} ra vared konid: "))
        total_sum += number
        count += 1
    
    print(f"majmo adad barabar ba {total_sum} mibashad.")

ask_count_num()