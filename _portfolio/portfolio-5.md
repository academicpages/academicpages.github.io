---
title: "[MGTG610] Multimodal Modeling of Product Matching: Kaggle Shopee Case Study"
excerpt: "Extended from KAIST GSDS interview project: Multimodal modeling for identifying same product listings using real-world text and image data from Shopee Kaggle Competition."
semester: "Spring-2025"
semester_sort: 202502
collection: portfolio
---

## 📝 Project Overview

This project was developed as an extension of my KAIST GSDS interview research proposal (See: [Portfolio #4](../portfolio4)).  
Building on my academic background in both Business and Computer Science, I investigated real-world applications of multimodal modeling through the lens of the Shopee Kaggle Competition. The goal was to analyze how multimodal embedding models—trained on both product images and texts enhance the prediction and what is important when building these models.

The project was presented as part of the **MGTG610 Business Data Science** course.

## 🔬 Methodology

- **Case Reference**: Shopee - Price Match Guarantee (Kaggle)
- **Data Modalities**:
  - Image: Product photos
  - Text: Titles, descriptions, and metadata
- **Model Architecture**:
  - Dual-encoder system: `eca_nfnetl1` for vision, `XLM-R` for text
  - Embedding Fusion: L2-normalization + Cosine Similarity + ArcMargin
  - Post-processing: Iterative Neighborhood Blending (INB)
- **Tools Used**: PyTorch, Faiss, Timm, HuggingFace

## 📈 Key Findings

- Shopee’s top models achieve up to **0.793 F1 score** using embedding fusion and neighborhood refinement
- Visual and textual embeddings offer **complementary signals** that boost product match accuracy
- Cultural and linguistic context may require model fine-tuning for region-specific e-commerce (Here, they used the cahya/bert-base-Indonesian-1.5G bert model that is specially tuned for Indonesian).

## 🎓 Learning Outcome

This project deepened my understanding of **cross-modal representation learning**, embedding architectures, and business implications of AI systems.  
By extending my KAIST interview topic into a real-world dataset and solution benchmark, I was able to explore not just research ideas but also production-ready model designs.

## 📎 Downloads

- [📄 Presentation Slides (PDF)](/files/Multimodal%20machine%20learning%3B%20Kaggle%20Shopee%20case.pdf)  
- [🗣️ Presentation Script (Korean)](/files/Primary%20Script.pdf)
