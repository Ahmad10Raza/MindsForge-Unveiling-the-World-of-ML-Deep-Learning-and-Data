
## 🧭 Roadmap: Custom Donut-Based Invoice Keyword Extractor

---

### ✅ **Phase 1: Environment Setup**

#### 1.1 Install Dependencies

```bash
pip install transformers datasets pytorch torchvision torchaudio
pip install accelerate sentencepiece
pip install pdf2image opencv-python
```

#### 1.2 Install Poppler (for PDF to image)

* **Ubuntu:**

  ```bash
  sudo apt install poppler-utils
  ```
* **Windows:**

  Download Poppler: [https://blog.alivate.com.au/poppler-windows/](https://blog.alivate.com.au/poppler-windows/) and add it to PATH.

---

### ✅ **Phase 2: Data Preparation**

#### 2.1 Convert PDF to Image (JPEG)

```python
from pdf2image import convert_from_path
images = convert_from_path("invoice.pdf", dpi=200)
for i, img in enumerate(images):
    img.save(f"invoice_page_{i}.jpg")
```

---

#### 2.2 Create Ground Truth (Labeling)

Use [Label Studio](https://labelstud.io/) or manual JSON creation.

Format the label as:

```json
{
  "image": "invoice_01.jpg",
  "ground_truth": {
    "invoice_number": "INV-981",
    "invoice_date": "2025-06-01",
    "vendor": "ABC Pvt Ltd",
    "amount": "$1,200.00"
  }
}
```

---

#### 2.3 Convert JSON to Donut Token Format

Transform above JSON to flat text string format:

```xml
<s_invoice><invoice_number>INV-981</invoice_number><invoice_date>2025-06-01</invoice_date><vendor>ABC Pvt Ltd</vendor><amount>$1,200.00</amount></s_invoice>
```

Final dataset format:

```json
{
  "image": "invoice_01.jpg",
  "text_input": "<s_invoice><invoice_number>INV-981</invoice_number>...</s_invoice>"
}
```

---

### ✅ **Phase 3: Dataset Loader (HuggingFace)**

```python
from datasets import load_dataset, Dataset
from PIL import Image
from transformers import DonutProcessor

processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base")

def preprocess(example):
    image = Image.open(example["image"]).convert("RGB")
    pixel_values = processor(image, return_tensors="pt").pixel_values.squeeze()
    input_ids = processor.tokenizer(example["text_input"], add_special_tokens=False, return_tensors="pt").input_ids.squeeze()
    return {
        "pixel_values": pixel_values,
        "labels": input_ids
    }

# Load your JSON list of samples
dataset = load_dataset("json", data_files="invoices.json")["train"]
dataset = dataset.map(preprocess)
```

---

### ✅ **Phase 4: Fine-Tuning Donut**

```python
from transformers import VisionEncoderDecoderModel, Seq2SeqTrainingArguments, Seq2SeqTrainer

model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base")

training_args = Seq2SeqTrainingArguments(
    output_dir="./donut-invoice-model",
    per_device_train_batch_size=2,
    num_train_epochs=5,
    save_total_limit=2,
    predict_with_generate=True,
    logging_dir="./logs",
    logging_steps=10,
    fp16=True
)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=processor.tokenizer,
)

trainer.train()
```

---

### ✅ **Phase 5: Inference Pipeline**

```python
from transformers import DonutProcessor
from PIL import Image

model = VisionEncoderDecoderModel.from_pretrained("./donut-invoice-model")
processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base")

image = Image.open("test_invoice.jpg").convert("RGB")
pixel_values = processor(image, return_tensors="pt").pixel_values

generated_ids = model.generate(pixel_values)
output = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

print("🔍 Extracted JSON-like text:\n", output)
```

---

### ✅ **Phase 6: Postprocessing (Convert Text to JSON)**

```python
import xml.etree.ElementTree as ET

def donut_output_to_json(text):
    text = text.replace("<s_invoice>", "<invoice>").replace("</s_invoice>", "</invoice>")
    root = ET.fromstring(text)
    return {child.tag: child.text for child in root}

parsed = donut_output_to_json(output)
print(parsed)
```

---

### ✅ **Phase 7: Optional - API Deployment**

Use FastAPI to serve predictions:

```bash
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI, UploadFile, File
import io

app = FastAPI()

@app.post("/extract/")
async def extract(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    pixel_values = processor(image, return_tensors="pt").pixel_values
    output_ids = model.generate(pixel_values)
    output = processor.batch_decode(output_ids, skip_special_tokens=True)[0]
    return donut_output_to_json(output)
```

Run:

```bash
uvicorn app:app --reload
```

---

## ✅ Deliverables You'll Have After This Roadmap:

* ✅ Trained Donut model on your **English invoices**
* ✅ Inference script that extracts keywords
* ✅ JSON output for downstream use
* ✅ Optional API for integration
