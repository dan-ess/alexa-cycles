# alexa-cycles
Alexa skill that enables users to find and rent cycles with docomo cycle service

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

