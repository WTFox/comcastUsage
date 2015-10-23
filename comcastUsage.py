__author__ = 'wtfox'

from xml.etree import ElementTree
from datetime import datetime
import sys
import calendar

import requests

USERNAME = ''
PASSWORD = ''
LOGIN_URL = 'https://umcs.comcast.net/usage_meter/login/uid?callback=?'
USAGE_URL = 'https://umcs.comcast.net/usage_meter/usage/current'

def get_usage():
    ''' A list of items that are accessible:
        <Element 'counter_start' at 0x02D0DAE0>
        <Element 'counter_end' at 0x02D0DB10>
        <Element 'context_code' at 0x02D0DB40>
        <Element 'usage_total' at 0x02D0DB70>
        <Element 'usage_allowable' at 0x02D0DBA0>
        <Element 'usage_remaining' at 0x02D0DBD0>
        <Element 'usage_percent' at 0x02D0DC00>
        <Element 'usage_uom' at 0x02D0DC30>
        <Element 'minutes_since_last_update' at 0x02D0DC90>
        <Element 'additional_billable_used' at 0x02D0DCF0>
        <Element 'additional_billable_included' at 0x02D0DD50>
        <Element 'additional_billable_remaining' at 0x02D0DDB0>
        <Element 'additional_billable_percentUsed' at 0x02D0DE10>
        <Element 'additional_billable_grace_amount_exceeded' at 0x02D0DE40>
        <Element 'additional_billable_units_per_block' at 0x02D0DE70>
        <Element 'additional_billable_cost_per_block' at 0x02D0DEA0>
        <Element 'additional_billable_blocks_used' at 0x02D0DF00>
    '''

    login_payload = {
        'username': USERNAME,
        'password': PASSWORD,
        'version': 4.0
    }

    resp = requests.post(LOGIN_URL, data=login_payload)
    tree = ElementTree.fromstring(resp.content)
    access_token = tree.find('access_token').text

    usage_payload = {
        'username': USERNAME,
        'access_token': access_token,
        'version': 4.0
    }

    resp = requests.post(USAGE_URL, data=usage_payload)
    tree = ElementTree.fromstring(resp.content)
    end_date = tree.find('device').find('counter_end').text
    usage_remaining = tree.find('device').find('usage_remaining').text
    usage_percent = tree.find('device').find('usage_percent').text
    usage_allowable = tree.find('device').find('usage_allowable').text
    usage_total = tree.find('device').find('usage_total').text

    end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%m/%d/%y')
    now = datetime.now()
    days_in_mon = calendar.monthrange(now.year, now.month)[1]
    perc = float(now.day) / float(days_in_mon) * 100

    print("")
    print("Comcast/Xfinity Data Usage for the Month.")
    print("-"*80)
    print("{}% of data used".format(usage_percent))
    print("{}% through the month.".format(int(perc)))
    print("{} GBs remaining until {}.".format(usage_remaining, end_date))
    print("{} GBs / {}GBs used.".format(usage_total, usage_allowable))
    print("-"*80)
    print("")

    sys.exit(0)


if __name__ == '__main__':
    get_usage()
