# def coords_2_num(coords, side_len):
#     x, y = coords
#     return y * side_len + x


# def num_2_coords(num, side_len):
#     x = int(num % side_len)
#     y = int(num / side_len)
#     return (x, y)


# def get_square_level_num(side_len):
#     return int(side_len / 2 + side_len % 2)


# def get_point_layer(idx, side_len):
#     level_num = get_square_level_num(side_len)

#     if idx < level_num:
#         return idx % level_num
#     else:
#         return level_num - idx % level_num - 1 - side_len % 2


# def get_point_level(coords, side_len):
#     x, y = coords

#     x_layer = get_point_layer(x, side_len)
#     y_layer = get_point_layer(y, side_len)

#     return min(x_layer, y_layer)


# def rotate_num(num, side_len):
#     x, y = num_2_coords(num, side_len)
#     point_level = get_point_level((x, y), side_len)

#     alt_x = x - point_level
#     alt_y = y - point_level
#     alt_side_len = side_len - point_level * 2

#     if alt_y == 0:
#         alt_y += alt_x
#         alt_x = alt_side_len - 1
#     elif alt_x == alt_side_len - 1:
#         alt_x -= alt_y
#         alt_y = alt_side_len - 1
#     elif alt_y == alt_side_len - 1:
#         alt_y = alt_x
#         alt_x = 0
#     elif alt_x == 0:
#         alt_x = alt_side_len - 1 - alt_y
#         alt_y = 0

#     return coords_2_num((alt_x + point_level, alt_y + point_level), side_len)


# # reading data
# with open("04-data.txt") as data:
#     key = data.readline()
#     txt = data.read()

# # formatting data
# # key = list(key.replace(" ", "").replace("\n", "").replace("[", "").replace("]", "").replace(",", ""))
# # key = [int(x) for x in key]
# key = [7, 10, 12]
# txt = txt.replace(" ", "")

# stencils = [key]
# prev_stencil = key
# side_len = len(key) + 1
# flattened = key

# for i in range(0, 3):
#     rotated_stencil = []
#     for num in prev_stencil:
#         rotated_num = rotate_num(num, side_len)
#         rotated_stencil.append(rotated_num)
#         flattened.append(rotated_num)
    
#     stencils.append(rotated_stencil)
#     prev_stencil = rotated_stencil

# print(flattened)

# # check what squares weren't used
# unused_squares = []
# for i in range(0, side_len**2):
#     if i in flattened:
#         continue
    
#     unused_squares.append(i)

# print(unused_squares)

# # preparing possible stencils
# possible_finished_stencils = []
# for item in unused_squares:
#     potential_set = []
#     next_num = item
#     print(item)
#     for stencil in stencils:
#         stencil.append(next_num)
#         next_num = rotate_num(next_num, side_len)
        
#     print(potential_set)
#     possible_finished_stencils.append(potential_set)

# printing possible answers


# print(possible_finished_stencils)
# print(possible_finished_stencils)





