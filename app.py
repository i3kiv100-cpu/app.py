import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="موقع خاص ومحمي لفضايح القحبان نواف ", layout="centered")

# --- كلمة السر ---
PASSWORD = "101909"  #


def check_password():
    """دالة للتحقق من الرمز المكتوب"""
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    # شاشة إدخال الرمز
    st.title("🔒 موقع فضايح نواف !!!!!!!!!")
    user_input = st.text_input("حط الرمز الخاص عشان تشوف فضايحه:", type="password")

    if st.button("دخول"):
        if user_input == PASSWORD:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ الرمز غير صحيح، حاول مرة أخرى.")
    return False


# --- تشغيل التطبيق ---
if check_password():
    # هنا يوضع المحتوى الذي لا يظهر إلا بعد كتابة الرمز
    st.success("دخلت لموقع فضايح القحبان !!!!!!!")
    st.title(" معرض الفيديو والرسائل")

    # قائمة البيانات
   videos_data = 
[
        {
            "message": "فضيحه القحبان الاولى",
            "url": "https://continental-tomato-qxq0zmekwt.edgeone.app/f9p75pf%20(ييييييييييييييييييييييييييييي%20(1).mp3",
            "image_url": "https://implicit-crimson-st2bbo1q1z.edgeone.app/Screenshot%202026-04-01%20181109.png"
        },
        {
            "message": "فضيحه القحبان 2",
            "url": "https://energetic-turquoise-2grr3zfums.edgeone.app/bmr4rrt%20(1).mp3",
            "image_url": "https://implicit-crimson-st2bbo1q1z.edgeone.app/Screenshot%202026-04-01%20181109.png"
        },
        {
            "message": "فضيحه القحبان تركي  3",
            "url": "https://vast-chocolate-d76pznjlr3.edgeone.app/تركي%20الممحون.mp3",
            "image_url": "https://implicit-crimson-st2bbo1q1z.edgeone.app/Screenshot%202026-04-01%20181109.png"
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
    # عرض المقاطع
    for item in videos_data:
        with st.container():
            st.markdown(f"### {item['message']}")
            # التعديل هنا فقط: تحويل من فيديو إلى صوت
            st.audio(item['url'], format="audio/mp3")
            st.write("---")

    # زر لتسجيل الخروج
    if st.button("تسجيل الخروج"):
        st.session_state["password_correct"] = False
        st.rerun()
