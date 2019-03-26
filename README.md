# alexa-cycles
Find and rent cycles from the docomo cycle service using Alexa.

After creating an [API for the docomo cycle service](https://github.com/dan-ess/pycycles), I thought I'd try using it with via a voice interface, i.e. Alexa.

Unfortunately, Alexa's voice API didn't provide much benefit over renting via the web site.

The "*Alexa, tell __{skill_name}__ __{something}__*" format is a bit clunky, and Alexa doesn't always recognize cycle port names, but for posterity's sake, here it is.

## Disclaimer
This is not officially associated with the docomo cycle service in any way. Use at your own discretion within the terms of use of the docomo cycle service.

## Usage
### Run alexa-cycles server
1. Download this code, then from the code directory:

```
$ pipenv install
```

2. Activate the env and run a shell:

```
$ pipenv shell
```

3. Start the server:

```
$ python3 server.py
```

4. Run ngrok, observe the forwarding hostname:

```
$ ngrok http 5000
```

### Create an AWS skill
1. Create a skill

2. Configure skill using interaction_model.json

3. Set endpoint to hostname from step #4 above

### Test the skill
1. To check how many cycles there are at a cycle port:

```
alexa ask <skillname> if there are any cycles at <portname>
```

2. To rent a cycle from a cycle port:

```
alexa tell <skillname> to rent a cycle from <portname>
```


## Development

To set up in your environment locally:
```
$ pipenv install
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/dan-ess/alexa-cycles

## License

This code is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

