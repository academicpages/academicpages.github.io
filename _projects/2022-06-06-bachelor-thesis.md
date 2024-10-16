---
title: "Bachelor Thesis: Visual Question Answering with Knowledge-based Semantics"
collection: projects
permalink: /projects/vqa-knowledge-semantics
excerpt: "<p style='text-align: justify'>This thesis considers an exhaustive state-of-the-art (SOTA) desription of VQA models, theoretical considerations and implementation details for training a VQA model learning towards a semantical- and conceptually strong latent space spanned by the Conceptnet Numberbatch embeddings as well an analysis of model behaviour by exploiting explainability tools.</p>"
date: 2022-06-06
venue: 'DTU, Department of Applied Mathematics and Computer Science'
paperurl: 'https://findit.dtu.dk/en/catalog/62c6c822d4fccf03d747b3db'
citation: ' Jacobsen, Albert Kjøller; Højbjerg, Phillip Chavarria; Jacobsen, Aron Djurhuus. (2022). &quot;Visual Question Answering with Knowledge-based Semantics.&quot; <i>DTU Department of Applied Mathematics and Computer Science </i>.'
---

Abstract 
======

<p style="text-align: justify"> Visual Question Answering (VQA) is a versatile problem combining major fields like Computer
Vision (CV) and Natural Language Processing (NLP) for successfully integrating information
from questions and images when generating answers requiring common-sense reasoning and
knowledge about the world. The task has received a lot of attention from researchers as it
is based on human-like capabilities and could as such potentially function as an augmented
intelligent system for e.g. helping visually impaired people, education systems or function as a
basis for investigating the amalgamation of the symbolic and subsymbolic Artifial Intelligence
(AI) paradigms. As creating a well-performing VQA system is far-from trivial - which is shown
through a literature review -, this project proposes a novel approach of incorporating external
knowledge in the model pipeline by training towards a knowledge-based semantic target space
spanned by the pre-trained ConceptNet Numberbatch embeddings, where it is assumed that
the Numberbatch-space is exactly what is needed for answering the image-question problems
provided through the dataset. Specifically, the Outside Knowledge VQA (OK-VQA) dataset
was utilized through the Multi-Modal Framework (MMF) given by Facebook Research. For
solving this exact task, experimentation on fusion modules, external knowledge and top-down
attention mechanisms were applied with the e↵ort of determining what specifically results in
a model’s answer using a well defined evaluation protocol covering qualitative analysis tools
such as explainability methods, as an initial analysis of the OK-VQA dataset raised potential
issues that might bias the model behaviour. Whether the proposed approach can be deemed
successful or not is something up for discussion, since the applied models performed marginally
below what was seen for baseline models presented in the OK-VQA paper, however, still
provides semantically and conceptually strong answers that encounters input from both the
visual- and textual-modality. However, discussions of what resulted in the observed outcome
can essentially be summarized in three pointers: 1) the assumption of the Numberbatch-space
capturing all what is required by the OK-VQA-proposed problem does not appear as valid, 2)
the objective function - manifested as a triplet loss function - is not capable of fully indicating
the performance of the model and 3) the optimization approach through hyperparameter
tuning should be extended. Regardless of the results, a great foundation for future work as
been set.</p>

[Download thesis here](https://findit.dtu.dk/en/catalog/62c6c822d4fccf03d747b3db)

<!-- Recommended citation: Jacobsen, Albert Kjøller; Højbjerg, Phillip Chavarria; Jacobsen, Aron Djurhuus. (2022). "Visual Question Answering with Knowledge-based Semantics." <i>DTU Department of Applied Mathematics and Computer Science </i>. -->