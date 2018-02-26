# favorites-generator

Excercise 

The attached text file contains the favorite musical artists of 1000 users from Some Popular Music Review Website. Each line is a list of up to 50 artists, formatted as follows:

Radiohead,Pulp,Morrissey,Delays,Stereophonics,Blur,Suede,Sleeper,The La's,Super Furry Animals,Iggy Pop\n

Band of Horses,Smashing Pumpkins,The Velvet Underground,Radiohead,The Decemberists,Morrissey,Television\n

etc.

Write a program that, using this file as input, produces an output file containing a list of pairs of artists which appear TOGETHER in at least fifty different lists. For example, in the above sample, Radiohead and Morrissey appear together twice, but every other pair appears only once. Your solution should be a cvs, with each row being a pair. For example:

Morrissey,Radiohead\n

Your solution MAY return a best guess, i.e. pairs which appear at least 50 times with high probability, as long as you explain why this tradeoff improves the performance of the algorithm. Please include, either in comments or in a separate file, a brief one-paragraph description of any optimizations you made and how they impact the run-time of the algorithm.

Please make your solution in a language you feel comfortable with. We prefer that you use: Python, Kotlin, OCaml, Python, or Java. If you prefer to do another language not on this list please let us know.


Resolution:

You can run it by calling python favorites-generator.py

In case you want to see the instructions you can run python favorites-generator.py -h . 

Please note that I have built the script using  Python 2.7.5 .  It does not run on Python 3 because there are some differences in the way it manages files and encoding.

