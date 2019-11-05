import argparse


def check_correct_input(size_of_flag):
    if isinstance(size_of_flag, int) and size_of_flag > 0 and size_of_flag % 2 == 0:
        return size_of_flag
    raise argparse.ArgumentError(
        None,
        '\n  your input: {} - wrong! entered size shall be: '
        '\n - type \'int\'; \n - number; \n - even.'.format(size_of_flag)
    )


def flag(size_of_flag):
    check_correct_input(size_of_flag)
    flag = []
    hight_flag, width_flag = size_of_flag * 2, size_of_flag * 3

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
                    "#" + (2 * size_of_flag-row) * " " +
                    "*" +  int(row - 1 - int(size_of_flag / 2)) * "oo" +
                    "*" +  (2 * size_of_flag-row) * " " + "#" + "\n"
                )

            elif row > int(hight_flag / 2):
                flag.append(
                    "#" + (row - 1) * " " + "*" +
                    int(hight_flag  - int(size_of_flag / 2)-row) * "oo" +
                    "*" + (row - 1) * " " + "#" + "\n"
                )
    flag = "".join(flag)
    return flag


if __name__ == "__main__":
    #print(flag(int(input("enter size of flag : "))))
    print(flag(2))
    input()
    print(flag(4))
    input()
    print(flag(6))
    input()
    print(flag(8))
    input()
    print(flag("A"))