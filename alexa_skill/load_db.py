import json
import argparse
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='filename of the target JSON')
parser.add_argument('-d', help='filename of the database')

args = parser.parse_args()
filename = getattr(args, 'f', 'target.json')
database = getattr(args, 'd', 'tasks.db')

fn = open(filename, 'r')
j = json.loads(fn.read().replace('\n',''))
fn.close()

name = j['name']
supplies = json.dumps(j['supplies'])
steps = json.dumps(j['steps'])

#print('name: {}'.format(name))
#print('supplies: {}'.format(supplies))
#print('steps: {}'.format(steps))

#add shit to database

conn = sqlite3.connect(database)
cur = conn.cursor()
command = 'INSERT INTO tasks VALUES(?, ?, ?)'
cur.execute(command, (name, supplies, steps))
conn.commit()
conn.close()

