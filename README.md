# internet-archive-downloader
This is a simple individual file downloader tailored for use on the Internet Archive. 

I wanted to learn how to parse data from an XML file, how to handle redirects using httpx, and how to use loading bars on the command line, so I came up with this use case. 

DISCLAIMER: I am not responsible for any videos that are downloaded for illegal purposes when someone uses this program. This was developed for educational purposes only.

## Use
This has been tested for use in Ubuntu 22.04. This was built using Python 3.10.

1. Clone the repo and go into the root directory.
2. Modify the `run_me.sh` file to make it executable.
```
chmod +x run_me.sh
```
3. Run the `run_me.sh` file.
4. When prompted, copy the URL for the web page that contains the listing of all of the videos. For example, `https://archive.org/download/47-mobile-suit-gundam-wing`
5. Press enter, and watch the bars go.

### NOTE

This currently only supports files with a MKV or MP4 file extention. 

## TO-DO
[] Make a chooser for different categories of file.
[] Pass login credentials.
[] Search the archive folder for files already downloaded and resume if a download was halted.