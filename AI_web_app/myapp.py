from api.AI import AIAPI
import streamlit as st

def get_api():
    return AIAPI(font="resources/malgun.ttf")

def main():
    api = get_api()

    st.title("2023 HAI Summer Web APP Project")
    st.subheader("책 읽어주는 인공지능")

    st.subheader("1. 글자 이미지를 넣으면 텍스트로 출력합니다.")
    response=""
    query = st.file_uploader('Input Image')
    if query is not None:
        st.image(query)
        response = api.query_image2text(query, key='image2text')
        st.markdown("**OCR 결과**")
        st.code(f"{response}", language="python")
    
    st.subheader("2. 변환된 텍스트를 요약해줍니다.")
    st.markdown("사진을 넣으면 아래의 기본 텍스트가 바뀝니다.")
    if response is not None: 
        title, summary = api.query_text2text(response)
        st.write("**제목**")
        st.write(title)
        st.write("**요약**")
        st.code(f"{summary}", language="csv")
    


if __name__ == '__main__':
    main()




