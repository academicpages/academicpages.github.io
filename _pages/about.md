---
permalink: /
title: "About Me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<audio src="resources/about.mp3" id="audio"></audio>
<button class="play-pause-button paused" onclick="play()" id="play">
    <i>P</i>
    <i>l</i>
    <i>a</i>
    <i>y</i>
    <i>use</i>
</button>
<script>
    function play() {
        var audio = document.getElementById('audio');
        var button = document.getElementById("play");
        if(button.classList.contains('playing')) {
            audio.pause();
            button.classList.remove('paused', 'playing');
            button.classList.add('paused');
        } else {
            if(button.classList.contains('paused')) {
                audio.play();
                button.classList.add('playing');
            }
        }
        if(!button.classList.contains('paused')) {
                    button.classList.add('paused');
                }
}
</script>

Hello, I'm Amirali Soltani Tehrani, a passionate MSc student specializing in Control Engineering at the University of Tehran, Iran. I hold a Bachelor's degree in Telecommunication Systems, also earned at the University of Tehran. I'm currently an active member of the Graduate Lab at the Brain Computing Laboratory, where my enthusiasm for exploring the intersection of technology and neuroscience thrives. My academic journey has led me to delve deep into the realms of system neuroscience, signal processing, deep learning, statistics, and various machine learning methods. During my undergraduate years, I embarked on an exciting project: the development of an eye-tracking system. It's incredibly rewarding to see that the system I created is still in use today, reflecting my commitment to crafting solutions with lasting impact. In my pursuit of knowledge, I am currently immersed in the world of modeling peripheral vision in rodents as part of my Master's thesis. This endeavor has allowed me to apply my skills and passion to further our understanding of the intricacies of vision and perception. 

I'm eagerly looking forward to continuing my academic journey in the field of computational neuroscience, where I can contribute to unraveling the mysteries of the brain and developing innovative solutions. Feel free to connect with me if you share similar interests or have any questions. Let's explore the fascinating world of science and technology together!

# Background

<audio src="resources/background.mp3" id="audio2"></audio>
<button class="play-pause-button paused" onclick="play2()" id="play2">
    <i>P</i>
    <i>l</i>
    <i>a</i>
    <i>y</i>
    <i>use</i>
</button>
<script>
    function play2() {
        var audio = document.getElementById('audio2');
        var button = document.getElementById("play2");
        if(button.classList.contains('playing')) {
            audio.pause();
            button.classList.remove('paused', 'playing');
            button.classList.add('paused');
        } else {
            if(button.classList.contains('paused')) {
                audio.play();
                button.classList.add('playing');
            }
        }
        if(!button.classList.contains('paused')) {
                    button.classList.add('paused');
                }
}
</script>

From an early age, my fascination with mathematics was ignited through the guidance of my father, who nurtured my problem-solving skills. This early exposure cultivated a profound interest in understanding the intricate workings of the human brain. Inspired by my uncle, a distinguished spinal cord and brain surgeon, I embarked on a journey to unravel the mysteries of the brain's inner workings. Throughout my high school years, I continued to delve into mathematics while charting a path towards electrical engineering. During my undergraduate studies, a newfound passion for probability and statistics led me to the captivating realm of information theory. This fascination eventually culminated in my exploration of signal processing, where I encountered the groundbreaking research of Dr. Abolghasemi. For my undergraduate thesis, I dedicated my efforts to developing an eye-tracking system, a project that not only solidified my technical skills but also kindled my interest in neuroscience. Subsequently, I eagerly joined Dr. Abolghasemi's lab, where I engaged in more profound and impactful neuroscience projects. As my academic journey unfolded, I furthered my knowledge by serving as a Teaching Assistant at Neuromatch Academy, honing my expertise in neural signal analysis. These experiences deepened my understanding of the intricacies of the brain and its neural processes. Currently, my primary research goal is to explore peripheral vision in rodents, dissecting the hierarchical steps involved in processing visual information. My aspiration is to compare and contrast this peripheral vision model with the foveal vision observed in macaques.

Through my GitHub repository, I aim to share my academic pursuits, projects, and insights in the realm of neuroscience and signal processing. Join me on this journey of discovery as we unlock the secrets of the brain's intricate machinery.