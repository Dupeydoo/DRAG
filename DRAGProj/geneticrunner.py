#Main runner
#another with amount of times to play each note input by user but also generated
#main method called when validation has finished

import DRAGProj.generators.populationgenerator as pg

populationsize = 10
copyratio = 0.4
tournamentsize = 5
timesignature = 8     #two bars at 4:4
crossprob = 0.3
mutaprob = 0.6
fitnesses = [0 for f in range(populationsize)]

"""
single form:
1. take input from user in the form of dropdown choices, each choice is mapped to
a drum number. mappings file from string to drum number. user also submits tempo and genre
time sig is 4/4, 15 bars in a minute, 2 bars of 4. User could also select presets here

2. [1,2,3,4,5,6,8] have input now in array form.

"""

inputlist = [7, 1, 11, 1, 7, 7, 11, 1]
genre = "Rock"

"""

3. Generate population: use some copies of that array and then also generate random individuals
constrained to the genre to fill the rest. E.g. if rock use rock generator
List of lists as collection of candidates
initialise list of fitness values at 0.
"""

population = pg.generatepopulation(populationsize, copyratio, inputlist, genre, timesignature)

"""
4. while(!userSatisified || !userFinished)
      foreach candidate()
        map values to sounds()
        fuse sounds into single wav()
        render a small audio player with dropdown rating default 0()
        render button to submit to server()
        submit and populate fitness array()

      perform tournament selection based on candidates fitness match index to index in collection()

      foreach selected candidate()
          perform crossover based on pc()
          perform mutation based on pm()

      replace lowest fitness candidates with new candidates()

5. Display final generation tracks for one more fitness eval
6. Favourite one single audio player render, can download from that

common interface to fuse wav files based on bpm
"""