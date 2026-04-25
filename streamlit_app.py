import os
import streamlit as st
import streamlit.components.v1 as components

VISITOR_FILE = "visitor_ids.txt"
VISITOR_STORAGE_KEY = "foodbridge_visitor_id"

# เก็บ unique visitor id ลงไฟล์ และคืนค่าสุดท้ายของจำนวน unique visitor
def get_unique_visitor_count(visitor_id: str) -> int:
    if not visitor_id:
        return 0

    visitor_ids = set()
    if os.path.exists(VISITOR_FILE):
        with open(VISITOR_FILE, "r") as f:
            visitor_ids = {line.strip() for line in f if line.strip()}

    if visitor_id not in visitor_ids:
        with open(VISITOR_FILE, "a") as f:
            f.write(visitor_id + "\n")
        visitor_ids.add(visitor_id)

    return len(visitor_ids)

# รับ visitor_id จาก query params แล้ว redirect หากยังไม่มี
params = st.experimental_get_query_params()
visitor_id = params.get("visitor_id", [None])[0]

if visitor_id is None:
    components.html(
        f"""
        <script>
          const STORAGE_KEY = "{VISITOR_STORAGE_KEY}";
          let visitorId = localStorage.getItem(STORAGE_KEY);
          if (!visitorId) {{
            visitorId = crypto.randomUUID ? crypto.randomUUID() :
              (Math.random().toString(36).substring(2) + Date.now().toString(36));
            localStorage.setItem(STORAGE_KEY, visitorId);
          }}
          const searchParams = new URLSearchParams(window.location.search);
          if (searchParams.get("visitor_id") !== visitorId) {{
            searchParams.set("visitor_id", visitorId);
            window.location.search = searchParams.toString();
          }}
        </script>
        """,
        height=0,
    )
    st.stop()

visitor_count = get_unique_visitor_count(visitor_id)

st.title("Wait listed... ทางทีมเรายินดีเป็นอย่างสูงที่ท่านแสดงความสนใจ")
st.write("ทางทีมพัฒนาของเรากำลังพัฒนาเว็ปไซต์อยู่ ณ ขณะนี้ โปรดติดตาม!")

st.metric("จำนวนผู้เข้าชมเว็บไซต์", visitor_count)
