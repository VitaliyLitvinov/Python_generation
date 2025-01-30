def draw_triangle(h, w):
    for i in range(1, h+1):
        print(' '*(w//2-i+1) + '*' * i)



draw_triangle(8,15)