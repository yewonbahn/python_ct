import itertools


def is_movable(cur_x, cur_y, next_x, next_y, rectangles):
    x, y = (cur_x + next_x) / 2, (cur_y + next_y) / 2
    print(x,y)
    is_on_any_border = any(
        (x in (x1, x2) and y1 <= y <= y2) or (y in (y1, y2) and x1 <= x <= x2)
        for x1, y1, x2, y2 in rectangles)
    is_inside_any_rect = any(
        x1 < x < x2 and y1 < y < y2 for x1, y1, x2, y2 in rectangles)
    return is_on_any_border and not is_inside_any_rect


def solution(rectangle, characterX, characterY, itemX, itemY):
    cur_pos = (characterX, chiaracterY)
    prev_pos = None
    print(itertools.count())
    for dist in itertools.count():
        if cur_pos == (characterX, characterY) and prev_pos:
            perimeter = dist
            break
        elif cur_pos == (itemX, itemY):
            dist_to_item = dist
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
            if next_pos != prev_pos and is_movable(*cur_pos, *next_pos,
                                                   rectangle):
                prev_pos, cur_pos = cur_pos, next_pos
                break
    return min(dist_to_item, perimeter - dist_to_item)

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))