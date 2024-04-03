import streamlit as st
import requests

def ocr_space_file(api_key, image_file):
    """ OCR.space API request with local file.
    :param api_key: OCR.space API key.
    :param image_file: The image file to process.
    :return: Result in JSON format.
    """
    api_url = 'https://api.ocr.space/parse/image'
    payload = {
        'apikey': api_key,
        'isOverlayRequired': True,
        'language': "eng",
    }
    with open(image_file, 'rb') as file:
        response = requests.post(api_url,
                                 files={'file': file},
                                 data=payload,
                                 )
    return response.json()

st.image("logo.png", width=300)
st.title('OCR Application using Streamlit and OCR.space API')

uploaded_file = st.file_uploader("Choose scanned document", type=["jpg", "jpeg", "png", "gif", "bmp"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Save uploaded file to the server temporarily
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    st.write('Processing...')
    
    # Replace 'helloworld' with your actual OCR.space API key
    result = ocr_space_file(api_key='helloworld', image_file=uploaded_file.name)
    
    if result['OCRExitCode'] == 1:  # Check if the API call was successful
        # Extracted text is in the 'ParsedResults' part of the response
        extracted_text = result['ParsedResults'][0]['ParsedText']
        st.write('Extracted Text:')
        st.write(extracted_text)
    else:
        st.write('Error:')
        st.write(result)
else:
    st.write("Please upload an image file.")
