from copy import copy
from .game_object import GameObject


class ObjectGroup:
    def __init__(self, sprites=None) -> None:
        if sprites == None:
            self.sprites = []
        else:
            self.sprites = sprites[:]

    def add(self, *sprites: GameObject) -> None:
        for sprite in sprites:
            self.sprites.append(sprite)

    def remove(self, sprite: GameObject) -> None:
        self.sprites.remove(sprite)

    def draw(self, surface) -> None:
        for sprite in self.sprites:
            sprite.draw(surface)

    def __copy__(self) -> 'ObjectGroup':
        cp = [copy(sprite) for sprite in self.sprites]
        return ObjectGroup(cp)

    def __len__(self) -> int:
        return len(self.sprites)
