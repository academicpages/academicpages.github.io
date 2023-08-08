---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---

<!-- {% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}
-->

<!-- the styles -->
<style>

div.noshow { display: none; }
div.bibtex {
  margin-right: 0%;
  margin-top: 1.2em;
  margin-bottom: 1.3em;
  border: 1px solid silver;
  padding: 0.3em 0.5em;
  background: #eeeeee;
}
div.bibtex pre { font-size: 75%; overflow: auto;  width: 100%; }
</style>


<!-- the scripts -->
<script>
function toggleBibtex(articleid) {
  var bib = document.getElementById(articleid);
  if (bib) {
    if(bib.className.indexOf('bibtex') != -1) {
    bib.className.indexOf('noshow') == -1?bib.className = 'bibtex noshow':bib.className = 'bibtex';
    }
  } else {
    return;
  }
}
</script>

> \* Corresponding author

## 📗 Peer-reviewed Journal Articles 
<ol>

<!-- 
<li>
<p>
<b>title</b><br>
author, <b>Zifeng Weng</b>, Rémy Mével*<br>
<i>journal</i> <br>
<a href="javascript:toggleBibtex('xxx')" class="textlink">[bib]</a>
<a href="researchgate download address" class="textlink" target="_blank">[pdf]</a>
</p>
</li> -->

<li>
<p>
<b>Implementation of an OpenFOAM solver for shock and detonation simulation at high pressure</b><br>
<b>Zifeng Weng</b>, Rémy Mével*<br>
<i>Computers & Fluids</i> <br>
<!-- <a href="javascript:toggleBibtex('xxx')" class="textlink">[bib]</a> -->
<a href="https://www.researchgate.net/profile/Zifeng-Weng/publication/372678897_Implementation_of_an_OpenFOAM_solver_for_shock_and_detonation_simulation_at_high_pressure/links/64c29e106f28555d86d7fe8b/Implementation-of-an-OpenFOAM-solver-for-shock-and-detonation-simulation-at-high-pressure.pdf?origin=publicationDetail&_sg%5B0%5D=Zp8RUhvh3Em_8cjC5A7jjZbRfUlXy65fzJFQpgh8kf2QDHhce_Ftlqt5cev0jboKfHlEa4m0m1c4rOe_I7i9KA.6B5r8uR9u-b780PPeFPWsJ9sd6DAlyIFV57jOEY1bTHJQvL3pbBSVRDBTCDgXOzv_2cVREcLl16zjPHAkaXHkg&_sg%5B1%5D=HjmzqMdUd72wPeaRzNrgTxHkLtoPBFNygKesqeEkRvvQDIyY-IzrK_vCak6UM0DTHiAKMxJjz1IAFjhhwuc3mA4ljNJ4ie3AFbKVmEfLnB4M.6B5r8uR9u-b780PPeFPWsJ9sd6DAlyIFV57jOEY1bTHJQvL3pbBSVRDBTCDgXOzv_2cVREcLl16zjPHAkaXHkg&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>
</li> 

<li>
<p>
<b>On the Critical Initiation of Planar Detonation in Noble-Abel and van der Waals Gas</b><br>
<b>Zifeng Weng</b>, Rémy Mével*, Chung K Law<br>
<i>Combustion and Flame</i> <br>
<a href="javascript:toggleBibtex('WengCNF2023b')" class="textlink">[bib]</a>
<a href="https://www.researchgate.net/profile/Zifeng-Weng/publication/371315501_On_the_Critical_Initiation_of_Planar_Detonation_in_Noble-Abel_and_van_der_Waals_Gas/links/647f0b2879a72237651394b4/On-the-Critical-Initiation-of-Planar-Detonation-in-Noble-Abel-and-van-der-Waals-Gas.pdf?origin=publicationDetail&_sg%5B0%5D=RatPQKKKnU4L7wcA9QeVfTxtJLci427HfeC4lWfSaRG2YtEI-DLVSPk4zMJArzzqSEok_gK02Bd8DROLaMaz-A.xy_aCG1P8b7IqLtfY-eBtZAhXGSSVUYVdY-bjgbOmBvZI-uNRFyXpp7pXgBmsvIs6fXQDAvZWK9sNbPpJ6SoFQ&_sg%5B1%5D=NyzlJSpWTSw3355A23PSmUTRQZ7moP-P1ix-F7tix7BqrIvSlv1krA8wGfXWs_WJ7N5Z9x5AhIVgazeigm9hB0K9vcppt2P-jteP3Muq5mOY.xy_aCG1P8b7IqLtfY-eBtZAhXGSSVUYVdY-bjgbOmBvZI-uNRFyXpp7pXgBmsvIs6fXQDAvZWK9sNbPpJ6SoFQ&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>

