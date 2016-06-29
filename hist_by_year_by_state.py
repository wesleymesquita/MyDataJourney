#!/usr/bin/python3

import sys
import os
import pandas as pd
import matplotlib.pyplot as mpl

class Excp(Exception):
    pass


def show_hists(base_dir, years=[]):
    
    #verify if 'raw' directory exists
    if os.path.exists('raw') == False:
        raise Excp("Error: Wrong directory structure")
        
        #verify if there is something to plot
    if len(years) == 0:
        raise Excp("Error: Nothing to print, especify some years")
          
    for year in years:
        pass

        

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
            print("""Error : Use python3 hist_by_year_by_state.py BaseDir YYYY1 YYYY2 YYY3 where  
                  BaseDir contains the Healhcare Marketplace directory from Kaggle, and YYYYx
                  are the years you want histograms. Eg. : python3 hist_by_year_by_state.py . 2014 2015""")
    else:
        years=sys.argv[2:]
        show_hists(sys.argv[1],years)

