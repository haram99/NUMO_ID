import streamlit as st
import os

def main():
    st.set_index = False
    st.set_page_config(page_title="Student File Portal", page_icon="📄")
    
    st.title("🎓 السجل الأكاديمي")
    st.write("ادخل رقم الهوية")

    # User Input
    student_id = st.text_input("", placeholder="e.g., 10000000001").strip()

    if st.button("بحث"):
        if student_id:
            file_path = f"files/{student_id}.pdf"
            
            if os.path.exists(file_path):
                st.success(f"الملف موجود للهوية: {student_id}")
                
                with open(file_path, "rb") as f:
                    file_bytes = f.read()
                
                # 1. Download Button
                st.download_button(
                    label="⬇️ Download PDF",
                    data=file_bytes,
                    file_name=f"{student_id}.pdf",
                    mime="application/pdf"
                )

                # 2. Print Instructions (No visual PDF preview underneath)
                st.info("💡 To print: Click 'Download PDF' above, open the file, and press Ctrl+P (or Cmd+P on Mac).")
                
            else:
                st.error(f"لم يتم العثور على ملف برقم الهوية: {student_id}")
        else:
            st.warning("الرجاء إدخال رقم الهوية أولاً.")

if __name__ == "__main__":
    main()
