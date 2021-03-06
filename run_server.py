#!/usr/bin/env python
import sys
import collab

def main(argv):
    if len(argv) == 1:
        if ':' not in argv[0]:
            sys.stderr.write("please provide `host:port' to bind or just `host:' for default port\n")
            return -2
        else:
            host, port = argv[0].split(':', 1)
    elif len(argv) == 2:
        host,port = [x.strip() for x in argv]
    elif len(argv) > 2:
        sys.stderr.write("use `host:port' arguments\n")
        return -3
    else:
        host, port = '', ''

    if host == '':
        host = '0.0.0.0'
    if port == '':
        port = 6633
    try:
        sys.stderr.write('Starting at ' + host +':' + str(port) + '...')
        server = collab.server.CollabServer({'host':host, 'port': int(port)})
        sys.stderr.write(' started.\n')
        server.run_forever()
    except KeyboardInterrupt:
        print("^C received, server stopped")
        return -1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
