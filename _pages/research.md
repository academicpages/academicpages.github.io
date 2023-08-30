---
layout: archive
title: ""
permalink: /research/
author_profile: true
---

## $$\color{olive}{Job \space Market \space Paper}$$ 

- **Do You See What I See? Employer Learning in the Labor Market for Computer Scientists** 
<a href="#/" onclick="visib('jmp')">Abstract</a>  | *Draft Coming Soon*
<div id='jmp' style="display: none; text-align: justify; line-height: 1.2" >
Identification of talent is necessary for the efficient allocation of workers to firms and tasks. However, employers often have limited information and make learning decisions to maximize private information rents rather than public talent revelation. This paper provides empirical evidence of employer learning, and quantifies the impact of learning on job mobility and innovation outputs in the labor market for computer scientists. The large volume of CS conference proceedings offers a peek into on-the-job research that is hard to observe, especially for workers outside academia. About 20% of papers by authors in the industry can be matched to a patent application, which indicates a more valuable innovation. Yet the patenting decision remains private information with the incumbent employer for more than a year. Workers with a new paper are 13-26% more mobile than similar coworkers without a paper, but initially, workers with a matched patent are less likely to move than those with a paper only. Once a patent application is publicly revealed, workers with a matched patent are 10-15% more likely to move and especially from the less productive firms into the top firms in the tech sector. These findings confirm the predictions of a dynamic model with two-sided heterogeneity that takes into account firms' endogenous investment in learning. Structural estimates of the model suggest if matched patents are disclosed at the same time as papers, job mobility of higher-ability workers would increase immediately, movers would be 10% more productive than before and the productivity gains from assortative matching offset the costs of firms' under-investment in public learning.  </div>



## $$\color{olive}{Works \space in \space Progress}$$ 
- **Who Becomes an Inventor? The Role of Firms in Talent Discovery**. (joint with Sabrina Di Addario) 
<a href="#/" onclick="visib('italy')">Abstract</a>  | *Draft Coming Soon*
<div id='italy' style="display: none; text-align: justify; line-height: 1.2" >
How does firm productivity relate to the speed of talent discovery? We assess this relationship empirically in the labor market for Italian inventors. We define talent discovery as a worker becoming an inventor who files a patent application for the first time. Using the employer-employee data from the Italian Social Security Institute matched with patent applications between 1987 and 2009, we find large heterogeneity in talent discovery across firms, particularly for workers early in their careers. On average a worker younger than 35 is 175% more likely to become an inventor at firms in the top quartile of productivity than at firms in the bottom quartile, conditional on differences across sectors and geographic areas. Workers who do invent at the bottom quartile on average receive an 8-10 log point increase in wages, rather than 2-4 log points at more productive firms. We interpret the empirical findings in an employer learning framework. We are working on a policy counterfactual that subsidizes low-productivity firms for increasing invention opportunities for young workers, and aim to investigate whether the gap in talent discovery between firms would shrink, and whether total innovation outputs would increase.  </div>


- **Self Signaling: Theory and Evidence from Open Source Contributions**. (joint with Jacob Weber)
<a href="#/" onclick="visib('github')">Abstract</a> 
<div id='github' style="display: none; text-align: justify; line-height: 1.2" >
How do workers credibly signal their ability to potential employers, and does self signaling matter for labor market outcomes?  We answer these questions in the labor market for software developers and engineers.  By matching GitHub and LinkedIn profiles, we measure self signaling from a worker's contributions to open-source projects, which are publicly observable to recruiters. We test if workers increase signaling before they change jobs, and estimate differential returns to signaling for workers from different education or demographic backgrounds. </div>


- **Knowledge Sharing and Organizational Structure: Evidence from Trade Secret Litigation**. (joint with Evgenii Fadeev)
<a href="#/" onclick="visib('law')">Abstract</a> 
<div id='law' style="display: none; text-align: justify; line-height: 1.2" >
We apply deep learning language models on trade secret litigation records to classify legal cases based on whether the (claimed) misappropriation of trade secrets happened through employees or business partners (e.g., input suppliers) and to compare technologies involved in trade secret litigation with inventions disclosed in patent files. We use this information to study how firms change their patenting, employment, and input sourcing decisions following misappropriation of trade secrets.   </div>




## $$\color{olive}{Publications}$$ 
- **Gender Bias in Rumors Among Professionals: An Identity-based Interpretation**. Review of Economics and Statistics, 102, 5, pp. 867-880. December 2020. 
<a href="#/" onclick="visib('ejr')">Abstract</a> | [Paper with Appendix](/files/wu_ejr_restat.pdf) |  [Replication](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/BLEBHI) 
<div id='ejr' style="display: none; text-align: justify; line-height: 1.2" >
This paper measures gender bias in what people say about women versus men in an anonymous online professional forum. I study the content of posts that refer to each gender, and the transitions in the topics of discussion that occur between consecutive posts in a thread once attention turns to one gender or the other. I find that discussions about women tend to highlight their personal characteristics (such as physical appearance or family circumstances) rather than their professional accomplishments. Posts about women are also more likely to lead to deviations from professional topics than posts about men. I interpret these findings through a model that highlights posters’ incentives to boost their own identities relative to the underrepresented out-group in a profession. </div>


- **Gendered Language on the Economics Job Market Rumors Forum** AEA Papers and Proceedings, 108, pp. 175-179. 
<a href="#/" onclick="visib('ejr0')">Abstract</a> | [Paper with Appendix](/files/wu-pp-appendix.pdf) |  [Replication](https://www.aeaweb.org/articles?id=10.1257/pandp.20181101) 
<div id='ejr0' style="display: none; text-align: justify; line-height: 1.2" >
This paper examines the existence of an unwelcoming or stereotypical culture using evidence on how women and men are portrayed in anonymous discussions on the Economics Job Market Rumors forum (EJMR). I use a Lasso-Logistic model to measure gendered language in EJMR postings, identifying the words that are most strongly associated with discussions about one gender or the other. I find that the words most predictive of a post about a woman are typically about physical appearance or personal information, whereas those most predictive of a post about a man tend to focus on academic or professional characteristics. 
</div>



<!-- note: function below was copied from ranzhuo17's research.md  -->
[//]: This java script is the button to show abstract 
<script>
 function visib(id) {
  var x = document.getElementById(id);
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
</script>

[//]:&emsp;<button onclick="visib('polariz')" class="btn btn--inverse btn--small">Abstract</button>


<!-- 
{% include base_path %}

{% for post in site.papers reversed %}
  {% include archive-single.html %}
{% endfor %} -->
