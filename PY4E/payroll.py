def computepay (h, r):
    hours = float(h)
    rate = float(r)
    if hours <=40:
        grosspay = hours * rate
        print(grosspay)
    elif hours > 40:
        regularhrs = 40
        otimerate = 1.5 * rate
        otimehrs = hours - regularhrs
        otimepay = otimehrs * otimerate
        grosspay = regularhrs*rate + otimepay
    #print (grosspay)

    return grosspay

hrs = input("Enter Hours:")
rte = input("Enter rate:")
p = computepay(hrs, rte)
print("Pay", p)
