
---

### **1. Feedforward Neural Networks (FNN)**

- **Description**: Basic neural networks where information flows in one direction (input → output).
- **Sub-models**:
  - **Multilayer Perceptron (MLP)** – A simple stack of fully connected layers.
  - **Autoencoder** – Used for unsupervised learning (encoder-decoder structure).
    - **Variational Autoencoder (VAE)** – Probabilistic twist for generative tasks.
    - **Denoising Autoencoder** – Learns to reconstruct clean data from noisy inputs.
    - **Sparse Autoencoder** – Introduces sparsity constraints.

---

### **2. Convolutional Neural Networks (CNN)**

- **Description**: Specialized for grid-like data (images, videos).
- **Sub-models & Architectures**:
  - **LeNet-5** (Yann LeCun) – Early CNN for digit recognition.
  - **AlexNet** (Krizhevsky et al.) – Deep CNN with ReLU and dropout.
  - **VGGNet** (Simonyan & Zisserman) – Deeper networks with small 3x3 filters.
  - **ResNet** (He et al.) – Introduced residual connections ("skip connections").
  - **Inception (GoogLeNet)** – Uses parallel convolutions (1x1, 3x3, 5x5).
  - **EfficientNet** – Scalable CNN with compound scaling.
  - **MobileNet** – Lightweight CNN for mobile devices (depthwise separable convolutions).
  - **DenseNet** – Connects all layers directly to improve feature reuse.
  - **U-Net** – For image segmentation (encoder-decoder with skip connections).
  - **YOLO (You Only Look Once)** – Real-time object detection.
  - **SSD (Single Shot MultiBox Detector)** – Another object detection model.

---

### **3. Recurrent Neural Networks (RNN)**

- **Description**: For sequential/temporal data.
- **Sub-models & Architectures**:
  - **Vanilla RNN** – Basic RNN with recurrent connections.
  - **Long Short-Term Memory (LSTM)** – Addresses vanishing gradients with gating.
  - **Gated Recurrent Unit (GRU)** – Simplified LSTM with fewer gates.
  - **Bidirectional RNN (BiRNN)** – Processes sequences forward and backward.
  - **Attention Mechanisms** – Enhances RNNs with focus on relevant parts.
  - **Transformer** (Vaswani et al.) – Replaced RNNs with self-attention.
    - **BERT (Bidirectional Encoder Representations from Transformers)** – Pre-trained for NLP.
    - **GPT (Generative Pre-trained Transformer)** – Autoregressive language model.
    - **T5 (Text-to-Text Transfer Transformer)** – Unified text-to-text model.
    - **ViT (Vision Transformer)** – Applies transformers to images.

---

### **4. Generative Models**

- **Description**: Generate new data samples.
- **Sub-models & Architectures**:
  - **Generative Adversarial Networks (GANs)**:
    - **DCGAN** (Deep Convolutional GAN) – CNN-based GAN.
    - **CycleGAN** – Unpaired image-to-image translation.
    - **StyleGAN** (NVIDIA) – High-quality face generation.
  - **Variational Autoencoders (VAE)** – Probabilistic generative model.
  - **Diffusion Models** – Generate data via iterative denoising.
    - **Stable Diffusion** – Text-to-image generation.
    - **DALL-E** (OpenAI) – CLIP + Diffusion for image generation.

---

### **5. Reinforcement Learning (RL) with Deep Learning**

- **Description**: Combines deep learning with RL.
- **Sub-models & Architectures**:
  - **Deep Q-Network (DQN)** – Q-learning with CNNs.
  - **Policy Gradient Methods** (e.g., **PPO, A3C**).
  - **AlphaGo/AlphaZero** (DeepMind) – Combines RL + Monte Carlo Tree Search.

---

### **6. Graph Neural Networks (GNN)**

- **Description**: For graph-structured data.
- **Sub-models & Architectures**:
  - **Graph Convolutional Network (GCN)** – Applies convolution to graphs.
  - **Graph Attention Network (GAT)** – Uses attention mechanisms.
  - **GraphSAGE** – Inductive learning on graphs.

---

### **7. Self-Supervised & Contrastive Learning**

- **Description**: Learns from unlabeled data.
- **Sub-models & Architectures**:
  - **SimCLR** – Contrastive learning for visual representations.
  - **MoCo (Momentum Contrast)** – Improves contrastive learning.
  - **BYOL (Bootstrap Your Own Latent)** – Self-supervised without negatives.

---

### **8. Other Notable Architectures**

- **Capsule Networks (CapsNet)** – Hinton’s alternative to CNNs.
- **Neural Turing Machines (NTM)** – Memory-augmented networks.
- **Spatial Transformer Networks (STN)** – Learns spatial transformations.

---
