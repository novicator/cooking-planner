"""Generate a simple cooking-themed app icon (fork & knife on a warm background)."""
from PIL import Image, ImageDraw

SIZE = 512
BG = (244, 124, 31)      # warm orange
WHITE = (255, 255, 255)


def rrect(d, box, r, fill):
    d.rounded_rectangle(box, radius=r, fill=fill)


def draw_icon():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    d = ImageDraw.Draw(img)

    # ---- Fork (left) ----
    fx = 196
    # tines
    for dx in (-34, 0, 34):
        rrect(d, [fx + dx - 9, 120, fx + dx + 9, 215], 9, WHITE)
    # neck joining the tines
    rrect(d, [fx - 43, 200, fx + 43, 240], 18, WHITE)
    # handle
    rrect(d, [fx - 17, 235, fx + 17, 405], 17, WHITE)

    # ---- Knife (right) ----
    kx = 330
    # blade
    rrect(d, [kx - 22, 120, kx + 22, 270], 22, WHITE)
    # handle
    rrect(d, [kx - 16, 255, kx + 16, 405], 16, WHITE)

    return img


def main():
    base = draw_icon()
    for size, name in [(512, "icon-512.png"), (192, "icon-192.png"), (180, "apple-touch-icon.png")]:
        base.resize((size, size), Image.LANCZOS).save(name)
        print("wrote", name)


if __name__ == "__main__":
    main()
