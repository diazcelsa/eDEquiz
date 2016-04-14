### eDEquiz | Learn German Vocabulary that You Need

The most boring part of learning a language is to memorize those large lists of vocabulary in order to reach the next level and finally feel fluid talking.

There are tones of books focused on vocabulary learning. However, you can not choose the content of the vocabulary you want or need to learn. Furthermore, in those books, you can not train again and again as much times as you need.

Here we present a tool based on Pandas package (Python) that can help you to memorize those words that you can not keep on mind. The software will take the vocabulary that you have to learn, it will randomly organize the order and will ask you for the translation in german. It differenciates between substantives, verbs and adjectives/adverbs/expresions. 

- Verbs: you may differenciate between transitive and intransitive and also give the preposition when the meaning includes the verb with prepositon
- Substantives: you may specify the gender of the substantive as well (die: Kueche, der: Balkon, das: Zimmer). We use a location-visualization tool to identify genders.
- Adverbs/Adjectives/Expressions: you just need to give the translation

The number of elements given and the correct answers as well as its propotion and the date of the quiz will be stored in results.csv so you can evaluate you progression.

The input data format is a .csv file with two columns (german and your original language), six columns when substantives with three genders and four columns when verbs transitive and intransitive. You can explore several examples in ./data/ of input files.
