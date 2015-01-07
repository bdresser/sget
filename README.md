# sget
A python utility to download files from a given URL

sget [-d depth] [-f folder] [-t timeout] URL

where

-d depth
  If the file pointed to by the URL contains any anchor tags (<a>), sget should
  parse those tags and download the files they point to; it should repeat this
  process upto the given depth.  By default, the depth is 0, which means that
  the file at URL is the only one to be downloaded.  The maximum depth is 5.
  Out of bounds / invalid values should exit with a one line error message to
  stderr and exit.
   
  All files should be downloaded, but only files of type php, html, and htm in
  the current domain need to be parsed.  Files must be internally linked.  That
  is, if a file has been successfully downloaded, all anchor (<a>) tags must
  point to the local copy.
   
-f folder
  The file(s) should be downloaded to the target folder; by default, this is
  the current folder.  Unreadable/inaccessible folder inputs should exit with a
  one line error message to stderr and exit.
   
-t timeout
  sget should wait for timeout seconds for a response from the server before it
  times out.  This should be a positive value less than 30.  By default, this
  should be 2 seconds.  Out of bounds / invalid values should exit with a one
  line error message to stderr and exit.
   
sget prints the URL, the current folder (from which the program was run), and
the target folder in the format shown in the example output below.  This should
be followed by an extra newline.  When printing the current and target folders,
you should not print the trailing slash.
