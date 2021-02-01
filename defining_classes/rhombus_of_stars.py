def draw_a_rhombus_first_half(n):
    stars_count = 1
    for space in range(n-1, -1, -1):
        print(" " * space + "* " * stars_count)
        stars_count += 1
    stars_count = n-1
    for space in range(1, n):
        print(" " * space + "* " * stars_count)
        stars_count -= 1


n = int(input())
draw_a_rhombus_first_half(n)