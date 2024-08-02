---
title: "Object Detection Using Transformers"
excerpt: "Developing a Machine Learning Algorithm for Accurate Counting of Roof Types in Rural Malawi Using Aerial Imagery <br/><img src='/images/object-detr.png'>"
collection: portfolio
---

---

**Project Title: Developing a Machine Learning Algorithm for Accurate Counting of Roof Types in Rural Malawi Using Aerial Imagery**

**Project Overview:**

The people of Malawi have faced numerous natural disasters and climatic shocks in recent years, such as droughts, floods, and landslides. These events, compounded by the impacts of Covid-19 and other global issues, have severely affected the health and well-being of most Malawians. Rural areas, where more than 80% of the population resides, have been particularly hard-hit. Accurate mapping of flood extents and corresponding damages using satellite imagery has seen significant progress globally. However, there remain substantial gaps in accurately determining the number of affected populations, especially in rural Malawi. Traditional grass-thatched roofs in rural areas are often missed by algorithms using satellite or aerial imagery to count populations or identify buildings affected by floods.

**Project Objectives:**

1. **Accurate Counting of Roof Types:**

   - Develop a machine-learning algorithm to accurately count the number of grass-thatch, tin, and other roofed houses in aerial (drone) imagery.
   - Improve the estimates of affected populations during natural disasters, ensuring effective evacuation and aid distribution in rural Malawi.
2. **Enhanced Disaster Response:**

   - Provide accurate data that helps in improving response times and saving lives by ensuring that the most affected communities receive timely assistance.

**Methodology:**

The project employs several state-of-the-art machine learning models to achieve the objectives:

1. **[Data Collection and Labeling](https://zindi.africa/competitions/arm-unicef-disaster-vulnerability-challenge/data):**

   - Aerial imagery has been collected over parts of Malawi, and these images have been labeled to identify different types of roofs: grass-thatch, tin, and others.
   - The dataset comprises 4,772 images for training and 2,045 images for testing.
2. **Model Development and Training:**

   - Several models are employed and evaluated for their performance in accurately identifying and counting different roof types:
     - **DETR (Detection Transformer) 50**
     - **CondDETR (Conditional DETR) 50**
     - **DETA 50**
     - **DETR 101**
     - **Yolos (You Only Look One-level Small) Base and Small**
     - **DETR-50-dc5**
   - Each model is trained on the provided dataset, with specific attention to the diverse structures of rural houses in Malawi, which are typically circular or rectangular with mud-built walls and grass-thatched roofs.
3. **Evaluation and Fine-Tuning:**

   - Models are evaluated based on their accuracy in counting roof types, with specific metrics such as Intersection over Union (IoU) and other relevant performance indicators.
   - Fine-tuning involves adjusting thresholds and improving model predictions to enhance accuracy, especially for minority classes like 'Other' roof types.

**Tools and Technologies:**

- **Python:** The primary programming language used for developing and implementing the models.
- **PyTorch:** The main deep learning framework utilized for building and training the models.
- **Google Colab:** An online platform providing GPU resources for running experiments and facilitating collaborative development.

**Domain Knowledge:**

- **Geospatial Analysis:** Understanding the principles of geospatial data and imagery analysis to effectively interpret aerial images.
- **Machine Learning:** Expertise in developing and fine-tuning machine learning models for image recognition and object detection.
- **Disaster Response and Management:** Knowledge of the requirements and challenges in disaster response to ensure the developed solution is practical and effective in real-world scenarios.

**Project Report:**

The project's results, methodologies, and findings are documented comprehensively, detailing the techniques used, experiments conducted, and outcomes observed. This documentation provides insights into the model's performance and highlights areas for future improvements.

**Outcome and Future Work:**

- **Improved Disaster Management:**

  - By accurately counting roof types and estimating affected populations, the project aims to enhance disaster response strategies, ensuring timely and efficient aid distribution in rural Malawi.
- **Model Generalization:**

  - Future work includes improving the generalizability of the models to other regions and incorporating additional features to handle different types of disasters and dwelling structures.
- **Continuous Improvement:**

  - Ongoing research and collaboration with local authorities and disaster management agencies to refine the models and incorporate feedback for better performance.



<img src='/images/object-detr.png'>