<div id="WengCNF2023b" class="bibtex noshow">
<pre>
@article{WengCNF2023b,
  title = {On the Critical Initiation of Planar Detonation in {{Noble-Abel}} and van der {{Waals}} Gas},
  author = {Weng, Zifeng and M{\'e}vel, R{\'e}my and Law, Chung K.},
  year = {2023},
  journal = {Combustion and Flame},
  volume = {255},
  pages = {112890},
  doi = {10.1016/j.combustflame.2023.112890}
}
</pre></div>
</li> 


<li>
<p>
<b>Entropy and Nitrogen Oxides Production in Steady Detonation Wave Propagating in Hydrogen-Air Mixtures</b><br>
Zituo Chen, <b>Zifeng Weng</b>, Rémy Mével*<br>
<i>International Journal of Hydrogen Energy</i> <br>
<!-- <a href="javascript:toggleBibtex('wengIJHE2023')" class="textlink">[bib]</a> -->
<a href="https://www.researchgate.net/profile/R-Mevel/publication/372109517_Entropy_and_Nitrogen_Oxides_Production_in_Steady_Detonation_Wave_Propagating_in_Hydrogen-Air_Mixtures/links/64a528fa95bbbe0c6e15001e/Entropy-and-Nitrogen-Oxides-Production-in-Steady-Detonation-Wave-Propagating-in-Hydrogen-Air-Mixtures.pdf?origin=publicationDetail&_sg%5B0%5D=TImkkuGkuBGuMqXs68x1FbydM1_VbUjqPhe5In8tDL4XcwTm0IszcDqHX4_RpvTLU46j2Ly8X0Tdx4ZQjz-OKQ.G2qYgKN1apWWPo4Fm4WC-MdrckKX75YQh6clbxWQEJPNOnOQdmC8oHD4ZDn21flA4IOuSpiL_hxSKgI0GoE1qw&_sg%5B1%5D=Nu-Fw37zzbB0LJBDGa3BdfXq-GqMfsjBWQXLXw4gyNjf0rO824nH2ih4y3ReJx_ZEy3GCyumcjG3ROrLRFGLIlqylelZ60cNOTPy-TQ3ogLJ.G2qYgKN1apWWPo4Fm4WC-MdrckKX75YQh6clbxWQEJPNOnOQdmC8oHD4ZDn21flA4IOuSpiL_hxSKgI0GoE1qw&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>
</li>

<li>
<p>
<b>Discontinuity in Cubic Equations of State: Impact of Attraction Term Mixing Rule on Combustion Simulation</b><br>
<b>Zifeng Weng</b>, Rémy Mével*<br>
<i>International Journal of Hydrogen Energy</i> <br>
<a href="javascript:toggleBibtex('wengIJHE2023')" class="textlink">[bib]</a>
<a href="https://www.researchgate.net/profile/Zifeng-Weng/publication/370604150_Discontinuity_in_Cubic_Equation_of_State_Impact_of_Attraction_Term_Mixing_Rule_on_Combustion_Simulation/links/6459b2b84af788735268beeb/Discontinuity-in-Cubic-Equation-of-State-Impact-of-Attraction-Term-Mixing-Rule-on-Combustion-Simulation.pdf?origin=publicationDetail&_sg%5B0%5D=qMvBd_m7g25Ilsm3DSx93rTicAnHJ1zisSs6HepN3MOuDjJJsyrZTN60JmzDI8VjqqfnJxoEDvAzL4pzlqMAkA.zEXDWf3u925Q6gTxDERUqqaB09Kd4ntnGWTlM9czGXH1gL_QLr6jtFWexqzErk0Mi_JrZq-lnJCS0BgHxd8MZQ&_sg%5B1%5D=EXfrj_YfNcqfTxJDBkqcxT804o9NTywhVV553yWsO29HcJklPL-Yh-hvXdyjREzYCclznyNcKePKy1-VGsEcYEDlyMFCqDhJudNnCLnZdfyg.zEXDWf3u925Q6gTxDERUqqaB09Kd4ntnGWTlM9czGXH1gL_QLr6jtFWexqzErk0Mi_JrZq-lnJCS0BgHxd8MZQ&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>

  
<div id="wengIJHE2023" class="bibtex noshow">
<pre>
@article{wengInternationalJournalofHydrogenEnergy2023,
  title = {Discontinuity in Cubic Equations of State: {{Impact}} of Attraction Term Mixing Rule on Combustion Simulation},
  shorttitle = {Discontinuity in Cubic Equations of State},
  author = {Weng, Zifeng and Mével, Rémy},
  year = {2023},
  journal = {International Journal of Hydrogen Energy},
  doi = {10.1016/j.ijhydene.2023.05.080}
}
</pre></div>
</li>
  
<li>
<p>
<b>Real Gas Effect on Ignition in Ideal and Non-Ideal Reactors</b><br>
Isaac Farias, <b>Zifeng Weng</b>, Rémy Mével*<br>
<i>Shock Waves</i> <br>
<a href="javascript:toggleBibtex('fariasShockWaves2023')" class="textlink">[bib]</a>
<a href="https://www.researchgate.net/profile/Zifeng-Weng/publication/370604150_Discontinuity_in_Cubic_Equation_of_State_Impact_of_Attraction_Term_Mixing_Rule_on_Combustion_Simulation/links/6459b2b84af788735268beeb/Discontinuity-in-Cubic-Equation-of-State-Impact-of-Attraction-Term-Mixing-Rule-on-Combustion-Simulation.pdf?origin=publicationDetail&_sg%5B0%5D=41uePROqNhJJe8ybQnT2T2l37nPX794xlhLDexVakZd5afhb-kRckVv10v0VcIeZ0mGpUbdZMdKP-4kHv-Fvkg.9bhaF0Yni7MAhrArCRg9gXg23CmvCP6ClKHBf2Z2WdZZAt0JG1LhAGFXOica9RoD5ZPszUVIoq-DZvtsy5qPKg&_sg%5B1%5D=NivO5NdAaQM8ry-AIOymaFy2_2xJ5vGmnQfTJOZzcb2lTqVORQCTlp_cfH5jvbxBTuZhnovKMa9o3w9fT8yrEvXyZVLymmbVd91R0UF4gkRx.9bhaF0Yni7MAhrArCRg9gXg23CmvCP6ClKHBf2Z2WdZZAt0JG1LhAGFXOica9RoD5ZPszUVIoq-DZvtsy5qPKg&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>
<div id="fariasShockWaves2023" class="bibtex noshow">
<pre>
@article{fariasShockWaves2023,
  title = {Real Gas Effect on Ignition in Ideal and Non-Ideal Reactors},
  author = {Farias, Isaac and Weng, Zifeng and Mével, Rémy},
  year = {2023},
  journal = {Shock Waves},
  doi = {10.1007/s00193-022-01118-x}
}
</pre></div>
</li>

<li>
<p>
<b>Detonation in Ammonia-Oxygen and Ammonia-Nitrous Oxide Mixtures</b><br>
<b>Zifeng Weng</b>, Rémy Mével*, Nabiha Chaumeix<br>
<i>Combustion and Flame</i> <br>
<a href="javascript:toggleBibtex('wengCNF2023a')" class="textlink">[bib]</a>
<a href="https://www.researchgate.net/profile/Zifeng-Weng/publication/368423470_Detonation_in_Ammonia-Oxygen_and_Ammonia-Nitrous_Oxide_Mixtures/links/63e6fd35dea61217579dcde3/Detonation-in-Ammonia-Oxygen-and-Ammonia-Nitrous-Oxide-Mixtures.pdf?origin=publicationDetail&_sg%5B0%5D=IkdxH3Nk25nKTPl4qBMtq4yDjDinNyENa8oB-BDqy7VJpYtinCreMTDerORkO1OENMz-90DRVekWs-syYyMtBw.Guf3ZpzGIMLS9bZ2KP3Wxgm16sK8aDyWTEtoV64sE7ntsC9HB_THnLuBMrZBP3LaU-q22NufQLmroub8OmIyKA&_sg%5B1%5D=vMHY831zhf_3JI28tRhKvg423rjVASqed0DjKRGq1CG0VmbWwlZqQZkhKruZlnKIiPZeXw7OKOZ4W2g5nDeKJOeoGXUC-CRqPttaXGaqivnr.Guf3ZpzGIMLS9bZ2KP3Wxgm16sK8aDyWTEtoV64sE7ntsC9HB_THnLuBMrZBP3LaU-q22NufQLmroub8OmIyKA&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>
<div id="wengCNF2023a" class="bibtex noshow">
<pre>
@article{wengCNF2023a,
  title = {Detonation in Ammonia-Oxygen and Ammonia-Nitrous Oxide Mixtures},
  author = {Weng, Zifeng and Mével, Rémy and Chaumeix, Nabiha},
  year = {2023},
  journal = {Combustion and Flame},
  volume = {251},
  pages = {112680},
  doi = {10.1016/j.combustflame.2023.112680}
}
</pre></div>
</li>

<li>
<p>
<b>Effect of Ozone Addition on Curved Detonations</b><br>
<b>Zifeng Weng</b>, Fernando Veiga-López, Josué Melguizo-Gavilanes, Rémy Mével*<br>
<i>Combustion and Flame</i> <br>
<a href="javascript:toggleBibtex('wengCNF2023')" class="textlink">[bib]</a>
<a href="https://www.researchgate.net/profile/Zifeng-Weng/publication/364830346_Effect_of_ozone_addition_on_curved_detonations/links/635ce89896e83c26eb6470f9/Effect-of-ozone-addition-on-curved-detonations.pdf?origin=publicationDetail&_sg%5B0%5D=dm56waifSCCrIQvP_y2kh7EwQKvxLc4ugTEawkXUgMa8-VKcDhcreDgK5dk9Y8L5bqPM-bIp9bnxTjDZ3z_weA.DY3ts3ybKu2uAXTzxkIVaCJG7lNeVqlKKdIMXk5qaW9rkDx1EtNlE7xJ6gXt-bp6sa4gaus13iK_4jtNqkDDpw&_sg%5B1%5D=suuwzYOkunx54WW3sfsckDgQpOEknRWeHdE9HkoieOxCOZ-rBHccIONQcF6RRgLVaCOib-MCnH-SkT_SmEwgAA7hnWRltWC8Qnk-ryBcLd8B.DY3ts3ybKu2uAXTzxkIVaCJG7lNeVqlKKdIMXk5qaW9rkDx1EtNlE7xJ6gXt-bp6sa4gaus13iK_4jtNqkDDpw&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>
<div id="wengCNF2023" class="bibtex noshow">
<pre>
@article{wengCNF2023,
  title = {Effect of Ozone Addition on Curved Detonations},
  author = {Weng, Zifeng and {Veiga-López}, Fernando and {Melguizo-Gavilanes}, Josué and Mével, Rémy},
  year = {2023},
  journal = {Combustion and Flame},
  volume = {247},
  pages = {112479},
  doi = {10.1016/j.combustflame.2022.112479}
}
</pre></div>
</li>

<li>
<p>
<b>Influence of Low-Temperature Chemistry on Steady Detonations with Curvature Losses</b><br>
Fernando Veiga-López*, <b>Zifeng Weng</b>, Rémy Mével, Josué Melguizo-Gavilanes<br>
<i>Proceedings of the Combustion Institute</i> <br>
<a href="javascript:toggleBibtex('veigaPCI2022')" class="textlink">[bib]</a>
<a href="https://www.researchgate.net/profile/Fernando-Veiga-Lopez/publication/365231929_Influence_of_low-temperature_chemistry_on_steady_detonations_with_curvature_losses/links/636b89e0431b1f530083fda4/Influence-of-low-temperature-chemistry-on-steady-detonations-with-curvature-losses.pdf?origin=publicationDetail&_sg%5B0%5D=yG8CgZ3_qr7Hx1daPy04u29aB-iLnn4cglKp3PzXUzZxn9K371CXwwZ4JZVTff1qP14BWV0jhBZt7m0rcjGg0g.Hqal--JMug85gmQq5Wvp6g7a2M0o8qztiyprqAOm60Gqn5hTCGbYnSGr9e0118xLpGkInXPyVAk44-LTDPSSDg&_sg%5B1%5D=ek3KCm8qPpXUZpWR6ZIbuclZsg_f62WitzftoQQAritLVjUASyPaEulaxKDocUDa5esZXHGMjYlda8olg7K2TG_-VSjw2Hs_AKtT9ndDxZYH.Hqal--JMug85gmQq5Wvp6g7a2M0o8qztiyprqAOm60Gqn5hTCGbYnSGr9e0118xLpGkInXPyVAk44-LTDPSSDg&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>
<div id="veigaPCI2022" class="bibtex noshow">
<pre>
@article{veigaPCI2022,
  title = {Influence of Low-Temperature Chemistry on Steady Detonations with Curvature Losses},
  author = {Veiga-López, Fernando and Weng, Zifeng and Mével, Rémy and {Melguizo-Gavilanes}, Josué},
  year = {2022},
  journal = {Proceedings of the Combustion Institute},
  doi = {10.1016/j.proci.2022.11.001}
}
</pre></div>
</li>

<li>
<p>
<b>Thermo-Chemical Analyses of Steady Detonation Wave Using the Shock and Detonation Toolbox in Cantera</b><br>
Zongtai Li, <b>Zifeng Weng</b>, Rémy Mével*<br>
<i>Shock Waves</i> <br>
<a href="javascript:toggleBibtex('liShockWaves2022')" class="textlink">[bib]</a>
<a href="https://www.researchgate.net/profile/R-Mevel/publication/364624492_Thermo-chemical_Analyses_of_Steady_Detonation_Wave_using_the_Shock_and_Detonation_Toolbox_in_Cantera/links/6353e1b66e0d367d91b70244/Thermo-chemical-Analyses-of-Steady-Detonation-Wave-using-the-Shock-and-Detonation-Toolbox-in-Cantera.pdf?origin=publicationDetail&_sg%5B0%5D=jp1_6K30xq7yTrMgvRbTyG7CLgKfpSYSzmqrApDM1Um_LWirwQF24MVp2TXTQUMHs9JUSVz-V8dJiT8QyHA9Sw.ukCuNZpcF8stLNprZHF16HppN9iPFZaqZzKakQj74D7Q0SQyDhROzeN4esmYgfvv3s-YzryykB2oJOHNuseyNQ&_sg%5B1%5D=rerYvyED6JUJsBGpn-D04psw8_VkYT6elS5NbzYZIhJZ-3XpE6R9TOu8ht4MbNmlvF_u1Oo28VWV-WMX1OkrnNMc-4Svqzfi9f0eKEhxmlKT.ukCuNZpcF8stLNprZHF16HppN9iPFZaqZzKakQj74D7Q0SQyDhROzeN4esmYgfvv3s-YzryykB2oJOHNuseyNQ&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>
<div id="xxx" class="bibtex noshow">
<pre>
@article{liShockWaves2022,
  title = {Thermo-Chemical Analyses of Steady Detonation Wave Using the {{Shock}} and {{Detonation Toolbox}} in {{Cantera}}},
  author = {Li, Zongtai and Weng, Zifeng and Mével, Rémy},
  year = {2022},
  journal = {Shock Waves},
  volume = {32},
  number = {8},
  pages = {759--762},
  doi = {10.1007/s00193-022-01107-0}
}
</pre></div>
</li>

<li>
<p>
<b>Real Gas Effect on Steady Planar Detonation and Uncertainty Quantification</b><br>
<b>Zifeng Weng</b>, Rémy Mével*<br>
<i>Combustion and Flame</i> <br>
<a href="javascript:toggleBibtex('wengCNF2022')" class="textlink">[bib]</a>
<a href="https://www.researchgate.net/journal/Shock-Waves-1432-2153/publication/367166547_Real_gas_effect_on_ignition_in_ideal_and_non-ideal_reactors/links/63f03d9251d7af0540342c6d/Real-gas-effect-on-ignition-in-ideal-and-non-ideal-reactors.pdf?origin=publicationDetail&_sg%5B0%5D=X5RuElypO_sixSua3Z6OEiR9luzAFxEJdTgMRBQho6xKENOhTJcFWyfBz6LRLay3x9p2uUCACtX6FuRrDBLqYQ.JvTicCagd1tJMQeZe3CjQYmdBKIQ29T5peHnj267_usDSRaJV2G7oTsAqUj_XerdOyl9tTA5OZmGoUQGzG-VZg&_sg%5B1%5D=QsWeON4bmXLW5AnODp_l-r7HkAgddBPcpPc_CAXeSQXVFg6mOUfD_zMfjKZUgPbVyU0eZwOUFvVawTgne-ETdy6hHEEeIMvp2hM5wfPVONJZ.JvTicCagd1tJMQeZe3CjQYmdBKIQ29T5peHnj267_usDSRaJV2G7oTsAqUj_XerdOyl9tTA5OZmGoUQGzG-VZg&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>
<div id="wengCNF2022" class="bibtex noshow">
<pre>
@article{wengCNF2022,
  title = {Real Gas Effect on Steady Planar Detonation and Uncertainty Quantification},
  author = {Weng, Zifeng and Mével, Rémy},
  year = {2022},
  journal = {Combustion and Flame},
  volume = {245},
  pages = {112318},
  doi = {10.1016/j.combustflame.2022.112318}
}
</pre></div>
</li>

<li>
<p>
<b>Direct Detonation Initiation: A Comparison between the Critical Curvature and Critical Decay Rate Models</b><br>
<b>Zifeng Weng</b>, Zhaoyuan Huang, Feixue Cai, Jiawei Xu, Rémy Mével*<br>
<i>Physics of Fluids</i> <br>
<a href="javascript:toggleBibtex('wengPoF2021')" class="textlink">[bib]</a>
<a href="https://www.researchgate.net/profile/R-Mevel/publication/354370331_Direct_Detonation_Initiation_A_Comparison_between_the_Critical_Curvature_and_Critical_Decay_Rate_Models/links/61433e2b27c6bf1457967df0/Direct-Detonation-Initiation-A-Comparison-between-the-Critical-Curvature-and-Critical-Decay-Rate-Models.pdf?origin=publicationDetail&_sg%5B0%5D=6sMVH4aLSJnr9-J4XHDWy0ufuDRP118-Ct1Kw2Fsxh4J6OqzGssZxN5vC8ZQ3c0VSl679koe3cQQwG0x3_V6vQ.-s0qAkvXIzthcxMuGxHL4I_rOnUh9iiDuanLdblm5SSV4MwuijihHntiiSjyx2YDOh1n7-4TRsWFGH55yGhvzw&_sg%5B1%5D=76nldBiWCBCrCoZfCRdOvA8UEdUk8XFIdMY6UpjIy0ez4SwNMOJZoixtsOA4Qq56ZJ-Iz5EJ6R5CU4nSvmrkWOrwhsRSApgFTqPocoJ6GMhq.-s0qAkvXIzthcxMuGxHL4I_rOnUh9iiDuanLdblm5SSV4MwuijihHntiiSjyx2YDOh1n7-4TRsWFGH55yGhvzw&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>
<div id="wengPoF2021" class="bibtex noshow">
<pre>
@article{wengPoF2021,
  title = {Direct Detonation Initiation: {{A}} Comparison between the Critical Curvature and Critical Decay Rate Models},
  shorttitle = {Direct Detonation Initiation},
  author = {Weng, Zifeng and Mével, Rémy and Huang, Zhaoyuan and Cai, Feixue and Xu, Jiawei},
  year = {2021},
  journal = {Physics of Fluids},
  volume = {33},
  number = {9},
  pages = {096110},
  doi = {10.1063/5.0062506}
}
</pre></div>
</li>

<li>
<p>
<b>On the Controlled Evolution for Wingtip Vortices of a Flapping Wing Model at Bird Scale</b><br>
Suyang Qin, <b>Zifeng Weng</b>, Zhuoqi Li, Yang Xiang*, Hong Liu<br>
<i>Aerospace Science and Technology</i> <br>
<a href="javascript:toggleBibtex('qinAST2021')" class="textlink">[bib]</a>
<a href="https://www.researchgate.net/profile/Zifeng-Weng/publication/348050576_On_the_controlled_evolution_for_wingtip_vortices_of_a_flapping_wing_model_at_bird_scale/links/5ff27837a6fdccdcb82a7544/On-the-controlled-evolution-for-wingtip-vortices-of-a-flapping-wing-model-at-bird-scale.pdf?origin=publicationDetail&_sg%5B0%5D=R7qiL20jecOSladRdXMKNSXeM13ITQkyH6tZPbicMqsKN90I4H9ZXgEZfxAyLvVfctafzpI3H1EzGA6FouqLkA.7kSUEUVmBw_l5JKcLNbfy8bkjAtbHkdbywkcSKp4WGruvJFh43UF5ihR_3wpzaDGpeWC8lqdkHYalTcsFtSUJg&_sg%5B1%5D=ZAANn7GC8jzTAQXk6T3Bddw7cctlgOAgkxzQa7Ev6f9POy_qVfz9hWI_akd5SU-9FplCc-QrmuDWsaE43LtRakruLbL6QYG1rXNRmGYti9JH.7kSUEUVmBw_l5JKcLNbfy8bkjAtbHkdbywkcSKp4WGruvJFh43UF5ihR_3wpzaDGpeWC8lqdkHYalTcsFtSUJg&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D" class="textlink" target="_blank">[pdf]</a>
</p>
<div id="qinAST2021" class="bibtex noshow">
<pre>
@article{qinAerospaceScienceandTechnology2021,
  title = {On the Controlled Evolution for Wingtip Vortices of a Flapping Wing Model at Bird Scale},
  author = {Qin, Suyang and Weng, Zifeng and Li, Zhuoqi and Xiang, Yang and Liu, Hong},
  year = {2021},
  journal = {Aerospace Science and Technology},
  volume = {110},
  pages = {106460},
  doi = {10.1016/j.ast.2020.106460}
}
</pre></div>
</li>

</ol>

## 📗 Peer-reviewed Conference Papers 
<ol>
To update
</ol>