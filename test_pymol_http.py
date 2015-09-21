#import __main__
#__main__.pymol_argv = ['pymol', '-qei']
import pymol
pymol.finish_launching()
import os

root = os.getcwd()

from web import pymolhttpd
httpd = pymolhttpd.PymolHttpd(port=8085, root=root)


port = httpd.port
# start handling requests
httpd.start()
# now launch a browser pointing at our server
import webbrowser
#webbrowser.open("http://localhost:%d"%port)
webbrowser.open("http://127.0.0.1:%d"%port)
import time
while 1:
    time.sleep(1)

#pdb_colors = '4PDJ_lpocket.pdb'
#pdb_name = '4PDJ'
#cmd.load(pdb_colors, pdb_name)
#cmd.spectrum("b", "blue_white_red", "%s and %s" % (pdb_name, pdb_name))

#print "done"