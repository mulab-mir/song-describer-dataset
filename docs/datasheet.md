# Datasheet: Song Describer Dataset

## Motivation

1. **For what purpose was the dataset created?** Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.

	*The dataset was created in order to provide the research community with a public dataset for music-and-language tasks containing audio with permissive licenses. The primary use case for the dataset is the evaluation of machine learning models on tasks such as music captioning, text-to-music generation and music-text retrieval.*

2. **Who created this dataset (e.g. which team, research group) and on behalf of which entity (e.g. company, institution, organization)**?

	*The dataset is a result of a research collaboration undertaken by Universal Music Group International Limited (part of Universal Music Group), Queen Mary University of London, and Music Technology Group (Universitat Pompeu Fabra).*

3. **What support was needed to make this dataset?** (e.g. who funded the creation of the dataset? If there is an associated grant, provide the name of the grantor and the grant name and number, or if it was supported by a company or government agency, give those details.)

	*The dataset creation was funded by: UK Research and Innovation [grant number EP/S022694/1], Universal Music Group, The Musical AI project - PID2019-111403GB-I00/AEI/10.13039/501100011033, (funded by the Spanish Ministerio de Ciencia e Innovación and the Agencia Estatal de Investigación)*

4. **Any other comments?**

	*-*


## Composition

