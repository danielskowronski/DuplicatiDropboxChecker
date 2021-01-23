#!python3
import sys
from dropbox import Dropbox

def print_result(alias, date):
    print("dropbox_duplicati_latest_file_%s %d" % (path, date))

if len(sys.argv)!=4:
    print("Usage: %s DROPBOX_API_TOKEN PROMETHEUS_ALIAS PATH_ON_DROPBOX" % (sys.argv[0]))
    sys.exit(1)

token = sys.argv[1]
alias = sys.argv[2]
path  = sys.argv[3]
dbx   = Dropbox(token)

try:
    files = dbx.files_list_folder(path=path)
    while files.has_more:
        files = dbx.files_list_folder_continue(cursor=files.cursor)
    last_file=files.entries[-1]
except Exception as e:
    print_result(alias, 0)
    exit(1)

print_result(alias, last_file.server_modified.timestamp())
