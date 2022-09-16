---
title: "A Long Short-Term Memory-Based Approach for Detecting Turns and Generating Road Intersections from Vehicle Trajectories"
collection: publications
permalink: /publication/202209-lstm-intxn
excerpt: ''
date: 2022-09-15
venue: 'Sensors'
paperurl: 'https://www.mdpi.com/1424-8220/22/18/6997'
citation: 'Wan, Z., Li, L., Yu, H., Yang, M. (2022). A Long Short-Term Memory-Based Approach for Detecting Turns and Generating Road Intersections from Vehicle Trajectories. <i>Sensors</i>, 22(18):6997. https://doi.org/10.3390/s22186997 '
---
Owing to the widespread use of GPS-enabled devices, sensing road information from vehicle trajectories is becoming an attractive method for road map construction and update. Although the detection of intersections is critical for generating road networks, it is still a challenging task. Traditional approaches detect intersections by identifying turning points based on the heading changes. As the intersections vary greatly in pattern and size, the appropriate threshold for heading change varies from area to area, which leads to the difficulty of accurate detection. To overcome this shortcoming, we propose a deep learning-based approach to detect turns and generate intersections. First, we convert each trajectory into a feature sequence that stores multiple motion attributes of the vehicle along the trajectory. Next, a supervised method uses these feature sequences and labeled trajectories to train a long short-term memory (LSTM) model that detects turning trajectory segments (TTSs), each of which indicates a turn occurring at an intersection. Finally, the detected TTSs are clustered to obtain the intersection coverages and internal structures. The proposed approach was tested using vehicle trajectories collected in Wuhan, China. The intersection detection precision and recall were 94.0% and 91.9% in a central urban region and 94.1% and 86.7% in a semi-urban region, respectively, which were significantly higher than those of the previously established local G* statistic-based approaches. In addition to the applications for road map development, the newly developed approach may have broad implications for the analysis of spatiotemporal trajectory data.

<!-- [Download paper here](http://academicpages.github.io/files/paper1.pdf) -->

Recommended citation: Wan, Z., Li, L., Yu, H., Yang, M. (2022). A Long Short-Term Memory-Based Approach for Detecting Turns and Generating Road Intersections from Vehicle Trajectories. <i>Sensors</i>, 22(18):6997. https://doi.org/10.3390/s22186997