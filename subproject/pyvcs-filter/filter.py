"""
Filter cvs file with the library pandas

@author https://github.com/vincenzopalazzo
"""
import csv
import sys
import logging


# TODO description
def from_file_to_file(fromFile, toFile):
    if (fromFile is None) or (toFile is None):
        raise ValueError('From file or to file are null')
    mapFilter = extract_data(fromFile)
    if mapFilter is not None:
        store_data(toFile, mapFilter)


# TODO description
def extract_data(fromFile):
    with open(fromFile,) as csvfile:
        readCsv = csv.reader(csvfile, delimiter=',')
        mapVelue = {}
        mapTime = {}
        mapResult = {}
        for row in readCsv:
            contrySelected = ''
            for (indexCol, valueCol) in enumerate(row):
                logging.debug('index %s', indexCol)
                logging.debug('Value %s', valueCol)
                if indexCol == 1:
                    contryName = pars_string(valueCol)
                    logging.debug(contryName)
                    if contryName is None:
                        continue
                    contrySelected = contryName
                    if contryName not in mapVelue:
                        logging.debug('*********** init value map ********************')
                        mapVelue[contryName] = 0.0
                        mapTime[contryName] = 0
                    mapTime[contryName] += 1
                elif (indexCol == 2) and (contryName in mapVelue):
                    logging.debug('Before: %s', mapVelue[contrySelected])
                    mapVelue[contrySelected] += float(valueCol)
                    logging.debug('After: %s', mapVelue[contrySelected])
        for (country, sumTemp) in mapVelue.items():
            logging.debug('Country %s', country)
            logging.debug('time %s', mapTime[country])
            logging.debug(' Avg temp: %s', (sumTemp / mapTime[country]))
            mapResult[country] = (sumTemp / mapTime[country])
        logging.debug('Result is: %s', mapResult)
        return mapResult


# TODO description
def store_data(toFile, data):
    with open(toFile, 'w', newline='') as csvfile:
        writeCvs = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writeCvs.writerow(['Country', 'Temp'])
        for country, temp in data.items():
            writeCvs.writerow([country, temp])


# TODO description
def pars_string(valueCol):
    spliStrign = valueCol.split()
    #print('parsString pars: ', spliStrign)
    if 'CD' in spliStrign:
        #print('parString', spliStrign[0])
        return spliStrign[0]
    return None


if __name__ == '__main__':
    if len(sys.argv) > 0:
        logging.basicConfig(level=logging.WARNING)
        logging.debug('Read Data from: %s', sys.argv[1])
        logging.debug('Store filter data: %s', sys.argv[2])
        from_file_to_file(sys.argv[1], sys.argv[2])

