from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

project = Path(__file__).resolve().parents[1]
www = project / "www"
res = project / "android" / "app" / "src" / "main" / "res"
icon = Image.open(www / "icon-512.png").convert("RGBA")
maskable = Image.open(www / "icon-maskable-512.png").convert("RGBA")
launcher_sizes = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}
foreground_sizes = {"mdpi": 108, "hdpi": 162, "xhdpi": 216, "xxhdpi": 324, "xxxhdpi": 432}

for density, size in launcher_sizes.items():
    folder = res / f"mipmap-{density}"
    folder.mkdir(parents=True, exist_ok=True)
    resized = icon.resize((size, size), Image.Resampling.LANCZOS)
    resized.save(folder / "ic_launcher.png", optimize=True)
    round_icon = resized.copy()
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    round_icon.putalpha(mask)
    round_icon.save(folder / "ic_launcher_round.png", optimize=True)
    foreground = maskable.resize((foreground_sizes[density], foreground_sizes[density]), Image.Resampling.LANCZOS)
    foreground.save(folder / "ic_launcher_foreground.png", optimize=True)

for splash in res.rglob("splash.png"):
    original = Image.open(splash)
    size = original.size
    background = ImageOps.fit(maskable.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
    background.save(splash, optimize=True)

preview = Image.new("RGB", (1200, 440), "#ECEFF1")
preview.paste(icon.resize((320, 320), Image.Resampling.LANCZOS), (40, 60))
preview.paste(maskable.resize((320, 320), Image.Resampling.LANCZOS), (440, 60))
splash_preview = Image.open(res / "drawable-port-xhdpi" / "splash.png").convert("RGB")
splash_preview.thumbnail((280, 360))
preview.paste(splash_preview, (850, 40))
draw = ImageDraw.Draw(preview)
draw.text((40, 22), "Launcher", fill="#14212B")
draw.text((440, 22), "Adaptive icon", fill="#14212B")
draw.text((850, 22), "Native splash", fill="#14212B")
preview.save(project / "assets-preview.png", optimize=True)

for desktop_ini in project.rglob("desktop.ini"):
    desktop_ini.unlink()

print("Generated launcher, adaptive icon and splash assets.")
