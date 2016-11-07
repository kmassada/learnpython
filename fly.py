count = 0


def fly(interest_rate, monthly_payment, count):
    if count >= (264):
        print(count)
        return monthly_payment
    else:
        count += 1
        return fly(interest_rate,
                                 (interest_rate*monthly_payment) + monthly_payment,
                                 count)

# one = fly(0.05, 260.0, 0)
two = fly(0.03, 185.0,0)

# print(one)
print(two)
