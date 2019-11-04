def flag(size_of_flag):
    flag = []
    hight_flag, width_flag = size_of_flag * 2, size_of_flag * 3
    print(hight_flag, width_flag, size_of_flag)
    for row in range(hight_flag + 2):
        if row == 0 or row == hight_flag + 1:
            flag.append("#" + width_flag * "#" + "#" + "\n")
        elif  row <= size_of_flag / 2 or size_of_flag * (3 / 2) + 1 <= row <= hight_flag + 1 :
            flag.append("#" + width_flag * " " + "#" + "\n")
        elif row == 1 + size_of_flag / 2 or row == hight_flag  - size_of_flag / 2:
            flag.append(
                "#" + (int(width_flag / 2) - 1) * " " + "**" + (int(width_flag / 2) - 1) * " " + "#" + "\n"
            )
        else:
            if row < int(hight_flag / 2 + 1):
                flag.append(
                    "#" + (2*size_of_flag-row) * " " + "*" +  int((row - 1 - int(size_of_flag/2))) * "oo" + "*" +  (2*size_of_flag-row) * " " + "#" + "\n"
                )
            elif row > int(hight_flag / 2):
                flag.append(
                    "#" + (row-1 ) * " " + "*" + int((hight_flag  - int(size_of_flag/2)-row) ) * "oo" + "*" + (row-1 ) * " " + "#" + "\n"
                )

    flag = "".join(flag)
    return flag

if __name__ == "__main__":
    print(flag(2))
    print(flag(4))
    print(flag(6))
    print(flag(8))
    print(flag(10))