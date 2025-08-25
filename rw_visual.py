import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

# Initalize one random walk






# Keep making new walks, as long as the program is active 
while True : 
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig,ax = plt.subplots()
    fig.canvas.manager.set_window_title('10.000 points simulation') 
    points_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = points_number, cmap = plt.cm.Blues, edgecolors='none',s=15)


    ax.set_title('A random walk from (0,0)')  
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n' : 
        break 