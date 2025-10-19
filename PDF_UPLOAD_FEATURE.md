# PDF Upload Feature

## Overview
The application now saves uploaded PDF documents to a local folder within the application codebase.

## Changes Made

### 1. Upload Folder Structure
- Created `uploads/` directory in the application root
- Added to `.gitignore` to prevent committing uploaded files

### 2. Configuration (`config.py`)
Added upload folder configuration:
```python
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'pdf'}
```

### 3. Application Updates (`app.py`)
Enhanced the PDF upload endpoint with:
- **File saving**: PDFs are saved with timestamp-prefixed filenames
- **Secure filenames**: Uses `secure_filename()` to sanitize file names
- **File size limit**: Maximum 16MB per upload
- **Automatic folder creation**: Creates upload folder if it doesn't exist

### 4. File Naming Convention
Uploaded PDFs are saved with the format:
```
YYYYMMDD_HHMMSS_original_filename.pdf
```
Example: `20251019_140530_scenario_document.pdf`

## Usage

### Upload a PDF via Web Interface
1. Click "📄 Upload PDF Scenario" button on the welcome screen
2. Select a PDF file
3. The file will be:
   - Saved to `uploads/` folder
   - Processed by AI to extract scenarios
   - Added to the game

### Upload a PDF via API
```bash
curl -X POST http://localhost:5000/api/scenarios/add-from-pdf \
  -F "pdf_file=@/path/to/document.pdf"
```

Response includes:
```json
{
  "success": true,
  "message": "Successfully added 3 scenarios from PDF",
  "scenarios_added": 3,
  "pdf_saved_as": "20251019_140530_document.pdf",
  "scenarios": [...]
}
```

### Test the Feature
Run the included test script:
```bash
python3 test_pdf_upload.py
```

This will:
1. Create a sample PDF document
2. Upload it to the server
3. Verify the upload was successful
4. Display the extracted scenarios

## Directory Structure
```
/workspace/
├── app.py                  # Main application with upload handling
├── config.py              # Configuration including UPLOAD_FOLDER
├── uploads/               # Uploaded PDFs stored here
│   └── YYYYMMDD_HHMMSS_*.pdf
├── test_pdf_upload.py     # Test script
└── ...
```

## Security Features
- **File type validation**: Only `.pdf` files accepted
- **Filename sanitization**: Uses `secure_filename()` to prevent path traversal
- **Size limits**: 16MB maximum file size
- **Timestamp prefixes**: Prevents filename collisions

## Benefits
1. **Audit trail**: All uploaded PDFs are preserved for review
2. **Reprocessing**: PDFs can be reprocessed if needed
3. **Debugging**: Easier to debug issues with specific documents
4. **Compliance**: Maintains records of uploaded content
