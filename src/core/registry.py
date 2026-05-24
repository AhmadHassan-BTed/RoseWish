from typing import Any, Dict, Type, TypeVar

T = TypeVar("T")


class Registry:
    """
    A central registry for services and providers.
    Facilitates modularity and prevents direct dependency on concrete implementations.
    """

    _services: Dict[Type, Any] = {}

    @classmethod
    def register(cls, service_type: Type[T], instance: T):
        cls._services[service_type] = instance

    @classmethod
    def get(cls, service_type: Type[T]) -> T:
        service = cls._services.get(service_type)
        if not service:
            raise RuntimeError(f"Service {service_type.__name__} not registered.")
        return service


# Shortcut for dependency injection
def inject(service_type: Type[T]) -> T:
    return Registry.get(service_type)
