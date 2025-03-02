
# "formal" dates

5 possible types:
* regular date
* date range
  * can be made with 2 dates or 1 date + 1 duration
  * can be closed or open (one of the dates is missing: = before or after)
* recurring date
  * can be made with 2 dates or 1 date + 1 duration
* estimated date
* estimated range

## regular date:

* format:
    ±YYYY[-MM[-DD[Thh:[mm[:ss]][±hh[:mm]|Z]]]]
* ±YYYY is required, YYYY is padded with leading zeroes if necessary
* ±hh[:mm]: time difference from UTC.
* Z: UTC

## duration:
* format:
    PnnnnYnnMnnDTnnHnnMnnS
* cannot be used by itself.
* example:
    P17Y6M2D = 17 years 6 months 2 days

## date range:
* indicated by the presence of a / (and the absence of an initial R)
* 4 types:
### range with two regular dates:
  {date1}/{date2}
### range with one date and one duration:
  {date1}/duration
### range without an end (= after x):
  {date}/
### range without a start (= before x):
  /{date}

## recurring dates
* format with 2 dates
    R[n]/{date1}/{date2}
* format with 1 date and one duration
    R[n]/{date1}/{duration}

## estimated date
  A{date}

## estimated range
  A{range}
