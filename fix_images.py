from pathlib import Path
from restaurants.models import Restaurant, FoodItem

media_root = Path("media")

for obj in list(Restaurant.objects.all()) + list(FoodItem.objects.all()):

    if not obj.image:
        continue

    wanted = media_root / str(obj.image)

    if wanted.exists():
        continue

    folder = wanted.parent
    wanted_lower = wanted.name.lower()

    matches = [
        p for p in folder.iterdir()
        if p.is_file() and p.name.lower() == wanted_lower
    ]

    if matches:
        source = matches[0]
        print(f"FIX: {source} -> {wanted.name}")
        source.rename(wanted)
    else:
        print(f"MISSING: {wanted}")