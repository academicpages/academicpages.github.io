import { FaGoogleScholar, FaRegIdBadge, FaGithub } from "react-icons/fa6";

export const profile = {
  name: `Matteo Guida`,
  headline: `PhD Candidate @ University of Melbourne`,
  email: `matteo.guidaa@gmail.com`,
  location: `Melbourne, Australia`,
  profileImage: `/images/second_profile.png`,
  links: [
    {
      name: `Google Scholar`,
      url: `https://scholar.google.com/citations?user=Z4WLFFIAAAAJ&hl=en&oi=ao`,
      icon: FaGoogleScholar
    },
    {
      name: `Résumé`,
      url: `/pdf/MatteoGuida_Resume_I.pdf`,
      icon: FaRegIdBadge
    },
    {
      name: `Github`,
      url: `https://github.com/mattguida`,
      icon: FaGithub
    }
  ],
  biography: `My research uses computational methods drawing from <em>natural language processing</em> and statistical methods to understand human behaviour through vast collections of online data — looking at how framing, moral values, and argumentation shape the way we read the news, respond to it, and reshape each other's views in the comments.
<div class="my-2"></div>
I'm a Ph.D. candidate at the University of Melbourne's School of Computing and Information Systems, supervised by <a href="https://www.frermann.de/" target="_blank" rel="noopener noreferrer">Prof. Lea Frermann</a>, <a href="https://findanexpert.unimelb.edu.au/profile/887453-eduard-hovy" target="_blank" rel="noopener noreferrer">Prof. Ed Hovy</a>, and <a href="https://scholar.google.com/citations?user=yzaozUUAAAAJ&hl=en" target="_blank" rel="noopener noreferrer">Dr. Yulia Otmakhova</a>. Before this, I completed a Masters in Speech and Language Processing at the University of Konstanz.
<div class="my-2"></div>
I'm currently looking for opportunities to apply my experience in natural language processing, machine learning, and large-scale data analysis — ideally in media intelligence, media analytics, audience insights, or a related field. Feel free to <a href="mailto:matteo.guidaa@gmail.com" target="_blank" rel="noopener noreferrer">reach out</a> to connect.`
};