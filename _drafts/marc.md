---
title: "Untitled"
output: md_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

```{r, message=FALSE}
library(tidyverse)
library(lubridate)
```

# Downloading the files

```{r}
download.file("https://s3.amazonaws.com/mdotmta-gtfs/google_transit.zip")
unzip("google_transit.zip")
```

# Reading in the files

Say I just want to load all the `.txt` files into the global environment, and name them after their filename. I want a tibble called `agency` that comes from reading `agency.txt`, and so on. This would be my first stab:

1. Loop over the files (e.g., `agency.txt`)
1. Make a nicer name for the file (e.g., `agency`)
1. Read in the data
1. Assign the data to a variable with the nicer name (i.e., run `agency <- read_csv("agency.txt")`)

```{r, message=FALSE}
for (fn in list.files(pattern = "*.txt")) {
  name <- str_split_fixed(fn, "\\.", 2)[, 1]
  data <- read_csv(fn)
  assign(name, data, envir = .GlobalEnv)
}
```

This naive approach leads to problems with two files.

## Problems with `trips.txt`

`trips.txt` has a field `trip_short_name` that `read_csv` guessed was a boolean but then, on reading row 8543, started to see names like "Train 870". This is clearly a character field!

There are two solutions. One is to use `read_csv(fn, guess_max = 10000)`, telling `read_csv` to read in 10,000 rows before guessing the data types. That way it will see "Train 870" and know this is a character field. The other is to specify, for just `trips.txt`, that `trip_short_name` is a character field with:
```
read_csv("trips.txt", col_types = cols(trip_short_name = "c"))
```

## Problems with `stop_times.txt`

`read_csv` has trouble with two fields in `stop_times.txt`:  `arrival_time` and `departure_time`. From just looking at a few random rows from the file, it's pretty clear that these are hours:minutes:seconds, in 24-hour format, with a space padding on the left:
```{r}
lines <- read_lines("stop_times.txt")
lines[c(1, 2, 100, 500, 1000, 10000, length(lines))]
```

There are two challenges here. The first is that some rows, identified by `read_csv` have weird values:
```{r}
lines[c(1883, 1884) + 1]
```
I expect that was intended to mean, e.g., 1 minute and 24 seconds after midnight, but it's clearly a problem with the underlying data. Hopefully none of the stop times we need will look like this, but we'll need to double-check later.

The second sub-problem is that `read_csv` interpreted this row as objects of class `difftime`:
```{r}
class(stop_times$arrival_time)
```
In other words, these appear to be time *intervals*: "05:41:00" was interpreted as an interval of 5 hours 41 minutes, not as 5:41 AM. Tidyverse has lots of functionality for dealing with *date-times*, but not just *times*. I could think of a few solutions:

- Intervals like 5 hrs 41 mins unambiguously map to clock times like 5:41 AM, so let `read_csv` parse the times as intervals and then figure it out later.
- Read `arrival_times` and `departure_times` as characters, prefix a time, and parse it that way. For example, read `05:41:00`, turn it into `2000-01-01 05:41:00`, and then use `as_datetime`




If we run the following, we get some errors about formats not matching, so I set the `guess_max` option higher.


Even still we get some errors in `stop_times`, where it looks like some times were entered improperly. For example, row 1883 has an `arrival_time` of `24:01:24`. 

walk(list.files(pattern = "*.txt"), function(fn) {
  name <- str_split_fixed(fn, "\\.", 2)[, 1]
  data <- read_csv(fn, col_types = cols(.default = "c"))
  assign(name, data, envir = .GlobalEnv)
})

my_route_id <- routes %>%
  filter(route_short_name == "MARC", route_long_name == "PENN - WASHINGTON") %>%
  pull(route_id)

weekday_service_id <- calendar %>%
  mutate_all(as.numeric) %>%
  filter(monday & tuesday & wednesday & thursday & friday) %>%
  pull(service_id)

my_trips <- trips %>%
  filter(route_id == my_route_id) %>%
  filter(service_id == weekday_service_id) %>%
  select(trip_id, trip_headsign, trip_short_name, direction_id)

my_stops <- stops %>%
  filter(str_detect(stop_name, "PENN STATION MARC") | str_detect(stop_name, "UNION STATION MARC")) %>%
  select(stop_id, stop_name)

my_data <- stop_times %>%
  inner_join(my_trips, by = "trip_id") %>%
  inner_join(my_stops, by = "stop_id") %>%
  filter(!is.na(arrival_time)) %T>%
  { stopifnot(all(.$arrival_time == .$departure_time)) } %>%
  select(trip_id, trip_headsign, trip_short_name, stop_name, stop_sequence, direction_id, arrival_time) %>%
  group_by(trip_id) %>%
  filter(any(str_detect(stop_name, "PENN")), any(str_detect(stop_name, "UNION"))) %>%
  ungroup() %>%
  mutate(
    arrival_time = as_datetime(str_c("2000-01-01 ", arrival_time)),
    direction_id == as.integer(direction_id)
  )

my_data %>%
  mutate_at("stop_sequence", as.integer) %>%
  nest(-trip_id) %>%
  pull(data) %>%
  walk(function(df) {
    stopifnot(nrow(df) == 2)
    stopifnot(length(unique(df$trip_short_name)) == 1)
    stopifnot(str_detect(df$trip_short_name, "Train \\d+"))
    stopifnot(df$stop_sequence[1] < df$stop_sequence[2])
    stopifnot(all(second(df$arrival_time) == 0))
  })

prettify <- function(direction_id, order_stop) {
  id_ <- direction_id

  my_data %>%
    filter(direction_id == id_) %>%
    select(dest = trip_headsign, train = trip_short_name, stop_name, time = arrival_time) %>%
    mutate(
      train = str_extract(train, "\\d+"),
      stop_name = recode(
        stop_name,
        `PENN STATION MARC nb` = "Penn",
        `PENN STATION MARC sb` = "Penn",
        `UNION STATION MARC Washington` = "Union"
      )
    ) %>%
    spread(stop_name, time) %>%
    select(dest, train, !!as.symbol(order_stop), everything()) %>%
    arrange_at(order_stop) %>%
    mutate_if(is.timepoint, ~ format(., "%I:%M %p"))
}

prettify(1, "Union") %>%
  print(n = Inf)

prettify(0, "Penn") %>%
  print(n = Inf)
