import copy
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from ..buildings import Building


__all__ = [
    "Binpacker",
]


class Binpacker:
    
    def __init__(self, width, height):
        self.root = {'width': width, 'height': height, 'x': 0, 'y': 0, 'used': False}
        self.placements = []

    def sort_blocks_by_title(self, blocks, is_reverse):
        return sorted(blocks, key=lambda block: block[0]['title'], reverse=is_reverse)
    
    def sort_blocks_by_area(self, blocks, is_reverse):
        # return sorted(blocks, key=lambda block: block['height'] * block['width'], reverse=is_reverse)
        return sorted(blocks, key=lambda block: block[0]['height'] * block[0]['width'], reverse=is_reverse)

    def sort_blocks_by_width(self, blocks, is_reverse):
        # return sorted(blocks, key=lambda block: block['width'], reverse=is_reverse)
        return sorted(blocks, key=lambda block: block[0]['width'], reverse=is_reverse)

    def sort_blocks_by_height(self, blocks, is_reverse):
        # return sorted(blocks, key=lambda block: block['height'], reverse=is_reverse)
        return sorted(blocks, key=lambda block: block[0]['height'], reverse=is_reverse)

    def __make_block(self, blocks):
        result = list()
        for block in blocks:
            result.append(
                {
                    "title": str(block.title),
                    "indent": int(block.indent),
                    "width": int(block.width + 2 * block.indent),
                    "height": int(block.length + 2 * block.indent),
                }
            )
        return result

    def fittable(self, blocks, rotatable=False, root=None):
        if root is None:
            root = self.root
        if not blocks:
            return True
        
        def fit_block(root, block_title, block_indent, block_width, block_height):
            tail = blocks[1:] 
            node = self.__find_node(root, block_width, block_height)
            if node is None:
                return False
            else:
                self.__split_node(node, block_width, block_height)
                self.placements.append((block_title, block_indent, block_width, block_height, node['x'], node['y']))
                return self.fittable(tail, rotatable, root)

        block = blocks[0]
        return fit_block(copy.deepcopy(root), block['title'], block['indent'], block['width'], block['height']) or \
            (rotatable and fit_block(copy.deepcopy(root), block['title'], block['indent'], block['height'], block['width']))

    def __find_node(self, root, width, height):
        if not 'used' in root:
            print(root)
        if root['used']:
            return self.__find_node(root['right'], width, height) or self.__find_node(root['down'], width, height)
        elif width <= root['width'] and height <= root['height']:
            return root
        else:
            return None

    def __split_node(self, node, width, height):
        node['used'] = True
        node['down'] = {'x': node['x'], 'y': node['y'] + height, 'width': node['width'], 'height': node['height'] - height, 'used': False}
        node['right'] = {'x': node['x'] + width, 'y': node['y'], 'width': node['width'] - width, 'height': height, 'used': False}
        return node

    def fit_blocks(self, blocks):
        blocks = self.__make_block(blocks)

        rotations = [0] * len(blocks) 
        max_rotations = [1 if blocks[i]['width'] != blocks[i]['height'] else 0 for i in range(len(blocks))]
        
        sort_permutations = self.generate_sort_permutations()
        for sorting, value in sort_permutations:
            combined = list(zip(blocks, max_rotations))
            combined_sorted = sorting(combined, value)
            blocks, max_rotations = zip(*combined_sorted)
            blocks, max_rotations = list(blocks), list(max_rotations)
            while True:
                if self.fittable(blocks):
                    return True
                self.placements.clear()
                
                rotated = False
                for i in range(len(blocks)):
                    if rotations[i] < max_rotations[i]:
                        blocks[i]['width'], blocks[i]['height'] = blocks[i]['height'], blocks[i]['width']
                        rotations[i] += 1
                        rotated = True
                        break
                    else:
                        blocks[i]['width'], blocks[i]['height'] = blocks[i]['height'], blocks[i]['width']
                        rotations[i] = 0
                
                if not rotated:
                    break
        
        for _ in range(len(blocks)):
            blocks = blocks[1:] + blocks[:1]
            max_rotations = max_rotations[1:] + max_rotations[:1]
            while True:
                if self.fittable(blocks):
                    return True
                self.placements.clear()
                
                rotated = False
                for i in range(len(blocks)):
                    if rotations[i] < max_rotations[i]:
                        blocks[i]['width'], blocks[i]['height'] = blocks[i]['height'], blocks[i]['width']
                        rotations[i] += 1
                        rotated = True
                        break
                    else:
                        blocks[i]['width'], blocks[i]['height'] = blocks[i]['height'], blocks[i]['width']
                        rotations[i] = 0
                
                if not rotated:
                    break
        
        # sort_permutations = self.generate_sort_permutations()
        # while True:
        #     for _ in range(3):
        #         random.shuffle(blocks)
        #         if self.fittable(blocks):
        #             return True
        #         self.placements.clear()
            
        #     for sorting, value in sort_permutations:
        #         if self.fittable(sorting(blocks, value)):
        #             return True
        #         self.placements.clear()
                
        #     rotated = False
        #     for i in range(len(blocks)):
        #         if rotations[i] < max_rotations[i]:
        #             blocks[i]['width'], blocks[i]['height'] = blocks[i]['height'], blocks[i]['width']
        #             rotations[i] += 1
        #             rotated = True
        #             break
        #         else:
        #             blocks[i]['width'], blocks[i]['height'] = blocks[i]['height'], blocks[i]['width']
        #             rotations[i] = 0
            
        #     if not rotated:
        #         break

    def generate_sort_permutations(self):
        return [
            (self.sort_blocks_by_area, True),
            (self.sort_blocks_by_area, False),
            (self.sort_blocks_by_height, True),
            (self.sort_blocks_by_height, False),
            (self.sort_blocks_by_width, True),
            (self.sort_blocks_by_width, False),
            (self.sort_blocks_by_title, False),
            (self.sort_blocks_by_title, True),
        ]

    def generate_color(self):
        def pastel_color_component():
            return random.randint(150, 255)

        r = pastel_color_component()
        g = pastel_color_component()
        b = pastel_color_component()
        return f'#{r:02X}{g:02X}{b:02X}'
        # return "#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        
    def plot_packing(self, ax):
        ax.set_xlim(0, self.root['width'])
        ax.set_ylim(self.root['height'], 0)
        ax.set_aspect('equal', 'box')
        ax.invert_yaxis()
        
        titles = {}
        for title, indent, width, height, x, y in self.placements:
            if title in titles:
                titles[title].append((title, indent, width, height, x, y))
            else:
                titles[title] = [(title, indent, width, height, x, y)]
                
        for blocks in titles.values():
            color = self.generate_color()
            for title, indent, width, height, x, y in blocks:
                rect = patches.Rectangle((x, y), width, height, edgecolor='black', facecolor='none')
                ax.add_patch(rect)
                smaller_rect = patches.Rectangle(
                    (x + int(indent), y + int(indent)), 
                    width - int(indent * 2), 
                    height - int(indent * 2),
                    edgecolor='black', 
                    facecolor=color
                )
                ax.add_patch(smaller_rect)
                ax.text(x + width/2, y + height/2, title, ha='center', va='center', rotation=45)