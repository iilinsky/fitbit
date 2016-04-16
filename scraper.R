library("fitbitScraper")

# PARSE ARGUMENTS
args <- commandArgs(trailingOnly = TRUE)
#mypassword <- readLines(".pw")
myemail <- args[1]
mypassword <- args[2]
mydate = args[3]

# GET COOKIE
cookie <- login(email=myemail, password=mypassword)

# GET DATA FRAMES
steps <- get_intraday_data(cookie, what="steps", date=mydate)
distance <- get_intraday_data(cookie, what="distance", date=mydate)
floors <- get_intraday_data(cookie, what="floors", date=mydate)
active_mins <- get_intraday_data(cookie, what="active-minutes", date=mydate)
cals_burned <- get_intraday_data(cookie, what="calories-burned", date=mydate)
hr <- get_intraday_data(cookie, what="heart-rate", date=mydate)

# MERGE DATA FRAMES
df = Reduce(function(x,y) merge(x, y, all=TRUE), list(steps, distance, floors, active_mins, cals_burned))

# NAMES FOR .CSV FILES
intraday_csv_name <- paste('intraday_data_', mydate, ".csv", sep="")
hr_csv_name <- paste('hr_', mydate, ".csv", sep="")

# WRITE .CSV FILES
write.csv(df, file = intraday_csv_name, row.names = FALSE)
write.csv(hr, file = hr_csv_name, row.names = FALSE)
