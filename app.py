import streamlit as st

st.set_page_config(page_title="موقع خاص ومحمي لفضايح القحبان نواف + فضايح FC  ", layout="centered")

PASSWORD = "34091837"

def check_password():
    """دالة للتحقق من الرمز المكتوب"""
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    st.title("🔒 موقع خاص ومحمي لفضايح القحبان نواف + فضايح FC  !!!!!!!!!")
    user_input = st.text_input("حط الرمز الخاص عشان تشوف فضايحه:", type="password")

    if st.button("دخول"):
        if user_input == PASSWORD:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error(" الرمز غير صحيح، حاول مرة أخرى.")
    return False


if check_password():
    st.success("دخلت لموقع فضايح القحبان !!!!!!!")
    st.title("معرض الفيديو والرسائل")

    videos_data = [
        {
            "message": "فضيحه القحبان نواف 1",
            "url": "https://continental-tomato-qxq0zmekwt.edgeone.app/f9p75pf%20(ييييييييييييييييييييييييييييي%20(1).mp3",
            "image_url": ""
        },
        {
            "message": "فضيحه القحبان نواف 2",
            "url": "https://energetic-turquoise-2grr3zfums.edgeone.app/bmr4rrt%20(1).mp3",
            "image_url": ""
        },
        {
            "message": "فضيحه القحبان تركي 3",
            "url": "https://vast-chocolate-d76pznjlr3.edgeone.app/تركي%20الممحون.mp3",
            "image_url": ""
        },
        {
            "message": "فضيحه القحبان 4",
            "url": "رابط_الملف_الصوتي_هنا",
            "image_url": "رابط_الصورة_هنا"
        },
        {
            "message": "فضيحه القحبان 5",
            "url": "رابط_الملف_الصوتي_هنا",
            "image_url": "رابط_الصورة_هنا"
        },
        {
            "message": "فضيحه القحبان 6",
            "url": "رابط_الملف_الصوتي_هنا",
            "image_url": "رابط_الصورة_هنا"
        }
    ]

    for item in videos_data:
        with st.container():
            st.markdown(f"### {item['message']}")
            
            if item["image_url"].startswith("http"):
                st.image(item["image_url"], use_container_width=True)
            
            if item["url"].startswith("http"):
                st.audio(item['url'], format="audio/mp3")
                
            st.write("---")

    if st.button("تسجيل الخروج"):
        st.session_state["password_correct"] = False
        st.rerun()
