# 🚀 Quick Start: PDF Scenario Creation (< 10 minutes)

## What Was Added?

New capability to automatically create game scenarios from PDF documents using AI.

## Files Changed

1. **requirements.txt** - Added `PyPDF2` and `reportlab`
2. **pdf_scenario_parser.py** - New file that extracts text from PDFs and uses Gemini AI to generate scenarios
3. **app.py** - New endpoint `/api/scenarios/add-from-pdf` for PDF uploads
4. **test_pdf_upload.py** - Test script with sample PDF
5. **PDF_SCENARIO_GUIDE.md** - Comprehensive guide
6. **README.md** - Updated with PDF feature info

## How to Use (3 Easy Steps)

### Step 1: Install Dependencies (1 minute)

```bash
pip install -r requirements.txt
```

### Step 2: Start the Server (30 seconds)

```bash
python app.py
# Server runs on http://localhost:5000
```

### Step 3: Upload a PDF (1 minute)

**Option A - Using the Test Script:**
```bash
python test_pdf_upload.py
```

**Option B - Using cURL with your own PDF:**
```bash
curl -X POST http://localhost:5000/api/scenarios/add-from-pdf \
  -F "pdf_file=@your_document.pdf"
```

**Option C - Using Python:**
```python
import requests

with open('document.pdf', 'rb') as f:
    response = requests.post(
        'http://localhost:5000/api/scenarios/add-from-pdf',
        files={'pdf_file': f}
    )
print(response.json())
```

## What Happens?

1. ✅ PDF is uploaded
2. ✅ Text is extracted from all pages
3. ✅ Gemini AI analyzes the content
4. ✅ 3-5 game scenarios are generated automatically
5. ✅ Scenarios are saved to `scenarios.json`
6. ✅ They appear in the game during play

## Example Response

```json
{
  "success": true,
  "message": "Successfully added 4 scenarios from PDF",
  "scenarios_added": 4,
  "scenarios": [
    {
      "id": "framework_selection_001",
      "title": "Choose Agent Development Framework",
      "category": "development",
      "week_available": 3,
      "options": [...]
    }
  ]
}
```

## Best PDFs to Use

✅ Technical documentation about:
- Multi-agent systems
- Enterprise architecture
- Software development practices
- AI/ML deployment
- Platform engineering
- DevOps and operations

## Troubleshooting

**"Could not connect to server"**
→ Start the server: `python app.py`

**"PDF appears to be empty"**
→ Use a text-based PDF (not scanned images)

**"Failed to parse AI response"**
→ Try a PDF with clearer technical content

## Architecture

```
PDF Document
    ↓
[PyPDF2] Extract Text
    ↓
[Gemini AI] Analyze & Generate Scenarios
    ↓
[Scenario Manager] Save to scenarios.json
    ↓
[Game Engine] Available in gameplay
```

## Time Breakdown

- Installation: ~1 minute
- Server start: ~30 seconds
- PDF upload: ~30 seconds
- AI processing: ~1-2 minutes
- **Total: Under 5 minutes!** ⚡

## Next Steps

1. Try the test script: `python test_pdf_upload.py`
2. Upload your own PDFs about agent platforms
3. Start a new game and see your scenarios appear
4. Share PDFs with your team to create custom training scenarios

## Need Help?

See [PDF_SCENARIO_GUIDE.md](PDF_SCENARIO_GUIDE.md) for detailed examples and troubleshooting.

---

**That's it! You're ready to create scenarios from PDFs in minutes.** 🎉
