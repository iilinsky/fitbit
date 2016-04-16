#!/bin/bash

# INTERACTIVE
printf "\n Hi! Let's login to your Fitbit account!\n"
while true; do
	printf "\n Select an option from the following choice:\n"
	printf " [1] Log in as emilyaugason@gmail.com\n"
	printf " [2] Log in as ivanilinsky@gmail.com\n"
	printf " [3] Exit\n\n"
	read -p "  " mychoice
	case $mychoice in
		1 ) myuser="emily"
                    myemail="emilyaugason@gmail.com"; 
		    mypassword=$(cat .eapw);
		    printf "\n Selected %s..." $myemail; 
		    break;;
		2 ) myuser="ivan"
                    myemail="ivanilinsky@gmail.com"; 
		    mypassword=$(cat .iipw);
		    printf "\n Selected %s..." $myemail; 
		    break;;
		3)  printf "\n Exiting!\n";
		    exit;;
	esac
done

yesterday=$(date --date="yesterday" +%F)
today=$(date +%F |tr -d '\n')
mydate=$yesterday
mydate="2016-04-11"

printf "\n Logging in..."; sleep 1
printf "\n Getting data from Fitbit...\n"
/usr/bin/Rscript /home/ivan/Documents/Projects/FitBit/scraper.R $myemail $mypassword $mydate 
chmod a+w /home/ivan/Documents/Projects/FitBit/*$mydate.csv

printf "\n Output files generated!"
printf "\n %s\t\t Heart rate " hr_$mydate.csv
printf "\n %s\t Steps / Distance / Active Minutes / Calories Burned\n" intraday_data_$mydate.csv
