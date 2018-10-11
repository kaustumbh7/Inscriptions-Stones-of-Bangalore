# Inscriptions-Stones-of-Bangalore

The Inscription Stones of Bangalore project aims at preserving the inscription stones discovered in Bangalore region and nearby places by making people aware of the historical significance and heritage of these stones.

This repository aims at OCR Correction of a book called Epigraphia Carnatica  [Epigraphia Carnatica](http://idb.ub.uni-tuebingen.de/opendigi/EC_17_1965#p=2)  by B.L. Rice. The OCR conversion of the book conatins many English as well as Kannada errors so first an analysis of different types of errors is done.
## Analysis of Errors ## 
Single characters recognized as multiple characters - SCMC                                                               Multiple characters recognized as one character - MCOC
Division and concatenation of words - DAC
Single character recognized as another character - SCAC
Format -  Original Characters = Misinterpreted Character

SCMC | MCOC | DAC | SAC | Unique Errors 
-----|------|------|----|---------
w = vv|	es = *|	goingbangalore|	f = i (6)| sprar = sprang
t = tt|	ti = a|	beit (2)|	r = i (3)| missing i (2)
h = ii (2)| 	( = c| 	foras|	l = i (6)|	missing d
m = tn|	re = n|	boundarie s|	u = a|		firm

The above table illustrates how the analysis of errors is done. 
## Implementation ##  
* A web scraper was designed to extract the book Epigraphia Karnataka into a Soft copy as it is not available online.
* Cleaned the text , removed diacritical marks and other symbols.
* Created a Kannada Words Dictionary to work on the Transliterations part of the book Epigraphia Karnataka.
* Removed all the English words from the text.(So we are left with English error words and proper nouns)
* Modified a spell checker algorithm to suit our need
* First we pass a small lexicon and check which words don’t change and can classify those words as proper nouns.
* After that we remove proper nouns from the list of error words.
* Now we are left with English error words , which are  passed through the algorithm and corrected.

## Further Work ## 
* Resolve all Kannada errors from Transliterations part.
* To be able to separate all the proper nouns from the text.
* Improve the accuracy of the algorithm to correct more error words precisely.