1. **What do the instances that comprise the dataset represent (e.g. documents, photos, people, countries)?** Are there multiple types of instances (e.g. movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description.

	*The dataset consists of music audio recordings (each recording of a different music track) associated with music captions (up to 5 captions per recording, written by different participants in the annotation platform).*

2. **How many instances are there in total (of each type, if appropriate)?**

	*There are 1106 captions of 706 recordings in total, written by 142 annotators. We also provide a cleaned subset containing manually validated annotations, consisting of 746 captions of 547 audio recordings, written by 114 annotators.*

3. **Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?** If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g. geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g. to cover a more diverse range of instances, because instances were withheld or unavailable).

	*The audio associated with music captions is a subset of the larger [MTG-Jamendo dataset](https://mtg.github.io/mtg-jamendo-dataset/) containing over 55k tracks. Due to the annotation effort, we sampled a random subset of tracks from the test set of the `split-0`. The representativeness of our random subset was validated by comparing the distribution of music tags in our subset to that of the full dataset.*

4. **What data does each instance consist of?** "Raw" data (e.g. unprocessed text or images) or features? In either case, please provide a description.

	*Each instance consists of an audio-text pair. Audio: one music audio segment per track, with segment duration up to 2 minutes, trimmed from the beginning of a music track (95\% of the segments are 2 minutes). Each audio file is provided in 320kbps 44.1 kHz MP3 audio encoding. Text: unprocessed music caption provided as a list of strings of text, associated with the audio segments.*

5. **Is there a label or target associated with each instance?** If so, please provide a description.

	*There is no ground-truth label. Depending on the task, either the audio or the text in a given instance constitutes the target (e.g. in music captioning, the target is the caption).*

6. **Is any information missing from individual instances?** If so, please provide a description, explaining why this information is missing (e.g. because it was unavailable). This does not include intentionally removed information, but might include, e.g. redacted text.

	*There is no missing information.*

7. **Are relationships between individual instances made explicit (e.g. users' movie ratings, social network links)?** If so, please describe how these relationships are made explicit.

	*Each instance is associated to a track ID which can be linked to the original MTG-Jamendo dataset. Relationships between instances can be easily explored from this through the MTG-Jamendo metadata, which contains additional information such as artist, album, genre etc.*

8. **Are there recommended data splits (e.g. training, development/validation, testing)?** If so, please provide a description of these splits, explaining the rationale behind them.

	*There is no recommended split, as the dataset is intended to be used solely for evaluation.*

9. **Are there any errors, sources of noise, or redundancies in the dataset?** If so, please provide a description.

	*The annotations may be prone to noise and bias due to the subjectivity of the task, different levels of familiarity with the kind of music being annotated by the participants, and differences in their English language level. The dataset creators manually reviewed all captions to ensure consistency with the annotation guidelines and overall quality, leading to a smaller, curated subset.*

10. **Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g. websites, tweets, other datasets)?** If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created); c) are there any restrictions (e.g. licenses, fees) associated with any of the external resources that might apply to a future user? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.

	*The dataset is self-contained (all audio and metadata are distributed as part of the dataset package, including CC licenses for the individual tracks). No fees or restrictions apply to any of the material making up the dataset. The dataset can be additionally mapped to the metadata in the MTG-Jamendo dataset via track IDs. Additionally, the annotation platform used in creating the dataset is open-source and publicly accessible at [https://github.com/ilaria-manco/song-describer](https://github.com/ilaria-manco/song-describer).*

11. **Does the dataset contain data that might be considered confidential (e.g. data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications)?** If so, please provide a description.

	*There is no confidential information in the dataset.*

12. **Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?** If so, please describe why.

	*Individual songs might contain lyrics that could be considered offensive by listeners. Annotators were appropriately informed about this risk.*

13. **Does the dataset relate to people?** If not, you may skip the remaining questions in this section.

	*The dataset includes human annotations of music recordings and therefore relates to people. However, the participation in the annotation platform was anonymous and no personal data or personally identifiable information was collected. *

14. **Does the dataset identify any subpopulations (e.g. by age, gender)?** If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.

	*No.*

15. **Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?** If so, please describe how.

	*No.*

16. **Does the dataset contain data that might be considered sensitive in any way (e.g. data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?** If so, please provide a description.

	*No.*

17. **Any other comments?**

	*No.*


## Collection

1. **How was the data associated with each instance acquired?** Was the data directly observable (e.g. raw text, movie ratings), reported by subjects (e.g. survey responses), or indirectly inferred/derived from other data (e.g. part-of-speech tags, model-based guesses for age or language)? If data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.

	*The data was reported by subjects in the form of free-form text annotations and manually validated by the authors following collection.*

2. **What mechanisms or procedures were used to collect the data (e.g. hardware apparatus or sensor, manual human curation, software program, software API)?** How were these mechanisms or procedures validated?

	*The data was collected via a [self-developed online software platform](https://song-describer.streamlit.app/). This was validated via two pilot studies prior to starting the data collection.*

3. **If the dataset is a sample from a larger set, what was the sampling strategy (e.g. deterministic, probabilistic with specific sampling probabilities)?**

	*The recordings were randomly sampled from the test set of split-0 of the MTG-Jamendo with weights proportional to play counts from the [Jamendo platform](https://developer.jamendo.com/v3.0).*

4. **Who was involved in the data collection process (e.g. students, crowdworkers, contractors) and how were they compensated (e.g. how much were crowdworkers paid)?**

	*Volunteers (above 18 years of age) were recruited via an open call circulated among relevant mailing lists and social networks. We hosted several rounds of annotation with a leaderboard showing (nicknames of) the participants and their number of annotations. The top-3 contributors for each round were rewarded with prizes. These consisted of online vouchers of a value ranging from £10 to £100.*

5. **Over what timeframe was the data collected?** Does this timeframe match the creation timeframe of the data associated with the instances (e.g. recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created. Finally, list when the dataset was first published.

	*YThe annotations were collected between 25th November 2022 and 14th April 2023. The instances are associated with music recordings created between 2004 and 2017.*

7. **Were any ethical review processes conducted (e.g. by an institutional review board)?** If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.

	*The project was approved by the Queen Mary Ethics of Research Committee (QMERC reference number: QMERC22.062). As part of the review, the following documentation was provided: a participant information sheet, a consent form, and an application form with detailed questions about the data collection procedure and potential risks. These were assessed by the committee through the low-risk approval route, according to the guidelines outlined on the [website](http://www.jrmo.org.uk/performing-research/conducting-research-with-human-participants-outside-the-nhs/applications-and-approval/).*

8. **Does the dataset relate to people?** If not, you may skip the remainder of the questions in this section.

	*Yes.*

9. **Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g. websites)?**

	*We collected the data via the online annotation platform we developed for this purpose (see questions above).*

10. **Were the individuals in question notified about the data collection?** If so, please describe (or show with screenshots or other information) how notice was provided, and provide a link or other access point to, or otherwise reproduce, the exact language of the notification itself.

	*Yes, the platform was built for data collection, thus it includes explicit notice and instructions. The landing page with most of the information can be accessed at [https://song-describer.streamlit.app](https://song-describer.streamlit.app). A more detailed description of the annotation platform can be found in [(Manco et al., 2022)](https://archives.ismir.net/ismir2022/latebreaking/000044.pdf). Below is the text that informs user about data collection and terms of use.*

    > Song Describer is a tool for crowdsourced collection of music captions, built by a team of researchers from Queen Mary University of London and Universitat Pompeu Fabra Barcelona. You will be asked to listen to some music and write a new description for it (Annotation) or evaluate an existing one (Evaluation). Each task takes only a few minutes. You can complete either task as many times as you'd like. By contributing to Song Describer, you are helping us release the first public dataset of music captions. We really appreciate your help! We will only collect data you provide by submitting your answers and no other personal information. To find out more about the project and how the data will be used, read our FAQs below.
    
    >This survey is part of a research project being undertaken by Universal Music Group International Limited (part of Universal Music Group), Queen Mary University of London, and Universitat Pompeu Fabra (together the “Research Team”). By participating in this survey, you acknowledge and agree to the following:
    
    ```
    • You must be aged 18 or over

    • You are participating in an academic study, the results of which may or may not be published in an academic journal.

    • Your participation is voluntary and you are free to leave at any time

    • All intellectual property rights which may arise or inure to you as a result of your participation in this survey are hereby assigned jointly, in full and in equal proportion to the members of the Research Team.

    • By participating in this study, you agree to waive any moral rights of authorship that you may have in the responses that you provide in the survey to the extent permitted by law.

    • The data collected by this survey is intended to be published and shall be freely available to all. The responses submitted by you shall not be attributable to you and your participation in the survey shall remain confidential.

11. **Did the individuals in question consent to the collection and use of their data?** If so, please describe (or show with screenshots or other information) how consent was requested and provided, and provide a link or other access point to, or otherwise reproduce, the exact language to which the individuals consented.

	*See the link and text in the previous question. At the bottom of the webpage is a button with "Get Started" text that shows a pop-up on hover: `By clicking here, you confirm that you agree with the statements above.`*

12. **If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?** If so, please provide a description, as well as a link or other access point to the mechanism (if appropriate).

	*Participants were made aware of the option to withdraw from the annotation procedure at any point.*

13. **Has an analysis of the potential impact of the dataset and its use on data subjects (e.g. a data protection impact analysis) been conducted?** If so, please provide a description of this analysis, including the outcomes, as well as a link or other access point to any supporting documentation.

	*No analysis of the potential impact was conducted.*

14. **Any other comments?**

	*No.*


## Preprocessing / Cleaning / Labeling

1. **Was any preprocessing/cleaning/labeling of the data done (e.g. discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?** If so, please provide a description. If not, you may skip the remainder of the questions in this section.

	*The annotations were manually validated by the research team. This was done by evaluating each caption on a 3-point Likert scale based on its adherence to the annotation guidelines provided. Although we distribute all the annotations (without any preprocessing or cleaning), validated captions are also marked as part of a higher-quality subset.*

2. **Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (e.g. to support unanticipated future uses)?** If so, please provide a link or other access point to the "raw" data.

	*All data is provided as part of the dataset release.*

3. **Is the software used to preprocess/clean/label the instances available?** If so, please provide a link or other access point.

	*We release code to preprocess, clean and analyse the data in an accompanying GitHub repository.*

4. **Any other comments?**

	*No.*


## Uses
1. **Has the dataset been used for any tasks already?** If so, please provide a description.

	*The dataset has been used for evaluating machine learning models on the following tasks: music captioning, text-to-music generation, and music-text retrieval.*

2. **Is there a repository that links to any or all papers or systems that use the dataset?** If so, please provide a link or other access point.

	*Links to papers and systems that use the dataset will be added to this repository.*

3. **What (other) tasks could the dataset be used for?**

	*The dataset may additionally be used to study how people describe music. However we note that due to the small sample size and an unbalanced representation of annotators from different countries, the make-up of the annotator pool must be carefully considered before drawing any conclusions from the analysis of the text in the dataset.*

4. **Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?** For example, is there anything that a future user might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g. stereotyping, quality of service issues) or other undesirable harms (e.g. financial harms, legal risks) If so, please provide a description. Is there anything a future user could do to mitigate these undesirable harms?

	*No.*

5. **Are there tasks for which the dataset should not be used?** If so, please provide a description.

	*We aim for this dataset to be used for evaluation and benchmarking of music-and-language models, thus we discourage using it for training.*

6. **Any other comments?**

	*No.*


## Distribution

1. **Will the dataset be distributed to third parties outside of the entity (e.g. company, institution, organization) on behalf of which the dataset was created?** If so, please provide a description.

	*The dataset will be publicly available online.*

2. **How will the dataset will be distributed (e.g. tarball on website, API, GitHub)?** Does the dataset have a digital object identifier (DOI)?

	*The dataset will be distributed via Zenodo (DOI: [10.5281/zenodo.10072001](https://doi.org/10.5281/zenodo.10072001)).*

3. **When will the dataset be distributed?**

	The dataset will be available from 17th November 2023.

4. **Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?** If so, please describe this license and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.

	*The dataset will be available under the [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0). The audio files, which are derived from the MTG-Jamendo dataset, are re-distributed as part of the dataset with the respective CC licenses. A list of individual licenses for all audio files is provided with the release.*

5. **Have any third parties imposed IP-based or other restrictions on the data associated with the instances?** If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.

	*No.*

6. **Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?** If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation.

	*No.*

7. **Any other comments?**

	*No.*


## Maintenance

*As with the previous section, dataset creators should provide answers to these questions prior to distributing the dataset. These questions are intended to encourage dataset creators to plan for dataset maintenance and communicate this plan with dataset consumers.*

1. **Who is supporting/hosting/maintaining the dataset?**

	*The dataset will be supported and maintained by Queen Mary University of London and the Music Technology Group (Universitat Pompeu Fabra). The dataset will be hosted on Zenodo and supporting code will be hosted on GitHub.*

2. **How can the owner/curator/manager of the dataset be contacted (e.g. email address)?**

	Queries about the datasets can be submitted by opening an issue on GitHub or emailing the dataset curators (i.manco@qmul.ac.uk, benno.weck01@estudiant.upf.edu). 

3. **Is there an erratum?** If so, please provide a link or other access point.

	*An erratum will be provided in the GitHub repository as necessary.*

4. **Will the dataset be updated (e.g. to correct labeling errors, add new instances, delete instances)?** If so, please describe how often, by whom, and how updates will be communicated to users (e.g. mailing list, GitHub)?

	*The dataset will be updated to correct errors if necessary. Additionally, it may be updated with new instances if further annotations are provided by volunteers through our data collection platform. If created, future versions of the dataset will be released via Zenodo and updates will be communicated via both GitHub and Zenodo.*

5. **If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g. were individuals in question told that their data would be retained for a fixed period of time and then deleted)?** If so, please describe these limits and explain how they will be enforced.

	*No personal data was collected and therefore there are no applicable limits on the retention of the data.*

6. **Will older versions of the dataset continue to be supported/hosted/maintained?** If so, please describe how. If not, please describe how its obsolescence will be communicated to users.

	*Older versions of the dataset will continue to be hosted and maintained. However any code related to the dataset will be updated to support only the most recent version. This will be explicitly mentioned in the repository.*

7. **If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?** If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to other users? If so, please provide a description.

	*The website to collect captions is currently available [online](https://song-describer.streamlit.app) and can be accessed for additional contributions. Its [source code](https://github.com/ilaria-manco/song-describer) is also public. Contributions are not directly integrated into the dataset, but will be considered for future version releases.*

8. **Any other comments?**

	*No.*
