
from flask import Flask, Response
from jsmin import jsmin

app = Flask(__name__)

@app.route('/pac', methods=['GET'])
def model_handler():

  # return response
  with open('pac.js', 'r') as file:
    minified = jsmin(file.read())
  return Response(minified, mimetype='text/plain')

if __name__ == '__main__':
  url = "http://tool.mkblog.cn/jsobfuscator/"
  print("using: %s to encripy your pac" %url)
  import argparse
  parser = argparse.ArgumentParser(description="arg parser")
  parser.add_argument('-p', type=int, default='8899', dest='port',
                      help='specify the port of server')
  parser.add_argument('--debug', dest='debug', action="store_true", help='debug mode')
  args = parser.parse_args()
  app.run(host='0.0.0.0', threaded=True, port=int(args.port), debug=args.debug)