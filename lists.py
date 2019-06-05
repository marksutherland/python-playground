fruit = ['apples', 'oranges', 'bananas', 'grapes']
vegetables = ['parsnips', 'peas', 'beetroot', 'radishes']
foods = [fruit, vegetables]
flat_foods = [*fruit, *vegetables]

print(foods)
print(flat_foods)

fruit.append('lemons')
more_fruit = fruit[:]
more_fruit.append('limes')
print(fruit == more_fruit)

for f in fruit[1:-1]:
    for c in f:
        print(c)
    print()

[print(f) for f in reversed(fruit) if 'n' in f]
print(fruit)

fruit.reverse()
print(fruit)

for i, v in enumerate(vegetables):
    print(f'{i}: {v}')
