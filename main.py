last_buffer = []
read_lines = [line.rstrip('\n') for line in open('input.txt', encoding='utf8')]

my_save_data = open("output.txt", "a")


for lines in read_lines:

    re_make_lines = lines.split(".")

    for items in re_make_lines:

        if items.replace(" ", "") == "":
            pass

        else:

            result = items.strip() + ".\n"
            my_save_data.write(result)

my_save_data.close()
