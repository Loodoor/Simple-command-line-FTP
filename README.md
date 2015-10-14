# Simple-command-line-FTP

I made this script because I needed to have a simpler and better program to manage my website (using command line, sir !)

## Commands

To have a list of the aviable command, use "help"

To close safely the connection, use "quit"

All the commands can be used with and without arguments

## Samples

```
$ cwd
New working directory > www
*cmd* 'CWD www'
*resp* '250 CWD command successful'
250 CWD command successful

$ cwd ..
*cmd* 'CDUP'
*resp* '250 CDUP command successful'
250 CDUP command successful

$ ls
*cmd* 'TYPE A'
*resp* '200 Type set to A'
*cmd* 'PASV'
*resp* '227 Entering Passive Mode (185,31,40,91,209,57).'
*cmd* 'LIST'
*resp* '150 Opening ASCII mode data connection for file list'
drwxr-xr-x   4 0        0              73 Oct 14 17:16 admin
drwxr-xr-x   2 loodoor  115687         88 Oct 14 17:16 cgi-bin
drwxr-xr-x   2 loodoor  115687         10 Oct 14 18:10 www
*resp* '226 Transfer complete'
None

$ ls www
*cmd* 'TYPE A'
*resp* '200 Type set to A'
*cmd* 'PASV'
*resp* '227 Entering Passive Mode (185,31,40,91,207,140).'
*cmd* 'LIST www'
*resp* '150 Opening ASCII mode data connection for file list'
*resp* '226 Transfer complete'
None
```
