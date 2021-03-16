DATURA_BOMBS = 40
CHERRY_BOMBS = 60
SMOKE_DECOY = 120


def mix_and_calculate(effects, casing):
    if effects[0] + casing[-1] == DATURA_BOMBS:
        bomb_pouch['Datura Bombs'] += 1
        return True
    elif effects[0] + casing[-1] == CHERRY_BOMBS:
        bomb_pouch['Cherry Bombs'] += 1
        return True
    elif effects[0] + casing[-1] == SMOKE_DECOY:
        bomb_pouch['Smoke Decoy Bombs'] += 1
        return True
    else:
        casing[-1] -= 5
        return False


def filled_bomb_pouch(bomb_dict):
    if bomb_dict['Datura Bombs'] >= 3 and bomb_dict['Cherry Bombs'] >= 3 and bomb_dict['Smoke Decoy Bombs'] >= 3:
        return True
    return False


def print_the_rest(bomb_pounch, effects, casing):
    if effects:
        print(f"Bomb Effects: {(', '.join(list(map(str, effects))))}")
    else:
        print("Bomb Effects: empty")
    if casing:
        print(f"Bomb Casings: {(', '.join(list(map(str, casing))))}")
    else:
        print("Bomb Casings: empty")

    print(f"Cherry Bombs: {bomb_pounch['Cherry Bombs']}")
    print(f"Datura Bombs: {bomb_pounch['Datura Bombs']}")
    print(f"Smoke Decoy Bombs: {bomb_pounch['Smoke Decoy Bombs']}")


bombs_effects = list(map(int, input().split(', ')))
bombs_casing = list(map(int, input().split(', ')))

bomb_pouch = {'Cherry Bombs': 0, 'Datura Bombs': 0, 'Smoke Decoy Bombs': 0}

while bombs_effects:
    is_bomb = False
    if mix_and_calculate(bombs_effects, bombs_casing):
        is_bomb = True

    if is_bomb:
        bombs_effects.pop(0)
        bombs_casing.pop()

    if filled_bomb_pouch(bomb_pouch):
        print('Bene! You have successfully filled the bomb pouch!')
        print_the_rest(bomb_pouch, bombs_effects, bombs_casing)
        break

    if not bombs_effects and not filled_bomb_pouch(bomb_pouch):
        print("You don't have enough materials to fill the bomb pouch.")
        print_the_rest(bomb_pouch, bombs_effects, bombs_casing)
        break
