from typing import Optional

class Local:
    def __init__(self, name: str, address: str, max_capacity: int) -> None:
        self.__name: str = name
        self.__address: str = address
        self.__max_capacity: int = max_capacity
        self.__current_occupancy: int = 0

    def get_name(self) -> str:
        return self.__name

    def get_address(self) -> str:
        return self.__address

    def get_max_capacity(self) -> int:
        return self.__max_capacity

    def get_current_occupancy(self) -> int:
        return self.__current_occupancy

    def is_available(self) -> bool:
        return self.__current_occupancy < self.__max_capacity

    def add_occupancy(self, count: int) -> None:
        if self.__current_occupancy + count <= self.__max_capacity:
            self.__current_occupancy += count
        else:
            raise ValueError("Exceeds maximum capacity.")

    def reduce_occupancy(self, count: int) -> None:
        if self.__current_occupancy - count >= 0:
            self.__current_occupancy -= count
        else:
            raise ValueError("Occupancy cannot be negative.")
