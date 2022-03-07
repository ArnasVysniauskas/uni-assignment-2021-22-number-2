from tracemalloc import start
import click
import numpy as np


class ProcessArray:

    def __init__(self, size: int) -> None:
        self.size = size
        self.numbers = np.random.random([self.size]) * 100
        self.numbers = self.numbers.round(0)
        print(str(self))

    def __str__(self) -> str:
        return f"Array of size {self.size}\n{self.numbers}"

    def hybrid_sort(self) -> None:
        sorted = False
        start_index = 0
        end_index = len(self.numbers) - 1

        while not sorted:
            changes_made = False
            current_value = self.numbers[start_index]

            minimum_value = current_value
            minimum_value_index = start_index

            for i in range(start_index, end_index):
                next_value = self.numbers[i + 1]

                if current_value > next_value:
                    self.numbers[i] = next_value
                    self.numbers[i + 1] = current_value
                    changes_made = True
                else:
                    current_value = next_value
                
                if i != start_index and self.numbers[i] < minimum_value:
                    minimum_value = self.numbers[i]
                    minimum_value_index = i
                    changes_made = True

            if start_index != minimum_value_index:
                print(f"value at {minimum_value_index} ({minimum_value}) placed at {start_index}")
                self.numbers = np.delete(self.numbers, minimum_value_index)
                self.numbers = np.insert(self.numbers, start_index, minimum_value)
            
            end_index = end_index - 1
            start_index = start_index + 1

            if not changes_made or start_index >= end_index:
                sorted = True


@click.command()
@click.option("--size", type=click.IntRange(min=2, max_open=True), required=True, help="size of array")
def main(size: int) -> None:

    my_list = ProcessArray(size)
    my_list.hybrid_sort()
    print(str(my_list))



if __name__ == "__main__":
    main()
