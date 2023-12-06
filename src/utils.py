from abc import ABC, abstractmethod


class BaseSolution(ABC):
    @abstractmethod
    def part_1(self, data: list) -> int:
        pass

    @abstractmethod
    def part_2(self, data: list) -> int:
        pass


class NotCompleteSolution(BaseSolution):
    def part_1(self, data: list) -> int:
        raise NotImplementedError()

    def part_2(self, data: list) -> int:
        raise NotImplementedError()
