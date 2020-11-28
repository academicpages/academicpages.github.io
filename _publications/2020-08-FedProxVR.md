---
title: "Federated Learning with Proximal Stochastic Variance Reduced Gradient Algorithms"
collection: publications
permalink: /publication/2020-08-FedProxVR
date: 2020-08-17
venue: "ICPP '20: 49th International Conference on Parallel Processing"
citation: "Canh T. Dinh, Nguyen H. Tran, Tuan Dung Nguyen, Wei Bao, Albert Y. Zomaya, and Bing B. Zhou. 2020. Federated Learning with Proximal Stochastic Variance Reduced Gradient Algorithms. In 49th International Conference on Parallel Processing - ICPP (ICPP '20). doi: 10.1145/3404397.3404457"
---

[[Paper](https://dl.acm.org/doi/10.1145/3404397.3404457)] [[Video](https://www.youtube.com/watch?v=cXsFYcXF0KM)]

Abstract: Federated Learning (FL) is a fast-developing distributed machine learning technique involving the participation of a massive number of user devices. While FL has benefits of data privacy and the abundance of user-generated data, its challenges of heterogeneity across users’ data and devices complicate algorithm design and convergence analysis. To tackle these challenges, we propose an algorithm that exploits proximal stochastic variance reduced gradient methods for non-convex FL. The proposed algorithm consists of two nested loops, which allow user devices to update their local models approximately up to an accuracy threshold (inner loop) before sending these local models to the server for global model update (outer loop). We characterize the convergence conditions for both local and global model updates and extract various insights from these conditions via the algorithm’s parameter control. We also propose how to optimize these parameters such that the training time of FL is minimized. Experimental results not only validate the theoretical convergence but also show that the proposed algorithm outperforms existing Stochastic Gradient Descent-based methods in terms of convergence speed in FL setting.
