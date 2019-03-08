from functools import wraps
import logging
import sys

from flask import Flask
from flask_ask import Ask, statement
from pycycles import Client, ServiceArea


logging.getLogger('flask_ask').setLevel(logging.DEBUG)
app = Flask(__name__)
ask = Ask(app, '/')


# set these.
USERNAME = ''
PASSWORD = ''


def get_cycles_statement(inputs):
    inputs['be_form'] = 'is' if len(inputs['cycles']) == 1 else 'are'
    inputs['cycles'] = 'no' if len(input['cycles']) == 0 else inputs['cycles']
    return statement('There {be_form} {count} cycles at {portname}'.format(**inputs))


def rent_cycle_statement(inputs):
    return statement('Cycle rented from {portname}. Your PIN is {pin}'.format(**inputs))


def port_not_found_statement(inputs):
    return statement('Could not find cycleport: {portname}'.format(**inputs))


def match_port(target_port, ports):
    match = None
    for port in ports:
        if target_port.lower() in port['name_en'].lower():
            match = port
            break
    return match


def get_client():
    client = Client(USERNAME, PASSWORD)
    client.login()
    return client


@ask.intent('GetCyclesForCycleport')
def get_cycles_for_port(client, portname):
    client = get_client()

    cycleports = client.cycleports(ServiceArea.CHUO)
    cycleport = match_port(portname, cycleports)

    if cycleport == None:
        return port_not_found_statement({'portname': portname})

    cycles = client.cycles(cycleport)
    return get_cycles_statement(
        {'cycles': cycles, 'portname': cycleport['name_en'], 'count': len(cycles)})


@ask.intent('RentCycle')
def rent_cycle_from_port(client, portname):
    client = get_client()

    cycleports = client.cycleports(ServiceArea.CHUO)
    cycleport = match_port(portname, cycleports)

    if cycleport == None:
        return port_not_found_statement({'portname': portname})

    cycles = client.cycles(cycleport)

    if len(cycles) == 0:
        return get_cycles_statement({'cycles': cycles, 'portname': portname})

    rental = client.rent(cycles[0])
    return rent_cycle_statement(
        {'portname': rental['cycleport']['name_en'], 'pin': rental['pin']})


if __name__ == '__main__':
    app.run()
