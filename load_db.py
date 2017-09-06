import json
import argparse
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='filename of the target JSON')
parser.add_argument('-d', help='filename of the database'))

args = parser.parse_args()
filename = getattr(args, 'f', 'target.json')
database = getattr(args, 'd', 'tasks.db')

fn = open(filename, 'r')
json = json.loads(fn.read().replace('\n',''))
fn.close()

name = json['name']
supplies = json['supplies']
steps = json['steps']

#add shit to database
conn = sqlite.connect(database)
cur = conn.cursor()
command = 'INSERT INTO tasks ({},{},{})'.format(name, supplies, steps)
cur.execute(command)
conn.commit()
conn.close()
