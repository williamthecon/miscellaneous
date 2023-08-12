from typing import List

def calculate_square_sum(**numbers: List[int | float]) -> int | float:
    x = sum([number ** 2 for number in numbers])
    return x if int(x) != x else int(x)

def calculate_root(index: int | float, radicand: int | float) -> int | float:
    x = radicand ** (1 / index)
    return x if int(x) != x else int(x)

def calculate_average(**numbers: List[int | float]) -> int | float:
    x = sum(numbers) / len(numbers)
    return x if int(x) != x else int(x)

def calculate_median(**numbers: List[int | float]) -> int | float:
    numbers.sort()
    x = numbers[len(numbers) // 2] if len(numbers) % 2 == 1 else (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 + 1]) / 2
    return x if int(x) != x else int(x)

def calculate_mode(**numbers: List[int | float]) -> int | float:
    counts = [numbers.count(number) for number in numbers]
    x = numbers[counts.index(max(counts))]
    return x

def calculate_factorial(number: int) -> int:
    def multiply_x_by(n: int):
        x *= n
        
    x = 1
    [add_to_x(i) for i in range(1, n + 1)]
    return x

def generate_fibonacci_sequence(length: int, start_index: int=0) -> List[int]:
    numbers, sequence = [0, 1], []
    
    while len(sequence) < length:
        if len(numbers) >= start_index:
            sequence.append(numbers[-1])

        numbers.append(numbers[-2] + numbers[-1])

    return sequence

def convert_to_binary(number: int) -> str:
    binary = ""

    while number:
        binary = str(number % 2) + binary
        number //= 2

    return binary

def calculate_pythagorean_hypothenuse(catheti_1: int | float, catheti_2: int | float) -> int | float:
    x = (catheti_1 ** 2 + catheti_2 ** 2) ** 0.5
    return x if int(x) != x else int(x)

def calculate_pythogorean_catheti(other_catheti: int | float, hypothenuse: int | float) -> int | float:
    x = (hypothenuse ** 2 - other_catheti ** 2) ** 0.5
    return x if int(x) != x else int(x)

def calculate_triangle_last_angle(other_angle_1: int | float, other_angle_2: int | float) -> int | float:
    x = 180 - other_angle_1 - other_angle_2
    return x if int(x) != x else int(x)

def calculate_rectangle_area(length: int | float, width: int | float) -> int | float:
    x = length * width
    return x if int(x) != x else int(x)

def calculate_rectangle_perimeter(length: int | float, width: int | float) -> int | float:
    x = length * 2 + width * 2
    return x if int(x) != x else int(x)

def calculate_rectangle_diameter(length: int | float, width: int | float) -> int | float:
    x = (length ** 2 + width ** 2) ** 0.5
    return x if int(x) != x else int(x)

def calculate_triangle_area(base: int | float, height: int | float) -> int | float:
    x = (base * height) / 2
    return x if int(x) != x else int(x)

def calculate_triangle_area_with_sides(side_1: int | float, side_2: int | float, side_3: int | float): int | float
    s = (side_1 + side_2 + side_3) / 2
    area = (s * (s - side_1) * (s - side_2) * (s - side_3)) ** 0.5
    return area if int(area) != area else int(area)

def calculate_triangle_height(area: int | float, base: int | float) -> int | float:
    height = (2 * area) / base
    return height

def calculate_triangle_height_with_sides(base: int | float, side_1: int | float, side_2: int | float) -> int | float:
    s = (base + side_1 + side_2) / 2
    area = (s * (s - base) * (s - side_1) * (s - side_2)) ** 0.5
    height = (2 * area) / base
    return height
