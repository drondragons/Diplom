import copy
from typing import List, Tuple

# import heapq

from ..price import Price
from ..buildings import Building, Apartment, Shop

# from ...geometry.one_dimensional import Line
from ...measurement.length import Length, LengthValidator, Meter
# from ...measurement.square import SquareConverter


__all__ = [
    "BoundedKnapsack",
]


class BoundedKnapsack:
    
    @classmethod
    def __prepare(
        cls, 
        buildings: List[Building],
        budget: Price
    ) -> Tuple[Length, List[Building], List[Building]]:
        area = 0
        new_buildings = list()
        required_buildings = list()
        for building in buildings:
            if not isinstance(building, Apartment | Shop):
                area += building.area_with_indent
                budget -= building.price_to_build
                required_buildings.append(building)
            else:
                new_buildings.append(building)

        amounts = list()
        for building in new_buildings:
            amount = int(budget // building.price_to_build)
            if amount > 1 and not isinstance(building, Apartment):
                amount = 1
            amounts.append(amount)
    
        return area, new_buildings, amounts, required_buildings
    
    @classmethod
    def _convert_to_binary_knapsack(cls, buildings, amounts):
        result = list()
        count = copy.deepcopy(amounts)
        for i, building in enumerate(buildings):
            j = 1
            while count[i] >= j:
                result.append((j * building.area_with_indent, j * building.profit))
                count[i] -= j
                j *= 2
            if count[i] > 0:
                result.append((count[i] * building.area_with_indent, count[i] * building.profit))
        return result, count
    
    @classmethod
    def solve_dynamic(
        cls, 
        capacity: Length, 
        buildings: List[Building],
        budget: Price
    ) -> List[Building]:
        area, new_buildings, amounts, required_buildings = cls.__prepare(buildings, budget)
        
        sum_area = sum(building.area_with_indent for building in required_buildings)
        sum_area += sum(building.area_with_indent * amounts[i] for i, building in enumerate(new_buildings))
        if sum_area < capacity:
            return required_buildings + [building \
                for building, amount in zip(new_buildings, amounts) \
                    for _ in range(amount)]
        
        # print(amounts)
        
        for i, (building, amount) in enumerate(zip(new_buildings, amounts)):
            building_area = building.area_with_indent * amount
            if building_area > capacity - area:
                amounts[i] = int((capacity - area) // building.area_with_indent)
    
        # print(amounts)
        
        # result, new_amounts = BoundedKnapsack._convert_to_binary_knapsack(new_buildings, amounts)
        # print(result)
        # print(new_amounts)
        # # input()
        
        # n = len(result)
        # W = int(round(capacity - area)) // 100
        # table = [[0.0 for _ in range(W + 1)] for _ in range(n + 1)]
        # print(n, W, capacity, area)
        # print(table)
        # # input()
        
        # for i in range(1, n + 1):
        #     area_with_indent, profit = result[i - 1]
        #     for c in range(1, W + 1):
        #         table[i][c] = table[i - 1][c]
        #         if c >= int(area_with_indent // 100):
        #             table[i][c] = max(
        #                 table[i][c], 
        #                 table[i - 1][c - int(area_with_indent // 100)] + profit
        #             )
                    
        # print(table)
        # # input()
        
        # solution = required_buildings
        # remaining_capacity = W
        
        # for i in range(min(n, len(amounts)), 0, -1):
        #     area_with_indent, profit = result[i - 1]
        #     if remaining_capacity >= int(area_with_indent // 100) and \
        #         table[i][remaining_capacity] == table[i - 1][remaining_capacity - int(area_with_indent // 100)] + profit:
        #         print(i - 1)
        #         print(amounts)
        #         print(amounts[i - 1])
        #         solution.append(new_buildings[(i - 1) // amounts[i - 1]])  # Определяем оригинальное здание
        #         remaining_capacity -= int(area_with_indent // 100)
        
        # i = n
        # while i > 0 and remaining_capacity > 0:
        #     print(table[i][remaining_capacity])
        #     print(table[i - 1][remaining_capacity])
        #     if table[i][remaining_capacity] != table[i - 1][remaining_capacity]:
        #         area_with_indent, profit = result[i - 1]
        #         print(area_with_indent, profit)
        #         # Определяем оригинальное здание
        #         original_building_index = (i - 1) // len(amounts)
        #         print(i - 1, len(amounts), original_building_index)
        #         print(len(new_buildings))
        #         original_building = new_buildings[original_building_index - 1]
        #         solution.append(original_building)
        #         remaining_capacity -= int(area_with_indent // 100)
        #     i -= 1
        
        # return solution
    
    
        # W = int(round(capacity - area)) // 100
        # table = [[[] for _ in range(W + 1)] for _ in range(len(new_buildings) + 1)]
        # table[0][0] = [(0, [])]
        
        # for i, building in enumerate(new_buildings):
        #     for c in range(W + 1):
        #         if table[i][c]:
        #             for k in range(1, amounts[i] + 1):
        #                 new_weight = c + int(k * building.area_with_indent // 100)
        #                 if new_weight <= W:
        #                     for profit, solution in table[i][c]:
        #                         new_profit = profit + k * building.profit
        #                         new_solution = solution + [building] * k
        #                         heapq.heappush(table[i + 1][new_weight], (new_profit, new_solution))
        #                         if len(table[i + 1][new_weight]) > 3:
        #                             heapq.heappop(table[i + 1][new_weight])
        
        # final_solutions = []
        # for profit, solution in table[len(new_buildings)][W]:
        #     final_solution = required_buildings + solution
        #     final_solutions.append(final_solution)
        
        # # Добавляем недостающие решения, если они меньше трех
        # if len(final_solutions) < 3:
        #     final_solutions.extend([required_buildings] * (3 - len(final_solutions)))
        
        # return final_solutions
        
        
        # ------------- РЕШАЕТ ОГРАНИЧЕННЫЙ РЮКЗАК С ЛУЧШИМ РЕШЕНИЕМ ------------
        W = int(round(capacity - area)) // 100
        table = [[0.0 for _ in range(W + 1)] for _ in range(len(new_buildings) + 1)]
        for i, building in enumerate(new_buildings):
            for c in range(1, W + 1):
                table[i + 1][c] = table[i][c]
                for k in range(1, amounts[i] + 1):
                    if c >= int(k * building.area_with_indent // 100):
                        table[i + 1][c] = max(
                            table[i + 1][c],
                            table[i][c - k * int(building.area_with_indent) // 100] + k * building.profit
                        )

        solution = required_buildings
        for i in range(len(new_buildings), 0, -1):
            for k in range(amounts[i - 1], 0, -1):
                if W >= int(k * new_buildings[i - 1].area_with_indent // 100):
                    if table[i][W] == table[i - 1][W - k * int(new_buildings[i - 1].area_with_indent) // 100] + k * new_buildings[i - 1].profit:
                        solution.extend([new_buildings[i - 1]] * k)
                        W -= k * int(new_buildings[i - 1].area_with_indent // 100)
                        break
        return solution
        
        
        
        # ------------ РЕШАЕТ 0-1 РЮКЗАК ----------------
        # W = int(round(capacity - area)) // 100
        # table = [[0.0 for _ in range(W + 1)] for _ in range(len(buildings) + 1)]
        # for i, building in enumerate(new_buildings):
        #     for c in range(1, W + 1):
        #         # item = table[i][c]
        #         table[i + 1][c] = table[i][c]
        #         if c >= building.area_with_indent // 100:
        #             # cur = table[i][c - int(building.area_with_indent) // 100]
        #             table[i + 1][c] = max(
        #                 table[i + 1][c],
        #                 table[i][c - int(building.area_with_indent) // 100] + building.profit
        #             )
        #         # else:
        #             # table[i + 1][c] = item

        # solution = required_buildings
        # for i in range(len(new_buildings), 0, -1):
        #     if table[i - 1][W] != table[i][W]:
        #         solution.append(new_buildings[i - 1])
        #         W -= int(new_buildings[i - 1].area_with_indent // 100)
        # return solution