import numpy as np


def gray_to_green():
    spotify_green   = [x/255 for x in [29, 185, 84]]
    github_gray     = [x/255 for x in [36, 41, 46]]

    print(spotify_green)
    print(github_gray)

    R = np.linspace(github_gray[0], spotify_green[0], 3)
    G = np.linspace(github_gray[1], spotify_green[1], 3)
    B = np.linspace(github_gray[2], spotify_green[2], 3)

    return [R, G, B]


gray_to_green()