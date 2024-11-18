from otree.api import *

# for QR code:
import segno
from otree.settings import BASE_URL

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'test_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass    


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

# FUNCTIONS
def vars_for_admin_report(subsession):
    qr_url = BASE_URL + "/join/" + subsession.session._anonymous_code
    qr_code = segno.make_qr(qr_url).svg_data_uri(scale=20)

    return {
        "qr_code": qr_code,
    }


    # PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
