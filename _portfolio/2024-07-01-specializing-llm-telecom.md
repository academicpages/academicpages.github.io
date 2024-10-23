---
title: "Specializing Large Language Models for Telecom Applications"
excerpt: "Enhancing the Accuracy of Falcon 7.5B and Phi-2 on Telecom Knowledge Using the TeleQnA Dataset <br/><img src='/images/llm-telecom.png'>"
collection: portfolio
---


**Project Overview:**

Large language models (LLMs) have become highly proficient in text generation, comprehension, and interaction. Despite their successes across various sectors, their application in the telecommunications industry remains limited. This project focuses on optimizing LLMs, specifically using a fine-tuned model called **Phi-3-mini-4k-instruct**, to improve telecom-specific knowledge tasks. The dataset, derived from the **TeleQnA** competition, contains telecom-related multiple-choice questions, and this project aims to enhance model performance using fine-tuning techniques and model-specific optimizations.

![LLM](/images/iStock-1486380350.webp)


**Project Objectives:**

1. **Fine-tune Phi-3-mini-4k-instruct on Telecom Knowledge:**

   - Train and optimize the Phi-3-mini-4k-instruct model to accurately respond to telecom-specific questions.
   - Leverage advanced training techniques such as **LoRA (Low-Rank Adaptation)** for efficient model tuning, along with 4-bit quantization to handle large-scale data while reducing memory footprint.
2. **Overcome Common Challenges:**

   - Address the complexities of telecom-specific terminology and concepts.
   - Reduce hallucinations common in LLMs when faced with domain-specific queries.
   - Ensure responses are accurate and can be justified using telecom knowledge.

**Methodology:**

The fine-tuning process included several key steps, leveraging efficient training techniques and domain-specific adjustments to ensure optimal model performance.

1. **Data Understanding and Preparation:**

   - The project utilized the **TeleQnA** dataset, ensuring the text data was properly structured and relevant for telecom knowledge tasks.
   - Data preprocessing was performed using custom utilities to clean and prepare telecom text for model consumption.
2. **Model Selection and Fine-Tuning:**

   - **Model Choice:** The model chosen for this task is **unsloth/Phi-3-mini-4k-instruct**, a lightweight but robust variant that supports **RoPE Scaling** for extended context length.
   - **Model Fine-Tuning:**
     - Implemented parameter-efficient tuning using **QLoRA**, targeting specific layers for low-rank adaptation such as `q_proj`, `k_proj`, and `v_proj` modules, which are critical for understanding attention in telecom-specific contexts.
     ![Llora](/images/lora-qlora.png)
     - Utilized **gradient checkpointing** and memory-efficient techniques like **4-bit quantization** to minimize GPU memory consumption, making the process viable for longer sequences.
3. **Training Setup:**

   - **Training Configuration:**
     - Used **SFTTrainer** from the `trl` library to manage the fine-tuning process. This allowed for flexible configurations with customized **sequence length**, **packing** strategy, and **multi-GPU support** for telecom-specific fine-tuning.
     - Batch sizes and learning rates were optimized based on the constraints of the telecom dataset, using **AdamW optimizer with 8-bit precision** to balance performance and memory efficiency.
4. **Mitigating Hallucinations and Fabrications:**

   - Focused on limiting fabricated responses by employing **fact-checking mechanisms** and reinforcement-based techniques to penalize hallucinations during the training process.
   - Integrated post-processing steps, validating output against a trusted telecom knowledge base to ensure factual consistency.
5. **Tools and Technologies:**

   - **Python** for coding and model management.
   - **PyTorch** for model training and handling LLMs.
   - **Unsloth Libraries** for fine-tuning and efficient memory utilization.
   - **Hugging Face** for accessing pre-trained language models like Phi-3-mini-4k-instruct and custom dataset handling.

**Technical Implementation:**

The fine-tuning was implemented using the following key configurations:

- **Sequence Length:** Set to 2048 tokens to handle the longer context often found in telecom data.
- **LoRA Parameters:**
  - `r=16`, `lora_alpha=16`, with dropout and bias optimizations, ensuring efficient parameter updates during training.
- **Training Optimizations:**
  - **CUDA and GPU Settings:** Optimized for GPU usage on Tesla-class hardware, ensuring fast execution and reduced memory overhead.
  - **Batch Size Adaptation:** Dynamic batch size adjustments based on GPU memory, along with gradient accumulation to ensure stable training.

**Outcome:**

- **Enhanced Accuracy:** The model demonstrated improved performance in answering telecom-specific questions, outperforming earlier baselines like **Falcon 7.5B**.
- **Improved Resource Utilization:** By employing **4-bit quantization** and **LoRA**, the model trained effectively on large datasets without exhausting GPU resources.

**Future Work:**

- **Dataset Expansion:** Continue expanding the dataset with more specialized telecom questions and edge cases.
- **Model Scaling:** Explore scaling the fine-tuning to larger models such as **LLaMA-2** or incorporating **RAG** (Retrieval-Augmented Generation) for even more accurate responses.

**Code:**
The full implementation is available [here](https://github.com/KameniAlexNea/specializing-llm-telecom).

---

This updated version aligns with the codebase you shared and includes details such as model-specific fine-tuning (Phi-3-mini-4k), memory optimizations (4-bit quantization), and the use of LoRA. Let me know if you need further adjustments!

Code made avalaible [here](https://github.com/KameniAlexNea/specializing-llm-telecom)


<img src='/images/llm-telecom.png'>
