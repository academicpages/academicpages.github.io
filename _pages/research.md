---
layout: archive
title: ""
permalink: /research/
author_profile: true
---

## $$\color{olive}{Job \space Market \space Paper}$$ 

- **Reveal or Conceal? Employer Learning in the Labor Market for Computer Scientists** 
<a href="#/" onclick="visib('jmp')">Abstract</a>  | *Draft Coming Soon*
<div id='jmp' style="display: none; text-align: justify; line-height: 1.2" >
The efficient allocation of labor relies on the identification of talent. When employee output is not publicly observable, employers have an incentive to take advantage of private information, potentially leading to the misallocation of labor among firms. This paper provides empirical evidence of employer learning and quantifies the impact of learning on job mobility and innovation outputs in the labor market for computer science (CS) Ph.D.'s. CS conference proceedings provide public information on research effort by existing CS workers. Among papers authored by researchers from industry, about one-quarter can be matched to a contemporaneous patent application - an indicator of a more valuable innovation. Yet the fact of the application remains private information at the incumbent employer for 18 months. Consistent with public learning, researchers with a new paper have higher inter-firm mobility rates than do coworkers without a paper. Initially, authors of papers with a matched patent are less likely to move than authors without a patent application. But once the patent application becomes public, their mobility rates cross over. Authors of papers with a matched patent are also 35% more likely to move to a top tech firm. These patterns confirm the predictions of a model in which incumbent firms have initially private information on more productive researchers. Structural estimates of the model suggest that if papers and patents were disclosed simultaneously, high-ability workers would sort more quickly to high-productivity firms. The implied increase in allocative efficiency would increase innovation outputs by about 5%. </div>



## $$\color{olive}{Works \space in \space Progress}$$ 
- **Who Becomes an Inventor? The Role of Firms in Talent Discovery**. (joint with [Sabrina Di Addario](https://scholar.google.com/citations?user=IgkUsgIAAAAJ&hl=en){target="_blank"})
<a href="#/" onclick="visib('italy')">Abstract</a>  | *Draft Coming Soon*
<div id='italy' style="display: none; text-align: justify; line-height: 1.2" >
How does firm productivity relate to the speed of talent discovery? We assess this relationship in the labor market for Italian inventors. We define talent discovery as a worker becoming an inventor who files a patent application for the first time. Using the employer-employee data from the Italian Social Security Institute matched with patent applications between 1987 and 2009, we find large heterogeneity in talent discovery across firms, particularly for workers early in their careers. On average a worker younger than 35 is 175% more likely to become an inventor at firms in the top quartile of productivity than at firms in the bottom quartile, conditional on differences across sectors and geographic areas. Workers who do invent at bottom quartile firms on average receive an 8-10 log point increase in wages, rather than 2-4 log points at more productive firms. We interpret the empirical findings in an employer learning framework.  </div>


- **The Labor Market Signaling Value of Open Source Contributions**. (joint with Jacob Weber)
<a href="#/" onclick="visib('github')">Abstract</a> 
<div id='github' style="display: none; text-align: justify; line-height: 1.2" >
Does the rise in open-source software development provide an opportunity for software developers and engineers to signal their ability to potential employers, and is this signaling value higher for workers from less advantaged backgrounds? We answer this question by matching open-source contributions on GitHub to employment outcomes from LinkedIn. We investigate whether workers increase open-source contributions before changing jobs. In particular, we examine whether the effects of this activity on labor market outcomes, such as moving into a higher-paid job, are stronger for workers from less advantaged education and demographic backgrounds. </div>


- **Does Trade Secret Litigation Increase Monopsony Power? Evidence from the Defends Trade Secret Act**. (joint with Evgenii Fadeev)
<a href="#/" onclick="visib('law')">Abstract</a> 
<div id='law' style="display: none; text-align: justify; line-height: 1.2" >
We use the texts of legal complaints from trade secret litigation to study how firms responded to the enactment of the Defend Trade Secret Act (DTSA) in 2016. One of the goals of this act was to increase the protection of American firms against international trade secret theft. Within a year of the act's passage, trade secret litigation surged by 33%. However, this increase was predominantly driven by US companies suing employees who transitioned to other domestic firms. We show that the spike in litigation post-DTSA was more pronounced in states with weaker enforceability of non-compete agreements. This evidence suggests that firms might resort to trade secret litigation as an alternative to non-compete clauses. We examine whether a trade secret lawsuit against an employee affects her own job mobility, productivity and business ventures, as well as spillover effects on her former co-workers at the plaintiff.    </div>




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
