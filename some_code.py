import argparse
import datetime

def workdays(d, end, excluded=(6, 7)):
    days = []
    while d.date() <= end.date():
        if d.isoweekday() not in excluded:
            day_to_append=int(d.strftime('%Y%m%d'))
            days.append(day_to_append)
        d += datetime.timedelta(days=1)
    return days

def valid_date_range(date_range):
   """ custom argparse date type for user dates values given from the command line"""
   try:
     date_limit=date_range.split('-')
     print date_limit
   except:
     print("Please respect the following format for the range value: 20180203-2010405")
   try:
     date_list=[]
     start_date=datetime.datetime.strptime(date_limit[0], "%Y%m%d")
     end_date=datetime.datetime.strptime(date_limit[1],"%Y%m%d")
     date_list.append(start_date)
     date_list.append(end_date)
     return date_list
   except ValueError:
     msg="Given range ({0}) not valid! Expected format YYYYMMDD-YYYYMMDD!".format(date_range)
     raise argparse.ArgumentTypeError(msg) 
   
     
parser = argparse.ArgumentParser(description='Example with non optional arguments')

parser .add_argument('--source','-s', 
                      type=str,
                      dest='source',
                      required=True,
                      help='Source if from where we copy files')
parser.add_argument('--dest','-d',
                     type=str,
                     dest='destination',
                     required=True,
                     help="Destination is where we copy files to")

parser.add_argument('--range', '-r',
                     type=valid_date_range,
                     dest='date_range',
                     help="This the range of ofdates, ofr instances it should be something like this 20191012-20191105")

parser.add_argument('--dates',
                   type=str,
                   dest='dates')

print parser.parse_args()

args=parser.parse_args()
source_arg=args.source
dest_arg=args.destination
date_range=args.date_range
dates_arg=args.dates
#print(source,dest, date_range, dates)
dates_list=[]
###################################################################################
if date_range is not None:
   start_date=date_range[0]
   end_date=date_range[1]
   dates_list=workdays(start_date,end_date)   
   print dates_list
###############################################"
if dates_arg is not None:
   dates_str=dates_arg.split(' ')
   dates_int=[int(d) for d in dates_str] 
   dates_list.extend(dates_int)
   print (dates_list)
