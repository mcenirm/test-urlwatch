#!/usr/bin/env python

import re
import sqlite3


table_name = 'CacheEntry'
guid = '83b07addbd7b6311bfe75f932225b958918b0c2d'
select_sql = '''
    SELECT data, timestamp FROM {table_name} WHERE guid = ?
'''.format(table_name=table_name)
update_sql = '''
    UPDATE {table_name} SET data=?, timestamp=? WHERE guid = ?
'''.format(table_name=table_name)

with sqlite3.connect('cache.db') as conn:
    c = conn.cursor()
    c.execute(select_sql, (guid,))
    old_data, old_time, = c.fetchone()
    new_data = '\n'.join([_ for _ in old_data.split('\n') if '2017' not in _])
    new_time = old_time - 86400
    c.execute(update_sql, (new_data, new_time, guid,))
    c.close()
