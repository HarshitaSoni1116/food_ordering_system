from pathlib import Path
from restaurants.models import Restaurant, FoodItem

media_root = Path("media")

objects = list(Restaurant.objects.all()) + list(FoodItem.objects.all())

for obj in objects:
    if not obj.image:
        continue

    wanted = media_root / str(obj.image)

    if wanted.exists():
        continue

    folder = wanted.parent

    if not folder.exists():
        print(f"MISSING FOLDER: {folder}")
        continue

    matches = [
        p for p in folder.iterdir()
        if p.is_file()
        and p.name.lower() == wanted.name.lower()
    ]

    if matches:
        source = matches[0]

        print(f"FIXING: {source.name} -> {wanted.name}")

        # Safe case-only rename on Windows
        temp = source.with_name(source.name + ".tmp")
        source.rename(temp)
        temp.rename(wanted)

    else:
        print(f"MISSING: {wanted}")