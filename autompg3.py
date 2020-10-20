#Eric Browne Student#: 873517924
#COMPP 3006: Python2
#Project 8: Autompg version 3

import sys
from collections import namedtuple
import matplotlib.pyplot as plt
import os
import csv
import logging
import requests
import argparse

FORMAT = '%(asctime)-15s %(levelname)s %(filename)s%(message)s'
logging.basicConfig(format=FORMAT,filename = "logfile.log",level=logging.DEBUG)
logger = logging.getLogger('autompg')
logger2 = logging.getLogger('autompg.data')
logger.debug(" Logging started")

class AutoMPG:
    ''' This class will represent an automobile, containing its make, model, year,
    and mgp
    '''
    def __init__(self, make, model, year, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg

    def __eq__(self,other):
        if type(self) == type(other):
            return self.make == other.make and self.model == other.model and \
                   self.year == other.year and self.mpg == other.mpg
        else:
            return NotImplemented

    def __repr__(self):
        return f"AutoMPG(\'{self.make}\',\'{self.model}\',\'{self.year}\',\'{self.mpg}\')"

    def __str__(self):
        return self.__repr__()
    def __lt__(self,other):
        ''' This will compare the make lexicographically.  Which is if they are equal, it will compares the model, mpg and year
        '''

        if type(self) == type(other):
            if self.make != other.make:
                return self.make < other.make
            if self.model != other.model:
                return self.model < other.model
            if self.year != other.year:
                return self.year < other.year

            return self.mpg < other.mpg

        else:
            return NotImplemented

    def __hash__(self):
        ## Since all instance variables are immutable types, put them in a tuple
        ## and hash the tuple
        return hash((self.make,self.model,self.year,self.mpg))

def byYear(a):
    return a.year

def byMPG(a):
    return a.mpg

corrections = [
    ["chevroelt","chevrolet"],
    ["chevy","chevrolet"],
    ["maxda","mazda"],
    ["mercedes-benz","mercedes"],
    ["toyouta","toyota"],
    ["vokswagen","volkswagen"],
    ["vw","volkswagen"]
]

#Now make the AUTOMPGDATA class:
class AutoMPGData:
    ''' Class that contains methods to parse a data file containing information
    on automobiles, and creates a list of AutoMPG types from that file.
    '''
    def __iter__(self):
        ## take advantage of the built in iterator for list types
        return iter(self.data)

    def __init__(self):
        self.data = list()
        self._load_data()

    def mpg_by_year(self):

        '''This will return a dictionary where the keys are the years that are present in the data set and the values are the average MPG for all cars in that year
        '''
        sums = {}
        counts = {}
        for entry in self.data:

            # test that the entry has a number for 'mpg'
            valid = False
            try:
                test = int(float(entry.mpg))
                # If the above conversion fails,
                # control goes straight to the 'except' block.
                valid = True
            except: # if not a number, exception will be thrown
                # we catch it to clear it,
                # and do nothing
                pass

            if valid:
                if entry.year in sums:
                    sums[str(entry.year)] += int(float(entry.mpg))
                    counts[str(entry.year)] += 1
                else:
                    sums[str(entry.year)] = int(float(entry.mpg))
                    counts[str(entry.year)] = 1

        for key in counts:
            sums[key] /= counts[key]

        return sums

    def mpg_by_make(self):
        '''This method should return a dictionary where the keys are the makes that are present in the data and the values are the average MPG for all cars of that make.
        '''
        sums = {}
        counts = {}
        for entry in self.data:

            valid = False

            try:
                test = int(float(entry.mpg))

                valid = True

            except:
                pass
            if valid:
                if entry.make in sums:
                    sums[entry.make] += int(float(entry.mpg))
                    counts[entry.make] += 1
                else:
                    sums[(entry.make)] = int(float(entry.mpg))
                    counts[entry.make] = 1

        for key in counts:
            sums[key] /= counts[key]

        return sums

    def _load_data(self):
        ''' Loads data from a 'cleaned' file; if the cleaned file doesn't exist,
        calls the method that creates a cleaned file and then proceeds. Reads
        each line of the data file, parses out the fields of interest, and creates
        AutoMPG types with that data.
        '''
        Record = namedtuple('Record',['mpg','cylinders','displacement',\
                            'horsepower','weight','acceleration','modelYear',\
                            'origin','carName'])

        if not os.path.exists("auto-mpg.data.txt"):
            self._get_data()


        if not os.path.exists("auto-mpg.clean.txt"):
            self._clean_data()

        with open("auto-mpg.clean.txt") as csvfile:
            mpgreader = csv.reader(csvfile,delimiter=' ',skipinitialspace=True)

            for row in mpgreader:
                rec = Record(*row)
                logger.debug("line "+str(rec) +" loaded from cleaned file.")
                ## The first word of the carname is the make, all following words
                ## are the model

                make = rec.carName.split()[0]
                model = ' '.join(word for word in rec.carName.split()[1:])
                self.data.append(AutoMPG(make,model,'19'+rec.modelYear,rec.mpg))

        logger.info(" Data succesfully loaded")

    def _clean_data(self):
        ''' Called only when a 'cleaned' data file doesn't exist. A cleaned file
        means one in which all tabs have been converted to spaces to make parsing
        the file easier.
        '''
        with open("auto-mpg.data.txt") as inFile:
            with open("auto-mpg.clean.txt","w") as outFile:
                for line in inFile:
                    corrected = line
                    for corr in corrections:
                        corrected = corrected.replace(corr[0],corr[1])
                    outFile.write(corrected.expandtabs(1))
                    logger.info("Data has been cleaned up")

    def sort_by_year(self):
        return self.data.sort(key=byYear,reverse=False)

    def sort_by_mpg(self):
        return self.data.sort(key=byMPG,reverse=False)

    def list_of_years(self):
        list = []
        for entry in self.data:
            list.append(entry.year)
        return list
    def sort_by_default(self):
        return self.data.sort()

    def list_of_makes(self):
        list = []
        for entry in self.data:
            list.append(entry.make)
        return list

    def list_of_mpgs(self):
        list = []
        for entry in self.data:
            list.append(entry.mpg)

        return list

    def _get_data(self):
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
        response = request.get(url)

        f = open("auto-mpg.data.txt","w+")

        response_Text = response.content.decode("utf-8")
        f.write(response_Text)
        f.close


def main():

    parser = argparse.ArgumentParser(description= "v")
    parser.add_argument('--sort', choices = ["default","mpg","year"],required = False)
    parser.add_argument('--ofile',type = str)
    parser.add_argument('--plot',action = 'store_true')
    parser.add_argument('--print',action = 'store_true')
    parser.add_argument('--mpg_by_year',action = 'store_true')
    parser.add_argument('--mpg_by_make',action = 'store_true')

    args = parser.parse_args(sys.argv[1:])

    sort = args.sort
    ofile = args.ofile
    plot = args.plot
    doPrint = args.print or ofile
    yearAvgs = args.mpg_by_year
    makeAvgs = args.mpg_by_make
    printDataset = not yearAvgs and not makeAvgs

    if ofile:
        original_stdout = sys.stdout
        #  repoening stdout
        sys.stdout = open(ofile, "w+")

    dataset = AutoMPGData()
    #print(sort)
    if sort:
        if sort == "mpg":
            dataset.sort_by_mpg()
        if sort == "year":
            dataset.sort_by_year()
    else:
        pass

    if doPrint:
        # Only print the whole dataset if neither mpg_by_year or mpg_bymake was specified
        if printDataset:
            for car in dataset:
                print(car.make + "\t" + car.model + "\t" + car.year + "\t" + car.mpg)
        else:
            if makeAvgs:
                avgs = dataset.mpg_by_make()
            else:
                avgs = dataset.mpg_by_year()
            for key in avgs:
                print(key + "\t" + str(avgs[key]))

    if plot:
        if yearAvgs:
            x = dataset.list_of_years()
        else:
            x = dataset.list_of_makes()
        y = dataset.list_of_mpgs()
        p = plt.bar(x,y)
        plt.show()

if __name__ == '__main__':
    main()

logger.info(" Program Run succesfully")
