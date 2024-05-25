def first_fit_decreasing(sizes, capacity):
    sizes.sort(reverse=True)
    drawers = []
    
    for size in sizes:
        placed = False
        for i in range(len(drawers)):
            if drawers[i] >= size:
                drawers[i] -= size
                placed = True
                break
        if not placed:
            drawers.append(capacity - size)
    
    return len(drawers), drawers

item_sizes = [4, 8, 1, 4, 2, 1]
drawer_capacity = 10
num_drawers, drawer_contents = first_fit_decreasing(item_sizes, drawer_capacity)

print(f"Минимум: {num_drawers}")
print(f"Содержание: {drawer_contents}")
