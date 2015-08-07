from flask import Flask
from flask_slack import Slack
from rdoclient import RandomOrgClient as rorgcli
import os

app = Flask(__name__)
slack = Slack(app)
app.add_url_rule('/', view_func=slack.dispatch)

slacktoken = os.getenv('SLACKTOKEN')
randokey = os.getenv('RANDOMORG_KEY')
team = os.getenv('SLACKTEAM')

@slack.command('oblique', token=slacktoken,
               team_id=team, methods=['POST'])
def oblique(**kwargs):
    with open('oblique.txt', 'r') as ost:
        strats = ost.readlines()
        length = len(strats)
    with open('iching-title.txt', 'r') as i:
        chis = i.readlines()

    r = rorgcli(randokey)
    idx = r.generate_integers(1, 0, length)
    ich = r.generate_integers(1,0,63)
    hexagram = ich[0]
    hexagram_no = hexagram + 1
    url = 'http://www.akirarabelais.com/i/i.html#%s' % hexagram_no
    strat = strats[idx[0]].strip()
    hexagram_title = chis[hexagram].strip()
    message = '%s\n <%s|%s>' % (strat, url, hexagram_title)
    return slack.response(message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)