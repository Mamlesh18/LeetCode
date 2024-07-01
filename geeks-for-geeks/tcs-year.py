def leap256(year):

    if year % 4 == 0:
        return "12.09."+ "".join(str(year))
    else:
        return "13.09."+ "".join(str(year))
year = int(input("yaer =  "))
print(leap256(year))