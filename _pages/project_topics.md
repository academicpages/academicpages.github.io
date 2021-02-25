1. Replicate "Rethinking ..." for sequence labeling and multi-labeling tasks
2. Explore self-supervision or weak-supervision on graphs (can you use the graph structure/subspaces effectively to improve on highly imbalanced problems?)
3. Explore methods discussed in this class for medical datasets (rare diseases etc)
4. Benchmark out of distribution detection methods (create a tooklit with common evaluation framework and several SoTA OoD methods. Can you provide some insights?)
5. Study whether any of these methods help in transfer learning between languages with different syntax (e.g., left-to-right and right-to-left languages). Make sure to see the effect with and without the use of bidirectional models such as biLSTM.
6. Cross-modal pseudolabeling on social network data (combine graph contrastive with cross-modal pseudolabeling) https://arxiv.org/pdf/2006.05582v1.pdf https://arxiv.org/pdf/1911.12667.pdf
7. Explore 3D mutli-view contrastive methods (using models and augmentation methods that handle for 3D data)
8. Use concept from the class to design time-series representations: https://xai-360.github.io/TSCL/ https://openreview.net/pdf?id=8qDwejCuCN 
9. Cirriculum contrastive learning https://arxiv.org/abs/2010.01028
10. Can GANs help contrastive learning? A paper in this direction: https://openreview.net/forum?id=eo6U4CAwVmg
12. Video constrastive learning Transformer model for video? Maybe? https://arxiv.org/abs/1812.02707 + Frame-level local representation r_l contrasted with global video-level representation r_g, i.e., L(r_l, r_g) + Audio representations r_a contrasted with global and local, i.e. L(r_a, r_g) + L(r_a, r_l) or do similar as above.

Emergent communication (we can focus on: multi-modal / noisy channels / explainability)
Check for papers in https://scholar.google.com/scholar?cites=17308624474306270808&as_sdt=400005&sciodt=0,14
Open problems https://arxiv.org/abs/2012.08630

Adversarial connections in *graphs* (useful for defenses against social media malicious user groups)
- Useful concepts: Network formation games / Graph bandits / Graph diffusion
https://www.kdd.org/exploration_files/8._CR.10.Misinformation_in_social_media_-_Final.pdf
https://paperswithcode.com/paper/graph-adversarial-networks-protecting
https://paperswithcode.com/paper/boundary-thickness-and-robustness-in-learning
https://paperswithcode.com/paper/smooth-adversarial-training
https://arxiv.org/abs/1805.04807

Weak supervision: learn from positive and unlabeled data (PU learning)
https://heartbeat.fritz.ai/positive-and-unlabelled-learning-recovering-labels-for-data-using-machine-learning-59c1def5452f
https://arxiv.org/pdf/1811.04820.pdf
https://www.aaai.org/AAAI21Papers/AAAI-7574.HuW.pdf
https://dl.acm.org/doi/abs/10.1145/3340531.3411971?casa_token=3M6E83NSfKMAAAAA:FoLyhMSYs32ARdUpJiOugGCN4OcapEXT6hm9XQBOEay8a5HiLEMmF0eIXic1ffUW3gq0C7nFTtK0
https://papers.nips.cc/paper/2020/file/98b297950041a42470269d56260243a1-Paper.pdf
