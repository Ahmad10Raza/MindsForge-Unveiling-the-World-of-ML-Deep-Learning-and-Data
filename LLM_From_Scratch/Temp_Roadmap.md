
## **LLM from Scratch Roadmap**

### **1. Foundations Refresher (you can skim if confident)**

* **Mathematics for LLMs**
  * Linear Algebra (matrix multiplications, eigenvalues, SVD)
  * Probability & Statistics (distributions, Bayes, KL divergence, entropy)
  * Calculus (gradients, Jacobians, optimization basics)
  * Information Theory (cross-entropy, perplexity, mutual information)
* **Deep Learning Core**
  * Feedforward & CNN architectures (for intuition of layers)
  * RNNs, LSTMs, GRUs (understand why transformers replaced them)
  * Loss functions (cross-entropy, NLL, MSE)
  * Optimization (SGD, Momentum, Adam, AdamW)

---

### **2. Sequence Models Before Transformers**

* **Word Embeddings**
  * Word2Vec, GloVe, FastText
  * One-hot vs dense representations
  * Subword tokenization (BPE, WordPiece, SentencePiece)
* **Language Models Before GPT**
  * N-gram LMs (Markov assumption)
  * RNN LMs & limitations (vanishing gradients, sequential bottlenecks)

---

### **3. Transformers: The Core of LLMs**

* **Attention Mechanism**
  * Scaled Dot-Product Attention
  * Query, Key, Value representation
  * Multi-Head Attention
  * Self-Attention vs Cross-Attention
* **Transformer Architecture**
  * Encoder-Decoder (original Vaswani paper, 2017)
  * Decoder-only (GPT-style)
  * Encoder-only (BERT-style)
* **Transformer Components**
  * Position embeddings (absolute, sinusoidal, rotary)
  * LayerNorm vs BatchNorm
  * Residual connections & skip-connections
  * Feedforward layers inside transformers
  * Causal masking (autoregressive training)
* **Training Objective**
  * Next-token prediction (causal LM)
  * Masked language modeling (BERT-style)
  * Perplexity metric

---

### **4. Scaling Laws & GPT-style Models**

* **GPT-1 → GPT-2 → GPT-3**
  * Differences in architecture, dataset size, and scaling laws
  * Zero-shot, few-shot, fine-tuning concepts
* **LLaMA, Falcon, Mistral**
  * Efficient transformer modifications (grouped-query attention, sliding window attention, etc.)
* **Training Tricks**
  * Weight initialization (Xavier, Kaiming, GPT-style init)
  * Gradient clipping
  * Mixed precision (FP16, BF16)
  * Checkpointing & gradient accumulation

---

### **5. Large-Scale Training Engineering**

* **Data**
  * Collecting & cleaning web-scale datasets
  * Deduplication, filtering, toxicity removal
  * Tokenization pipeline at scale
* **Distributed Training**
  * Data parallelism
  * Model parallelism (tensor parallelism, pipeline parallelism)
  * ZeRO optimization (DeepSpeed)
  * Sharded optimizers
* **Hardware**
  * GPUs (NVIDIA A100, H100)
  * TPUs
  * Cluster orchestration (Kubernetes, Slurm, Ray)

---

### **6. Fine-Tuning & Alignment**

* **Supervised Fine-Tuning (SFT)**
  * Train on human-labeled datasets
  * Domain adaptation
* **RLHF (Reinforcement Learning with Human Feedback)**
  * Preference modeling
  * Reward models
  * PPO (Proximal Policy Optimization)
* **Instruction Tuning**
  * Training on task-like datasets (e.g., Alpaca, Dolly, Flan-T5)
* **LoRA & Parameter-Efficient Fine-Tuning**
  * Low-Rank Adaptation
  * Prefix-tuning, adapters

---

### **7. Advanced Architectures & Research**

* **Efficiency**
  * Sparse Transformers
  * Linear Attention (Performer, Linformer)
  * FlashAttention
  * KV-cache optimizations
* **Next-Gen LLMs**
  * Mixture-of-Experts (MoE, e.g., Switch Transformers)
  * Multimodal LLMs (text + image + audio)
  * Retrieval-Augmented Generation (RAG)

---

### **8. Evaluation**

* **Intrinsic Metrics**
  * Perplexity
  * Loss curves
* **Extrinsic Benchmarks**
  * GLUE, SuperGLUE
  * MMLU, BIG-bench
  * HELM, LM-Eval Harness
* **Safety & Bias**
  * Jailbreak attacks
  * Toxicity, fairness, hallucination testing

---

### **9. Deployment & Serving**

* **Inference Optimization**
  * Quantization (INT8, 4-bit, GPTQ, AWQ)
  * Pruning & distillation
  * KV-caching
* **Serving at Scale**
  * Hugging Face `transformers`
  * vLLM, TGI (Text Generation Inference)
  * Triton Inference Server
  * Streaming APIs

---

### **10. Hands-On Implementation Path**

* Step 1: Implement **Word2Vec** from scratch.
* Step 2: Build a  **tiny RNN LM** .
* Step 3: Implement **Transformer from scratch** (PyTorch).
* Step 4: Train a **tiny GPT** on a small dataset (like TinyShakespeare).
* Step 5: Scale to **GPT-2 level model** using Hugging Face + DeepSpeed.
* Step 6: Try **instruction fine-tuning** on open datasets.
* Step 7: Explore **LoRA fine-tuning** on LLaMA/Mistral.
