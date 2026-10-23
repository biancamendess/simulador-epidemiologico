import numpy as np

fazenda = np.zeros((5, 5), dtype=int)

fazenda[2, 2] = 1

def propagate_infection(matriz):
    #creation of the matrices shifted in each direction place
    right = np.roll(matriz, 1, axis=1)
    left =np.roll(matriz, -1, axis=1)
    up = np.roll(matriz, 1, axis=0)
    down = np.roll(matriz, -1, axis=0)

    #correction of the edges to prevent "wrap-around"
    right[:, 0] = 0
    left[:, -1 ] = 0
    up[0, :] = 0
    down[-1, :] = 0

    #masks for each direction
    mask_right = right == 1
    mask_left = left == 1
    mask_up = up == 1
    mask_down = down == 1

    #combination of the masks
    mask_combined_horizontal = mask_right | mask_left
    mask_combined_vertical = mask_up | mask_down
    mask_combined = mask_combined_horizontal | mask_combined_vertical

    new_infected = (matriz == 0) & mask_combined    

    matriz[new_infected] = 1

    return matriz 

for rodada in range(4):
    fazenda = propagate_infection(fazenda)
    print(f"Rodada {rodada + 1}:" )
    print(fazenda)