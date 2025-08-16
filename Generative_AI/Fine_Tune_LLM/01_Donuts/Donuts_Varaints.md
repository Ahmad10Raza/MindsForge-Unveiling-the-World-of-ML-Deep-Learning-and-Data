
---

## 📦 Available Donut Model Variants (with Parameters)

| Model Name                                             | Parameters | Description                                                                                                         |
| ------------------------------------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------- |
| `donut-base`                                         | ~120M      | General-purpose small model for lightweight tasks<br />Note: We are going this model beaucse it match out use cases |
| `donut-small`                                        | ~77M       | Lightweight variant, faster but less accurate                                                                       |
| `naver-clova-ix/donut-base-finetuned-docvqa`         | ~120M      | Fine-tuned for**document QA**on DOCVQA dataset (ideal for form-like data)                                     |
| `naver-clova-ix/donut-base-finetuned-rvlcdip`        | ~120M      | Fine-tuned for**document classification**                                                                     |
| `naver-clova-ix/donut-base-finetuned-cord-v2`        | ~120M      | Fine-tuned for**receipt/invoice understanding**(CORD dataset)                                                 |
| `naver-clova-ix/donut-base-finetuned-synthdog-naver` | ~120M      | Trained on**synthetic receipts/invoices** , good base for fine-tuning                                         |
| `naver-clova-ix/donut-base-finetuned-zh-synthdog`    | ~120M      | Fine-tuned on**Chinese**synthetic receipts                                                                    |

---

## 🔍 Model Variant Details

### 1. **`donut-base`**

* General-purpose pretrained model.
* ✅ Best for: Custom fine-tuning on your own data.
* ❌ Doesn't perform well out-of-the-box.

### 2. **`donut-small`**

* Lower memory & faster inference (~77M params).
* ✅ Use for quick prototyping.
* ❌ Lower accuracy than base model.

### 3. **`donut-base-finetuned-docvqa`**

* Fine-tuned for **question-answering** from documents.
* Input: document image + question
* Output: answer (text)
* ✅ Use if you want to ask specific questions like: *"What is the invoice number?"*

### 4. **`donut-base-finetuned-cord-v2`**

* Trained on the **CORD** dataset (public Korean receipts).
* Structured field extraction from receipts.
* ✅ Closest to **invoice keyword extraction**
* ❌ Needs domain adaptation for Indian-style invoices

### 5. **`donut-base-finetuned-synthdog-naver`**

* Trained on large **synthetic invoice + receipt** dataset (SynthDog).
* ✅ Excellent starting point for your own fine-tuning on real invoices.

---

## 🧠 Recommended Model for You

| Situation                                   | Best Model                                        |
| ------------------------------------------- | ------------------------------------------------- |
| Starting from scratch                       | `donut-base`                                    |
| Invoices/receipts base available            | `donut-base-finetuned-synthdog-naver`           |
| You want fast inference + light             | `donut-small`                                   |
| Want to fine-tune for structured extraction | `donut-base`or `donut-base-finetuned-cord-v2` |

---

## 🛠️ Tip for Fine-Tuning

When fine-tuning on your data:

* Start with `donut-base-finetuned-synthdog-naver` if your invoices are invoice-style (contains amount, date, ID, etc.)
* Else, start with `donut-base` and customize
