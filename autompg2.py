import os
import logging
import requests
import argparse
import sys
import csv
from collections import namedtuple

FORMAT = '%(asctime)-15s %(levelname)s %(filename)s%(message)s'
logging.basicConfig(format=FORMAT,filename = "logfile.log",level=logging.DEBUG)
logger = logging.getLogger('autompg')
logger2 = logging.getLogger('autompg.data')
logger.debug(" Logging started")

class AutoMPG:
    ''' Class to represent an automobile, containing its make, model, year,
    and miles per gallon
    '''

    def __init__(self, make, model, year, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg

    def __repr__(self):
        return f"AutoMPG(\'{self.make}\',\'{self.model}\',\'{self.year}\',\'{self.mpg}\')"

    def __str__(self):
        return self.__repr__()

    def __eq__(self,other):
        if type(self) == type(other):
            return self.make == other.make and self.model == other.model and \
                   self.year == other.year and self.mpg == other.mpg
        else:
            return NotImplemented

    def __lt__(self,other):
        ''' Compares the make lexicographically: if they are equal, compares the model;
        if they are equal, compares the year; if they are equal, compares the mpg
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

class AutoMPGData:
    ''' Class that contains methods to parse a data file containing information
    on automobiles, and creates a list of AutoMPG types from that file.
    '''
    def __init__(self):
        self.data = list()
        self._load_data()

    def __iter__(self):
        ## take advantage of the built in iterator for list types
        return iter(self.data)
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
                    outFile.write(line.expandtabs(1))
                    logger.info("Data has been cleaned up")
    def sort_by_default(self):
        return self.data.sort()
    def sort_by_year(self):
        return self.data.sort(key=byYear,reverse=False)
    def sort_by_mpg(self):
        return self.data.sort(key=byMPG,reverse=False)
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
    args = parser.parse_args(sys.argv[1:])
    sort = args.sort
    dataset = AutoMPGData()
    print(sort)
    if sort:
        print("sorted")
        if sort == "mpg":
            print("sort by mpg")
            dataset.sort_by_mpg()
    else:
        print('no')
    for car in dataset:
        print(car)
if __name__ == '__main__':
    main()

logger.info(" Program Run succesfully")
