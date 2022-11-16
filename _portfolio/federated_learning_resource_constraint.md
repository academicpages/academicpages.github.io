---
title: "Tackling Resource Constraints in Federated Learning"
excerpt: "Discussion of two papers tackling two different resource constraints in Federated Learning
<br/><img src='/images/fl_intro.png'>"
collection: portfolio
---

![fl_intro.png](/images/fl_intro.png "[Source: https://blog.ml.cmu.edu/2019/11/12/federated-learning-challenges-methods-and-future-directions/]")
*[Source: https://blog.ml.cmu.edu/2019/11/12/federated-learning-challenges-methods-and-future-directions/]*

## Why Federated Learning?
Traditional AI training requires all data to be stored in one place. Even if data were not stored in one place, they had to be streamed to one place for training.

But we have distributed training for that, then what is the problem?

Even with distributed training, all the nodes and infrastructure have to be owned by one entity. It solves the huge data issue, but not data ownership, as it still has to be controlled by one entity.

Also, all companies do not have the means to spin up expensive hardware for high-volume training. So it becomes a limiting factor for new companies with less funding.

You and I should be able to give our data to these companies to get the benefits of deep learning models, but without actually giving them the data.

Additionally, data privacy concerns also motivate us to explore distributed training with heterogeneous devices. Organizations such as hospitals, and other non-profit entities with limited training resources, can collaboratively train large models without revealing their datasets.

There comes Federated Learning…

## Challenges of Federated Learning
If training is done on heterogeneous devices without data being shared, the challenges are mainly because of **Non-IID data** and the **Unreliability of devices**.

**Non-IID data**: Data is not independent and identically distributed across nodes as in distributed learning. The training performance may vary significantly according to the unbalancedness of local data samples as well as the probability distribution of the training examples at each node.

**Unreliable devices**: Devices can vary from small IoT EDGE devices to phones and sometimes servers. All have varying computing, storage, and network connectivity. So the training process has to be robust enough for all the failures and limitations of the nodes in the network.

In this write-up, we will be looking at two papers that tackle unreliable device issues from two different angles. This write-up is a detailed view of a presentation that me and my teammate Laxman did for our graduate course. Check out the tackling Non-IID data part [here](https://medium.com/@lk2970/tackling-non-independent-and-identically-distributed-data-in-federated-learning-a9f4f5614ca3).

## Group Knowledge Transfer: Federated Learning of Large CNNs at the Edge
This paper [1] tackles the compute constraint problem at EDGE devices. This is a classic problem in federated learning systems where low-compute phones and IoT devices are also part of the network. To handle this, they combine the advantages of Split learning (model split into large and small; large in server and small replicated in all nodes. Trained using passing weights from the split layer across the network), Federated learning (model replicated in clients and server; gradients shared periodically ) and Knowledge Distillation (transfers weights learned from server to all clients).

![fl_sl.png](/images/fl_sl.png "[Source: https://arxiv.org/abs/2007.14513]")
*(a) Federated learning where the entire model is trained in all clients and weights are aggregated at the server. (b) Split learning is where the forward and backward passes are happening across the network. (c) The author's approach is where only the hidden feature vector learning at the client is shared with the server.*

Model parallelism by split learning attempts to break the computational constraint by splitting W into two portions and offloading the larger portion into the server side, but a single mini-batch iteration requires remote forward propagation and backpropagation. For edge computing, such a highly frequent synchronization mechanism may lead to a severe straggler problem that significantly slows down the training process. As shown in the figure above, the communication bandwidth for transferring H_i(k) to the server is substantially less than communicating all model parameters as is done in traditional federated learning.

The authors demonstrate training large CNN models with small devices that cannot train large models individually.

A large CNN is divided into a small feature extraction model and a large-scale server-side model. A simple classification layer is added at all the edge nodes to create a small but fully trainable model on the edge. The figure (from the paper) below is a clear depiction

![](/images/kt_cnn.png "[Source: https://arxiv.org/abs/2007.14513]")

The server model and the edge models are trained simultaneously using cross-entropy and knowledge distillation loss.

Knowledge distillation is transferring “knowledge” from a large model to a small model without loss of accuracy. Knowledge here refers to the softmax logits learned at the server. After the server is done with a round of training, these logits are broadcasted to all the nodes. The nodes then use KL divergence loss along with their cross-entropy loss to minimize the difference in their softmax output with that received from the server.

In this paper, they propose an additional “Bidirectional mutual learning”. Wherein, both the server and the clients learn from each other. The loss functions at the server and each of the client is given below (from paper)

![](/images/kt_cnn_loss.png "[Source: https://arxiv.org/abs/2007.14513]")

l_s is the loss function at the server and l_c(k) is the loss function at the kth client. The second summation term is the KL divergence loss minimizing the difference between the logits from the client (p_k) and the server (p_s). Experimentally it was seen that this is more helpful than the classical one-way knowledge distillation as the dataset becomes increasingly difficult. This training approach is named FedGKT standing for Federated Group Knowledge Transfer.

The KL divergence loss appears to attempt to bring the soft label and the ground truth closer together. As a result, the server model incorporates the knowledge gained from each of the edge models. Similarly, the edge models attempt to bring their predictions closer to the server model’s prediction, absorbing server model knowledge in the process to improve their feature extraction capability.

Without Group Knowledge Transfer, each client would be expected to train its feature extractor sufficiently to produce an accurate hidden feature for any input image. However, in Federated Learning systems, the dataset on each edge device may be small, making training a CNN-based feature extractor solely on the local dataset insufficient.

Also, since the server does not need to wait for updates from all clients to start training, FedGKT naturally supports asynchronous training

FedGKT can efficiently train small CNNs on edge devices and periodically transfer their knowledge to a server-side CNN with a large capacity via knowledge distillation. FedGKT achieves several benefits in a single framework: reduced edge computation demand, lower communication cost for large CNNs, and asynchronous training, all while maintaining model accuracy comparable to Federated Learning. The source code is released at [FedML](https://fedml.ai/).

## Moshpit SGD: Communication-Efficient Decentralized Training on Heterogeneous Unreliable Devices
This paper [2] tackles the unreliable network problem. They propose an iterative averaging protocol that allows communication-efficient and fault-tolerant all-reduce protocols that significantly reduce network load and are able to operate in unreliable hardware and network conditions.

This is truly a decentralized training paradigm.

Usually distributed training can utilize hundreds of computers via specialized message-passing protocols such as Ring All-Reduce. Averaging protocols like Butterfly, Ring or Tree, etc All-Reduce enable highly efficient averaging but they cannot tolerate node failures or network instability. However, running these protocols at scale requires reliable high-speed networking that is only available in dedicated clusters. Again a theme that cannot be expected in real-world FL applications.

As a result, these applications are restricted to using parameter servers or gossip-based averaging protocols.

In gossip protocols, however, the communication required to perform gossip grows linearly with the number of neighbors. Hence, when scaling to hundreds of peers, decentralized SGD has to keep the communication graph sparse which slows down the convergence of the model.

In this algorithm, instead of relying on a predefined communication graph, participants dynamically organize themselves into groups using a fully decentralized matchmaking algorithm which is named Moshpit All-Reduce. In Moshpit All-Reduce workers perform averaging in small independent groups. So any failure in a node will only affect its own group. Hence, this strategy allows us to use communication-efficient all-reduce protocols like butterfly all-reduce, while still being able to operate in unreliable hardware and network conditions.

Using this averaging protocol Moshpit SGD is done for distributed optimization. The algorithm for the Moshpit All-Reduce and SGD is given below (from the paper)

![](/images/moshpit_allreduce.png "[Source: https://arxiv.org/abs/2007.14513]")

![](/images/moshpit_sgd.png "[Source: https://arxiv.org/abs/2007.14513]")

The composition of the groups is dynamic and if two peers were in the same group in round t, they must choose different groups in round t+1. After the matchmaking is over, each group runs a single all reduce round to compute the average

Using this in Moshpit SGD, workers perform independent local SGD steps and periodically synchronize their parameters with other peers using Moshpit All-Reduce.

It is proven in the paper that this random grouping and reducing converge the model to a global minimum. However, the authors assume that if and when clients drop off or fail in the network they do not change the global average of the gradients in Moshpit SGD too much.

Using Moshpit SGD, the authors trained ResNet-50 on ImageNet to 75% accuracy 1.3 times faster than existing decentralized training algorithms, and trained ALBERT-large from scratch 1.5 times faster on preemptible cloud VMs.

## Conclusion
To overcome the computing issue in naive federated learning systems instead of model replication in the client nodes, we can adapt from split learning and knowledge distillation to run smaller models on the client and collectively train a larger model.

Also, aggregation algorithms like Moshpit SGD can converge to a global model even though weight aggregation is not done on all the client nodes. This is particularly useful in unreliable networks where clients can go down and join unreliably.

## References
1. He, Chaoyang, Murali Annavaram, and Salman Avestimehr. “Group knowledge transfer: Federated learning of large cnns at the edge.” Advances in Neural Information Processing Systems 33 (2020): 14068–14080.
2. Ryabinin, Max, et al. “Moshpit sgd: Communication-efficient decentralized training on heterogeneous unreliable devices.” Advances in Neural Information Processing Systems 34 (2021): 18195–18211.
3. https://research.ibm.com/blog/what-is-federated-learning
4. https://ai.googleblog.com/2017/04/federated-learning-collaborative.html