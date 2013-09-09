import requests


def get_solar_intensity(longitude, latitude):
    # result = requests.post('http://re.jrc.ec.europa.eu/pvgis/apps4/PVcalc.php',
    #                        data={'regionname': 'europe',
    #                              'pv_database': 'PVGIS-CMSAF',
    #                              'MAX_FILE_SIZE': '10000',
    #                              'pvtechchoice': 'crystSi',
    #                              'peakpower': '1',
    #                              'efficiency': '14',
    #                              'mountingplace': 'free',
    #                              'angle': '35',
    #                              'aspectangle': '0',
    #                              'outputchoicebuttons': 'text',
    #                              'sbutton': 'Calculate',
    #                              'outputformatchoice': 'window',
    #                              'optimalchoice': '',
    #                              'latitude': str(latitude),
    #                              'longitude': str(longitude),
    #                              'regionname': 'europe',
    #                              'language': 'en_en'
    #                              },
    #                              files={}
    #                        )
    result = requests.post('http://re.jrc.ec.europa.eu/pvgis/apps4/MRcalc.php',
                           data={'regionname': 'europe',
                                 'mr_database': 'PVGIS-classic',
                                 'horirrad': 'true',
                                 'optrad': 'true',
                                 'selectrad': 'true',
                                 'monthradangle': '90',
                                 'optincl': 'true',
                                 'avtemp': 'true',
                                 'degreedays': 'true',
                                 'outputchoicebuttons': 'text',
                                 'sbutton': 'Calculate',
                                 'outputformatchoice': 'window',
                                 'optimalchoice': '',
                                 'latitude': str(latitude),
                                 'longitude': str(longitude),
                                 'regionname': 'europe',
                                 'language': 'en_en'
                                 },
                           )
    print result.text

if __name__ == '__main__':
    get_solar_intensity(10.283, 59.727)
