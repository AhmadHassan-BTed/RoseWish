from typing import Dict, Type, TypeVar, Optional, List, Any

T = TypeVar("T")

class Entity:
    """
    A generic container for components. 
    The core of the ECS-lite architecture.
    """
    def __init__(self, name: str = "Entity"):
        self.name = name
        self.components: Dict[Type, Any] = {}
        self.active = True

    def add_component(self, component: Any):
        self.components[type(component)] = component
        return self

    def get_component(self, component_type: Type[T]) -> Optional[T]:
        return self.components.get(component_type)

    def has_component(self, component_type: Type) -> bool:
        return component_type in self.components

class World:
    """
    Manages all entities and systems.
    """
    def __init__(self):
        self.entities: List[Entity] = []

    def create_entity(self, name: str = "Entity") -> Entity:
        entity = Entity(name)
        self.entities.append(entity)
        return entity

    def remove_entity(self, entity: Entity):
        if entity in self.entities:
            self.entities.remove(entity)

