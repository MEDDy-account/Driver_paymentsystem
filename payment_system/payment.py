from PIL import Image
import pytesseract
import re

# Tesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

import os

png_files = [f for f in os.listdir(".") if f.endswith(".png")]

print(png_files)

for file in png_files:
    print(file)

    img = Image.open(file)

    # 正しい向き
    img = img.rotate(270, expand=True)

    text = pytesseract.image_to_string(
        img,
        config="--psm 6"
    )

    print("=== OCR結果 ===")
    print(text)

    nums = [int(x) for x in re.findall(r"\d+", text)]

    print("\n抽出数字")
    print(nums)

    if len(nums) < 8:
        print(f"{file} はスキップ")
        continue

    b1 = nums[3]
    b2 = nums[7]

    fee1 = b1 * 180
    fee2 = b2 * 160
    total = fee1 + fee2

    print(f"\n{file}")
    print(f"宅急便個数: {b1}")
    print(f"ネコポス個数: {b2}")
    print(f"合計: {total:,}円")
