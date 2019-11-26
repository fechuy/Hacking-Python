import argparse
description = """Ejemplo de uso:
	+ Escaneo basico: 
		-target 127.0.0.1
	+ Indica un puerto en especifico:
		-target 127.0.0.1 -port 21
	+ Solo mostrar puertos abiertos:
		-target 127.0.0.1 --open True"""
parser = argparse.ArgumentParser(description='params port scan', epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-t", dest="target", help="target", required=True)
#parser.add_argument("-p", "--port", dest="port", type=int, default=80, help="port to scan. Default: 80")
parser.add_argument("-p", "--ports", dest="ports", default="80,8000,8080", help="Please specify the target port(s) separed by comma[80,8000,8080 by default]")
parser.add_argument('-v', dest="verbosity", help="verbosity level", type=int, default=0)
parser.add_argument("--open", dest="only_open", action="store_true", help="only display open ports", default=False)
params = parser.parse_args()
print("Target: ", params.target)
portList = params.ports.split(',')
#print(params.ports)
#print(portList)
for port in portList:
	print("Puerto: " + port)
print("Verbosity: ", params.verbosity)
print("Only open: ", params.only_open)