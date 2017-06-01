
# Setup

## Create `urlwatch.yaml`
```
./test-urlwatch
```

## Create `urls.yaml`
```
./test-urlwatch --edit
```

## Create `hooks.yaml`
```
./test-urlwatch --edit-hooks
```

# Force difference with ATCF master list

```
$ ./test-urlwatch
$ ./remove2017fromcache.py
$ ./test-urlwatch
===========================================================================
01. CHANGED: ATCF master list
===========================================================================

---------------------------------------------------------------------------
CHANGED: ATCF master list (http://ftp.nhc.noaa.gov/atcf/index/master_list.txt)
---------------------------------------------------------------------------
--- @	Tue, 30 May 2017 16:47:10 -0500
+++ @	Thu, 01 Jun 2017 16:50:35 -0500
@@ -1,3 +1,4 @@
+AL012017, ARLENE
 AL052015, ERIKA
 AL112015, JOAQUIN
 AL122016, KARL
@@ -28,6 +29,8 @@
 CP942016, INVEST
 CP952016, INVEST
 CP992015, INVEST
+EP012017, ADRIAN
+EP022017, BEATRIZ
 EP042015, ELA
 EP042016, CELIA
 EP052016, DARBY
@@ -54,5 +57,6 @@
 EP942015, INVEST
 SH922016, TEST
 SL902012, INVEST
+WP012017, NONAME
 WP302016, NOCK-TEN
 WP962013, INVEST

---------------------------------------------------------------------------


-- 
urlwatch 2.6, Copyright 2008-2016 Thomas Perl
Website: http://thp.io/2008/urlwatch/
watched 2 URLs in 0 seconds
```
