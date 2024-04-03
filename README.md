
# Streamlit OCR Application

This application allows users to upload scanned documents in various formats (JPG, JPEG, PNG, GIF, BMP) and utilizes the OCR.space API to extract text from these images. Built with Streamlit, this simple and interactive application demonstrates the power of combining OCR technology with a user-friendly web interface.

## Features

- **File Upload**: Users can upload images of scanned documents directly to the application.
- **OCR Processing**: Leveraging the OCR.space API, the application processes uploaded images to extract text.
- **Display Results**: Extracted text is displayed on the same page, providing immediate results to the user.

## Demo Video

Check out the demo video of the application in action by clicking the link below:

[View Demo Video](https://github.com/KeenSightStreamLit/OCR_POC/blob/main/video.webm)


## Installation

To run this application, you need Python installed on your system. The application also requires a virtual environment with specific packages installed.

### Steps:

1. **Clone the repository**  
   Clone this repository to your local machine using `git clone`.

2. **Create a virtual environment**  
   Navigate to the cloned directory and create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**  
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`

4. **Install required packages**  
   Install the required Python packages using the following command:
   ```bash
   pip install streamlit requests
   ```

## Usage

To run the application, navigate to the directory containing the application files and execute the following command:

```bash
streamlit run app.py
```

Open your web browser and go to the address provided in the terminal output. You can now use the application to upload images and extract text.

## Obtaining OCR.space API Key

This application requires an OCR.space API key. You can obtain a free API key by registering at [OCR.space API](https://ocr.space/OCRAPI). Replace `'helloworld'` in the script with your actual API key.

## Limitations

- The application currently supports image files up to 1MB in size.
- Supported file types are JPG, JPEG, PNG, GIF, and BMP.

## Acknowledgments

This application uses the OCR.space API for OCR processing. OCR.space is a powerful OCR engine that provides accurate and fast text extraction capabilities.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
