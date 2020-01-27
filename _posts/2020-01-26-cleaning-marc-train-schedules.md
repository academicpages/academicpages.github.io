---
title: Cleaning MARC train schedules
date: 2020-01-26
permalink: /posts/2020/01/cleaning-marc-train-schedules
---

I’ve ridden the [MARC train](https://en.wikipedia.org/wiki/MARC_Train) between
DC and Baltimore a few times, and I got frustrated with clicking through the
[“Schedule”](https://www.mta.maryland.gov/schedule/marc-penn) and
[“Timetable”](https://www.mta.maryland.gov/schedule/timetable/marc-penn)
interfaces to see train times. There’s a
[pdf](https://s3.amazonaws.com/mta-website-staging/mta-website-staging/files/Routes+Schedules/marc_penn-washington_weekday.pdf),
but it’s a pain to read: I only want to know which trains go between DC and
Baltimore, and what times they leave/arrive.

After fiddling with the pdf for a while, or thinking about manually copying the
data, I decided to look for the raw data in a machine-readable format. I mean,
Google and whoever can tell you when trains will leave/arrive, so why can’t I?

In fact the data are on the MTA’s [developer resources
page](https://www.mta.maryland.gov/developer-resources), in General
Transit Feed Specification (GTFS) format (specification
[here](https://gtfs.org/reference/static/)).

The GTFS data consist of a number of files, a few of which are important
to us:

-   `calendar.txt`: Specifies what services run on which days. I’ll be
    looking just for weekday services.
-   `stops.txt`: Gives the names of stops. I’m just interested in
    Washington Union Station and Baltimore Penn Station.
-   `routes.txt`: I’ll be looking just at the MARC trains.
-   `trips.txt`: In our case, a “trip” corresponds to a train (in the
    sense of, Train 123 to Baltimore).
-   `stop_times.txt`: This says which trips, on which services, stop at
    which stops, at what times.

Downloading the files
=====================

Let’s start by grabbing the data. Always load up the
[tidyverse](https://tidyverse.tidyverse.org/) first! I also use the
[lubridate](https://lubridate.tidyverse.org/) package to order trains by
their times.

```r
library(tidyverse)
library(lubridate)
```

Then, download and extract the zip file.

```r
url <- "https://s3.amazonaws.com/mdotmta-gtfs/google_transit.zip"
target_file <- "google_transit.zip"

if (!file.exists(target_file)) {
    download.file(url, target_file)
    unzip(target_file, junkpaths = FALSE)
}
```

Reading in the files
====================

To make it easier to play around with and manipulate the data files,
I’ll load all the `.txt` files into the global environment, naming them
after their filename. For example, I want a tibble `calendar` that comes
from reading `calendar.txt`, and so on.

```r
# unzip with list=TRUE just lists the files in the zip archive
for (filename in unzip(target_file, list = TRUE)$Name) {
    # str_match will get "calendar" out of "calendar.txt"
    name <- str_match(filename, "(.+)\\.txt")[, 2]
    contents <- read_csv(filename)
    # this is equivalent to running `calendar <- contents` in the global environment
    assign(name, contents, envir = .GlobalEnv)
}

## Warning: 146186 parsing failures.
## row            col   expected   actual             file
## 835 arrival_time   valid date 24:00:42 'stop_times.txt'
## 835 departure_time valid date 24:00:42 'stop_times.txt'
## 836 arrival_time   valid date 24:01:23 'stop_times.txt'
## 836 departure_time valid date 24:01:23 'stop_times.txt'
## 837 arrival_time   valid date 24:01:42 'stop_times.txt'
## ... .............. .......... ........ ................
## See problems(...) for more details.
```

In loading, we got some errors from the stop times table:

```r
head(problems(stop_times))

## # A tibble: 6 x 5
##     row col            expected   actual   file
##   <int> <chr>          <chr>      <chr>    <chr>
## 1   835 arrival_time   valid date 24:00:42 'stop_times.txt'
## 2   835 departure_time valid date 24:00:42 'stop_times.txt'
## 3   836 arrival_time   valid date 24:01:23 'stop_times.txt'
## 4   836 departure_time valid date 24:01:23 'stop_times.txt'
## 5   837 arrival_time   valid date 24:01:42 'stop_times.txt'
## 6   837 departure_time valid date 24:01:42 'stop_times.txt'
```

`read_csv` has trouble with the two time fields in `stop_times.txt`
because of values like `24:00:24`. In accordance with the
[specification](https://gtfs.org/reference/static#stop_timestxt), these
fields are formatted as hours:minutes:seconds, in 24-hour format.
Although starting with “24” isn’t typical 24-hour time format (you would
write “00:00:42”, for example), the specification is clear that
“24:00:24” is intentional, and it refers to a post-midnight stop on a
trip that started before midnight.

None of the MARC train times I’m interested in have stops after
midnight, so hopefully we won’t have to deal with this problem, which
would manifest as `NA` values under the arrival or departure time. So
let’s set this aside.

Watching the calendar
=====================

First, I’ll look at the calendar file:

```r
calendar

## # A tibble: 8 x 10
##   service_id start_date end_date monday tuesday wednesday thursday friday
##   <chr>           <dbl>    <dbl>  <dbl>   <dbl>     <dbl>    <dbl>  <dbl>
## 1 1_merged_…   20200202 20200620      1       1         1        1      1
## 2 401_merge…   20200202 20200620      0       0         0        0      1
## 3 401_merge…   20190901 20200201      0       0         0        0      1
## 4 3_merged_…   20200202 20200620      0       0         0        0      0
## 5 1_merged_…   20190901 20200201      1       1         1        1      1
## 6 2_merged_…   20200202 20200620      0       0         0        0      0
## 7 3_merged_…   20190901 20200201      0       0         0        0      0
## 8 2_merged_…   20190901 20200201      0       0         0        0      0
## # … with 2 more variables: saturday <dbl>, sunday <dbl>
```

I only want the schedule for the weekday service that will be running
after Feb 1:

```r
my_service <- calendar %>%
    # parse YYYYMMDD columns
    mutate_at(vars(ends_with("_date")), ymd) %>%
    filter(
    monday & tuesday & wednesday & thursday & friday,
    end_date > ymd("2020-02-01")
    ) %>%
    pull(service_id)

# there's just one service_id
stopifnot(length(my_service) == 1)
my_service

## [1] "1_merged_2542393"
```

I’ll use this `service_id` to filter the trips later on.

Finding the stops of interest
=============================

The stops file has a lot of information and a lot of stops:

```r
stops

## # A tibble: 4,724 x 12
##    stop_lat wheelchair_boar… stop_code stop_lon stop_timezone stop_url
##       <dbl>            <dbl>     <dbl>    <dbl> <lgl>         <lgl>
##  1     39.3                0     10841    -76.5 NA            NA
##  2     39.3                0      3210    -76.6 NA            NA
##  3     39.5                0     11542    -76.2 NA            NA
##  4     39.5                0     11543    -76.2 NA            NA
##  5     39.5                0     11540    -76.2 NA            NA
##  6     39.5                0     11541    -76.2 NA            NA
##  7     38.5                0     11546    -76.5 NA            NA
##  8     38.9                0     11547    -77.0 NA            NA
##  9     39.6                0     11544    -76.1 NA            NA
## 10     39.3                0      4021    -76.6 NA            NA
## # … with 4,714 more rows, and 6 more variables: parent_station <lgl>,
## #   stop_desc <lgl>, stop_name <chr>, location_type <dbl>, stop_id <dbl>,
## #   zone_id <lgl>
```

I only want to know about the times that train stops at Washington Union
Station and Baltimore Penn Station. It took a little rooting around, but
I was able to identify those stops by looking for “MARC” and either
“UNION” or “PENN”:

```r
my_stops <- stops %>%
    filter(
    str_detect(stop_name, "MARC"),
    str_detect(stop_name, "(UNION|PENN)")
    ) %>%
    select(stop_id, stop_name)

my_stops

## # A tibble: 3 x 2
##   stop_id stop_name
##     <dbl> <chr>
## 1   12002 PENN STATION MARC nb
## 2   11980 PENN STATION MARC sb
## 3   11958 UNION STATION MARC Washington
```

Putting together the data
=========================

I now have everything I need to extract the relevant data from the stop
times table:

```r
stop_times

## # A tibble: 1,475,869 x 9
##    trip_id arrival_time departure_time stop_id stop_sequence stop_headsign
##      <dbl> <time>       <time>           <dbl>         <dbl> <lgl>
##  1 2482921 06:22:00     06:22:00         14135             1 NA
##  2 2482921 06:22:08     06:22:08         12558             2 NA
##  3 2482921 06:23:31     06:23:31          6564             3 NA
##  4 2482921 06:24:07     06:24:07          6566             4 NA
##  5 2482921 06:26:12     06:26:12         12687             5 NA
##  6 2482921 06:27:13     06:27:13         12727             6 NA
##  7 2482921 06:28:47     06:28:47         12073             7 NA
##  8 2482921 06:29:39     06:29:39           625             8 NA
##  9 2482921 06:30:30     06:30:30          6578             9 NA
## 10 2482921 06:34:00     06:34:00          2397            10 NA
## # … with 1,475,859 more rows, and 3 more variables: pickup_type <lgl>,
## #   drop_off_type <lgl>, shape_dist_traveled <dbl>
```

and the trips table:

```r
trips

## # A tibble: 30,990 x 10
##    block_id bikes_allowed route_id wheelchair_acce… direction_id trip_headsign
##    <chr>            <dbl>    <dbl>            <dbl>        <dbl> <chr>
##  1 b_389363             1    11650                1            0 51 DOWNTOWN
##  2 b_389624             1    11659                1            0 65 CCBC DUND…
##  3 b_389623             1    11659                1            0 65 CCBC DUND…
##  4 b_389623             1    11659                1            0 65 CCBC DUND…
##  5 b_389623             1    11659                1            0 65 CCBC DUND…
##  6 b_389507             1    11659                1            0 65 CCBC DUND…
##  7 b_389619             1    11659                1            0 65 CCBC DUND…
##  8 b_389624             1    11659                1            0 65 CCBC DUND…
##  9 b_389624             1    11659                1            0 65 CCBC DUND…
## 10 b_392132             1    12191                1            0 94 FORT McHE…
## # … with 30,980 more rows, and 4 more variables: shape_id <dbl>,
## #   service_id <chr>, trip_id <dbl>, trip_short_name <chr>
```

I run a few steps here to get the data I want:

1.  I start with all the stop times.
2.  I inner join the stop times with the list of my stops, thus keeping
    only the stop time information at the 3 stops of interest (i.e.,
    Penn and Union).
3.  Join in the trip information (for the `trip_short_name`, which is
    actually the train number, and the `trip_headsign`, which is things
    like “WASHINGTON EXPRESS”).
4.  Filter for my service ID, so we only get the correct weekday
    schedule.
5.  Select only the “trips” (i.e., trains) that have at least 2 of my
    stops of interest. This removes trips that run through Penn but not
    Union, say.
6.  Check that arrival and departure times are the same, and then just
    use one of those.

```r
my_data <- stop_times %>%
    inner_join(my_stops, by = "stop_id") %>%
    inner_join(trips, by = "trip_id") %>%
    filter(service_id == my_service) %>%
    group_by(trip_id) %>%
    filter(n() > 1) %>%
    ungroup() %T>%
    { stopifnot(all(.$arrival_time == .$departure_time)) } %>%
    select(
    direction_id,
    headsign = trip_headsign, train = trip_short_name,
    stop = stop_name, time = arrival_time
    )

my_data
## # A tibble: 110 x 5
##    direction_id headsign   train     stop                          time
##           <dbl> <chr>      <chr>     <chr>                         <time>
##  1            0 WASHINGTON Train 505 PENN STATION MARC sb          05:10
##  2            0 WASHINGTON Train 505 UNION STATION MARC Washington 06:10
##  3            0 WASHINGTON Train 409 PENN STATION MARC sb          06:15
##  4            0 WASHINGTON Train 409 UNION STATION MARC Washington 07:10
##  5            0 WASHINGTON Train 525 PENN STATION MARC sb          09:18
##  6            0 WASHINGTON Train 525 UNION STATION MARC Washington 10:20
##  7            0 WASHINGTON Train 423 PENN STATION MARC sb          08:50
##  8            0 WASHINGTON Train 423 UNION STATION MARC Washington 09:51
##  9            0 WASHINGTON Train 401 PENN STATION MARC sb          04:10
## 10            0 WASHINGTON Train 401 UNION STATION MARC Washington 05:05
## # … with 100 more rows
```

I kept the "direction ID", which "\[i\]ndicates the direction of travel
for a trip", because I saw that it corresponds to northbound or
southbound.

Beautify-ing
============

Now it’s just a matter of making things pretty:

-   Recast the times as lubridate date-time objects. This requires
    adding a random date (I picked 1 Jan 2000) but has the advantage
    that I can now sort trains by times.
-   Shorten the stop names to “Penn” and “Union”.
-   Rather than say “Train 123”, “Train 456”, etc., just say 123, 456,
    etc.

```r
my_pretty_data <- my_data %>%
mutate(
time = as_datetime(str_c("2000-01-01 ", time)),
stop = recode(
    stop,
    `PENN STATION MARC sb` = "Penn",
    `PENN STATION MARC nb` = "Penn",
    `UNION STATION MARC Washington` = "Union"
),
train = str_extract(train, "\\d+")
)
```

And now I’m ready to show the southbound (direction ID `0`) from Penn to
Union:

```r
my_pretty_data %>%
    filter(direction_id == 0) %>%
    spread(stop, time) %>%
    arrange(Penn) %>%
    select(headsign, train, Penn, Union) %>%
    mutate_at(c("Penn", "Union"), ~ format(., "%H:%M %p"))

## # A tibble: 27 x 4
##    headsign   train Penn     Union
##    <chr>      <chr> <chr>    <chr>
##  1 WASHINGTON 401   04:10 AM 05:05 AM
##  2 WASHINGTON 403   04:40 AM 05:40 AM
##  3 WASHINGTON 505   05:10 AM 06:10 AM
##  4 WASHINGTON 407   05:40 AM 06:43 AM
##  5 WASHINGTON 409   06:15 AM 07:10 AM
##  6 WASHINGTON 511   06:30 AM 07:24 AM
##  7 WASHINGTON 413   06:40 AM 07:43 AM
##  8 WASHINGTON 415   06:55 AM 07:58 AM
##  9 WASHINGTON 517   07:25 AM 08:20 AM
## 10 WASHINGTON 419   07:45 AM 08:47 AM
## # … with 17 more rows
```

As an exercise, I’ll show how to write that code without specifying
which of Penn or Union will come first:

```r
pretty_table <- function(direction, from_stop, to_stop) {
    my_pretty_data %>%
    filter(direction_id == direction) %>%
    spread(stop, time) %>%
    arrange_at(from_stop) %>%
    select_at(c("headsign", "train", from_stop, to_stop)) %>%
    mutate_at(c(from_stop, to_stop), ~ format(., "%H:%M %p"))
}
```

And now I can create the two tables, and have the order of the columns make
sense when you read from left to right:

```r
pretty_table(0, "Penn", "Union")

## # A tibble: 27 x 4
##    headsign   train Penn     Union
##    <chr>      <chr> <chr>    <chr>
##  1 WASHINGTON 401   04:10 AM 05:05 AM
##  2 WASHINGTON 403   04:40 AM 05:40 AM
##  3 WASHINGTON 505   05:10 AM 06:10 AM
##  4 WASHINGTON 407   05:40 AM 06:43 AM
##  5 WASHINGTON 409   06:15 AM 07:10 AM
##  6 WASHINGTON 511   06:30 AM 07:24 AM
##  7 WASHINGTON 413   06:40 AM 07:43 AM
##  8 WASHINGTON 415   06:55 AM 07:58 AM
##  9 WASHINGTON 517   07:25 AM 08:20 AM
## 10 WASHINGTON 419   07:45 AM 08:47 AM
## # … with 17 more rows

pretty_table(1, "Union", "Penn")

## # A tibble: 28 x 4
##    headsign          train Union    Penn
##    <chr>             <chr> <chr>    <chr>
##  1 BALTIMORE         400   05:25 AM 06:29 AM
##  2 PERRYVILLE        502   06:05 AM 07:03 AM
##  3 BALTIMORE EXPRESS 404   06:35 AM 07:25 AM
##  4 BALTIMORE EXPRESS 408   07:05 AM 07:49 AM
##  5 BALTIMORE         410   07:10 AM 08:10 AM
##  6 MARTIN AIRPORT    610   08:05 AM 09:00 AM
##  7 MARTIN AIRPORT    612   08:20 AM 09:18 AM
##  8 BALTIMORE         412   09:05 AM 09:59 AM
##  9 BALTIMORE         414   09:30 AM 10:30 AM
## 10 BALTIMORE         416   10:15 AM 11:20 AM
## # … with 18 more rows
```

The last thing would be to put these values into a spreadsheet to get
the fonts and sizing right, and make it an easy-to-read document!
