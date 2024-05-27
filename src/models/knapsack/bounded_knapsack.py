from typing import List, Tuple

import heapq

from ..price import Price
from ..buildings import Building, Apartment, Shop

from ...geometry.one_dimensional import Line
from ...measurement.length import Length, LengthValidator, Meter
from ...measurement.square import SquareConverter


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
        # print(budget)
        amounts = list()
        for building in new_buildings:
            amount = int(budget // building.price_to_build)
            if amount > 1 and not isinstance(building, Apartment):
                amount = 1
            amounts.append(amount)
        # print(result)
        return area, new_buildings, amounts, required_buildings
    
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