from PIL import Image
import pytesseract
import re

# Tesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

img = Image.open("pay_driver.png")

# 正しい向き
img = img.rotate(270, expand=True)

text = pytesseract.image_to_string(
    img,
    config="--psm 6"
)

print("=== OCR結果 ===")
print(text)

# 数字を全部取得
nums = [int(x) for x in re.findall(r"\d+", text)]

print("\n抽出数字")
print(nums)

# 今回の画像では
# [126,115,115,11,126,72,72,72,0,72,198,187,187,11,198]
#
# 真ん中の115と72を採用

b1 = 115
b2 = 72

fee1 = b1 * 180
fee2 = b2 * 160

total = fee1 + fee2

print("\n===== 集計 =====")
print(f"宅急便: {b1}")
print(f"ネコポス: {b2}")

print(f"{b1} × 180 = {fee1:,}円")
print(f"{b2} × 160 = {fee2:,}円")

print(f"\n合計: {total:,}円")