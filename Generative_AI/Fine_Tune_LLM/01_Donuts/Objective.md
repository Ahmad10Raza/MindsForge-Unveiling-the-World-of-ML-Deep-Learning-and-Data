### **Objective Statement:**

> To build a custom AI-powered document understanding system using the `donut-base or LLM` model that can automatically extract structured keywords (e.g., invoice number, date, vendor, amount) from unstructured **English invoice documents** (both scanned and text PDFs), and return the extracted information in a clean  **JSON format** , without relying on OCR engines.

---

#### **Key Goals:**

1. ✅ **Train a layout-aware model** on a custom dataset of English invoices using the `donut-base` or `LLM` model.
2. ✅ **Enable support for both scanned and text-based PDFs** by converting them into images and leveraging Donut’s vision-text transformer architecture.
3. ✅ **Eliminate the need for OCR** by using Donut’s image-to-sequence prediction capability.
4. ✅ **Automatically extract relevant invoice fields** like:
   * Invoice Number
   * Invoice Date
   * Vendor Name
   * Total Amount
   * Payment Due Date (if applicable)
5. ✅ **Generate structured outputs** in machine-readable JSON format.
6. ✅ **Build an inference pipeline or deploy as an API** for integration into downstream systems (e.g., ERP, finance automation).

---

#### 📌 **Why This Project Matters**

* Traditional OCR systems fail or require heavy template engineering when dealing with varied invoice formats.
* Many invoices have  **non-standard layouts** , especially when scanned.
* This approach uses a **generalizable, layout-aware, OCR-free** transformer that can be fine-tuned on your domain-specific data for high accuracy.
