import numpy as np
import matplotlib 
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


#Representation of the farm as a 5x5 matrix with a single infected cell in the center
farm = np.zeros((5, 5), dtype=int)
farm[2, 2] = 1
img = plt.imshow(farm, cmap='Blues', vmin=0, vmax=1)
plt.axis('off')


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

#loop to propagate the infection for 4 iterations
for iteration in range(4):
    farm = propagate_infection(farm)
    infected_count = np.count_nonzero(farm == 1)
    healthy_count = np.count_nonzero(farm == 0)
    print(f"Round {iteration + 1}:" )
    print(farm)
    print(f"Number of infected cells: {infected_count}\n")
    print(f"Number of healthy cells: {healthy_count}\n")
    plt.title(f"Round:{iteration + 1}\n Infected Cells: {infected_count} | Healthy Cells: {healthy_count}")
    img.set_data(farm)
    plt.pause(0.5)  

plt.show()  
