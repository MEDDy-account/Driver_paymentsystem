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
# 数字を全部取得
nums = [int(x) for x in re.findall(r"\d+", text)]

print("\n抽出数字")
print(nums)

if len(nums) < 8:
    raise ValueError("必要な数字が取得できませんでした")

# OCR結果の位置から取得
b1 = nums[3]
b2 = nums[7]

print(f"宅急便個数: {b1}")
print(f"ネコポス個数: {b2}")

fee1 = b1 * 180
fee2 = b2 * 160

total = fee1 + fee2

print("\n===== 集計 =====")
print(f"宅急便売上: {fee1:,}円")
print(f"ネコポス売上: {fee2:,}円")
print(f"合計: {total:,}円")
print("sales_history.csv に保存しました")
