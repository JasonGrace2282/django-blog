from __future__ import annotations


__all__ = ["BlogConfig"]


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton,
                cls
            ).__call__(*args, **kwargs)
        return cls._instances[cls]


class _BlogConfig(metaclass=Singleton):
    admin_data: AdminProfile | None = None


BlogConfig = _BlogConfig()


class AdminProfile:
    def __init__(self, profile):
        # very primitive system
        for k, v in profile.items():
            setattr(self, k, v)

    def __getitem__(self, item):
        return getattr(self, item)

    def __bool__(self) -> bool:
        return True
