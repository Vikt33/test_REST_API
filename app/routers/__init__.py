# app/routers/__init__.py
import sys

routers = {}

try:
    from .organizations import router
    routers["organizations"] = router
    print("Successfully imported organizations router")
except ImportError as e:
    print(f"Error importing organizations router: {e}")
    sys.exit(1)

try:
    from .buildings import router
    routers["buildings"] = router
    print("Successfully imported buildings router")
except ImportError as e:
    print(f"Error importing buildings router: {e}")
    sys.exit(1)

try:
    from .activities import router
    routers["activities"] = router
    print("Successfully imported activities router")
except ImportError as e:
    print(f"Error importing activities router: {e}")
    sys.exit(1)

# Экспортируем роутеры
organizations = routers["organizations"]
buildings = routers["buildings"]
activities = routers["activities"]

__all__ = ["organizations", "buildings", "activities"]