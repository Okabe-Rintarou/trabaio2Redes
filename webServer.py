'''


Uses pyping, available at: https://pypi.python.org/pypi/pyping/
'''

import argparse

import sys
import itertools
import socket
import pyping
from socket import *
#localhost:2080/hello.html

def main():

    serverPort = 2080
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print 'The web server running on port: ', serverPort
    x = 50;
    while True:
		print ('Ready to serve...')

		connectionSocket, addr = serverSocket.accept()
		request = connectionSocket.recv(1024).decode('ascii')
		
		#netinfo = get_net_info()
		reply = http_handle(request)
		connectionSocket.send(reply.encode('ascii'))
		connectionSocket.close()

		print("\n\nReceived request")
		print("======================")
		print(request.rstrip())
		print("======================")


		print("\n\nReplied with")
		print("======================")
		print(reply.rstrip())
		print("======================")

    pass
    
def create_HTML(string):

	html = "<!DOCTYPE html PUBLIC \"-//IETF//DTD HTML 2.0//EN\"><HTML><HEAD><TITLE>PING TEST</TITLE></HEAD><BODY><H1>Hi</H1><p>" + string + "</p> </BODY></HTML>"
	return html
	pass
	
def get_net_info():
	youtube = get_site_info('www.youtube.com.br')
	facebook = get_site_info('www.facebook.com.br')
	amazon = get_site_info('www.amazon.com.br')
	icmc = get_site_info('www.icmc.usp.br')
	wikipedia = get_site_info('www.wikipedia.org')
	google = get_site_info('www.google.com.br')
	twitter = get_site_info('twitter.com');
	jupiter = get_site_info('uspdigital.usp.br');
	codeforces = get_site_info('codeforces.com');
	steam = get_site_info('store.steampowered.com');

	sites = jupiter + '\n' + steam + '\n' + codeforces + '\n' + str(youtube) + '\n' + str(facebook) + '\n';
	sites += str(amazon) + '\n' + str(icmc) + '\n' + '\n' + twitter + '\n' + str(wikipedia) + '\n' + str(google);

	return sites;

	pass

def get_site_info(site):
	s = pyping.ping(site, udp = False)
	#sInfo = ''
	print ("ho\n");
	if(s.ret_code == 0):#DEU BOM
		
		sInfo = '<h3>CONNECTION SUCCESS: </h3>' + str(s.destination)
		sInfo = sInfo + '<br>IP: ' + str(s.destination_ip)
		sInfo = sInfo + '<br>PACKETS LOST: ' + str(s.packet_lost) 
		sInfo = sInfo + '<br>MINIMUM ROUND TRIP TIME (in ms): ' + str(s.min_rtt)
		sInfo = sInfo + '<br>AVERAGE ROUND TRIP TIME (in ms): ' + str(s.avg_rtt)
		sInfo = sInfo + '<br>MAXIMUM ROUND TRIP TIME (in ms): ' + str(s.max_rtt)
		sInfo = sInfo + '<br>';
		pass
	else:
		sInfo = '<h3> CONNECTION FAILED </h3>' + site
	return sInfo
	pass

def http_handle(request_string):

    #assert not isinstance(request_string, bytes)
	#print 'ORIGINAL REQUEST: ', request_string
	print("ha\n")
	request = []
	request = request_string.split('\r\n')#Lista com todas as linhas enviadas
	print 'LISTA REQUEST: ', request
	request.remove("")#Remove a blank link

	fileReq = request[0].split()[1][1:];#Linha 0 da request, segunda palavra, ignore primeiro caracter
	print 'requested File:', fileReq
	#Tenta abrir o arquivo requisitado
	try:
		#f = open(fileReq)
		#fileData = f.read()#Le o arquivo de nome enviado pelo request
		#print fileData
		fileData = create_HTML(get_net_info())
		output = ('\nHTTP/1.1 200 Ok\n\n') + fileData
		return output
	#Falha na tentativa de abrir o arquivo
	except IOError:
		output = ('\nHTTP/1.1 404 Not Found\n\n')
		return output
	pass
   #raise NotImplementedError
if __name__ == '__main__':
    main()
