import os
import psycopg2
import urlparse

from flask import Flask, jsonify, request

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database = url.path[1:],
    user = url.username,
    password = url.password,
    host = url.hostname,
    port = url.port
)



app = Flask(__name__)


#queries the postgres database for recipes by ingredient names
# ex: '/search?name=banana,butter' --> search for recipes that contain banana or butter(or both) 
@app.route('/search')
def search():
    name = request.args.get('ingrds')
    ingrds_split = name.split(",")
    
    cur = conn.cursor()
    jsons = []
    
    for ingrd in ingrds_split:
        cur.execute("""SELECT id from ingredients WHERE name = '%s'""" % ingrd)
        ingrd_id = cur.fetchone()         
        if ingrd_id != None:
           cur.execute("""SELECT * from recipes WHERE id IN (SELECT r_id from relations WHERE i_id = '%s')""" % ingrd_id)
           for row in cur.fetchall():
              jsons.append({'Name': str(row[1]), 'Id': str(row[0]), 'image_url': str(row[2]), 'url': str(row[3]), 'Matching ingredient': ingrd})
    return jsonify(jsons)


@app.route('/')
def home():
    name = request.args.get('name')

    cur = conn.cursor()
    cur.execute("""SELECT * from recipes WHERE name = '%s'""" % name)
    jsons = []
    for row in cur.fetchall():
        # jsons.append({'Name': str(cur.fetchone()[1]), 'Id': str(cur.fetchone()[0]), 'url': str(cur.fetchone()[2])})
        jsons.append({'Name': str(row[1]), 'Id': str(row[0]), 'image_url': str(row[2]), 'url': str(row[3]) })
    
    return jsonify(jsons)
    # return(jsonify(str(cur.fetchone()[1])))

     
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

