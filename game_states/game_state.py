from abc import ABC, abstractmethod

class GameState(ABC):
    @abstractmethod
    def update(self):
        ...
    
    @abstractmethod
    def render(self):
        ...