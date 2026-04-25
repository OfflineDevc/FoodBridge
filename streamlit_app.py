import streamlit as st
import os

# ฟังก์ชันสำหรับนับผู้เข้าชม
def get_visitor_count():
    count_file = "visitor_count.txt"
    if os.path.exists(count_file):
        with open(count_file, "r") as f:
            count = int(f.read().strip())
    else:
        count = 0
    count += 1
    with open(count_file, "w") as f:
        f.write(str(count))
    return count

# เรียกฟังก์ชันนับผู้เข้าชม
visitor_count = get_visitor_count()

st.title("Wait listed... ทางทีมเรายินดีเป็นอย่างสูงที่ท่านแสดงความสนใจ")
st.write(
    "ทางทีมพัฒนาของเรากำลังพัฒนาเว็ปไซต์อยู่ ณ ขณะนี้ โปรดติดตาม!"
)

# แสดงจำนวนผู้เข้าชม
st.metric("จำนวนผู้เข้าชมเว็บไซต์", visitor_count)
