from email.mime import image
import click
import numpy as np
import matplotlib.pyplot as plt
import random

BLACK = 0
WHITE = 255

class NoisyPattern:
    def __init__(self) -> None:
        self.image = np.full([80,80], WHITE)
        self.set_lines()
        self.add_noise()

    def set_lines(self) -> None:
        self.image[:,0:16] = BLACK
        self.image[:,32:48] = BLACK
        self.image[:,64:80] = BLACK
        plt.imsave('./data/lines.png', self.image, cmap=plt.cm.gray)

    def add_noise(self) -> None:
        noise=0.05
        for i in range (0, self.image.shape[0]):
            for j in range(0, self.image.shape[1]):
                if(noise > random.random()):
                    self.image[i,j] = WHITE
        plt.imsave('./data/noisy_pattern.png', self.image, cmap=plt.cm.gray)

    def remove_noise(self) -> None:
        for i in range (0,self.image.shape[0]):
            for j in range(0,self.image.shape[1]):
                if self.image[i][j] == WHITE:
                    black_neighbours = self.count_black_neighbours(i, j)
                    if black_neighbours >= 4:
                        self.image[i][j] = BLACK
        plt.imsave('./data/noise_removed.png', self.image, cmap=plt.cm.gray)

    def filter_1(self) -> None:
        for i in range (0,self.image.shape[0]):
            for j in range(0,self.image.shape[1]):
                self.image[i][j] = self.average_neighbours(i, j)
        plt.imsave('./data/pattern_filter_1.png', self.image, cmap=plt.cm.gray)
    
    def count_black_neighbours(self, x: int, y: int) -> int:
        count: int = 0
        for i in self.coordinate_range(x-1, x+2, self.image.shape[0]):
            for j in self.coordinate_range(y-1, y+2, self.image.shape[1]):
                if self.image[i][j] == BLACK:
                    count = count + 1
        return count
    
    def average_neighbours(self, x: int, y: int) -> int:
        sum: int = 0
        for i in self.coordinate_range(x-1, x+2, self.image.shape[0]):
            for j in self.coordinate_range(y-1, y+2, self.image.shape[1]):
                sum = sum + self.image[i][j]
        return int(sum / 9)

    def coordinate_range(self, start_c: int, end_c: int, end_limit: int) -> list[int]:
        if end_limit > end_c:
            return [i for i in range(start_c, end_c)]
        else:
            return [i for i in range(start_c, end_limit)] + [i for i in range(0, end_c-end_limit)]
    

@click.command()
def main():
    image_generator = NoisyPattern()
    image_generator.remove_noise()
    image_generator.filter_1()


if __name__ == "__main__":
    main()